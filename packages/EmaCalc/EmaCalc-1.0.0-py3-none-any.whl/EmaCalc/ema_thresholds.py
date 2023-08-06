"""This module defines help classes to calculate response thresholds
from given model parameters.

*** Classes:
Thresholds: OLD model version allowing all response thresholds freely adaptable.
ThresholdsFree: allowing all response thresholds freely adaptable, new version.
ThresholdsMidFixed: forcing one mid-range threshold -> zero, other thresholds free

*** Version history:
* Version 0.9.5: NEW module, with functions moved from ema_base
"""
import numpy as np
from scipy.special import logit, expit
# ***** logit, expit are NOT symmetric around mid-point for extreme arguments
# logit(expit(37.)) = 37.; logit(expit(38.)) = +inf; logit(expit(-38.)) = -38.
# logit(expit(-709.)) = -709.; logit(expit(-710.)) = -inf
# ***** need safer variant here? can use scipy.special.log_expit?
# ***** No, sufficiently protected by mapped_width() function

from scipy.special import logsumexp, softmax

ETA_W_EPSILON = np.finfo(float).eps
# = additive constant to prevent too small mapped_width(eta)


# -------------------------------------------------------------
class Thresholds:
    """Superclass for threshold calculations, given parameters,
    using the simple approach with one log-width parameter eta
    for each response interval / response category
    i.e., M free parameters but only M-1 free model thresholds.
    """
    @staticmethod
    def n_param(n_categories):
        """Number of log-category-width parameters, given number of response categories
        :param n_categories: integer number of response categories
                == number of response intervals
        :return: integer number of log-category-width parameters
                needed to specify response thresholds
        """
        return n_categories

    @staticmethod
    def tau(eta):
        """Mapping of given log-category-width parameters to response thresholds.
        :param eta: 1D or 2D array with
            eta[..., m] = ...-th sample of parameter defining
                non-normalized log-width of m-th interval in mapped domain [0, 1].
            eta.shape[-1] == self.n_param(M), with M == number of response categories.
        :return: tau = 1D or 2D array, incl. all elements in [-inf, +inf]
            (tau[..., m], tau[..., m+1] = (LOWER, UPPER) limits for m-th ordinal response interval
            tau[..., 0] ==  - np.inf
            tau[..., -1] == + np.inf
            tau.ndim == eta.ndim; tau.shape[-1] == M + 1, with M == number of response categories.
        """
        cum_w = np.cumsum(mapped_width(eta), axis=-1)
        z_shape = (*cum_w.shape[:-1], 1)
        cum_w = np.concatenate((np.zeros(z_shape), cum_w),
                               axis=-1)  # include cum_w[..., 0] = 0.
        # sum_w = cum_w[..., -1:]
        return logit(cum_w / cum_w[..., -1:])

    @staticmethod
    def d_tau(eta):
        """Jacobian of tau(eta) with respect to eta
        :param eta: = 1D or 2D array with
            eta[..., m] = ...-th sample of parameter defining
                non-normalized width of m-th interval in mapped domain [0, 1].
            eta.shape[-1] == self.n_param(M), with M == number of response categories.
        :return: 2D or 3D array d_tau, with
            d_tau[..., m, i] = d tau[..., m] / d eta[..., i],
                for m = 0,..., M + 1; i = 0, ..., self.n_param(M) - 1
                where (tau[s, m], tau[s, m+1]) = (LOWER, UPPER) limits of m-th response interval
            d_tau[..., 0, :] = d_tau[..., -1, :] == 0., for extreme limits at +-inf
            d_tau.shape == (N, M+1, self.n_param(M)); N = n_samples; M = n_categories
        """
        w = mapped_width(eta)
        # (n_samples, nw) = w.shape
        nw = w.shape[-1]
        cum_w = np.cumsum(w, axis=-1)
        cw = cum_w[..., :-1, np.newaxis]  # only inner limits
        sw = cum_w[..., -1:, np.newaxis]
        # tau[..., m+1] = ln cw[..., m]  - ln (sw[..., 0] - cw[..., m])
        # dcw_dw[..., m, i] = dcw[..., m] / dw[..., i]  = 1. if i <= m else 0.
        dcw_dw = np.tril(np.ones((nw - 1, nw), dtype=int))
        dtau_dw = dcw_dw / cw - (1 - dcw_dw) / (sw - cw)
        dtau_d_eta = dtau_dw * d_mapped_width_d_eta(w)[..., np.newaxis, :]
        # dtau_d_eta.shape = (n_samples, nw - 1, nw)  OR (nw - 1, nw)
        z_shape = (*dtau_d_eta.shape[:-2], 1, dtau_d_eta.shape[-1])
        return np.concatenate((np.zeros(z_shape),  # *** use np.pad ???
                               dtau_d_eta,
                               np.zeros(z_shape)), axis=-2)

    @staticmethod
    def tau_inv(tau):
        """Inverse of tau(eta)
        :param tau: 1D or 2D array with response thresholds, EXCEPT extremes at +-inf,
            i.e., all tau elements in (-inf, +inf),
            tau[..., m] = UPPER limit for m-th interval,
                = LOWER limit for the (m+1)-th interval
            tau.shape[-1] == M - 1 == number of response intervals - 1
        :return: eta: 1D or 2D array with
            eta[..., m] = ...-th sample of log non-normalized width of m-th interval.
            eta.shape[-1] == M == number of response intervals.

        Method:
            Normalized widths and interval limits are defined in transformed domain (0, 1.),
            using a logistic mapping function,
            y = expit(tau), where y in (0, 1]
                y[..., m] =  (w_0 +...+ w_m) / (w_0 + ... + w_{M-1};  0 <= m <= M-1
                w_m = _w(eta[..., m])
        """
        y = expit(tau)
        cat_shape = (*y.shape[:-1], 1)
        # include extreme limits at 0 and 1:
        y = np.concatenate((np.zeros(cat_shape),
                            y,
                            np.ones(cat_shape)), axis=-1)
        w = np.diff(y, axis=-1)
        return mapped_width_inv(w)


ThresholdsOld = Thresholds


# -------------------------------------------------------------
class ThresholdsFree(Thresholds):
    """All internal thresholds freely variable, as specified by model parameter vector eta,
    with number of parameters == number of internal thresholds == M - 1, where
    M = number of response categories
    """
    @staticmethod
    def n_param(n_categories):
        return n_categories - 1

    @staticmethod
    def tau(eta):
        """Mapping given log-category-width parameters to response thresholds.
        :param eta: = 1D or 2D array with
            eta[..., m] = ...-th sample of parameter defining
                non-normalized width of m-th interval in mapped domain [0, 1].
            eta.shape[-1] == self.n_param(M), with M == number of response categories.
            eta[..., M] assumed fixed == 0, NOT included in input argument
        :return: tau = 1D or 2D array, incl. all elements in [-inf, +inf]
            (tau[..., m], tau[..., m+1]) = (LOWER, UPPER) limits for m-th ordinal response interval
            tau[..., 0] ==  - np.inf
            tau[..., -1] == + np.inf
            tau.ndim == eta.ndim; tau.shape[-1] == eta.shape[-1] + 2
        """
        z_shape = (*eta.shape[:-1], 1)
        eta = np.concatenate((eta, np.zeros(z_shape)), axis=-1)
        return Thresholds.tau(eta)

    @staticmethod
    def d_tau(eta):
        """Jacobian of thresholds with respect to eta
        :param eta: = 1D or 2D array with
            eta[..., m] = ...-th sample of parameter defining
                 non-normalized width of m-th interval in mapped domain [0, 1].
            eta.shape[-1] == M - 1, where M == number of response intervals.
            eta[..., M] assumed fixed == 0, NOT given as input
        :return: 2D or 3D array d_tau, with
            d_tau[..., m, i] = d tau[..., m] / d eta[..., i]; m = 0,..., M; i = 0, ..., M-1
                 where (tau[s, m], tau[s, m+1] = (LOWER, UPPER) limits of m-th response interval
            d_tau[..., 0, :] = d_tau[..., -1, :] = 0., for extreme limits at +-inf
            d_tau.ndim == eta.ndim + 1; d_tau.shape[-2:] == (M+1, M-1)
        """
        z_shape = (*eta.shape[:-1], 1)
        zeta = np.concatenate((eta, np.zeros(z_shape)), axis=-1)
        d_tau_d_zeta = Thresholds.d_tau(zeta)
        return d_tau_d_zeta[..., :, :-1]

    @staticmethod
    def tau_inv(tau):
        """Inverse of tau(eta)
        :param tau: 1D or 2D array with response thresholds, EXCEPT extremes at +-inf,
            i.e., all tau elements in (-inf, +inf),
            tau[..., m] = UPPER limit for m-th interval,
                = LOWER limit for the (m+1)-th interval
            tau.shape[-1] == M - 1; M == number of response intervals
        :return: eta: 1D or 2D array with
            eta[..., m] = ...-th sample of log non-normalized width of m-th interval.
            eta[..., M] == 0. NOT included
            eta.shape[-1] == self.n_param(M) for M == number of response intervals.
        """
        eta = Thresholds.tau_inv(tau)
        # last element always -> 0., NOT included:
        return eta[..., :-1] - eta[..., -1:]


# -------------------------------------------------------------
class ThresholdsMidFixed(Thresholds):
    """One mid-range threshold fixed == 0.,
    other thresholds mapped from parameter array eta,
    with number of parameters == M - 2, where
    M = number of response categories
    """
    @staticmethod
    def n_param(n_categories):
        return n_categories - 2

    @staticmethod
    def tau(eta):
        """Mapping given log-category-width parameters to response thresholds.
        :param eta: = 1D or 2D array with
            eta[..., m - 1] = ...-th sample of parameter defining
                non-normalized width of m-th interval in mapped domain [0, 1].
            eta.shape[-1] == self.n_param(M), with M == number of response categories.
            w[..., 0] assumed fixed == 1, NOT given as input
            w[..., M] assumed fixed == 1, NOT given as input
        :return: tau = 1D or 2D array, incl. all elements in [-inf, +inf]
            (tau[..., m], tau[..., m+1]) = (LOWER, UPPER) limits for m-th ordinal response interval
            tau[..., 0] ==  - np.inf
            tau[..., -1] == + np.inf
            tau.ndim == eta.ndim; tau.shape[-1] == eta.shape[-1] + 2
        """
        z_shape = (*eta.shape[:-1], 1)
        zeta = np.concatenate((np.zeros(z_shape), eta, np.zeros(z_shape)),
                              axis=-1)
        n_half = zeta.shape[-1] // 2
        zeta[..., :n_half] -= logsumexp(zeta[..., :n_half], axis=-1, keepdims=True)
        zeta[..., n_half:] -= logsumexp(zeta[..., n_half:], axis=-1, keepdims=True)
        # = normalized to same total width in both halves
        return Thresholds.tau(zeta)
        # **** old method:
        # z_shape = (*eta.shape[:-1], 1)
        # v = np.concatenate((np.ones(z_shape), mapped_width(eta), np.ones(z_shape)),
        #                    axis=-1)
        # # = non-normalized widths
        # n_half = v.shape[-1] // 2
        # # w[..., :n_half] /= np.sum(w[..., :n_half], axis=-1, keepdims=True)
        # # w[..., n_half:] /= np.sum(w[..., n_half:], axis=-1, keepdims=True)
        # w = np.concatenate((v[..., :n_half] / np.sum(v[..., :n_half], axis=-1, keepdims=True),
        #                     v[..., n_half:] / np.sum(v[..., n_half:], axis=-1, keepdims=True)),
        #                    axis=-1)
        # # -> lower and upper intervals normalized separately to equal sum
        # cum_w = np.concatenate((np.zeros(z_shape), np.cumsum(w, axis=-1)),
        #                        axis=-1)
        # # sum_w = cum_w[..., -1:]
        # tau = logit(cum_w / cum_w[..., -1:])
        # if not np.all(np.isclose(tau, tau_new)):
        #     err_max = np.amax(tau[..., 1:-1] - tau_new[..., 1:-1], axis=0)
        #     err_min = np.amin(tau[..., 1:-1] - tau_new[..., 1:-1], axis=0)
        #     print('tau != tau_new')
        # return tau

    @staticmethod
    def d_tau(eta):
        """Jacobian of tau(eta) w.r.t. eta
        :param eta: = 1D or 2D array with
            eta[..., m - 1] = ...-th sample of parameter defining
                non-normalized width of m-th interval in mapped domain [0, 1].
            eta.shape[-1] == self.n_param(M), with M == number of response categories.
        :return: 2D or 3D array d_tau, with
            d_tau[..., m, i] = d tau[..., m] / d eta[..., i]; m = 0,..., M; i = 0, ..., M-1
                 where (tau[s, m], tau[s, m+1] = (LOWER, UPPER) limits of m-th response interval
            d_tau[..., 0, :] = d_tau[..., -1, :] = 0., for extreme limits at +-inf
            d_tau.ndim == eta.ndim + 1; d_tau.shape[-2:] == (M+1, M-2)
        """
        z_shape = (*eta.shape[:-1], 1)
        zeta = np.concatenate((np.zeros(z_shape), eta, np.zeros(z_shape)),
                              axis=-1)
        n_half = zeta.shape[-1] // 2
        zeta[..., :n_half] -= logsumexp(zeta[..., :n_half], axis=-1, keepdims=True)
        zeta[..., n_half:] -= logsumexp(zeta[..., n_half:], axis=-1, keepdims=True)
        # = normalized to same total width in both halves
        d_zeta_d_eta = np.tile(np.identity(zeta.shape[-1]),
                               (*zeta.shape[:-1], 1, 1))
        d_zeta_d_eta[..., :n_half, :n_half] -= softmax(zeta[..., None, :n_half], axis=-1)
        d_zeta_d_eta[..., n_half:, n_half:] -= softmax(zeta[..., None, n_half:], axis=-1)
        return Thresholds.d_tau(zeta) @ d_zeta_d_eta[..., 1:-1]
        # *** old method:
        # z_shape = (*eta.shape[:-1], 1)
        # v = np.concatenate((np.ones(z_shape), mapped_width(eta), np.ones(z_shape)),
        #                    axis=-1)
        # # = non-normalized widths
        # dv_deta = d_mapped_width_d_eta(v[..., 1:-1])  # variable intervals only
        # nv = v.shape[-1]
        # n_half = nv // 2
        # s1 = np.sum(v[..., :n_half], axis=-1, keepdims=True)
        # s2 = np.sum(v[..., n_half:], axis=-1, keepdims=True)
        # w = np.concatenate((v[..., :n_half] / s1, v[..., n_half:] / s2),
        #                    axis=-1)
        # # = normalized widths, separately in lower and upper intervals
        # dw_dv = np.zeros((*w.shape, v.shape[-1]))
        # dw_dv[..., range(n_half), range(n_half)] = 1. / s1[...]
        # dw_dv[..., range(n_half, nv), range(n_half, nv)] = 1. / s2[...]
        # dw_dv[..., :n_half, :n_half] -= v[..., :n_half, None] / s1[..., None, :]**2
        # dw_dv[..., n_half:, n_half:] -= v[..., n_half:, None] / s2[..., None, :]**2
        # dw_deta = dw_dv[..., :, 1:-1] * dv_deta[..., None, :]
        # cum_w = np.cumsum(w, axis=-1)
        # cw = cum_w[..., :-1, np.newaxis]  # only inner limits
        # sw = cum_w[..., -1:, np.newaxis]
        # # tau[..., m+1] = ln cw[..., m]  - ln (sw[..., 0] - cw[..., m])
        # # dcw_dw[..., m, i] = dcw[..., m] / dw[..., i]  = 1. if i <= m else 0.
        # nw = nv
        # dcw_dw = np.tril(np.ones((nw - 1, nw), dtype=int))
        # dtau_dw = dcw_dw / cw - (1 - dcw_dw) / (sw - cw)
        # dtau_d_eta = dtau_dw @ dw_deta
        # # dtau_d_eta.shape = (n_samples, nw - 1, n_eta); only finite thresholds
        # z_shape = (*dtau_d_eta.shape[:-2], 1, dtau_d_eta.shape[-1])
        # # include zero derivative for extreme -inf, +inf thresholds
        # d_tau_d_eta = np.concatenate((np.zeros(z_shape),
        #                        dtau_d_eta,
        #                        np.zeros(z_shape)), axis=-2)
        # # if not np.all(np.isclose(d_tau_new, d_tau_d_eta)):
        #     print('d_tau_new != d_tau_d_eta')
        # return d_tau_d_eta

    @staticmethod
    def tau_inv(tau):
        """Inverse of tau(eta)
        :param tau: 1D or 2D array with response thresholds, EXCEPT extremes at +-inf,
            i.e., all tau elements in (-inf, +inf),
            tau[..., m] = UPPER limit for m-th interval,
                = LOWER limit for the (m+1)-th interval
            tau.shape[-1] == M - 1 == number of response intervals - 1
        :return: eta: 1D or 2D array, such that
            self.tau(eta)[..., 1:-1] == tau, adjusted for mid tau value -> 0
        """
        n_categories = tau.shape[-1] + 1
        n_half = n_categories // 2
        # ensure tau[..., n_half - 1] -> 0
        tau = tau - tau[..., (n_half-1):n_half]
        # ensure local copy, with mid tau -> 0.
        eta = Thresholds.tau_inv(tau)
        eta[..., :n_half] -= eta[..., :1]
        eta[..., n_half:] -= eta[..., -1:]
        # with first and last elements == 0., excluded:
        return eta[..., 1:-1]


# ----------------------------- module help functions

# ----------- Original up to version 0.9.1 -> numeric overflow in some extreme cases
# mapped_width = _w = np.exp
# _w_inv = np.log  # _w_inv(w) -> eta, such that _w(eta) == w
#
# ---------- *** piecewise (exp, linear ) variant, tested no good
# ---------- *** piecewise (inverted linear, linear ) variant, tested no good


def mapped_width(eta):
    """Mapping function from model eta param to
    non-normalized interval widths in (0, 1) range
    :param eta: = 1D or 2D array with
        eta[..., m] = ...-th sample of parameter defining
            non-normalized width of m-th interval in mapped domain [0, 1].
        eta.shape[-1] == M == number of response-scale intervals.
    :return: w = array with mapped widths
        w.shape == eta.shape
    """
    return np.exp(eta) + ETA_W_EPSILON


def d_mapped_width_d_eta(w):
    """Derivative of mapped_width, as a function of w, NOT eta.
    :param w: = mapped_width(eta) = 1D or 2D array
    :return: array dw, with
        dw[..., m] = d _w(eta)[..., m] / d eta[..., m]
    """
    return w - ETA_W_EPSILON


def mapped_width_inv(w):
    """Inverse of mapped_width(eta),
    used only after each VI iteration,
    so it is OK to be slightly inconsistent with mapped_width()
    :param w: = 1D or 2D array with
        w[..., m] = ...-th sample of
            non-normalized width of m-th interval in mapped domain [0, 1].
        sum_m w[..., m] approx == 1.
        w.shape[-1] == M == number of response-scale intervals.
    :return: eta = array with mapped widths mapped back to eta parameter
        eta.shape == w.shape
    """
    # avoid log(0.) for numerical stability
    return np.log(w + np.finfo(float).tiny)


# ------------------------------------------------- TEST:
if __name__ == '__main__':
    # ******************** TEST extreme eta, too ********************
    from scipy.optimize import approx_fprime, check_grad
    n_samples = 3
    n_categories = 5
    print(f'n_categories = {n_categories}')

    test_w = np.ones(n_categories)
    test_w = 1. + np.arange(n_categories)

    test_w = np.tile(test_w, (n_samples, 1))
    print(f'test_w = {test_w}')

    for thr in [Thresholds, ThresholdsFree, ThresholdsMidFixed]:

        eta = np.log(test_w[..., :thr.n_param(test_w.shape[-1])])

        # test one extreme eta value:
        # eta[..., 0] = -50.

        print(f'\n*** Testing {thr.__name__}.tau ***')

        tau = thr.tau(eta)
        print(f'eta = ', eta)
        print(f'_w(eta) = ', mapped_width(eta))
        print(f'tau({eta}) = ', tau)
        print(f'tau_inv(tau[..., 1:-1] = ', thr.tau_inv(tau[..., 1:-1]))
        print(f'tau(tau_inv(tau[..., 1:-1]) = ', thr.tau(thr.tau_inv(tau[..., 1:-1])))

        # ----- **** check extreme tau, that might occur in restrict_xi ************
        print('*** Testing extreme tau:')
        tau = np.array([-np.inf, -100., 0., 0., 100., np.inf])
        print(f'tau = ', tau)
        print(f'tau_inv(tau[1:-1] = ', thr.tau_inv(tau[1:-1]))
        print(f'tau(tau_inv(tau[1:-1]) = ', thr.tau(thr.tau_inv(tau[1:-1])))

        def fun(eta):
            eta = np.tile(eta, (n_samples, 1))
            return thr.tau(eta)[0, limit]

        def jac(eta):
            eta = np.tile(eta, (n_samples, 1))
            return thr.d_tau(eta)[0, limit]

        if eta.ndim > 1:
            eta_test = eta[0]  # must be 1D vector for gradient test
        else:
            eta_test = eta

        for limit in range(1, n_categories):
            print(f'\n*** Testing Jacobian {thr.__name__}.d_tau[..., {limit}, :] ***')

            print(f'tau({eta_test}) = {thr.tau(eta_test)}')

            print('approx gradient = ', approx_fprime(eta_test, fun, epsilon=1e-3))
            print('exact  gradient = ', jac(eta_test))
            err = check_grad(fun, jac, eta_test, epsilon=1e-6)
            print('check_grad err = ', err)

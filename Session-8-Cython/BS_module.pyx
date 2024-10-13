
cimport cython
from libc.math cimport  sqrt,log,exp,erf
cdef double ONE_OVER_SQRT_TWO=0.7071067811865476

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
cdef double gaussian_cdf(double x) nogil:
    return 0.5*(1+erf(x*ONE_OVER_SQRT_TWO))

@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)
cpdef double module_price_european_option(double sigma, double S0, double K, double CP, double T,double t=0) nogil:
    cdef double tau = T - t
    cdef double sigmtau = sigma*sqrt(tau)
    cdef double k = log(K/S0)
    cdef double dp = -k / sigmtau + 0.5*sigmtau
    cdef double dm = dp - sigmtau
    return S0*(CP*gaussian_cdf(CP*dp) - CP*exp(k)*gaussian_cdf(CP*dm))

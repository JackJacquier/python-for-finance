cimport cython


cdef extern from "./LetsBeRational/lets_be_rational.h" nogil:
    double implied_volatility_from_a_transformed_rational_guess(double price, double F, double K, double T, double q)
    
@cython.cdivision(True)
@cython.boundscheck(False)
@cython.wraparound(False)
@cython.nonecheck(False)	
cpdef double implied_volatility(double price, double F, double K, double T, double q):
    return implied_volatility_from_a_transformed_rational_guess(price, F, K, T, q)

//
// This source code resides at www.jaeckel.org/LetsBeRational.7z .
//
// ======================================================================================
// Copyright © 2013-2014 Peter Jäckel.
// 
// Permission to use, copy, modify, and distribute this software is freely granted,
// provided that this notice is preserved.
//
// WARRANTY DISCLAIMER
// The Software is provided "as is" without warranty of any kind, either express or implied,
// including without limitation any implied warranties of condition, uninterrupted use,
// merchantability, fitness for a particular purpose, or non-infringement.
// ======================================================================================
//
#ifndef   LETS_BE_RATIONAL_H
#define   LETS_BE_RATIONAL_H

#include "importexport.h"

#define ENABLE_SWITCHING_THE_OUTPUT_TO_ITERATION_COUNT
#define ENABLE_CHANGING_THE_HOUSEHOLDER_METHOD_ORDER

EXPORT_EXTERN_C double set_implied_volatility_maximum_iterations(double n);
EXPORT_EXTERN_C double set_implied_volatility_output_type(double k);
EXPORT_EXTERN_C double set_implied_volatility_householder_method_order(double m);
EXPORT_EXTERN_C double normalised_black_call(double x, double s);
EXPORT_EXTERN_C double normalised_vega(double x, double s);
EXPORT_EXTERN_C double normalised_black(double x, double s, double q /* q=±1 */);
EXPORT_EXTERN_C double black(double F, double K, double sigma, double T, double q /* q=±1 */);
EXPORT_EXTERN_C double normalised_implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(double beta, double x, double q /* q=±1 */, int N);
EXPORT_EXTERN_C double normalised_implied_volatility_from_a_transformed_rational_guess(double beta, double x, double q /* q=±1 */);
EXPORT_EXTERN_C double implied_volatility_from_a_transformed_rational_guess_with_limited_iterations(double price, double F, double K, double T, double q /* q=±1 */, int N);
EXPORT_EXTERN_C double implied_volatility_from_a_transformed_rational_guess(double price, double F, double K, double T, double q /* q=±1 */);

#endif // NORMAL_DISTRIBUTION_H

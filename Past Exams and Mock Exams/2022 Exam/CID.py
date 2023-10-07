import numpy as np
from abc import ABC,abstractmethod
from scipy.stats import norm
import time as time
import pandas as pd


"""QUESTION 1"""


class GreekEngine(ABC):
    def __init__(self, S0, sigma):
        self.S0 = S0
        self.sigma = sigma

    def delta_european_call_option(self, K: float, T: float, epsilon: float) -> float:
        '''
        #Inputs:
        K: strike
        T: time to maturity
        epsilon: finite difference bump parameter
        #Outputs:
        finite difference delta value
        '''
        # calculate call_price for 𝐶(𝑆0 + epsilon, sigma)
        original_S0=self.S0
        self.S0 = original_S0 + epsilon
        epsilon_plus_price = self.price_european_call_option(K, T)

        # calculate call_price for 𝐶(𝑆0, sigma)
        self.S0 = original_S0
        no_epsilon_price = self.price_european_call_option(K, T)

        delta = (epsilon_plus_price - no_epsilon_price) / epsilon

        return delta

    def vega_european_call_option(self, K: float, T: float, epsilon: float) -> float:
        '''
        #Inputs:
        K: strike
        T: time to maturity
        epsilon: finite difference bump parameter
        #Outputs:
        finite difference vega value
        '''
        # calculate call_price for 𝐶(𝑆0, sigma+epsilon)
        sigma_original = self.sigma
        self.sigma = sigma_original + epsilon
        epsilon_plus_price = self.price_european_call_option(K, T)

        # calculate call_price for 𝐶(𝑆0, sigma-epsilon)
        self.sigma = sigma_original - epsilon
        epsilon_minus_price = self.price_european_call_option(K, T)

        vega = (epsilon_plus_price - epsilon_minus_price) / (2 * epsilon)

        self.sigma = sigma_original

        return vega

    @abstractmethod
    def price_european_call_option(self, K: float, T: float, epsilon: float) -> float:
        '''
        #Inputs:
        T: time to maturity
        K: strike
        #Outputs:
        european option price
        '''

        pass


class Black_Scholes(GreekEngine):
    def __init__(self, S0, sigma):
        super().__init__(S0, sigma)

    def price_european_call_option(self, K: float, T: float) -> float:
        """
        # Inputs:
        K: Stike price
        T: time to maturity
        #Output:
        float european call price calculated by Black_Scholes
        """
        # calculate d1 and d2
        d_1 = 1 / self.sigma * np.sqrt(T) * (np.log(self.S0 / K) + self.sigma ** 2 * T / 2)
        d_2 = d_1 - self.sigma * np.sqrt(T)

        # calculate call price
        BS_call = norm.cdf(d_1) * self.S0 - norm.cdf(d_2) * K

        return BS_call


class Bachelier(GreekEngine):
    def __init__(self, S0, sigma):
        super().__init__(S0, sigma)

    def price_european_call_option(self, K: float, T: float) -> float:
        """
        # Inputs:
        K: Stike price
        T: time to maturity
        # Outputs:
        float european call price calculated by Bachelier
        """
        # calculate b1
        b1 = (self.S0 - K) / (self.sigma * np.sqrt(T))

        # calculate call price
        Ba_call = (self.S0 - K) * norm.cdf(b1) + self.sigma * np.sqrt(T) * norm.pdf(b1)

        return Ba_call


"""Question 2"""


def variance_intBM_loop(nsteps: int, nsimul: int, gaussian_vector: np.array, delta: float, f):
    """
        #Inputs:
        nsteps (int): number of time steps (m)
        nsimul (int): number of simulations (n)
        gaussian_vector (np.array): Gaussian random samples of size (nsteps-1, nsimul)
        delta (float): time increment
        f: function f()
        #Outputs:
        variance estimator (float)
    """
    function_variable = f(np.sqrt(delta) * np.cumsum(gaussian_vector[:-1], axis=0))
    # function_variable represents a nxm matrix with element j,i representing f^j(W_{t_i})
    phi = np.zeros(nsimul)
    for n in range(nsimul):
        wt = 0;
        for j in range(nsteps - 1):
            f_wt = f(wt)
            # print(n,j,f_wt)
            phi[n] += delta * f_wt
            wt += gaussian_vector[j, n] * np.sqrt(delta)
    variance1 = 1.0 / (nsimul - 1) * np.sum(np.power(phi - 1.0 / nsimul * np.sum(phi), 2))

    return variance1


def variance_intBM(nsteps, nsimul, gaussian_vector, delta, f):
    """
        #Inputs:
        nsteps (int): number of time steps (m)
        nsimul (int): number of simulations (n)
        gaussian_vector (np.array): Gaussian random samples of size (nsteps-1, nsimul)
        delta (float): time increment
        f: function f()
        #Outputs:
        variance estimator (float)
    """
    f_wt = np.zeros((nsteps - 1, nsimul))  # alocate f_wt matrix
    f_wt[0, :] = f(0)  # start at zero as w_0=0
    f_wt[1:, :] = f(np.sqrt(delta) * np.cumsum(gaussian_vector[:-1, :],axis=0))
    # cumulative sum over rows (axis=0) since nsimul is the column axis
    phi = delta * np.sum(f_wt, axis=0)  # sum over columns (axis=0) since nsimul is the column axis
    variance2 = 1.0 / (nsimul - 1) * np.sum(np.power(phi - 1 / nsimul * np.sum(phi), 2))

    return 1.0 / (nsimul - 1) * np.sum(np.power(phi - 1.0 / nsimul * np.sum(phi), 2))




"""Question 3"""

df=pd.read_csv("AAPL_options.csv")


def find_number_options_with_volume_threshold(df:pd.DataFrame,expiration:str,min_vol_threshold:int)->int:
    """
    following specification
    Input:
    - df:pd.DataFrame input dataframe
    - expiration:str expiration date
    - min_vol_threshold:int minimum volume

    Output:
    - Number of options (both Calls and Puts) available with expiration equal to the input `expiration` and volume larger than or equal `min_vol_threshold`

    """
    return len(df.loc[(df.expiration==expiration) & (df.volume>=min_vol_threshold)])


def find_mean_volume_per_expiration_per_option_type(df:pd.DataFrame,min_expiration:str)->pd.DataFrame:
    """
    Input:
         - df:pd.DataFrame input dataframe
         - min_expiration:str minimum expiration date
 
    Output:

        - pandas dataframe with columns ["expiration","optionType","averageVolume"] for expirations larger than or equal `min_expiration`
        - expiration: is the expiration in YYYY-mm-dd format
        - optionType: is all or Put
        - averageVolume: is the average traded volume per expiration and option type e.g. for each expiration we want to compute the average volume for Calls and Puts separately
    """
    return df.loc[df.expiration>=min_expiration,["expiration","optionType","volume"]].groupby(["expiration","optionType"]).mean().reset_index().rename(columns = {'expiration':'expiration', 'optionType':'optionType','volume':'averageVolume'})

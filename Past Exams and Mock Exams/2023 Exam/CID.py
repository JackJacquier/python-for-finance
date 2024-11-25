
import platform
print("Current Python Version",platform.python_version())
if platform.python_version()<"3.10":
    print("ERROR: you are using a Python version lower than 3.10")
import numpy as np
from abc import ABC,abstractmethod
import time as time
import pandas as pd



#################################
######### PROBLEM 1 #############
#################################

class InterestRateEngine(ABC):
    def __init__(self, r0):
        self.r0=r0
    
    def theta_zero_coupon_bond(self,T:float,epsilon:float)->float:
        '''
        #Inputs:
        T: time to maturity
        epsilon: finite difference bump parameter
        #Outputs:
        finite difference theta value
        '''
        

        return 
    
        
    @abstractmethod
    def price_zero_coupon_bond(self,T:float)->float:
        '''
        #Inputs:
        T: time to maturity
        #Outputs:
        zero coupon bond price
        '''
        
        pass

    def compute_term_structure(self,T_array:np.array)->np.array:
        return np.array([self.price_zero_coupon_bond(T) for T in T_array])
    
class Constant(InterestRateEngine): 
    def __init__(self, r0):
        super().__init__(r0)
        
    def price_zero_coupon_bond(self,T:float)->float:
        """
        # Inputs:
        T: time to maturity
        #Output: 
        float zero coupon bond price in constant interest rate
        """
        
        return 
    

class Vasicek(InterestRateEngine):
    def __init__(self, r0,sigma,a,b):
        """
         # Constructor Inputs:
         r_0,sigma,a,b need to be initiated!!!
        """
        pass
        
    def price_zero_coupon_bond(self,T:float)->float:
        """
        # Inputs:
        T: time to maturity
        # Outputs:
        zero coupon bond price calculated by Vasicek
        """
       
        
        return 

#################################
######### PROBLEM 2 #############
#################################


#### Q1:

def gaussian_pdf(mu:float,sigma:float,x:np.array)->np.array:
    return 
    
#### Q2:

def gaussian_integration(mu:float,sigma:float,N:int,f)->float:
    
    return 

##### Q3:

def gaussian_simulation(mu:float,sigma:float,random_array:np.array,f)->float:
    
    return 



#################################
######### PROBLEM 3 #############
#################################

#### Q1:

def compute_CAPM_coefficients(df:pd.DataFrame,list_of_symbols:list)->pd.DataFrame:
    """
    following specification
    Input:
    - df:pd.DataFrame input dataframe (same as the one provided above)
    - list_of_symbols:list of strings representign symbols e.g. ["TSLA","AMD"]

    Output:
    - Pandas Dataframe with the same columns as the input list_of_symbols 
    and 2 rows first one being the intercept and the second one being the slope of a CAPM regression
    """

    
    return 
    
#### Q2:

def  find_max_price_per_month(df:pd.DataFrame,list_of_symbols:list)->pd.DataFrame:
    """
    Input:
         - df:pd.DataFrame input dataframe
         - list_of_symbols:list of strings representign symbols e.g. ["TSLA","AMD"]
 
    Output:

        - Pandas Dataframe with the same columns as the input list_of_symbols 
        and rows with an index in the form YYYY-MM e.g. 2022-01. The values returned shoul drepresent the maximum stock value per month
    """
    
    return 
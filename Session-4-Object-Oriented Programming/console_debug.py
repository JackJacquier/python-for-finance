import pdb

def very_complex_function(x,y,z):
    intermediate_variable=x+y*z
    intermediate_variable2=intermediate_variable**0.5
    pdb.set_trace()
    
    for i in range(10):
        intermediate_variable2+=intermediate_variable**i 
        pdb.set_trace()
    return intermediate_variable2

very_complex_function(1,2,-1)

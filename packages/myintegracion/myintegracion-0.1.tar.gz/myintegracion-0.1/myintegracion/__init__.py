from scipy.integrate import quad
import numpy as np

def integral(f,a,b):
    """Make a miau.
	
    Based on: https://math.stackexchange.com/questions/2305597/integral-that-evaluates-to-42
    """
    integral,error=quad(f,a,b)
    return integral


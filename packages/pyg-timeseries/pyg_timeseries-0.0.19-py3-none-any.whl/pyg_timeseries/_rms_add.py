# -*- coding: utf-8 -*-
from pyg_timeseries._multibuffer import near_correlation_matrix, beta_correlation_matrix
import numpy as np

def np_shift(arr, n = 1):
    """
    performs a shift of a 1d, 2d or 3d array along first axis

    Parameters:
    ------------
    arr: np.array
        array whose values are to be shifted
    n: int
        shift. n = 0 means no shift, positive n is forward and negative is backwards
    
    Example:
    --------        
    >>> arr = np.array([1.,2.,3.])
    >>> assert eq(np_shift(arr,1), np.array([np.nan, 1, 2]))
    >>> assert eq(np_shift(arr,-1), np.array([2, 3, np.nan]))

    Example: 2d shifting
    --------
    >>> arr = np.array([[1.,1.], [2.,2.], [3.,3.]])
    >>> nans = [np.nan, np.nan]
    >>> assert eq(np_shift(arr,1), np.array([nans, [1.,1.], [2.,2.]]))
    >>> assert eq(np_shift(arr,-1), np.array([[2.,2.], [3.,3.], nans]))
    
    """
    if n == 0: 
        return arr
    nans = np.full((abs(n),) + arr.shape[1:], np.nan)
    if n > 0:
        return np.concatenate([nans, arr[:-n]])
    else:
        return np.concatenate([arr[-n:], nans])
import numpy as np

def window1d(input_array: list | np.ndarray, size: int, shift: int = 1, stride: int = 1) -> list[list | np.ndarray]:
    """
    This function converts a 1D list / np.array into window subsets of the input, given additional parameters on size, shift & stride.

    Parameters:
        input_array (list | np.ndarray): list or numpy array of real numbers.
        size (int): positive integer that specifies the size (lenght) of a window.
        [OPTIONAL] shift (int): positive integer that specifies the step between windows (DEFAULT int=1).
        [OPTIONAL] stride (int): positive integer that specifies the step within a window (DEFAULT int=1).

    Returns:
        result_windows (list[list | np.ndarray]): a list of lists or numpy arrays, containing generated windows based on input parameters.
    """
    for parameter in [size, shift, stride]:
        if not isinstance(parameter, int) or parameter <= 0:
            raise ValueError('Parameter input for `size`, `shift`, `stride` must be a positive integer.')
    
    _tp_array = np.array(input_array) #Needed to allow checks on dimensions and real number elements if `input_array` is a list.
    if not isinstance(input_array, (list, np.ndarray)) or len(_tp_array.shape) != 1:
        raise TypeError('`input_array` must be a 1-Dimensional list or np.ndarray.')
    
    if not (np.issubdtype(_tp_array.dtype, np.integer) or np.issubdtype(_tp_array.dtype, np.floating)):
        raise TypeError('Single elements within `input_array` must be real numbers.')
    
    if len(input_array) < size:
        raise ValueError('Parameter input for `size` must be equal or smaller than length of input list/array.')
    
    result_windows = []
    for i in range(0, len(input_array) - size + 1, shift): #Starting element for each window.
        window = input_array[i:i+size*stride:stride] #Input slice from start to window size, adjusted to stride.
        if len(window) == size: #Check current window length is of correct size or if it should be disregarded, otherwise output with a non-default stride will have output with incorrect window-sizing.
            result_windows.append(window)

    if isinstance(input_array, np.ndarray):
        return np.array(result_windows)
    return result_windows
import numpy as np

def convolution2d(input_matrix: np.ndarray, kernel: np.ndarray, stride: int = 1) -> np.ndarray:
    """
    Function takes an input 2D array, a kernel 2D array and combines them to produce a 2D array using cross-correlation operations.

    Parameters:
        input_matrix (np.ndarray): a 2D numpy.array of real numbers.
        kernel (np.ndarray): a 2D numpy.array of real numbers.
        [OPTIONAL] stride (int): an integer specifying the shift of the patch in the input_matrix between cross-correlation operations. (DEFAULT int=1)

    Returns:
        output_matrix (np.ndarray): a tranformed 2D numpy.array of real numbers following cross-correlation operations.
    """
    if not isinstance(stride, int) or stride <= 0:
        raise ValueError('`stride` must be a positive integer.')
    
    if not isinstance(input_matrix, np.ndarray) or not isinstance(kernel, np.ndarray):
        raise TypeError('`input_matrix` & `kernel` must be numpy.arrays.')
    
    if len(input_matrix.shape) != 2 or len(kernel.shape) != 2:
        raise TypeError('`input_matrix` & `kernel` must np.arrays of 2-Dimensions.')
    
    if not (np.issubdtype(input_matrix.dtype, np.integer) or np.issubdtype(input_matrix.dtype, np.floating)):
        raise TypeError('Single elements within `input_matrix` must be real numbers.')
    
    if not (np.issubdtype(kernel.dtype, np.integer) or np.issubdtype(kernel.dtype, np.floating)):
        raise TypeError('Single elements within `kernel` must be real numbers.')
    
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    #Create placeholder matrix of correct output size with empty(zeroes) data. To be used for appending cross-correlation operation data to correct positions.
    output_height = (input_height - kernel_height) // stride + 1 #Formula for output size is (input_h - kernel_h + 1) x (input_w - kernel_w + 1), but needed adjustment for stride.
    output_width = (input_width - kernel_width) // stride + 1
    output_matrix = np.zeros((output_height, output_width))

    for i in range(0, input_height - kernel_height + 1, stride): #Starting position for input_patch height, movement adjusted to stride.
        for j in range(0, input_width - kernel_width + 1, stride): #Starting position for input_patch width, movement adjusted to stride.
            input_patch = input_matrix[i:i+kernel_height, j:j+kernel_width] #Matrix patch on current position. Array slice reads: for i+ik elements in the array, return values at indexes j+jk for each element selected.
            output_matrix[i//stride, j//stride] = np.sum(input_patch * kernel) #Sum of same size matrix multiplication using Numpy. Set result at correct output matrix position.

    return output_matrix
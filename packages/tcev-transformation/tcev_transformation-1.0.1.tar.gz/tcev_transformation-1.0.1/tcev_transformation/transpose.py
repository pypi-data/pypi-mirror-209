def transpose2d(input_matrix: list[list[float]]) -> list:
    """
    Function takes in a 2D matrix of real numbers and swaps the axis (standard transpose).

    Parameters:
        input_matrix (list[list[float]]): a 2D matrix of real numbers (float or int) in the form of a nested list

    Returns:
        transposed_matrix (list[list[float]]): a transposed 2D matrix of real numbers
    """
    if not isinstance(input_matrix, list) or any(not isinstance(row, list) 
                                                 or any(not isinstance(elem, (float, int)) for elem in row) for row in input_matrix):
        raise TypeError('Input should be a 2D matrix of real numbers `list[list[float]]`')
    
    transposed_matrix = [[input_matrix[j][i] for j in range(len(input_matrix))] for i in range(len(input_matrix[0]))]
    return transposed_matrix
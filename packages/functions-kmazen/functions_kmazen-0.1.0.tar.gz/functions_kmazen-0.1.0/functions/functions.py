import numpy as np

def transpose2d(input_matrix):
    """
    Transposes a 2-dimensional matrix.

    Args:
        input_matrix (list): The input matrix to be transposed.

    Returns:
        list: The transposed matrix.

    Raises:
        Exception: If an error occurs during matrix transpose.
    """
    try:
        transposed_matrix = [[input_matrix[j][i] for j in range(len(input_matrix))] for i in range(len(input_matrix[0]))]
        print("Matrix transposed successfully!")
        for row in transposed_matrix:
            print(row)
        return transposed_matrix
        
         
    except Exception as e:
        print("Error occurred during matrix transpose:", str(e))
        return None
            
def window1d(input_array, size, shift=1, stride=1):
    """
    Creates sliding windows of a specified size from a 1-dimensional array.

    Args:
        input_array (array-like): The input array.
        size (int): The size of the sliding window.
        shift (int, optional): The number of elements to shift the window by. Defaults to 1.
        stride (int, optional): The stride value for subsampling within the window. Defaults to 1.

    Returns:
        list: A list of sliding windows.

    Raises:
        Exception: If an error occurs during time series windowing.
    """
    try:
        windows = []
        for i in range(0, len(input_array) - size + 1, shift):
            window = np.array(input_array[i:i+size])
            if stride > 1:
                window = window[::stride]
            windows.append(window)
        print("Time series windowing completed successfully!")
        for window in windows:
            print(window)
        return windows
    except Exception as e:
        print("Error occurred during time series windowing:", str(e))
        return None

def convolution2d(input_matrix, kernel, stride=1):
    """
    Performs 2-dimensional convolution on an input matrix using a kernel.

    Args:
        input_matrix (numpy.ndarray): The input matrix.
        kernel (numpy.ndarray): The convolution kernel.
        stride (int, optional): The stride value for moving the kernel. Defaults to 1.

    Returns:
        numpy.ndarray: The output matrix after convolution.

    """
    input_height, input_width = input_matrix.shape
    kernel_height, kernel_width = kernel.shape

    output_height = (input_height - kernel_height) // stride + 1
    output_width = (input_width - kernel_width) // stride + 1

    output_matrix = np.zeros((output_height, output_width))

    for i in range(0, output_height):
        for j in range(0, output_width):
            start_row = i * stride
            start_col = j * stride
            end_row = start_row + kernel_height
            end_col = start_col + kernel_width
            receptive_field = input_matrix[start_row:end_row, start_col:end_col]
            output_matrix[i, j] = np.sum(receptive_field * kernel)

            # Print intermediate results for better understanding
            print(f"Receptive Field [{i}, {j}]:")
            print(receptive_field)
            print(f"Element-wise multiplication with kernel:")
            print(receptive_field * kernel)
            print(f"Sum of multiplied values: {np.sum(receptive_field * kernel)}")
            print(f"Output value [{i}, {j}]: {output_matrix[i, j]}")
            print("----------------END-----------------")

    return output_matrix



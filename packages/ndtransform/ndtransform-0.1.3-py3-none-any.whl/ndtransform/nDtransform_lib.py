import numpy as np
from typing import List
from dataclasses import dataclass

@dataclass
class Tensor:
    '''This class provides basic framework for inputing tensors. Simple enforsment of type on input'''
    tensor_2d: List[List[float]]

@dataclass
class TimeSeries:
    '''Time series needs to have multiple inputs, 2 of which(shift and stride) need to have a default
    of 1. This class is used as enforcement of types. array and size must be provided in input.
    '''
    array: list|np.ndarray
    size: int
    shift: int = 1
    stride: int = 1

@dataclass
class Convolution:
    '''Last dataclass. Matrix and kernel need t obe provided. Stride is the only optional value,
    since by default it will always be 1'''
    matrix: np.ndarray
    kernel: np.ndarray
    stride: int = 1

def transpose2d(tensor):
    '''This function transposes provided tensor using 2 for loops, by going through provided list.'''
    Tensor.tensor_2d = tensor
    transposed_row = [[float(Tensor.tensor_2d[row][value]) 
                        for row in range(len(Tensor.tensor_2d))] 
                        for value in range(len(Tensor.tensor_2d[0]))]
    return transposed_row


def window1d(array, size, *args) -> list[list | np.ndarray]:
    '''window1d function uses TimeSeries class and calculates window of provided array akin to TensorFlow
        tf.data.Dataset.range(n).window(m) function.
    '''
    input_seq = TimeSeries(array,size,*args)
    result_win = []
    starting_positions = [i for i in range(0,len(input_seq.array),input_seq.shift)]

    for position in range(len(starting_positions)):
        value = input_seq.array[starting_positions[position]
                                :starting_positions[position] + input_seq.size * input_seq.stride
                                : input_seq.stride ]
        result_win.append(value)
    return result_win
                

def convolution2d(matrix, kernel, *args) -> np.ndarray:
    '''convolution2d takes in 2 arrays and 1 optional argument of stride and calculates cross-correlation operation
    it utilizes 2 for loops to iterate through target matrix and calculate sums of each iterations multiplications.
    Stride argument is there in case there is a need to iterate only on matrices after some steps.
    '''
    input_args = Convolution(matrix, kernel, *args)


    '''Here will be stored all relevant values as a higher dimensional overview. Source is class Convolution.'''
    stride = input_args.stride

    matrix_full = input_args.matrix
    kernel_full = input_args.kernel

    matrix_1d_shape = input_args.matrix.shape[0]
    kernel_1d_shape = input_args.kernel.shape[0]
    matrix_2d_shape = input_args.matrix.shape[1]
    kernel_2d_shape = input_args.kernel.shape[1]


    result = []
    for point_1 in range(0,matrix_1d_shape - kernel_1d_shape + 1, stride):
            for point_2 in range(0,matrix_2d_shape - kernel_2d_shape + 1, stride):
                value = 0
                gen_matrix = matrix_full[point_1:point_1 + np.size(kernel_full, 0) 
                                                 ,point_2:point_2 + np.size(kernel_full, 1) 
                                                 ] 
                if gen_matrix.shape == kernel_full.shape :
                    value = np.sum(np.multiply(gen_matrix, kernel_full))

                    result.append(value)

    return np.ndarray(shape=((matrix_1d_shape - kernel_1d_shape)//stride + 1, 
                             (matrix_2d_shape - kernel_2d_shape)//stride + 1)
                             ,buffer = np.array(result), dtype=int)


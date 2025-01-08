import numpy as np

def mean(list):
    reshaped_arr = np.array(list).reshape(3, 3)

    column_mean = np.mean(reshaped_arr, axis=0)
    row_mean = np.mean(reshaped_arr, axis=1)
    flattened_mean = np.mean(reshaped_arr)
    mean = [column_mean.tolist(), row_mean.tolist(), float(flattened_mean)]

    return mean

def variance(list):
    reshaped_arr = np.array(list).reshape(3, 3)

    column_var = np.var(reshaped_arr, axis=0)
    row_var = np.var(reshaped_arr, axis=1)
    flattened_var = np.var(reshaped_arr)
    variance = [column_var.tolist(), row_var.tolist(), float(flattened_var)]

    return variance

def std(list):
    reshaped_arr = np.array(list).reshape(3, 3)

    column_std = np.std(reshaped_arr, axis=0)
    row_std = np.std(reshaped_arr, axis=1)
    flattened_std = np.std(reshaped_arr)
    standard_variation = [column_std.tolist(), row_std.tolist(), float(flattened_std)]

    return standard_variation

def max(list):
    reshaped_arr = np.array(list).reshape(3, 3)

    column_max = np.max(reshaped_arr, axis=0)
    row_max = np.max(reshaped_arr, axis=1)
    flattened_max = np.max(reshaped_arr)
    maximum = [column_max.tolist(), row_max.tolist(), float(flattened_max)]

    return maximum

def min(list):
    reshaped_arr = np.array(list).reshape(3, 3)

    column_min = np.min(reshaped_arr, axis=0)
    row_min = np.min(reshaped_arr, axis=1)
    flattened_min = np.min(reshaped_arr)
    minimum = [column_min.tolist(), row_min.tolist(), float(flattened_min)]

    return minimum

def sum(list):
    reshaped_arr = np.array(list).reshape(3, 3)

    column_sum = np.sum(reshaped_arr, axis=0)
    row_sum = np.sum(reshaped_arr, axis=1)
    flattened_sum = np.sum(reshaped_arr)
    total_sum = [column_sum.tolist(), row_sum.tolist(), float(flattened_sum)]

    return total_sum

def calculate(list):
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    calculations ={
        'mean': mean(list),
        'variance': variance(list),
        'standard deviation': std(list),
        'max': max(list),
        'min': min(list),
        'sum': sum(list)
    }
    return calculations

calculate([1,2,3,4,5,6,7,8,9])

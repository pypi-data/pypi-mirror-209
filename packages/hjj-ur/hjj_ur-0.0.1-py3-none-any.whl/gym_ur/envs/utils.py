import numpy as np

def distance(a: np.ndarray, b: np.ndarray):
    # 计算两个数组之间的距离
    assert a.shape == b.shape
    return np.linalg.norm(a - b, axis=-1)

def angle_distance(a: np.ndarray, b: np.ndarray):
    # 计算两个角度阵列之间的测地线距离
    assert a.shape == b.shape
    dist = 1 - np.inner(a, b) ** 2
    return dist
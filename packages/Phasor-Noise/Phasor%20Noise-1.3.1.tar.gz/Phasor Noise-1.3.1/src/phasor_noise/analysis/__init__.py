import numpy as np


def PSD(signal: list) -> np.array:
    """
    PSD = |x̂(f)|² with x̂ the Fourier Transform of the Signal scale by the time of integration
    :param signal : a ndarray or list containing the evaluated value by a function
    return : the Power Spectral Density of a signal
    """
    f = np.fft.fft2(signal)
    f_s = np.fft.fftshift(f)
    resp = np.power(np.absolute(f_s), 2)
    return -resp


def mean(noise_array: list) -> float:
    """
    mean permet de calculer la moyenne des pixels passés en arguments
    """
    return np.average(noise_array)


def std_gap(noise_array: list) -> float:
    """
    std_gap permet de calculer l'écart-type des pixels passés en arguments
    """
    return np.std(noise_array)

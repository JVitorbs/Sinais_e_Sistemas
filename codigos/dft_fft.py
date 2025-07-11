import numpy as np

def dft_fft(x):
    """
    Calcula a DFT de uma sequência x utilizando a FFT do NumPy.

    Parâmetros:
    x : array-like
        Vetor de entrada com N amostras.

    Retorna:
    X : array-like
        Transformada de Fourier Discreta da sequência x.
    """
    return np.fft.fft(x)  # Utiliza a implementação otimizada da FFT

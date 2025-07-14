import numpy as np

def dft_vandermonde(x):
    N = len(x)                     # Número de pontos na sequência de entrada
    n = np.arange(N)               # Vetor de índices de tempo: [0, 1, ..., N-1]
    k = n.reshape((N, 1))          # Vetor de índices de frequência (como coluna)

    # Matriz de Vandermonde complexa:
    # Cada elemento W[k, n] = exp(-j*2π*k*n/N)
    # Essa matriz representa as bases complexas usadas na DFT
    W = np.exp(-2j * np.pi * k * n / N)

    # Multiplicação da matriz W pelo vetor x realiza a DFT: X = W * x
    # Resultado é o espectro de frequência X (complexo)
    X = np.dot(W, x)

    return X

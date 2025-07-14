import numpy as np

# ---------- Funções DFT ----------

def dft_vandermonde(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    return np.dot(W, x)

def dft_fft(x):
    return np.fft.fft(x)

# ---------- Função para exibir resultados ----------

def comparar_dfts(x, label):
    print(f"\n=== Comparação para {label} ===")
    N = len(x)
    X_vand = dft_vandermonde(x)
    X_fft = dft_fft(x)

    print(f"{'k':>2} | {'|X[k]| (Vandermonde)':>25} | {'∠X[k] (Vandermonde)':>25} | {'|X[k]| (FFT)':>20} | {'∠X[k] (FFT)':>20}")
    print("-" * 100)

    for k in range(N):
        amp_vand = np.abs(X_vand[k])
        phase_vand = np.angle(X_vand[k])
        amp_fft = np.abs(X_fft[k])
        phase_fft = np.angle(X_fft[k])
        print(f"{k:2d} | {amp_vand:25.10f} | {phase_vand:25.10f} | {amp_fft:20.10f} | {phase_fft:20.10f}")

# ---------- Sinais ----------

# Sinal 1: Simétrico (N = 8)
x8 = np.array([1, 2, 3, 4, 4, 3, 2, 1])
comparar_dfts(x8, "x8 - Vetor Simétrico (N=8)")

# Sinal 2: Cossenoidal (N = 16)
n16 = np.arange(16)
x16 = np.cos(np.pi * n16 / 4)
comparar_dfts(x16, "x16 - Cossenoidal (N=16)")

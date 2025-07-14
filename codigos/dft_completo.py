import numpy as np
import matplotlib.pyplot as plt

# -----------------------------------------------------------
# Função para gerar os gráficos de amplitude e fase de um vetor no domínio da frequência
# -----------------------------------------------------------
def plot_spectra(X, N, title_prefix):
    k = np.arange(N)               # Vetor de índices de frequência
    amplitude = np.abs(X)          # Módulo de cada componente espectral
    phase = np.angle(X)            # Fase de cada componente espectral (ângulo em radianos)

    # -------------------- Gráfico do Espectro de Amplitude --------------------
    plt.figure(figsize=(10, 4))
    plt.stem(k, amplitude, basefmt=" ")  # Gráfico de hastes (stem plot)
    plt.title(f'{title_prefix} - Espectro de Amplitude')
    plt.xlabel('k')                      # Eixo x representa o índice de frequência
    plt.ylabel('|X[k]|')                 # Eixo y representa a magnitude
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()

    # -------------------- Gráfico do Espectro de Fase --------------------
    plt.figure(figsize=(10, 4))
    plt.stem(k, phase, basefmt=" ")      # Gráfico de fase
    plt.title(f'{title_prefix} - Espectro de Fase')
    plt.xlabel('k')
    plt.ylabel('∠X[k]')                  # Fase dos coeficientes da DFT
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()

    # Retorna None porque os gráficos não estão sendo salvos em arquivo
    return None, None


# -----------------------------------------------------------
# QUESTÃO 1 - DFT usando matriz de Vandermonde
# -----------------------------------------------------------
def dft_vandermonde(x):
    """
    Calcula a Transformada Discreta de Fourier (DFT) manualmente
    usando multiplicação de matriz de Vandermonde complexa.
    """
    N = len(x)                          # Número de pontos do sinal
    n = np.arange(N)                    # Vetor de tempo discreto
    k = n.reshape((N, 1))               # Vetor coluna para formar o produto matricial

    # Matriz de Vandermonde com expoentes complexos
    W = np.exp(-2j * np.pi * k * n / N)

    # Multiplicação da matriz W pelo vetor x → X = W.x
    X = np.dot(W, x)
    return X

# ------------ Teste para N = 8 com um sinal simétrico ------------
x8 = np.array([1, 2, 3, 4, 4, 3, 2, 1])        # Sinal discreto no tempo
X8_vand = dft_vandermonde(x8)                 # DFT via matriz
path_amp_8, path_phase_8 = plot_spectra(X8_vand, 8, "Vandermonde_N8")  # Geração dos gráficos

# ------------ Teste para N = 16 com sinal cossenoidal ------------
n16 = np.arange(16)                           # Vetor de tempo
x16 = np.cos(np.pi * n16 / 4)                 # Cosseno com frequência conhecida
X16_vand = dft_vandermonde(x16)
path_amp_16, path_phase_16 = plot_spectra(X16_vand, 16, "Vandermonde_N16")


# -----------------------------------------------------------
# QUESTÃO 2 - DFT usando FFT (algoritmo rápido da DFT)
# -----------------------------------------------------------
def dft_fft(x):
    """
    Calcula a DFT de forma eficiente utilizando a implementação da FFT
    (Fast Fourier Transform) da biblioteca NumPy.
    """
    return np.fft.fft(x)

# ------------ FFT com N = 8 usando mesmo vetor anterior ------------
X8_fft = dft_fft(x8)
path_fft_amp_8, path_fft_phase_8 = plot_spectra(X8_fft, 8, "FFT_N8")

# ------------ FFT com N = 16 usando o cosseno anterior ------------
X16_fft = dft_fft(x16)
path_fft_amp_16, path_fft_phase_16 = plot_spectra(X16_fft, 16, "FFT_N16")


# -----------------------------------------------------------
# Estrutura de retorno com os caminhos para os gráficos
# Isso pode ser usado para gerar tabelas em LaTeX ou relatórios
# -----------------------------------------------------------
{
    "vandermonde": {
        "N8": {"amp": path_amp_8, "fase": path_phase_8},
        "N16": {"amp": path_amp_16, "fase": path_phase_16}
    },
    "fft": {
        "N8": {"amp": path_fft_amp_8, "fase": path_fft_phase_8},
        "N16": {"amp": path_fft_amp_16, "fase": path_fft_phase_16}
    }
}

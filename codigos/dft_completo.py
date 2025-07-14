import numpy as np
import matplotlib.pyplot as plt

# Função para gerar os gráficos de amplitude e fase
def plot_spectra(X, N, title_prefix):
    k = np.arange(N)
    amplitude = np.abs(X)
    phase = np.angle(X)

    # Gráfico do espectro de amplitude
    plt.figure(figsize=(10, 4))
    plt.stem(k, amplitude, basefmt=" ")
    plt.title(f'{title_prefix} - Espectro de Amplitude')
    plt.xlabel('k')
    plt.ylabel('|X[k]|')
    plt.grid(True)
    plt.tight_layout()
    # amp_path = f'/mnt/data/{title_prefix}_amplitude.png' # commented out to avoid permission errors
    # plt.savefig(amp_path) # commented out to avoid permission errors
    plt.show() # added show to display plots directly
    plt.close()

    # Gráfico do espectro de fase
    plt.figure(figsize=(10, 4))
    plt.stem(k, phase, basefmt=" ")
    plt.title(f'{title_prefix} - Espectro de Fase')
    plt.xlabel('k')
    plt.ylabel('∠X[k]')
    plt.grid(True)
    plt.tight_layout()
    # phase_path = f'/mnt/data/{title_prefix}_fase.png' # commented out to avoid permission errors
    # plt.savefig(phase_path) # commented out to avoid permission errors
    plt.show() # added show to display plots directly
    plt.close()

    # return amp_path, phase_path # commented out as saving is commented out
    return None, None # return None for paths as saving is commented out


# ---------- QUESTÃO 1 - MATRIZ DE VANDERMONDE ----------

def dft_vandermonde(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)  # matriz de Vandermonde
    X = np.dot(W, x)
    return X

# Teste para N=8
x8 = np.array([1, 2, 3, 4, 4, 3, 2, 1])
X8_vand = dft_vandermonde(x8)
path_amp_8, path_phase_8 = plot_spectra(X8_vand, 8, "Vandermonde_N8")

# Teste para N=16
n16 = np.arange(16) # n = {0, . . . , 15}
x16 = np.cos(np.pi * n16 / 4)
X16_vand = dft_vandermonde(x16)
path_amp_16, path_phase_16 = plot_spectra(X16_vand, 16, "Vandermonde_N16")

# ---------- QUESTÃO 2 - FFT ----------

def dft_fft(x):
    return np.fft.fft(x)

# FFT para N=8
X8_fft = dft_fft(x8) # Usando o mesmo array de antes e mesmo tamanho
path_fft_amp_8, path_fft_phase_8 = plot_spectra(X8_fft, 8, "FFT_N8")

# FFT para N=16
X16_fft = dft_fft(x16) # Usando o mesmo cosseno de antes e mesmo tamanho
path_fft_amp_16, path_fft_phase_16 = plot_spectra(X16_fft, 16, "FFT_N16")

# Retornar caminhos para LaTeX - fiz isso para importar diretamente no overleaf
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
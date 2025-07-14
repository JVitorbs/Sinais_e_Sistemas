# 📊 Análise de Espectros com DFT e FFT

Este repositório contém um código Python que calcula e plota os **espectros de amplitude e fase** de sinais utilizando duas abordagens:

- Transformada Discreta de Fourier (DFT) via **matriz de Vandermonde**
- Transformada Rápida de Fourier (FFT) via `numpy.fft.fft`

O código serve como ferramenta educacional para ilustrar a diferença entre o cálculo manual e o algoritmo eficiente da FFT.

---

## 🧠 Conceitos Envolvidos

### 🔷 DFT com Matriz de Vandermonde

A DFT é definida por:

```
X[k] = ∑_{n=0}^{N-1} x[n] · e^{-j2πkn/N}
```

Pode ser representada como uma multiplicação de uma matriz de Vandermonde complexa por um vetor de entrada `x`.

### ⚡ FFT (Fast Fourier Transform)

A FFT é um algoritmo eficiente para calcular a DFT em tempo `O(N log N)`. Neste projeto, usamos a função `np.fft.fft()` do NumPy.

---

## 📁 Estrutura do Código

### 1. `dft_vandermonde(x)`

Calcula a DFT manualmente com a matriz de Vandermonde:

```python
def dft_vandermonde(x):
    N = len(x)
    n = np.arange(N)
    k = n.reshape((N, 1))
    W = np.exp(-2j * np.pi * k * n / N)
    X = np.dot(W, x)
    return X
```

---

### 2. `dft_fft(x)`

Calcula a FFT usando NumPy:

```python
def dft_fft(x):
    return np.fft.fft(x)
```

---

### 3. `plot_spectra(X, N, title_prefix)`

Gera os gráficos de **amplitude** e **fase** de um vetor transformado:

```python
def plot_spectra(X, N, title_prefix):
    k = np.arange(N)
    amplitude = np.abs(X)
    phase = np.angle(X)

    plt.figure(figsize=(10, 4))
    plt.stem(k, amplitude, basefmt=" ")
    plt.title(f'{title_prefix} - Espectro de Amplitude')
    plt.xlabel('k')
    plt.ylabel('|X[k]|')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()

    plt.figure(figsize=(10, 4))
    plt.stem(k, phase, basefmt=" ")
    plt.title(f'{title_prefix} - Espectro de Fase')
    plt.xlabel('k')
    plt.ylabel('∠X[k]')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()

    return None, None
```

---

## 🔢 Sinais de Entrada

Dois sinais são utilizados para testes:

### Sinal 1: Vetor Simétrico (N = 8)

```python
x8 = np.array([1, 2, 3, 4, 4, 3, 2, 1])
```

### Sinal 2: Cossenoidal (N = 16)

```python
n16 = np.arange(16)
x16 = np.cos(np.pi * n16 / 4)
```

---

## 🧪 Execução Completa

```python
# Cálculo com Vandermonde
X8_vand = dft_vandermonde(x8)
plot_spectra(X8_vand, 8, "Vandermonde_N8")

X16_vand = dft_vandermonde(x16)
plot_spectra(X16_vand, 16, "Vandermonde_N16")

# Cálculo com FFT
X8_fft = dft_fft(x8)
plot_spectra(X8_fft, 8, "FFT_N8")

X16_fft = dft_fft(x16)
plot_spectra(X16_fft, 16, "FFT_N16")
```

---

## ⚙️ Requisitos

Com o arquivo `requirements.txt` na pasta em que estão os códigos, instale as bibliotecas necessárias com um simples comando:

```bash
pip install -r requirements.txt
```

Outra opção é digitar diretamente no terminal sem ter o arquivo `requirements.txt`:

```bash
pip install numpy matplotlib
```

---

## ▶️ Como Executar

1. Salve os códigos em dois arquivos chamados `dft_completo.py` e `dft_saida.py` 
2. Execute no terminal ou na IDE:

```bash
python dft_completo.py
python dft_saida.py
```

Os gráficos de amplitude e fase serão exibidos diretamente na tela, caso haja problema na execução do código, pode acessar meu Colab no final desse `README.md`.

---
# Problemas possíveis
Existem problemas que podem ocorrer caso rode localmente, um deles é:

```bash
UserWarning: FigureCanvasAgg is non-interactive, and thus cannot be shown
plt.show() # added show to display plots directly
```
Isso significa que você está tentando usar plt.show() em um ambiente que não tem interface gráfica, como o terminal sem suporte a GUI (por exemplo, se estiver rodando via SSH, WSL ou só no terminal do Ubuntu sem um ambiente de desktop ativo).

Caso isso ocorra uma opção simples é usar o google Colab.

---

## 💾 Salvamento de Imagens (Opcional)

Você pode ativar o salvamento dos gráficos editando a função `plot_spectra()`:

```python
plt.savefig(f'{title_prefix}_amplitude.png')
plt.savefig(f'{title_prefix}_fase.png')
```

Em vez de `plt.show()`.

---

## 📌 Aplicações

- Análise espectral de sinais digitais
- Ensino de processamento de sinais e transformadas
- Comparação entre métodos numéricos e computacionais
- Preparação de imagens para relatórios (ex: Overleaf/LaTeX)

---

## Estrutura de Arquivos do Projeto

```plaintext
DFT_FFT_Project/
├── README.md            # Documentação do projeto
├── requirements.txt     # Lista de dependências (numpy, matplotlib)
├── codigos/              # Código principal com as funções DFT e FFT e exemplos
    ├── dft_completo.py
    ├── dft_fft.py
    ├── dft_saida.py
    └── dft_vandermonde.y
└── outputs/             # Imagens e resultados gerados (opcional)
    ├── FFT_N8_amplitude.png
    ├── FFT_N8_phase.png
    ├── FFT_N16_amplitude.png
    ├── FFT_N16_phase.png
    ├── Vandermonde_N8_amplitude.png
    ├── Vandermonde_N8_phase.png
    ├── Vandermonde_N16_amplitude.png
    └── Vandermonde_N16_phase.png
```

---

## 👨‍💻 Autor

**João Vitor Batista Silva**

- [LinkedIn](https://www.linkedin.com/in/jo%C3%A3o-vitor-batista-silva-50b280279?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
- [Colab](https://colab.research.google.com/drive/1kwMIIVIxUfYBJ2oYKGRkIuohxrJJVhq3?usp=sharing)
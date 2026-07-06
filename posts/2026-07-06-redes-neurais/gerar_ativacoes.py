import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

bg = '#fafafa'
c1 = '#0d9488'   # função
c2 = '#8b5cf6'   # derivada
c_ax = '#94a3b8'
c_txt = '#1e293b'

plt.rcParams.update({
    'font.family': 'DejaVu Serif',
    'axes.facecolor': bg,
    'figure.facecolor': bg,
    'axes.edgecolor': c_ax,
    'xtick.color': c_ax,
    'ytick.color': c_ax,
    'axes.labelcolor': c_txt,
    'grid.alpha': 0.25,
    'grid.linestyle': '--',
    'grid.color': '#94a3b8',
})

z = np.linspace(-4, 4, 400)

# ---- definições ----
def sigmoid(z):   return 1 / (1 + np.exp(-z))
def d_sigmoid(z): s = sigmoid(z); return s * (1 - s)

def tanh_(z):     return np.tanh(z)
def d_tanh(z):    return 1 - np.tanh(z)**2

def relu(z):      return np.maximum(0, z)
def d_relu(z):    return (z > 0).astype(float)

funcs = [
    (r'Sigmoide: $\sigma(z) = \frac{1}{1+e^{-z}}$',
     r"$\sigma'(z) = \sigma(z)(1-\sigma(z))$",
     sigmoid, d_sigmoid),
    (r'Tanh: $\tanh(z)$',
     r"$\tanh'(z) = 1 - \tanh^2(z)$",
     tanh_, d_tanh),
    (r'ReLU: $\max(0, z)$',
     r"ReLU$'(z) = \mathbf{1}[z > 0]$",
     relu, d_relu),
]

fig = plt.figure(figsize=(12, 8), facecolor=bg)
gs = gridspec.GridSpec(2, 3, hspace=0.55, wspace=0.38,
                       top=0.90, bottom=0.08, left=0.07, right=0.97)

for col, (ftitle, dtitle, f, df) in enumerate(funcs):
    ax_f = fig.add_subplot(gs[0, col])
    ax_d = fig.add_subplot(gs[1, col])

    # função
    ax_f.plot(z, f(z), color=c1, lw=2.0)
    ax_f.axhline(0, color=c_ax, lw=0.6)
    ax_f.axvline(0, color=c_ax, lw=0.6)
    ax_f.set_title(ftitle, fontsize=8.5, color=c_txt, pad=6)
    ax_f.grid(True)
    ax_f.tick_params(labelsize=7)
    ax_f.set_xlabel('$z$', fontsize=8)

    # derivada
    ax_d.plot(z, df(z), color=c2, lw=2.0, linestyle='--')
    ax_d.axhline(0, color=c_ax, lw=0.6)
    ax_d.axvline(0, color=c_ax, lw=0.6)
    ax_d.set_title(dtitle, fontsize=8.5, color=c_txt, pad=6)
    ax_d.grid(True)
    ax_d.tick_params(labelsize=7)
    ax_d.set_xlabel('$z$', fontsize=8)

# legenda global
from matplotlib.lines import Line2D
handles = [Line2D([0],[0], color=c1, lw=2, label='Função'),
           Line2D([0],[0], color=c2, lw=2, ls='--', label='Derivada')]
fig.legend(handles=handles, loc='upper center', ncol=2,
           fontsize=9, frameon=False,
           bbox_to_anchor=(0.5, 0.975))

fig.savefig('ativacoes.png', dpi=180, bbox_inches='tight', facecolor=bg)
plt.close()
print("Figura gerada: ativacoes.png")

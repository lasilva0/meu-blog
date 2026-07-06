import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Cor de fundo do blog
bg_color = '#fafafa'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.size': 10,
    'axes.facecolor': bg_color,
    'figure.facecolor': bg_color,
    'savefig.facecolor': bg_color,
    'axes.grid': True,
    'grid.alpha': 0.3,
    'grid.linestyle': '--',
    'axes.spines.top': False,
    'axes.spines.right': False,
})

# ---- Figura 1: função quadrática em 2D ----
x = np.linspace(-2, 12, 300)
f = (x - 5)**2 + 10

fig1, ax1 = plt.subplots(figsize=(4.5, 3.5))
ax1.plot(x, f, color='#0d9488', linewidth=2)
ax1.axvline(5, color='#8b5cf6', linestyle='--', alpha=0.5, linewidth=1)
ax1.scatter([5], [10], color='#8b5cf6', s=50, zorder=5, edgecolors='white', linewidths=0.8)
ax1.set_xlabel('x')
ax1.set_ylabel('f(x)')
ax1.set_title('$f(x) = (x-5)^2 + 10$', fontsize=11, pad=8)
ax1.annotate('mínimo', xy=(5, 10), xytext=(7, 25),
             fontsize=8, color='#6b7280',
             arrowprops=dict(arrowstyle='->', color='#6b7280', lw=0.8))
plt.tight_layout()
fig1.savefig('funcao_2d.png', dpi=180, bbox_inches='tight')
plt.close(fig1)

# ---- Figura 2: superfície em 3D ----
x2 = np.linspace(5, 35, 80)
y2 = np.linspace(5, 35, 80)
X, Y = np.meshgrid(x2, y2)
Z = (X - 20)**2 + (Y - 20)**2 + 50

fig2, ax2 = plt.subplots(figsize=(4.5, 3.5), subplot_kw={'projection': '3d'})
ax2.set_facecolor(bg_color)
surf = ax2.plot_surface(X, Y, Z, cmap='cool', alpha=0.75, edgecolor='none',
                        antialiased=True, rstride=2, cstride=2)
ax2.scatter([20], [20], [50], color='#8b5cf6', s=40, zorder=5)
ax2.set_xlabel('x', fontsize=9, labelpad=2)
ax2.set_ylabel('y', fontsize=9, labelpad=2)
ax2.set_zlabel('z', fontsize=9, labelpad=2)
ax2.set_title('$z = (x-20)^2 + (y-20)^2 + 50$', fontsize=10, pad=4)
ax2.view_init(elev=28, azim=140)
ax2.tick_params(labelsize=7)
ax2.xaxis.pane.fill = False
ax2.yaxis.pane.fill = False
ax2.zaxis.pane.fill = False
ax2.xaxis.pane.set_edgecolor(bg_color)
ax2.yaxis.pane.set_edgecolor(bg_color)
ax2.zaxis.pane.set_edgecolor(bg_color)
plt.tight_layout()
fig2.savefig('funcao_3d.png', dpi=180, bbox_inches='tight')
plt.close(fig2)

print("Figuras geradas: funcao_2d.png e funcao_3d.png")

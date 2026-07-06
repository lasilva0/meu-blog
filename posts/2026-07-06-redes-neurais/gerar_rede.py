import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
from matplotlib.patches import Circle, FancyArrowPatch

bg = '#fafafa'
fig, ax = plt.subplots(figsize=(11, 7), facecolor=bg)
ax.set_facecolor(bg)
ax.set_xlim(0, 11)
ax.set_ylim(0, 8)
ax.axis('off')

# ---- layout ----
x_inp, x_hid, x_out = 2.0, 5.5, 9.0
inp_y  = [5.5, 2.5]
hid_y  = [6.2, 4.0, 1.8]
out_y  = [5.5, 2.5]
R = 0.38

c_inp = '#1a1a2e'
c_hid = '#16213e'
c_out = '#0f3460'
c_edge = '#475569'
c_wlbl = '#1e293b'
c_layer = '#64748b'

# ---- helper: seta com sombra de texto ----
def arrow(p1, p2):
    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]
    length = np.hypot(dx, dy)
    ux, uy = dx/length, dy/length
    start = (p1[0] + R*ux, p1[1] + R*uy)
    end   = (p2[0] - R*ux, p2[1] - R*uy)
    ax.annotate('', xy=end, xytext=start,
                arrowprops=dict(arrowstyle='->', color=c_edge,
                                lw=0.9, mutation_scale=9))

def weight_label(p1, p2, txt, frac=0.42, perp=0.18):
    mx = p1[0] + frac*(p2[0]-p1[0])
    my = p1[1] + frac*(p2[1]-p1[1])
    dx = p2[0]-p1[0]; dy = p2[1]-p1[1]
    L  = np.hypot(dx, dy)
    px, py = -dy/L, dx/L          # perpendicular unit vector
    tx, ty = mx + perp*px, my + perp*py
    ax.text(tx, ty, txt, fontsize=7.5, color=c_wlbl, ha='center', va='center',
            fontfamily='DejaVu Serif',
            bbox=dict(boxstyle='round,pad=0.08', fc=bg, ec='none', alpha=0.9))

def neuron(cx, cy, lbl, color):
    circ = Circle((cx, cy), R, facecolor=color, edgecolor='white',
                  linewidth=1.4, zorder=5)
    ax.add_patch(circ)
    ax.text(cx, cy, lbl, ha='center', va='center', fontsize=10,
            color='white', fontweight='bold', zorder=6,
            fontfamily='DejaVu Serif')

# ---- posições ----
inp = [(x_inp, y) for y in inp_y]
hid = [(x_hid, y) for y in hid_y]
out = [(x_out, y) for y in out_y]

# ---- pesos W1: w^(1)_{neuronio, entrada} ----
W1 = [[r'$w^{(1)}_{11}$', r'$w^{(1)}_{12}$'],
      [r'$w^{(1)}_{21}$', r'$w^{(1)}_{22}$'],
      [r'$w^{(1)}_{31}$', r'$w^{(1)}_{32}$']]

# ---- pesos W2: w^(2)_{saida, neuronio} ----
W2 = [[r'$w^{(2)}_{11}$', r'$w^{(2)}_{12}$', r'$w^{(2)}_{13}$'],
      [r'$w^{(2)}_{21}$', r'$w^{(2)}_{22}$', r'$w^{(2)}_{23}$']]

# perp sign: positivo = acima da linha, negativo = abaixo
# entrada -> oculta
perp_W1 = [[+0.22, +0.22],   # h1 <- x1, x2
           [ 0.00,  0.00],   # h2 <- x1, x2
           [-0.22, -0.22]]   # h3 <- x1, x2

for j, hp in enumerate(hid):
    for i, ip in enumerate(inp):
        arrow(ip, hp)
        weight_label(ip, hp, W1[j][i], frac=0.40, perp=perp_W1[j][i])

# oculta -> saída
perp_W2 = [[+0.22, +0.22, +0.22],   # y1 <- h1, h2, h3
           [-0.22, -0.22, -0.22]]   # y2 <- h1, h2, h3

for k, op in enumerate(out):
    for j, hp in enumerate(hid):
        arrow(hp, op)
        weight_label(hp, op, W2[k][j], frac=0.55, perp=perp_W2[k][j])

# ---- neurônios ----
for i, p in enumerate(inp):
    neuron(*p, f'$x_{i+1}$', c_inp)
for j, p in enumerate(hid):
    neuron(*p, f'$h_{j+1}$', c_hid)
for k, p in enumerate(out):
    neuron(*p, f'$y_{k+1}$', c_out)

# ---- bias (pequenos nós acima de cada camada) ----
for layer_x, layer_nodes, lbl in [
    (x_hid, hid, r'$\mathbf{b}^{(1)}$'),
    (x_out, out, r'$\mathbf{b}^{(2)}$'),
]:
    bx = layer_x - 0.7
    by = max(p[1] for p in layer_nodes) + 1.1
    circ = Circle((bx, by), 0.28, facecolor='#e2e8f0',
                  edgecolor='#94a3b8', linewidth=1.0, zorder=5)
    ax.add_patch(circ)
    ax.text(bx, by, lbl, ha='center', va='center', fontsize=7.5,
            color='#334155', zorder=6, fontfamily='DejaVu Serif')
    for p in layer_nodes:
        ax.annotate('', xy=(p[0]-R*0.7, p[1]+R*0.7),
                    xytext=(bx+0.28*0.7, by-0.28*0.7),
                    arrowprops=dict(arrowstyle='->', color='#94a3b8',
                                   lw=0.7, linestyle='dashed',
                                   mutation_scale=7))

# ---- rótulos das camadas (linha horizontal com texto) ----
for xc, lbl in [(x_inp, 'Camada de Entrada'),
                (x_hid, 'Camada Oculta'),
                (x_out, 'Camada de Saída')]:
    ax.text(xc, 7.7, lbl, ha='center', va='center', fontsize=9,
            color=c_layer, fontfamily='DejaVu Serif',
            style='italic')
    ax.plot([xc-1.0, xc+1.0], [7.45, 7.45], color='#cbd5e1', lw=0.8)

# ---- legenda de notação ----
ax.text(0.15, 0.3,
        r'$w^{(\ell)}_{ki}$: peso da entrada $i$ para o neurônio $k$ na camada $\ell$',
        fontsize=7.5, color='#64748b', va='bottom', fontfamily='DejaVu Serif')

plt.tight_layout(pad=0.3)
fig.savefig('rede_neural.png', dpi=200, bbox_inches='tight', facecolor=bg)
plt.close()
print("Figura gerada: rede_neural.png")

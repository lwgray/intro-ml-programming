"""
Patience Parameter Explained - Visual from Day 2 Deep Dive example.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

fig, ax = plt.subplots(figsize=(16, 9), facecolor='white')

# Data from the teaching guide
epochs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
val_loss = [0.50, 0.40, 0.35, 0.38, 0.39, 0.36, 0.33, 0.35, 0.36, 0.37]

best_epoch = 7
best_val = 0.33

colors = {
    'improving': '#2ecc71',
    'best': '#27ae60',
    'patience': '#e67e22',
    'stop': '#e74c3c',
    'line': '#3498db',
    'primary': '#2c3e50',
}

# Plot val_loss curve
ax.plot(epochs, val_loss, linewidth=3, color=colors['line'], zorder=3,
        marker='o', markersize=10, markeredgecolor='white', markeredgewidth=2)

# Color-code each marker
for i, (e, vl) in enumerate(zip(epochs, val_loss)):
    if e == best_epoch:
        color = colors['best']
        size = 16
    elif e > best_epoch:
        color = colors['patience']
        size = 12
    else:
        color = colors['improving']
        size = 10
    ax.plot(e, vl, 'o', color=color, markersize=size, zorder=5,
            markeredgecolor='white', markeredgewidth=2)

    # Val loss labels above/below each point
    offset = -0.018 if vl < 0.37 else 0.015
    ax.text(e, vl + offset, f'{vl:.2f}', fontsize=11, ha='center',
            va='top' if offset < 0 else 'bottom', fontweight='bold',
            color=colors['primary'])

# Best epoch annotation
ax.annotate('BEST!\nval_loss = 0.33',
            xy=(best_epoch, best_val), xytext=(best_epoch - 1.8, best_val - 0.06),
            fontsize=13, fontweight='bold', color=colors['best'],
            arrowprops=dict(arrowstyle='->', lw=2.5, color=colors['best']),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#d5f5e3',
                      edgecolor=colors['best'], linewidth=2))

# Patience counter brackets
bracket_y = 0.51
for i, (e, label) in enumerate([(8, '1'), (9, '2'), (10, '3')]):
    ax.annotate('', xy=(e, bracket_y), xytext=(e, bracket_y + 0.015),
                arrowprops=dict(arrowstyle='-', lw=1.5, color=colors['patience']))
    ax.text(e, bracket_y + 0.02, f'counter\n= {label}',
            fontsize=11, ha='center', va='bottom', fontweight='bold',
            color=colors['patience'])

# Patience bracket spanning epochs 8-10
ax.annotate('', xy=(7.8, 0.495), xytext=(10.2, 0.495),
            arrowprops=dict(arrowstyle='<->', lw=2, color=colors['patience']))
ax.text(9, 0.49, 'patience = 3', fontsize=13, ha='center', va='top',
        fontweight='bold', color=colors['patience'],
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#fef9e7',
                  edgecolor=colors['patience'], linewidth=1.5))

# STOP marker at epoch 10
ax.annotate('STOP!',
            xy=(10, val_loss[9]), xytext=(10.5, val_loss[9] + 0.04),
            fontsize=14, fontweight='bold', color=colors['stop'],
            arrowprops=dict(arrowstyle='->', lw=2.5, color=colors['stop']),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#fdedec',
                      edgecolor=colors['stop'], linewidth=2))

# Restore arrow from epoch 10 back to epoch 7
ax.annotate('restore_best_weights\n→ go back to epoch 7',
            xy=(best_epoch, best_val + 0.005),
            xytext=(9.2, 0.30),
            fontsize=11, fontweight='bold', color=colors['best'],
            arrowprops=dict(arrowstyle='->', lw=2, color=colors['best'],
                            connectionstyle='arc3,rad=0.3'),
            bbox=dict(boxstyle='round,pad=0.4', facecolor='#d5f5e3',
                      edgecolor=colors['best'], linewidth=1.5))

# Horizontal dashed line at best val_loss
ax.axhline(y=best_val, color=colors['best'], linestyle='--', linewidth=1.5, alpha=0.4)

# Two scenario boxes at bottom
box_y = 0.22
# patience=3
ax.text(4, box_y, 'With patience=3:\nStops at epoch 10\nRestores epoch 7 weights',
        fontsize=12, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#fef9e7',
                  edgecolor=colors['patience'], linewidth=2))

# patience=5
ax.text(9.5, box_y, 'With patience=5:\nWould keep going →\nMight find something better!',
        fontsize=12, ha='center', va='center', fontweight='bold',
        bbox=dict(boxstyle='round,pad=0.6', facecolor='#eaf2f8',
                  edgecolor=colors['line'], linewidth=2))

# Title
ax.set_title('How Patience Works in EarlyStopping',
             fontsize=20, fontweight='bold', color=colors['primary'], pad=15)
ax.set_xlabel('Epoch', fontsize=14, fontweight='bold')
ax.set_ylabel('Validation Loss', fontsize=14, fontweight='bold')
ax.set_xticks(epochs)
ax.set_xlim(0.3, 11.2)
ax.set_ylim(0.15, 0.58)
ax.grid(True, alpha=0.3)
ax.invert_yaxis()  # Lower loss = better, so flip so "better" is up
# Actually let's NOT invert - lower on chart = lower loss = better, which is intuitive
ax.invert_yaxis()  # undo the invert

# Legend
legend_elements = [
    mpatches.Patch(facecolor=colors['improving'], edgecolor='white', label='Improving'),
    mpatches.Patch(facecolor=colors['best'], edgecolor='white', label='Best Epoch'),
    mpatches.Patch(facecolor=colors['patience'], edgecolor='white', label='Patience Counter'),
]
ax.legend(handles=legend_elements, loc='upper right', fontsize=11,
          frameon=True, fancybox=True)

plt.tight_layout()
plt.savefig('patience_explained.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Created patience_explained.png")

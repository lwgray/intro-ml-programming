# Visual Materials Creation Instructions

## Critical Visual: Training Curves Patterns

### What to Create
PNG or PDF showing 4 training curve patterns side-by-side:
1. Healthy Learning
2. Beginning to Overfit  
3. Severe Overfitting
4. Underfitting

### Specifications
- **Size:** 11x17" or A3 (for printing) OR 1920x1080px (for screen)
- **Format:** PNG (screen) or PDF (print)
- **Tools:** Matplotlib, PowerPoint, Canva, or design software

### Example Matplotlib Code
```python
import matplotlib.pyplot as plt
import numpy as np

fig, axes = plt.subplots(2, 4, figsize=(16, 8))

# Pattern 1: Healthy Learning
epochs = np.arange(20)
train_loss = 0.5 * np.exp(-epochs/10) + 0.1
val_loss = 0.5 * np.exp(-epochs/10) + 0.15

axes[0, 0].plot(epochs, train_loss, label='Train', linewidth=2)
axes[0, 0].plot(epochs, val_loss, label='Val', linewidth=2)
axes[0, 0].set_title('Healthy Learning', fontsize=14, fontweight='bold')
axes[0, 0].legend()

# Repeat for other patterns...
plt.tight_layout()
plt.savefig('training_curves_patterns.png', dpi=300)
```

### Alternative: PowerPoint
1. Create 4 simple line charts
2. Label clearly
3. Export as PDF
4. Print large format

## Other Visuals

### Three-Way Split Diagram
- Simple boxes showing Train/Val/Test
- Can draw on whiteboard during class

### Dropout Mechanism
- Neurons with some crossed out
- Can draw on whiteboard

### EarlyStopping Timeline
- Timeline showing epochs and patience
- Can draw on whiteboard

## Usage During Class

**Display:** Keep training curves patterns visible throughout Segments 3-7
**Reference:** Point to specific patterns when analyzing curves
**Student Copy:** Optionally include in student workbook

*Visual Creation Guide | Version 1.0 | February 2026*

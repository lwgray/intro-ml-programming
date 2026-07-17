"""
Week 7 Visual Materials Generator

This script generates all 8 PNG visual files for Week 7 (Deep Learning Best Practices).
Run this script to create all visual materials at once.

Usage:
    python generate_all_visuals.py

Output:
    Creates 8 PNG files in the current directory:
    1. training_curves_patterns.png
    2. dropout_diagram.png
    3. three_way_split.png
    4. architecture_comparison.png
    5. fashion_mnist_samples.png
    6. early_stopping_flowchart.png
    7. callback_workflow.png
    8. model_saving_formats.png
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle
import numpy as np
import warnings
warnings.filterwarnings('ignore')

# Set style
plt.style.use('seaborn-v0_8-darkgrid')
colors = {
    'train': '#3498db',       # Blue
    'val': '#e74c3c',         # Red
    'healthy': '#2ecc71',     # Green
    'warning': '#f39c12',     # Orange
    'danger': '#e74c3c',      # Red
    'neutral': '#95a5a6',     # Gray
    'background': '#ecf0f1',  # Light gray
    'primary': '#2c3e50',     # Dark blue
    'accent': '#9b59b6',      # Purple
    'dropout': '#bdc3c7',     # Light gray (dropped neurons)
    'active': '#2ecc71',      # Green (active neurons)
}


def generate_training_curves_patterns():
    """Generate the CRITICAL 4-pattern training curves visual (Visual 1)"""
    print("Generating training_curves_patterns.png...")

    fig, axes = plt.subplots(2, 2, figsize=(16, 10), facecolor='white')
    fig.suptitle('Training Curve Patterns: Diagnose Your Model',
                 fontsize=20, fontweight='bold', y=0.98)

    epochs = np.arange(0, 25)
    np.random.seed(42)

    # Pattern 1: Healthy Learning
    ax = axes[0, 0]
    train_loss = 2.0 * np.exp(-epochs / 6) + 0.15 + np.random.normal(0, 0.02, len(epochs))
    val_loss = 2.0 * np.exp(-epochs / 6) + 0.22 + np.random.normal(0, 0.03, len(epochs))
    train_loss = np.maximum(train_loss, 0.1)
    val_loss = np.maximum(val_loss, 0.15)

    ax.plot(epochs, train_loss, linewidth=3, color=colors['train'], label='Training Loss', marker='o', markersize=3)
    ax.plot(epochs, val_loss, linewidth=3, color=colors['val'], label='Validation Loss', marker='s', markersize=3)
    ax.set_title('1. Healthy Learning', fontsize=16, fontweight='bold', color=colors['healthy'])
    ax.set_xlabel('Epoch', fontsize=12)
    ax.set_ylabel('Loss', fontsize=12)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 2.5)

    # Diagnosis box
    ax.text(0.5, 0.15, 'Both ↓ together, small gap\nAction: Continue training',
            transform=ax.transAxes, fontsize=11, ha='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f5e3', edgecolor=colors['healthy'], linewidth=2))

    # Pattern 2: Beginning to Overfit
    ax = axes[0, 1]
    train_loss2 = 2.0 * np.exp(-epochs / 5) + 0.08 + np.random.normal(0, 0.02, len(epochs))
    val_loss2 = np.where(epochs < 10,
                         2.0 * np.exp(-epochs / 5) + 0.25,
                         0.55 + np.random.normal(0, 0.03, len(epochs)))
    val_loss2[:10] += np.random.normal(0, 0.03, 10)
    train_loss2 = np.maximum(train_loss2, 0.05)
    val_loss2 = np.maximum(val_loss2, 0.2)

    ax.plot(epochs, train_loss2, linewidth=3, color=colors['train'], label='Training Loss', marker='o', markersize=3)
    ax.plot(epochs, val_loss2, linewidth=3, color=colors['val'], label='Validation Loss', marker='s', markersize=3)
    ax.set_title('2. Beginning to Overfit', fontsize=16, fontweight='bold', color=colors['warning'])
    ax.set_xlabel('Epoch', fontsize=12)
    ax.set_ylabel('Loss', fontsize=12)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 2.5)

    # Mark divergence point
    ax.axvline(x=10, color=colors['warning'], linestyle='--', linewidth=2, alpha=0.7)
    ax.text(11, 2.0, 'Gap\nwidens', fontsize=10, color=colors['warning'], fontweight='bold')

    ax.text(0.5, 0.15, 'Train ↓, Val → (flattening)\nAction: Watch closely, consider stopping',
            transform=ax.transAxes, fontsize=11, ha='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef9e7', edgecolor=colors['warning'], linewidth=2))

    # Pattern 3: Severe Overfitting
    ax = axes[1, 0]
    train_loss3 = 2.0 * np.exp(-epochs / 4) + 0.03 + np.random.normal(0, 0.01, len(epochs))
    val_loss3_base = np.where(epochs < 8,
                              2.0 * np.exp(-epochs / 5) + 0.3,
                              0.5 + 0.08 * (epochs - 8))
    val_loss3 = val_loss3_base + np.random.normal(0, 0.04, len(epochs))
    train_loss3 = np.maximum(train_loss3, 0.02)
    val_loss3 = np.maximum(val_loss3, 0.2)

    ax.plot(epochs, train_loss3, linewidth=3, color=colors['train'], label='Training Loss', marker='o', markersize=3)
    ax.plot(epochs, val_loss3, linewidth=3, color=colors['val'], label='Validation Loss', marker='s', markersize=3)
    ax.set_title('3. Severe Overfitting', fontsize=16, fontweight='bold', color=colors['danger'])
    ax.set_xlabel('Epoch', fontsize=12)
    ax.set_ylabel('Loss', fontsize=12)
    ax.legend(fontsize=11, loc='center right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 2.5)

    # Annotate divergence
    ax.annotate('', xy=(20, val_loss3[20]), xytext=(20, train_loss3[20]),
                arrowprops=dict(arrowstyle='<->', lw=2, color=colors['danger']))
    ax.text(21, (val_loss3[20] + train_loss3[20]) / 2, 'BIG\nGAP', fontsize=10,
            color=colors['danger'], fontweight='bold')

    ax.text(0.5, 0.15, 'Train ↓↓, Val ↑ (diverging!)\nAction: STOP + add regularization',
            transform=ax.transAxes, fontsize=11, ha='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fdedec', edgecolor=colors['danger'], linewidth=2))

    # Pattern 4: Underfitting
    ax = axes[1, 1]
    train_loss4 = 1.8 - 0.015 * epochs + np.random.normal(0, 0.04, len(epochs))
    val_loss4 = 1.9 - 0.012 * epochs + np.random.normal(0, 0.05, len(epochs))
    train_loss4 = np.maximum(train_loss4, 1.0)
    val_loss4 = np.maximum(val_loss4, 1.1)

    ax.plot(epochs, train_loss4, linewidth=3, color=colors['train'], label='Training Loss', marker='o', markersize=3)
    ax.plot(epochs, val_loss4, linewidth=3, color=colors['val'], label='Validation Loss', marker='s', markersize=3)
    ax.set_title('4. Underfitting', fontsize=16, fontweight='bold', color=colors['neutral'])
    ax.set_xlabel('Epoch', fontsize=12)
    ax.set_ylabel('Loss', fontsize=12)
    ax.legend(fontsize=11, loc='upper right')
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 2.5)

    ax.text(0.5, 0.15, 'Both → (flat, high loss)\nAction: Increase model capacity',
            transform=ax.transAxes, fontsize=11, ha='center',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#eaecee', edgecolor=colors['neutral'], linewidth=2))

    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('training_curves_patterns.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created training_curves_patterns.png")


def generate_dropout_diagram():
    """Generate dropout mechanism visualization (Visual 2)"""
    print("Generating dropout_diagram.png...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), facecolor='white')
    fig.suptitle('Dropout Regularization: "Network on a Diet"',
                 fontsize=18, fontweight='bold', y=0.98)

    def draw_network(ax, title, drop_mask=None):
        """Draw a neural network with optional dropout"""
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        ax.set_title(title, fontsize=15, fontweight='bold', pad=10)

        # Layer positions
        layers = [
            {'x': 2, 'neurons': 4, 'label': 'Input\n(4)'},
            {'x': 4.5, 'neurons': 6, 'label': 'Dense\n(6)'},
            {'x': 7, 'neurons': 6, 'label': 'Dense\n(6)'},
            {'x': 9.5, 'neurons': 3, 'label': 'Output\n(3)'},
        ]

        all_positions = []
        for layer_idx, layer in enumerate(layers):
            x = layer['x']
            n = layer['neurons']
            y_positions = np.linspace(1.5, 6.5, n)
            positions = []

            for neuron_idx, y in enumerate(y_positions):
                # Check if this neuron should be dropped
                is_dropped = False
                if drop_mask and layer_idx in drop_mask:
                    if neuron_idx in drop_mask[layer_idx]:
                        is_dropped = True

                if is_dropped:
                    color = colors['dropout']
                    alpha = 0.3
                    circle = Circle((x, y), 0.2, color=color, ec='gray',
                                    linewidth=1.5, alpha=alpha, linestyle='--')
                    ax.add_patch(circle)
                    # X mark on dropped neuron
                    ax.plot([x - 0.12, x + 0.12], [y - 0.12, y + 0.12],
                            'r-', linewidth=2.5, alpha=0.8)
                    ax.plot([x - 0.12, x + 0.12], [y + 0.12, y - 0.12],
                            'r-', linewidth=2.5, alpha=0.8)
                else:
                    color = colors['active']
                    alpha = 0.8
                    circle = Circle((x, y), 0.2, color=color, ec='black',
                                    linewidth=1.5, alpha=alpha)
                    ax.add_patch(circle)

                positions.append((x, y, is_dropped))

            all_positions.append(positions)

            # Layer label
            ax.text(x, 0.7, layer['label'], fontsize=9, ha='center', fontweight='bold')

        # Draw connections
        for i in range(len(all_positions) - 1):
            for x1, y1, drop1 in all_positions[i]:
                for x2, y2, drop2 in all_positions[i + 1]:
                    if drop1 or drop2:
                        ax.plot([x1 + 0.2, x2 - 0.2], [y1, y2],
                                'k-', linewidth=0.3, alpha=0.05)
                    else:
                        ax.plot([x1 + 0.2, x2 - 0.2], [y1, y2],
                                'k-', linewidth=0.5, alpha=0.2)

    # Left: Training (with dropout)
    drop_mask = {
        1: [0, 3, 5],   # Drop 3 of 6 in first hidden layer (50%)
        2: [1, 4, 2],   # Drop 3 of 6 in second hidden layer (50%)
    }
    draw_network(ax1, 'During Training (Dropout = 0.3)', drop_mask=drop_mask)
    ax1.text(5.75, 7.3, '30% of neurons randomly deactivated each batch',
             fontsize=11, ha='center', style='italic', color=colors['danger'])

    # Right: Inference (all active)
    draw_network(ax2, 'During Inference (All Active)')
    ax2.text(5.75, 7.3, 'All neurons active, weights scaled automatically',
             fontsize=11, ha='center', style='italic', color=colors['active'])

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor=colors['active'], edgecolor='black', label='Active Neuron'),
        mpatches.Patch(facecolor=colors['dropout'], edgecolor='gray',
                       linestyle='--', label='Dropped Neuron'),
    ]
    fig.legend(handles=legend_elements, loc='lower center', ncol=2,
               fontsize=12, frameon=True, fancybox=True)

    plt.tight_layout(rect=[0, 0.06, 1, 0.95])
    plt.savefig('dropout_diagram.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created dropout_diagram.png")


def generate_three_way_split():
    """Generate train/validation/test split visualization (Visual 3)"""
    print("Generating three_way_split.png...")

    fig, ax = plt.subplots(figsize=(16, 7), facecolor='white')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 7)
    ax.axis('off')

    ax.text(5, 6.5, 'Three-Way Data Split: Train / Validation / Test',
            fontsize=20, fontweight='bold', ha='center')

    # Main split bar
    bar_y = 4.5
    bar_height = 1.0

    # Training (60%)
    rect_train = FancyBboxPatch((0.5, bar_y), 5.4, bar_height,
                                 boxstyle="round,pad=0.05",
                                 facecolor=colors['train'], edgecolor='black',
                                 linewidth=2, alpha=0.85)
    ax.add_patch(rect_train)
    ax.text(3.2, bar_y + 0.5, 'Training Set (60%)', fontsize=14,
            ha='center', va='center', fontweight='bold', color='white')
    ax.text(3.2, bar_y - 0.3, '48,000 samples', fontsize=10,
            ha='center', style='italic', color=colors['train'])

    # Validation (20%)
    rect_val = FancyBboxPatch((5.9, bar_y), 1.8, bar_height,
                               boxstyle="round,pad=0.05",
                               facecolor=colors['warning'], edgecolor='black',
                               linewidth=2, alpha=0.85)
    ax.add_patch(rect_val)
    ax.text(6.8, bar_y + 0.5, 'Validation\n(20%)', fontsize=13,
            ha='center', va='center', fontweight='bold', color='white')
    ax.text(6.8, bar_y - 0.3, '12,000 samples', fontsize=10,
            ha='center', style='italic', color=colors['warning'])

    # Test (20%)
    rect_test = FancyBboxPatch((7.7, bar_y), 1.8, bar_height,
                                boxstyle="round,pad=0.05",
                                facecolor=colors['danger'], edgecolor='black',
                                linewidth=2, alpha=0.85)
    ax.add_patch(rect_test)
    ax.text(8.6, bar_y + 0.5, 'Test\n(20%)', fontsize=13,
            ha='center', va='center', fontweight='bold', color='white')
    ax.text(8.6, bar_y - 0.3, '10,000 samples', fontsize=10,
            ha='center', style='italic', color=colors['danger'])

    # Analogy row
    analogy_y = 2.8
    ax.text(5, analogy_y + 0.8, 'The Textbook Analogy', fontsize=14,
            ha='center', fontweight='bold', color=colors['primary'])

    analogies = [
        (3.2, 'Textbook\n(Learn from)', colors['train'],
         'Model trains on this data\nWeights get updated'),
        (6.8, 'Practice Test\n(Check progress)', colors['warning'],
         'Monitor during training\nDetect overfitting'),
        (8.6, 'Final Exam\n(One-time eval)', colors['danger'],
         'NEVER touch until the end\nFinal performance report'),
    ]

    for x, label, color, desc in analogies:
        rect = FancyBboxPatch((x - 1.0, analogy_y - 0.7), 2.0, 0.9,
                               boxstyle="round,pad=0.1",
                               facecolor=color, edgecolor='black',
                               linewidth=1.5, alpha=0.2)
        ax.add_patch(rect)
        ax.text(x, analogy_y, label, fontsize=11, ha='center', va='center',
                fontweight='bold', color=color)
        ax.text(x, analogy_y - 1.1, desc, fontsize=9, ha='center', va='center',
                style='italic')

    # Key rule
    ax.text(5, 0.5, 'GOLDEN RULE: Never use the test set to make training decisions!',
            fontsize=13, ha='center', fontweight='bold', color=colors['danger'],
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fdedec',
                      edgecolor=colors['danger'], linewidth=2))

    plt.tight_layout()
    plt.savefig('three_way_split.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created three_way_split.png")


def generate_architecture_comparison():
    """Generate side-by-side architecture with/without dropout (Visual 4)"""
    print("Generating architecture_comparison.png...")

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8), facecolor='white')
    fig.suptitle('Architecture Comparison: Without vs With Dropout',
                 fontsize=18, fontweight='bold', y=0.98)

    def draw_arch(ax, title, layers_info, title_color='black'):
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis('off')
        ax.set_title(title, fontsize=15, fontweight='bold', color=title_color, pad=10)

        y_cursor = 9.0
        for layer in layers_info:
            name = layer['name']
            color = layer['color']
            height = layer.get('height', 0.8)
            is_dropout = layer.get('is_dropout', False)

            rect = FancyBboxPatch((2, y_cursor - height), 6, height,
                                   boxstyle="round,pad=0.1",
                                   facecolor=color, edgecolor='black',
                                   linewidth=2, alpha=0.8)
            ax.add_patch(rect)

            if is_dropout:
                ax.text(5, y_cursor - height / 2, name, fontsize=11,
                        ha='center', va='center', fontweight='bold',
                        style='italic', color='white')
            else:
                ax.text(5, y_cursor - height / 2, name, fontsize=12,
                        ha='center', va='center', fontweight='bold', color='white')

            # Arrow to next layer
            if layer != layers_info[-1]:
                ax.annotate('', xy=(5, y_cursor - height - 0.15),
                            xytext=(5, y_cursor - height + 0.05),
                            arrowprops=dict(arrowstyle='->', lw=2, color='black'))

            y_cursor -= (height + 0.3)

    # Left: Without Dropout (overfits)
    layers_no_dropout = [
        {'name': 'Input: Flatten(28×28)', 'color': colors['train'], 'height': 0.7},
        {'name': 'Dense(128, relu)', 'color': colors['active'], 'height': 0.8},
        {'name': 'Dense(64, relu)', 'color': colors['active'], 'height': 0.8},
        {'name': 'Dense(10, softmax)', 'color': colors['danger'], 'height': 0.7},
    ]
    draw_arch(ax1, 'Without Dropout → OVERFITS', layers_no_dropout, title_color=colors['danger'])
    ax1.text(5, 0.8, 'Neurons co-adapt\n→ Memorizes training data',
             fontsize=11, ha='center',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#fdedec',
                       edgecolor=colors['danger'], linewidth=2))

    # Right: With Dropout (regularized)
    layers_with_dropout = [
        {'name': 'Input: Flatten(28×28)', 'color': colors['train'], 'height': 0.7},
        {'name': 'Dense(128, relu)', 'color': colors['active'], 'height': 0.8},
        {'name': 'Dropout(0.3)', 'color': colors['accent'], 'height': 0.5, 'is_dropout': True},
        {'name': 'Dense(64, relu)', 'color': colors['active'], 'height': 0.8},
        {'name': 'Dropout(0.3)', 'color': colors['accent'], 'height': 0.5, 'is_dropout': True},
        {'name': 'Dense(10, softmax)', 'color': colors['danger'], 'height': 0.7},
    ]
    draw_arch(ax2, 'With Dropout → GENERALIZES', layers_with_dropout, title_color=colors['active'])
    ax2.text(5, 0.8, 'Forces redundancy\n→ Learns robust patterns',
             fontsize=11, ha='center',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f5e3',
                       edgecolor=colors['active'], linewidth=2))

    # Warning box
    fig.text(0.5, 0.02, 'NEVER place Dropout after the output layer!',
             fontsize=13, ha='center', fontweight='bold', color=colors['danger'],
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#fdedec',
                       edgecolor=colors['danger'], linewidth=2))

    plt.tight_layout(rect=[0, 0.06, 1, 0.95])
    plt.savefig('architecture_comparison.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created architecture_comparison.png")


def generate_fashion_mnist_samples():
    """Generate Fashion-MNIST sample images grid (Visual 5)"""
    print("Generating fashion_mnist_samples.png...")

    try:
        import keras
        import os
        os.environ.setdefault('KERAS_BACKEND', 'torch')
        (X_train, y_train), _ = keras.datasets.fashion_mnist.load_data()

        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

        fig, axes = plt.subplots(2, 5, figsize=(15, 7), facecolor='white')
        fig.suptitle('Fashion-MNIST: 10 Clothing Categories',
                     fontsize=18, fontweight='bold')

        # Show one example per class
        for class_idx in range(10):
            ax = axes[class_idx // 5, class_idx % 5]
            # Find first sample of this class
            idx = np.where(y_train == class_idx)[0][0]
            ax.imshow(X_train[idx], cmap='gray')
            ax.set_title(f'{class_idx}: {class_names[class_idx]}',
                         fontsize=11, fontweight='bold')
            ax.axis('off')

        plt.tight_layout()
        plt.savefig('fashion_mnist_samples.png', dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        print("✓ Created fashion_mnist_samples.png (actual data)")

    except Exception as e:
        print(f"  Could not load Fashion-MNIST, creating placeholder: {e}")

        class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                       'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

        fig, axes = plt.subplots(2, 5, figsize=(15, 7), facecolor='white')
        fig.suptitle('Fashion-MNIST: 10 Clothing Categories',
                     fontsize=18, fontweight='bold')

        np.random.seed(42)
        for class_idx in range(10):
            ax = axes[class_idx // 5, class_idx % 5]
            img = np.random.rand(28, 28) * 0.3 + 0.1
            ax.imshow(img, cmap='gray')
            ax.set_title(f'{class_idx}: {class_names[class_idx]}',
                         fontsize=11, fontweight='bold')
            ax.axis('off')

        fig.text(0.5, 0.01, '(Placeholder - run with keras installed for actual images)',
                 ha='center', fontsize=10, style='italic', color='gray')

        plt.tight_layout()
        plt.savefig('fashion_mnist_samples.png', dpi=300, bbox_inches='tight', facecolor='white')
        plt.close()
        print("✓ Created fashion_mnist_samples.png (placeholder)")


def generate_early_stopping_flowchart():
    """Generate EarlyStopping decision flowchart (Visual 6)"""
    print("Generating early_stopping_flowchart.png...")

    fig, ax = plt.subplots(figsize=(14, 10), facecolor='white')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.5, 'EarlyStopping: "The Validation Alarm"',
            fontsize=18, fontweight='bold', ha='center')

    # Start box
    rect = FancyBboxPatch((5, 8.3), 4, 0.7, boxstyle="round,pad=0.1",
                           facecolor=colors['train'], edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(7, 8.65, 'Start Training\npatience_counter = 0', fontsize=10,
            ha='center', va='center', fontweight='bold', color='white')

    # Arrow down
    ax.annotate('', xy=(7, 7.6), xytext=(7, 8.3),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))

    # Train one epoch
    rect = FancyBboxPatch((5, 7.0), 4, 0.6, boxstyle="round,pad=0.1",
                           facecolor=colors['active'], edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(7, 7.3, 'Train one epoch', fontsize=11,
            ha='center', va='center', fontweight='bold', color='white')

    # Arrow down
    ax.annotate('', xy=(7, 6.3), xytext=(7, 7.0),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))

    # Decision diamond (simulated with rotated square)
    diamond_x, diamond_y = 7, 5.7
    diamond_size = 0.6
    diamond = plt.Polygon([
        (diamond_x, diamond_y + diamond_size),
        (diamond_x + diamond_size * 1.8, diamond_y),
        (diamond_x, diamond_y - diamond_size),
        (diamond_x - diamond_size * 1.8, diamond_y),
    ], facecolor=colors['warning'], edgecolor='black', linewidth=2)
    ax.add_patch(diamond)
    ax.text(diamond_x, diamond_y, 'val_loss\nimproved?', fontsize=10,
            ha='center', va='center', fontweight='bold')

    # YES branch (left)
    ax.annotate('', xy=(3, 5.2), xytext=(5.2, 5.7),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['active']))
    ax.text(4.0, 5.8, 'YES', fontsize=12, fontweight='bold', color=colors['active'])

    rect = FancyBboxPatch((1.5, 4.5), 3, 0.7, boxstyle="round,pad=0.1",
                           facecolor=colors['active'], edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(3, 4.85, 'Reset counter = 0\nSave best weights', fontsize=10,
            ha='center', va='center', fontweight='bold', color='white')

    # Arrow back up to "Train one epoch"
    ax.annotate('', xy=(5, 7.3), xytext=(1.5, 4.85),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['active'],
                                connectionstyle="arc3,rad=-0.3"))

    # NO branch (right)
    ax.annotate('', xy=(11, 5.2), xytext=(8.8, 5.7),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['danger']))
    ax.text(9.8, 5.8, 'NO', fontsize=12, fontweight='bold', color=colors['danger'])

    rect = FancyBboxPatch((9.5, 4.5), 3, 0.7, boxstyle="round,pad=0.1",
                           facecolor=colors['warning'], edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(11, 4.85, 'patience_counter += 1', fontsize=10,
            ha='center', va='center', fontweight='bold')

    # Arrow down from NO
    ax.annotate('', xy=(11, 3.6), xytext=(11, 4.5),
                arrowprops=dict(arrowstyle='->', lw=2, color='black'))

    # Second decision
    diamond2_y = 3.0
    diamond2 = plt.Polygon([
        (11, diamond2_y + 0.5),
        (12.5, diamond2_y),
        (11, diamond2_y - 0.5),
        (9.5, diamond2_y),
    ], facecolor=colors['warning'], edgecolor='black', linewidth=2)
    ax.add_patch(diamond2)
    ax.text(11, diamond2_y, 'counter ≥\npatience?', fontsize=10,
            ha='center', va='center', fontweight='bold')

    # NO - loop back
    ax.annotate('', xy=(9, 7.3), xytext=(9.5, 3.0),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['active'],
                                connectionstyle="arc3,rad=0.3"))
    ax.text(8.8, 4.8, 'NO\n(keep\ngoing)', fontsize=9, fontweight='bold',
            color=colors['active'], ha='center')

    # YES - stop
    ax.annotate('', xy=(11, 1.6), xytext=(11, 2.5),
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['danger']))
    ax.text(11.8, 2.2, 'YES', fontsize=12, fontweight='bold', color=colors['danger'])

    rect = FancyBboxPatch((9, 0.8), 4, 0.8, boxstyle="round,pad=0.1",
                           facecolor=colors['danger'], edgecolor='black', linewidth=2)
    ax.add_patch(rect)
    ax.text(11, 1.2, 'STOP Training!\nRestore best weights', fontsize=11,
            ha='center', va='center', fontweight='bold', color='white')

    # Example box
    example_text = ('Example with patience=3:\n'
                    'Epoch 10: val_loss=0.45 ← Best! (counter=0)\n'
                    'Epoch 11: val_loss=0.46 (counter=1)\n'
                    'Epoch 12: val_loss=0.48 (counter=2)\n'
                    'Epoch 13: val_loss=0.47 (counter=3) → STOP!\n'
                    'Restore weights from Epoch 10')
    ax.text(3.5, 2.5, example_text, fontsize=10, ha='center', va='center',
            family='monospace',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef9e7',
                      edgecolor=colors['warning'], linewidth=2))

    plt.tight_layout()
    plt.savefig('early_stopping_flowchart.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created early_stopping_flowchart.png")


def generate_callback_workflow():
    """Generate callback timeline showing epochs with events (Visual 7)"""
    print("Generating callback_workflow.png...")

    fig, ax = plt.subplots(figsize=(16, 8), facecolor='white')
    ax.set_xlim(0, 22)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(11, 9.5, 'Callback Workflow: EarlyStopping + ModelCheckpoint',
            fontsize=18, fontweight='bold', ha='center')

    # Timeline
    timeline_y = 6.5
    ax.plot([1, 21], [timeline_y, timeline_y], 'k-', linewidth=3)

    # Epoch data
    epochs = list(range(1, 21))
    val_losses = [2.1, 1.5, 1.1, 0.85, 0.72, 0.65, 0.58, 0.52, 0.48, 0.45,
                  0.44, 0.46, 0.45, 0.47, 0.49, 0.51, 0.52, 0.54, 0.56, 0.58]

    best_epoch = 11  # epoch 11 (val_loss=0.44)
    stop_epoch = 14  # patience=3, stops at epoch 14

    for i, (epoch, vl) in enumerate(zip(epochs, val_losses)):
        x = epoch
        if epoch <= stop_epoch:
            # Draw epoch marker
            if epoch == best_epoch:
                color = colors['active']
                marker_size = 12
            elif epoch > best_epoch:
                color = colors['danger']
                marker_size = 8
            else:
                color = colors['train']
                marker_size = 8

            ax.plot(x, timeline_y, 'o', color=color, markersize=marker_size,
                    zorder=5, markeredgecolor='black', markeredgewidth=1)
            ax.text(x, timeline_y - 0.4, str(epoch), fontsize=8, ha='center')

            # Val loss below
            ax.text(x, timeline_y - 0.8, f'{vl:.2f}', fontsize=7,
                    ha='center', color='gray')
        else:
            # Grayed out (not reached)
            ax.plot(x, timeline_y, 'o', color='lightgray', markersize=6,
                    zorder=5, markeredgecolor='gray', markeredgewidth=0.5)
            ax.text(x, timeline_y - 0.4, str(epoch), fontsize=7,
                    ha='center', color='lightgray')

    # Labels
    ax.text(0.5, timeline_y, 'Epoch:', fontsize=10, ha='right', fontweight='bold')
    ax.text(0.5, timeline_y - 0.8, 'val_loss:', fontsize=9, ha='right', color='gray')

    # Best model star
    ax.text(best_epoch, timeline_y + 0.6, '★ BEST', fontsize=12, ha='center',
            fontweight='bold', color=colors['active'])

    # ModelCheckpoint saves
    for e in [5, 8, 10, 11]:
        ax.annotate('💾', xy=(e, timeline_y + 0.3), fontsize=10, ha='center')

    # Stop marker
    ax.annotate('STOP', xy=(stop_epoch, timeline_y + 0.5), fontsize=11,
                ha='center', fontweight='bold', color=colors['danger'],
                bbox=dict(boxstyle='round', facecolor='#fdedec', edgecolor=colors['danger']))

    # Patience bracket
    bracket_y = timeline_y + 1.3
    ax.annotate('', xy=(best_epoch + 0.1, bracket_y), xytext=(stop_epoch - 0.1, bracket_y),
                arrowprops=dict(arrowstyle='<->', lw=2, color=colors['warning']))
    ax.text((best_epoch + stop_epoch) / 2, bracket_y + 0.3, 'patience = 3',
            fontsize=11, ha='center', fontweight='bold', color=colors['warning'])

    # Val loss curve below
    curve_y_base = 3.5
    curve_epochs = epochs[:stop_epoch]
    curve_losses = val_losses[:stop_epoch]

    # Scale to fit
    scaled_x = [e for e in curve_epochs]
    scaled_y = [curve_y_base + (2 - vl) * 1.5 for vl in curve_losses]

    ax.plot(scaled_x, scaled_y, linewidth=3, color=colors['val'],
            marker='s', markersize=5, label='Validation Loss')

    # Train loss (lower)
    train_losses_curve = [2.0, 1.3, 0.9, 0.65, 0.50, 0.40, 0.32, 0.26, 0.22, 0.19,
                          0.17, 0.15, 0.14, 0.13]
    scaled_y_train = [curve_y_base + (2 - tl) * 1.5 for tl in train_losses_curve]
    ax.plot(scaled_x, scaled_y_train, linewidth=3, color=colors['train'],
            marker='o', markersize=5, label='Training Loss')

    ax.text(0.5, curve_y_base + 1.5, 'Loss', fontsize=10, ha='center',
            fontweight='bold', rotation=90)

    # Best epoch vertical line on curve
    best_scaled_y = curve_y_base + (2 - val_losses[best_epoch - 1]) * 1.5
    ax.axvline(x=best_epoch, ymin=0.15, ymax=0.55, color=colors['active'],
               linestyle='--', linewidth=2, alpha=0.7)

    # Restore arrow
    ax.annotate('restore_best_weights\n→ Epoch 11 weights', xy=(best_epoch, best_scaled_y),
                xytext=(best_epoch + 4, best_scaled_y - 0.5),
                fontsize=10, fontweight='bold', color=colors['active'],
                arrowprops=dict(arrowstyle='->', lw=2, color=colors['active']))

    ax.legend(fontsize=11, loc='lower left')

    # Code snippet box
    code = ('EarlyStopping(\n'
            '  monitor="val_loss",\n'
            '  patience=3,\n'
            '  restore_best_weights=True\n'
            ')')
    ax.text(18, 3, code, fontsize=10, ha='center', va='center',
            family='monospace',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#eaecee',
                      edgecolor='black', linewidth=1.5))

    plt.tight_layout()
    plt.savefig('callback_workflow.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created callback_workflow.png")


def generate_model_saving_formats():
    """Generate model saving/loading comparison (Visual 8)"""
    print("Generating model_saving_formats.png...")

    fig, ax = plt.subplots(figsize=(14, 8), facecolor='white')
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.3, 'Model Saving & Loading',
            fontsize=20, fontweight='bold', ha='center')

    # Table header
    header_y = 8.2
    col_x = [3.5, 7, 10.5]
    headers = ['', 'model.save()', 'model.save_weights()']
    for x, h in zip(col_x, headers):
        ax.text(x, header_y, h, fontsize=13, ha='center', fontweight='bold',
                color='white' if h else 'black',
                bbox=dict(boxstyle='round,pad=0.3',
                          facecolor=colors['primary'] if h else 'none',
                          edgecolor='none'))

    # Table rows
    rows = [
        ('Architecture', '✓', '✗'),
        ('Weights', '✓', '✓'),
        ('Optimizer State', '✓', '✗'),
        ('Training Config', '✓', '✗'),
        ('File Format', '.keras', '.weights.h5'),
    ]

    for i, (label, v1, v2) in enumerate(rows):
        y = 7.2 - i * 0.8
        bg_color = '#f8f9fa' if i % 2 == 0 else 'white'

        # Row background
        rect = Rectangle((1, y - 0.3), 12, 0.6, facecolor=bg_color,
                          edgecolor='#dee2e6', linewidth=0.5)
        ax.add_patch(rect)

        ax.text(3.5, y, label, fontsize=12, ha='center', va='center', fontweight='bold')

        for val, x in zip([v1, v2], [7, 10.5]):
            color = colors['active'] if val == '✓' else (colors['danger'] if val == '✗' else 'black')
            fontsize = 16 if val in ('✓', '✗') else 11
            ax.text(x, y, val, fontsize=fontsize, ha='center', va='center',
                    fontweight='bold', color=color)

    # Code examples
    code_y = 3.0
    ax.text(7, code_y + 0.8, 'Code Examples', fontsize=14, ha='center',
            fontweight='bold', color=colors['primary'])

    # Save example
    save_code = ('# Save complete model (RECOMMENDED)\n'
                 'model.save("my_model.keras")\n'
                 '\n'
                 '# Load complete model\n'
                 'loaded_model = keras.models.load_model(\n'
                 '    "my_model.keras"\n'
                 ')')
    ax.text(4, code_y - 0.5, save_code, fontsize=9, ha='center', va='top',
            family='monospace',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f5e3',
                      edgecolor=colors['active'], linewidth=2))

    # Weights example
    weights_code = ('# Save weights only\n'
                    'model.save_weights(\n'
                    '    "my_weights.weights.h5"\n'
                    ')\n'
                    '\n'
                    '# Load weights (rebuild arch first!)\n'
                    'new_model = build_model()\n'
                    'new_model.load_weights(\n'
                    '    "my_weights.weights.h5"\n'
                    ')')
    ax.text(10, code_y - 0.5, weights_code, fontsize=9, ha='center', va='top',
            family='monospace',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#fef9e7',
                      edgecolor=colors['warning'], linewidth=2))

    # Recommendation
    ax.text(7, 0.3, 'Recommendation: Use model.save() for complete portability',
            fontsize=13, ha='center', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#d5f5e3',
                      edgecolor=colors['active'], linewidth=2))

    plt.tight_layout()
    plt.savefig('model_saving_formats.png', dpi=300, bbox_inches='tight', facecolor='white')
    plt.close()
    print("✓ Created model_saving_formats.png")


def main():
    """Generate all visual materials"""
    print("=" * 60)
    print("Week 7 Visual Materials Generator")
    print("Generating 8 PNG files for Deep Learning Best Practices")
    print("=" * 60)
    print()

    try:
        generate_training_curves_patterns()
        generate_dropout_diagram()
        generate_three_way_split()
        generate_architecture_comparison()
        generate_fashion_mnist_samples()
        generate_early_stopping_flowchart()
        generate_callback_workflow()
        generate_model_saving_formats()

        print()
        print("=" * 60)
        print("✓ SUCCESS: All 8 visual files generated!")
        print("=" * 60)
        print()
        print("Generated files:")
        print("  1. training_curves_patterns.png  (CRITICAL - show 5+ times)")
        print("  2. dropout_diagram.png           (Segment 5)")
        print("  3. three_way_split.png           (Segment 2)")
        print("  4. architecture_comparison.png   (Segment 5)")
        print("  5. fashion_mnist_samples.png     (Segment 2)")
        print("  6. early_stopping_flowchart.png  (Segment 5)")
        print("  7. callback_workflow.png         (Segments 5, 6)")
        print("  8. model_saving_formats.png      (Segment 6)")
        print()
        print("These files are ready to use in your Week 7 teaching session!")
        print()

    except Exception as e:
        print()
        print(f"ERROR: {e}")
        print()
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()

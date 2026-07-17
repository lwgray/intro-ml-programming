"""Generate Fashion-MNIST samples grid using torchvision."""

import matplotlib.pyplot as plt
import numpy as np
import torchvision

ds = torchvision.datasets.FashionMNIST(root='/tmp/fmnist', download=True, train=True)

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

fig, axes = plt.subplots(2, 5, figsize=(15, 7), facecolor='white')
fig.suptitle('Fashion-MNIST: 10 Clothing Categories (28×28 Grayscale)',
             fontsize=18, fontweight='bold')

# Show one example per class
for class_idx in range(10):
    ax = axes[class_idx // 5, class_idx % 5]
    # Find first sample of this class
    for i in range(len(ds)):
        img, label = ds[i]
        if label == class_idx:
            ax.imshow(np.array(img), cmap='gray')
            ax.set_title(f'{class_idx}: {class_names[class_idx]}',
                         fontsize=12, fontweight='bold')
            ax.axis('off')
            break

plt.tight_layout()
plt.savefig('fashion_mnist_samples.png', dpi=300, bbox_inches='tight', facecolor='white')
plt.close()
print("✓ Created fashion_mnist_samples.png (actual Fashion-MNIST data)")
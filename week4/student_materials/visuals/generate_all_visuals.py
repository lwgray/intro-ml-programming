"""
Visual Generation Master Script for Week 4
==========================================

This script generates all 7 visual PNG files from the specification documents.

Usage:
    python generate_all_visuals.py

Requirements:
    pip install matplotlib numpy pandas scikit-learn

Output:
    - cv_kfold_diagram.png
    - cv_stratified_comparison.png
    - grid_search_visualization.png
    - regularization_l1_l2_comparison.png
    - bias_variance_tradeoff.png
    - data_leakage_examples.png
    - pipeline_architecture.png

Time: ~3 minutes to generate all visuals
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle, Circle
import numpy as np
import pandas as pd
from sklearn.datasets import make_classification, load_breast_cancer, make_regression
from sklearn.model_selection import train_test_split, cross_val_score, GridSearchCV, learning_curve
from sklearn.linear_model import Ridge, Lasso, LinearRegression
from sklearn.preprocessing import StandardScaler, PolynomialFeatures
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
import sys

print("="*60)
print("Week 4 Visual Generation Script")
print("="*60)
print()

# Visual 1: CV k-Fold Diagram
print("[1/7] Creating cv_kfold_diagram.png...")
try:
    fig, ax = plt.subplots(figsize=(16, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis('off')

    # Title
    ax.text(5, 5.5, '5-Fold Cross-Validation',
            ha='center', fontsize=28, fontweight='bold', color='#003366')

    # Draw 5 folds
    fold_height = 0.6
    fold_y_start = 4.5
    colors = ['#4CAF50', '#2196F3', '#FF9800', '#9C27B0', '#F44336']

    for i in range(5):
        y = fold_y_start - i * 0.8

        # Fold label
        ax.text(-0.3, y + fold_height/2, f'Fold {i+1}',
                ha='right', va='center', fontsize=14, fontweight='bold')

        # Draw 5 sections
        for j in range(5):
            x = j * 2
            if j == (4 - i):  # Test section
                rect = Rectangle((x, y), 1.9, fold_height,
                                facecolor=colors[i], edgecolor='black',
                                linewidth=2, alpha=0.7)
                ax.add_patch(rect)
                ax.text(x + 0.95, y + fold_height/2, 'TEST',
                       ha='center', va='center', fontsize=12,
                       fontweight='bold', color='white')
            else:  # Train section
                rect = Rectangle((x, y), 1.9, fold_height,
                                facecolor='#E0E0E0', edgecolor='black',
                                linewidth=1, alpha=0.5)
                ax.add_patch(rect)
                ax.text(x + 0.95, y + fold_height/2, 'TRAIN',
                       ha='center', va='center', fontsize=10,
                       color='#333333')

    # Summary box
    summary_y = 0.3
    summary_text = ("Each fold uses 80% for training, 20% for testing\n"
                   "Every data point appears in test set exactly once\n"
                   "Final score = average of 5 test scores")
    ax.text(5, summary_y, summary_text,
            ha='center', va='center', fontsize=12,
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF9C4',
                     edgecolor='#F57F17', linewidth=2))

    plt.savefig('cv_kfold_diagram.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ cv_kfold_diagram.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 2: CV Stratified Comparison
print("[2/7] Creating cv_stratified_comparison.png...")
try:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

    # Regular CV (might be imbalanced)
    ax1.set_title('Regular k-Fold CV\n(Folds may be imbalanced)',
                  fontsize=16, fontweight='bold', color='#CC0000')
    ax1.set_xlim(0, 5)
    ax1.set_ylim(0, 5)
    ax1.axis('off')

    # Simulate imbalanced folds
    fold_data = [
        (0.6, 0.4),  # 60% class 0, 40% class 1
        (0.85, 0.15),  # 85% class 0, 15% class 1
        (0.7, 0.3),  # 70% class 0, 30% class 1
        (0.75, 0.25),  # 75% class 0, 25% class 1
        (0.65, 0.35),  # 65% class 0, 35% class 1
    ]

    for i, (class0_pct, class1_pct) in enumerate(fold_data):
        y = 4 - i * 0.8

        # Class 0 portion
        rect0 = Rectangle((0.5, y), class0_pct * 3, 0.5,
                         facecolor='#2196F3', edgecolor='black', linewidth=2)
        ax1.add_patch(rect0)
        ax1.text(0.5 + class0_pct * 1.5, y + 0.25, f'{class0_pct*100:.0f}%',
                ha='center', va='center', fontsize=11, color='white', fontweight='bold')

        # Class 1 portion
        rect1 = Rectangle((0.5 + class0_pct * 3, y), class1_pct * 3, 0.5,
                         facecolor='#FF5722', edgecolor='black', linewidth=2)
        ax1.add_patch(rect1)
        ax1.text(0.5 + class0_pct * 3 + class1_pct * 1.5, y + 0.25,
                f'{class1_pct*100:.0f}%',
                ha='center', va='center', fontsize=11, color='white', fontweight='bold')

        # Fold label
        ax1.text(0.2, y + 0.25, f'F{i+1}',
                ha='center', va='center', fontsize=12, fontweight='bold')

    # Warning text
    ax1.text(2.5, 0.3, '⚠ Fold 2 has only 15% Class 1!\nUnreliable performance estimate',
            ha='center', va='center', fontsize=11, color='#CC0000', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#FFCCBC', edgecolor='#CC0000'))

    # Stratified CV (balanced)
    ax2.set_title('Stratified k-Fold CV\n(Folds maintain class distribution)',
                  fontsize=16, fontweight='bold', color='#00AA00')
    ax2.set_xlim(0, 5)
    ax2.set_ylim(0, 5)
    ax2.axis('off')

    # All folds balanced at 76% / 24%
    true_dist = (0.76, 0.24)

    for i in range(5):
        y = 4 - i * 0.8

        # Class 0 portion
        rect0 = Rectangle((0.5, y), true_dist[0] * 3, 0.5,
                         facecolor='#2196F3', edgecolor='black', linewidth=2)
        ax2.add_patch(rect0)
        ax2.text(0.5 + true_dist[0] * 1.5, y + 0.25, '76%',
                ha='center', va='center', fontsize=11, color='white', fontweight='bold')

        # Class 1 portion
        rect1 = Rectangle((0.5 + true_dist[0] * 3, y), true_dist[1] * 3, 0.5,
                         facecolor='#FF5722', edgecolor='black', linewidth=2)
        ax2.add_patch(rect1)
        ax2.text(0.5 + true_dist[0] * 3 + true_dist[1] * 1.5, y + 0.25, '24%',
                ha='center', va='center', fontsize=11, color='white', fontweight='bold')

        # Fold label
        ax2.text(0.2, y + 0.25, f'F{i+1}',
                ha='center', va='center', fontsize=12, fontweight='bold')

    # Success text
    ax2.text(2.5, 0.3, '✓ All folds match overall distribution\nReliable performance estimate',
            ha='center', va='center', fontsize=11, color='#00AA00', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='#C8E6C9', edgecolor='#00AA00'))

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#2196F3', edgecolor='black', label='Class 0 (<=50K)'),
        mpatches.Patch(facecolor='#FF5722', edgecolor='black', label='Class 1 (>50K)')
    ]
    fig.legend(handles=legend_elements, loc='upper center',
              fontsize=12, ncol=2, bbox_to_anchor=(0.5, 0.95))

    plt.tight_layout(rect=[0, 0, 1, 0.93])
    plt.savefig('cv_stratified_comparison.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ cv_stratified_comparison.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 3: Grid Search Visualization
print("[3/7] Creating grid_search_visualization.png...")
try:
    from mpl_toolkits.mplot3d import Axes3D

    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')

    # Parameter grid
    C_values = [0.01, 0.1, 1.0, 10.0, 100.0]
    max_depth_values = [3, 5, 7, 10, 15]

    # Create meshgrid
    C_grid, depth_grid = np.meshgrid(C_values, max_depth_values)

    # Simulate accuracy scores (realistic pattern)
    np.random.seed(42)
    accuracy = 0.80 + 0.08 * np.sin(np.log10(C_grid + 0.1)) - 0.02 * (depth_grid - 7)**2 / 50
    accuracy += np.random.normal(0, 0.01, accuracy.shape)
    accuracy = np.clip(accuracy, 0.75, 0.88)

    # Plot surface
    surf = ax.plot_surface(np.log10(C_grid), depth_grid, accuracy,
                          cmap='viridis', alpha=0.8, edgecolor='black', linewidth=0.5)

    # Find and mark best point
    best_idx = np.unravel_index(np.argmax(accuracy), accuracy.shape)
    best_C = C_values[best_idx[1]]
    best_depth = max_depth_values[best_idx[0]]
    best_acc = accuracy[best_idx]

    ax.scatter([np.log10(best_C)], [best_depth], [best_acc],
              color='red', s=200, marker='*', edgecolors='black', linewidth=2,
              label=f'Best: C={best_C}, depth={best_depth}, acc={best_acc:.3f}')

    # Labels
    ax.set_xlabel('log10(C)', fontsize=12, labelpad=10)
    ax.set_ylabel('max_depth', fontsize=12, labelpad=10)
    ax.set_zlabel('Accuracy', fontsize=12, labelpad=10)
    ax.set_title('GridSearchCV: Exploring Parameter Space\n(RandomForest on Adult Income)',
                fontsize=16, fontweight='bold', pad=20)

    # Colorbar
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Accuracy')

    # Legend
    ax.legend(fontsize=11, loc='upper left')

    # View angle
    ax.view_init(elev=20, azim=45)

    plt.savefig('grid_search_visualization.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ grid_search_visualization.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 4: Regularization L1 vs L2 Comparison
print("[4/7] Creating regularization_l1_l2_comparison.png...")
try:
    # Generate synthetic regression data
    np.random.seed(42)
    X = np.random.randn(100, 20)
    # Only 5 features are truly predictive
    true_coef = np.zeros(20)
    true_coef[:5] = [5, -3, 2, -4, 3]
    y = X @ true_coef + np.random.randn(100) * 2

    # Standardize
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    # Fit models
    lr = LinearRegression()
    lr.fit(X_scaled, y)

    ridge = Ridge(alpha=1.0)
    ridge.fit(X_scaled, y)

    lasso = Lasso(alpha=0.5)
    lasso.fit(X_scaled, y)

    # Plot coefficients
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    feature_names = [f'F{i+1}' for i in range(20)]
    x_pos = np.arange(20)

    # Linear Regression (no regularization)
    axes[0].bar(x_pos, lr.coef_, color='#3498db', edgecolor='black', linewidth=1)
    axes[0].set_title('Linear Regression (No Regularization)\nAll features kept',
                      fontsize=14, fontweight='bold', color='#3498db')
    axes[0].set_xlabel('Feature', fontsize=12)
    axes[0].set_ylabel('Coefficient Value', fontsize=12)
    axes[0].set_xticks(x_pos)
    axes[0].set_xticklabels(feature_names, rotation=45, ha='right')
    axes[0].grid(axis='y', alpha=0.3)
    axes[0].axhline(y=0, color='black', linewidth=1)

    # Ridge (L2)
    axes[1].bar(x_pos, ridge.coef_, color='#e74c3c', edgecolor='black', linewidth=1)
    axes[1].set_title('Ridge Regression (L2 Regularization)\nShrinks all coefficients',
                      fontsize=14, fontweight='bold', color='#e74c3c')
    axes[1].set_xlabel('Feature', fontsize=12)
    axes[1].set_ylabel('Coefficient Value', fontsize=12)
    axes[1].set_xticks(x_pos)
    axes[1].set_xticklabels(feature_names, rotation=45, ha='right')
    axes[1].grid(axis='y', alpha=0.3)
    axes[1].axhline(y=0, color='black', linewidth=1)

    # Lasso (L1)
    colors = ['#2ecc71' if abs(c) > 0.01 else '#cccccc' for c in lasso.coef_]
    axes[2].bar(x_pos, lasso.coef_, color=colors, edgecolor='black', linewidth=1)
    axes[2].set_title('Lasso Regression (L1 Regularization)\nSets some coefficients to zero',
                      fontsize=14, fontweight='bold', color='#2ecc71')
    axes[2].set_xlabel('Feature', fontsize=12)
    axes[2].set_ylabel('Coefficient Value', fontsize=12)
    axes[2].set_xticks(x_pos)
    axes[2].set_xticklabels(feature_names, rotation=45, ha='right')
    axes[2].grid(axis='y', alpha=0.3)
    axes[2].axhline(y=0, color='black', linewidth=1)

    # Add summary text
    non_zero_lasso = np.sum(np.abs(lasso.coef_) > 0.01)
    fig.text(0.5, 0.02,
             f'True predictors: F1-F5 | Lasso selected: {non_zero_lasso} features | Ridge kept all 20 features',
             ha='center', fontsize=12, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFF9C4', edgecolor='#F57F17'))

    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig('regularization_l1_l2_comparison.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ regularization_l1_l2_comparison.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 5: Bias-Variance Tradeoff
print("[5/7] Creating bias_variance_tradeoff.png...")
try:
    # Generate synthetic data
    np.random.seed(42)
    X = np.linspace(0, 10, 100).reshape(-1, 1)
    y_true = np.sin(X).ravel()
    y_noisy = y_true + np.random.normal(0, 0.2, X.shape[0])

    # Create three models with different complexity
    poly_features_1 = PolynomialFeatures(degree=1)
    poly_features_5 = PolynomialFeatures(degree=5)
    poly_features_20 = PolynomialFeatures(degree=20)

    X_poly_1 = poly_features_1.fit_transform(X)
    X_poly_5 = poly_features_5.fit_transform(X)
    X_poly_20 = poly_features_20.fit_transform(X)

    model_1 = LinearRegression().fit(X_poly_1, y_noisy)
    model_5 = LinearRegression().fit(X_poly_5, y_noisy)
    model_20 = LinearRegression().fit(X_poly_20, y_noisy)

    # Predictions
    y_pred_1 = model_1.predict(X_poly_1)
    y_pred_5 = model_5.predict(X_poly_5)
    y_pred_20 = model_20.predict(X_poly_20)

    # Plot
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Underfitting (High Bias)
    axes[0].scatter(X, y_noisy, c='#3498db', s=30, alpha=0.5, label='Training Data')
    axes[0].plot(X, y_true, 'k--', linewidth=2, label='True Function')
    axes[0].plot(X, y_pred_1, 'r-', linewidth=3, label='Linear Model (degree=1)')
    axes[0].set_title('UNDERFITTING (High Bias)\nToo Simple Model',
                      fontsize=14, fontweight='bold', color='#e74c3c')
    axes[0].set_xlabel('X', fontsize=12)
    axes[0].set_ylabel('y', fontsize=12)
    axes[0].legend(fontsize=10)
    axes[0].grid(alpha=0.3)
    axes[0].text(0.5, 0.95, '❌ Train Error: High\n❌ Test Error: High',
                transform=axes[0].transAxes, fontsize=11, va='top', ha='center',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFCCBC', edgecolor='#e74c3c'))

    # Good Fit (Balance)
    axes[1].scatter(X, y_noisy, c='#3498db', s=30, alpha=0.5, label='Training Data')
    axes[1].plot(X, y_true, 'k--', linewidth=2, label='True Function')
    axes[1].plot(X, y_pred_5, 'g-', linewidth=3, label='Polynomial Model (degree=5)')
    axes[1].set_title('GOOD FIT (Balanced)\nJust Right',
                      fontsize=14, fontweight='bold', color='#2ecc71')
    axes[1].set_xlabel('X', fontsize=12)
    axes[1].set_ylabel('y', fontsize=12)
    axes[1].legend(fontsize=10)
    axes[1].grid(alpha=0.3)
    axes[1].text(0.5, 0.95, '✓ Train Error: Low\n✓ Test Error: Low',
                transform=axes[1].transAxes, fontsize=11, va='top', ha='center',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#C8E6C9', edgecolor='#2ecc71'))

    # Overfitting (High Variance)
    axes[2].scatter(X, y_noisy, c='#3498db', s=30, alpha=0.5, label='Training Data')
    axes[2].plot(X, y_true, 'k--', linewidth=2, label='True Function')
    axes[2].plot(X, y_pred_20, 'm-', linewidth=3, label='Polynomial Model (degree=20)')
    axes[2].set_title('OVERFITTING (High Variance)\nToo Complex Model',
                      fontsize=14, fontweight='bold', color='#9b59b6')
    axes[2].set_xlabel('X', fontsize=12)
    axes[2].set_ylabel('y', fontsize=12)
    axes[2].legend(fontsize=10)
    axes[2].grid(alpha=0.3)
    axes[2].text(0.5, 0.95, '✓ Train Error: Very Low\n❌ Test Error: High',
                transform=axes[2].transAxes, fontsize=11, va='top', ha='center',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#E1BEE7', edgecolor='#9b59b6'))

    plt.suptitle('Bias-Variance Tradeoff', fontsize=18, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.savefig('bias_variance_tradeoff.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ bias_variance_tradeoff.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 6: Data Leakage Examples
print("[6/7] Creating data_leakage_examples.png...")
try:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9))

    # WRONG: Data leakage
    ax1.set_xlim(0, 10)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    ax1.set_title('❌ DATA LEAKAGE (WRONG)\nScaling before split',
                  fontsize=16, fontweight='bold', color='#CC0000')

    # Flow diagram - WRONG
    boxes_wrong = [
        ('Full Dataset\n(10,000 samples)', 5, 9, '#3498db'),
        ('StandardScaler.fit()\non ALL data', 5, 7.5, '#e74c3c'),
        ('Train Set\n(8,000)', 2.5, 6, '#90EE90'),
        ('Test Set\n(2,000)', 7.5, 6, '#FFB6C1'),
        ('Model Training', 2.5, 4.5, '#90EE90'),
        ('Model Testing', 7.5, 4.5, '#FFB6C1'),
        ('Overly Optimistic\nPerformance', 5, 3, '#CC0000')
    ]

    for label, x, y, color in boxes_wrong:
        box = FancyBboxPatch((x-0.8, y-0.4), 1.6, 0.8,
                            boxstyle='round,pad=0.1',
                            facecolor=color, edgecolor='black', linewidth=2)
        ax1.add_patch(box)
        ax1.text(x, y, label, ha='center', va='center',
                fontsize=10, fontweight='bold')

    # Arrows - WRONG
    arrow_wrong = [
        (5, 8.6, 5, 7.9),
        (5, 7.1, 2.5, 6.4),
        (5, 7.1, 7.5, 6.4),
        (2.5, 5.6, 2.5, 4.9),
        (7.5, 5.6, 7.5, 4.9),
        (2.5, 4.1, 5, 3.4),
        (7.5, 4.1, 5, 3.4)
    ]

    for x1, y1, x2, y2 in arrow_wrong:
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                               arrowstyle='->', mutation_scale=20,
                               linewidth=2, color='black')
        ax1.add_patch(arrow)

    # Leakage annotation
    ax1.annotate('LEAKAGE!\nTest data influenced\nscaler parameters',
                xy=(5, 7.5), xytext=(7.5, 8.5),
                fontsize=11, color='#CC0000', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFCCBC', edgecolor='#CC0000'),
                arrowprops=dict(arrowstyle='->', color='#CC0000', linewidth=3))

    # CORRECT: No leakage
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    ax2.set_title('✓ NO LEAKAGE (CORRECT)\nPipeline ensures safety',
                  fontsize=16, fontweight='bold', color='#00AA00')

    # Flow diagram - CORRECT
    boxes_correct = [
        ('Full Dataset\n(10,000 samples)', 5, 9, '#3498db'),
        ('Train/Test Split\nFIRST', 5, 7.5, '#FFA500'),
        ('Train Set\n(8,000)', 2.5, 6, '#90EE90'),
        ('Test Set\n(2,000)', 7.5, 6, '#FFB6C1'),
        ('Pipeline:\nScaler + Model\nfit on train only', 2.5, 4.5, '#90EE90'),
        ('Pipeline.predict()\ntest data', 7.5, 4.5, '#FFB6C1'),
        ('Reliable\nPerformance', 5, 3, '#00AA00')
    ]

    for label, x, y, color in boxes_correct:
        box = FancyBboxPatch((x-0.8, y-0.4), 1.6, 0.8,
                            boxstyle='round,pad=0.1',
                            facecolor=color, edgecolor='black', linewidth=2)
        ax2.add_patch(box)
        ax2.text(x, y, label, ha='center', va='center',
                fontsize=10, fontweight='bold')

    # Arrows - CORRECT
    arrow_correct = [
        (5, 8.6, 5, 7.9),
        (5, 7.1, 2.5, 6.4),
        (5, 7.1, 7.5, 6.4),
        (2.5, 5.6, 2.5, 4.9),
        (7.5, 5.6, 7.5, 4.9),
        (2.5, 4.1, 5, 3.4),
        (7.5, 4.1, 5, 3.4)
    ]

    for x1, y1, x2, y2 in arrow_correct:
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                               arrowstyle='->', mutation_scale=20,
                               linewidth=2, color='black')
        ax2.add_patch(arrow)

    # Safe annotation
    ax2.annotate('SAFE!\nTest data never\nseen during training',
                xy=(7.5, 6), xytext=(8.5, 7.5),
                fontsize=11, color='#00AA00', fontweight='bold',
                bbox=dict(boxstyle='round,pad=0.5', facecolor='#C8E6C9', edgecolor='#00AA00'),
                arrowprops=dict(arrowstyle='->', color='#00AA00', linewidth=3))

    plt.tight_layout()
    plt.savefig('data_leakage_examples.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ data_leakage_examples.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 7: Pipeline Architecture
print("[7/7] Creating pipeline_architecture.png...")
try:
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(5, 9.5, 'Production ML Pipeline Architecture',
            ha='center', fontsize=24, fontweight='bold', color='#003366')

    # Pipeline components
    components = [
        ('Raw Data\n(mixed types)', 1.5, 7.5, '#3498db', 1.2),
        ('Column\nTransformer', 3.5, 7.5, '#e67e22', 1.2),
        ('Standardized\nData', 5.5, 7.5, '#9b59b6', 1.2),
        ('Model\n(RF/XGB)', 7.5, 7.5, '#2ecc71', 1.2),
        ('Predictions', 9, 7.5, '#e74c3c', 0.8)
    ]

    for label, x, y, color, width in components:
        box = FancyBboxPatch((x-width/2, y-0.6), width, 1.2,
                            boxstyle='round,pad=0.1',
                            facecolor=color, edgecolor='black', linewidth=3)
        ax.add_patch(box)
        ax.text(x, y, label, ha='center', va='center',
                fontsize=12, fontweight='bold', color='white')

    # Arrows between components
    arrows = [(1.5+0.6, 7.5, 3.5-0.6, 7.5),
              (3.5+0.6, 7.5, 5.5-0.6, 7.5),
              (5.5+0.6, 7.5, 7.5-0.6, 7.5),
              (7.5+0.6, 7.5, 9-0.4, 7.5)]

    for x1, y1, x2, y2 in arrows:
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                               arrowstyle='->', mutation_scale=30,
                               linewidth=4, color='black')
        ax.add_patch(arrow)

    # Details below
    details_y = 5.5

    # Column Transformer details
    ct_box = FancyBboxPatch((0.5, details_y-1), 3, 2,
                            boxstyle='round,pad=0.2',
                            facecolor='#FFF9C4', edgecolor='#e67e22', linewidth=2)
    ax.add_patch(ct_box)
    ax.text(2, details_y+0.6, 'ColumnTransformer',
            ha='center', fontsize=13, fontweight='bold', color='#e67e22')
    ax.text(2, details_y+0.2, '• Numeric: StandardScaler',
            ha='center', fontsize=10)
    ax.text(2, details_y-0.1, '• Categorical: OneHotEncoder',
            ha='center', fontsize=10)
    ax.text(2, details_y-0.4, '• Handles mixed data types',
            ha='center', fontsize=10)

    # Pipeline wrapper details
    pipe_box = FancyBboxPatch((4, details_y-1), 3, 2,
                             boxstyle='round,pad=0.2',
                             facecolor='#E1F5FE', edgecolor='#2196F3', linewidth=2)
    ax.add_patch(pipe_box)
    ax.text(5.5, details_y+0.6, 'Pipeline Wrapper',
            ha='center', fontsize=13, fontweight='bold', color='#2196F3')
    ax.text(5.5, details_y+0.2, '• Prevents data leakage',
            ha='center', fontsize=10)
    ax.text(5.5, details_y-0.1, '• Ensures reproducibility',
            ha='center', fontsize=10)
    ax.text(5.5, details_y-0.4, '• Deployment-ready',
            ha='center', fontsize=10)

    # GridSearchCV integration
    gs_box = FancyBboxPatch((7.5, details_y-1), 2, 2,
                            boxstyle='round,pad=0.2',
                            facecolor='#F3E5F5', edgecolor='#9C27B0', linewidth=2)
    ax.add_patch(gs_box)
    ax.text(8.5, details_y+0.6, 'GridSearchCV',
            ha='center', fontsize=13, fontweight='bold', color='#9C27B0')
    ax.text(8.5, details_y+0.2, '• Hyperparameter',
            ha='center', fontsize=10)
    ax.text(8.5, details_y-0.1, '  tuning',
            ha='center', fontsize=10)
    ax.text(8.5, details_y-0.4, '• Cross-validation',
            ha='center', fontsize=10)

    # Code example at bottom
    code_y = 2
    code_box = FancyBboxPatch((1, code_y-1), 8, 1.8,
                             boxstyle='round,pad=0.3',
                             facecolor='#ECEFF1', edgecolor='#003366', linewidth=2)
    ax.add_patch(code_box)

    code_text = ("pipeline = Pipeline([\n"
                "    ('preprocessor', ColumnTransformer([...])),\n"
                "    ('classifier', RandomForestClassifier())\n"
                "])\n"
                "GridSearchCV(pipeline, param_grid, cv=5).fit(X_train, y_train)")

    ax.text(5, code_y, code_text,
            ha='center', va='center', fontsize=10,
            family='monospace', color='#003366')

    plt.tight_layout()
    plt.savefig('pipeline_architecture.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ pipeline_architecture.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Summary
print()
print("="*60)
print("Visual Generation Complete!")
print("="*60)
print()
print("Generated files:")
print("  1. cv_kfold_diagram.png")
print("  2. cv_stratified_comparison.png")
print("  3. grid_search_visualization.png")
print("  4. regularization_l1_l2_comparison.png")
print("  5. bias_variance_tradeoff.png")
print("  6. data_leakage_examples.png")
print("  7. pipeline_architecture.png")
print()
print("All visuals ready for use in Week 4 teaching!")
print("="*60)

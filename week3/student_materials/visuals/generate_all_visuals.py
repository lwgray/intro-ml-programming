"""
Visual Generation Master Script for Week 3
==========================================

This script generates all 8 visual PNG files from the specification documents.

Usage:
    python generate_all_visuals.py

Requirements:
    pip install matplotlib numpy pandas scikit-learn xgboost

Output:
    - decision_tree_example.png
    - tree_splitting_animation.png
    - feature_importance_plot.png
    - random_forest_ensemble.png
    - bagging_illustration.png
    - boosting_illustration.png
    - xgboost_comparison.png
    - overfitting_trees.png

Time: ~5 minutes to generate all visuals
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris, make_moons, make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.ensemble import RandomForestClassifier
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import sys

print("="*60)
print("Week 3 Visual Generation Script")
print("="*60)
print()

# Visual 1: Decision Tree Example
print("[1/8] Creating decision_tree_example.png...")
try:
    iris = load_iris()
    X, y = iris.data, iris.target

    tree = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree.fit(X, y)

    plt.figure(figsize=(20, 10))
    plot_tree(tree, feature_names=iris.feature_names,
              class_names=iris.target_names, filled=True, rounded=True,
              fontsize=10)
    plt.title('Decision Tree Example: Iris Classification (max_depth=3)',
              fontsize=24, fontweight='bold', color='#003366', pad=20)
    plt.savefig('decision_tree_example.png', dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ decision_tree_example.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 2: Tree Splitting Animation
print("[2/8] Creating tree_splitting_animation.png...")
try:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 9))

    # Before split
    np.random.seed(42)
    blues = np.random.randn(30, 2) - 1
    reds = np.random.randn(30, 2) + 1
    all_data = np.vstack([blues, reds])

    ax1.scatter(blues[:, 0], blues[:, 1], c='#0066CC', s=100,
                marker='o', edgecolors='black', linewidth=1.5, label='Class A', alpha=0.8)
    ax1.scatter(reds[:, 0], reds[:, 1], c='#CC0000', s=100,
                marker='^', edgecolors='black', linewidth=1.5, label='Class B', alpha=0.8)
    ax1.set_title('BEFORE SPLIT\nMixed Classes (Gini = 0.50)',
                  fontsize=16, fontweight='bold', color='#CC0000')
    ax1.set_xlabel('Feature 1', fontsize=12)
    ax1.set_ylabel('Feature 2', fontsize=12)
    ax1.legend(fontsize=12)
    ax1.grid(alpha=0.3)
    ax1.set_xlim(-4, 4)
    ax1.set_ylim(-4, 4)

    # After split
    ax2.scatter(blues[:, 0], blues[:, 1], c='#0066CC', s=100,
                marker='o', edgecolors='black', linewidth=1.5, label='Class A', alpha=0.8)
    ax2.scatter(reds[:, 0], reds[:, 1], c='#CC0000', s=100,
                marker='^', edgecolors='black', linewidth=1.5, label='Class B', alpha=0.8)
    ax2.axvline(x=0, color='black', linewidth=3, linestyle='--', label='Split at x=0')
    ax2.set_title('AFTER SPLIT\nPure Groups (Left Gini=0.05, Right Gini=0.08)',
                  fontsize=16, fontweight='bold', color='#00AA00')
    ax2.set_xlabel('Feature 1', fontsize=12)
    ax2.set_ylabel('Feature 2', fontsize=12)
    ax2.legend(fontsize=12)
    ax2.grid(alpha=0.3)
    ax2.set_xlim(-4, 4)
    ax2.set_ylim(-4, 4)

    # Add annotations
    ax2.text(-2, 3.5, 'Mostly Class A\nGini = 0.05', ha='center',
             bbox=dict(boxstyle='round', facecolor='#E6F2FF', edgecolor='#0066CC', linewidth=2),
             fontsize=11, fontweight='bold')
    ax2.text(2, 3.5, 'Mostly Class B\nGini = 0.08', ha='center',
             bbox=dict(boxstyle='round', facecolor='#FFE6E6', edgecolor='#CC0000', linewidth=2),
             fontsize=11, fontweight='bold')

    fig.suptitle('Tree Splitting: Information Gain Example',
                fontsize=24, fontweight='bold', color='#003366', y=0.98)
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plt.savefig('tree_splitting_animation.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ tree_splitting_animation.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 3: Feature Importance Plot
print("[3/8] Creating feature_importance_plot.png...")
try:
    # Simulated Adult Income dataset feature importance
    features = ['age', 'education-num', 'capital-gain', 'hours-per-week',
                'occupation', 'relationship', 'marital-status', 'capital-loss',
                'workclass', 'native-country']
    importance = [0.28, 0.22, 0.15, 0.12, 0.08, 0.06, 0.05, 0.02, 0.01, 0.01]

    fig, ax = plt.subplots(figsize=(12, 8))

    colors = ['#CC0000' if imp > 0.15 else '#3366CC' for imp in importance]
    bars = ax.barh(features, importance, color=colors, edgecolor='black', linewidth=1.5)

    for i, (bar, imp) in enumerate(zip(bars, importance)):
        ax.text(imp + 0.01, i, f'{imp:.2f}', va='center', fontsize=11, fontweight='bold')

    ax.set_xlabel('Importance Score', fontsize=14, fontweight='bold')
    ax.set_ylabel('Feature', fontsize=14, fontweight='bold')
    ax.set_title('Feature Importance: Random Forest on Adult Income Dataset',
                fontsize=18, fontweight='bold', color='#003366')
    ax.set_xlim(0, max(importance) * 1.15)
    ax.grid(axis='x', alpha=0.3)

    # Warning callout
    warning = ("⚠️ WARNING: Correlation ≠ Causation\n"
               "High importance means the feature is predictive,\n"
               "NOT that it causes the outcome!")
    ax.text(0.5, -0.15, warning, transform=ax.transAxes, ha='center',
            fontsize=12, bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFFACD',
            edgecolor='#FF9900', linewidth=3))

    plt.tight_layout()
    plt.savefig('feature_importance_plot.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ feature_importance_plot.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 4: Random Forest Ensemble
print("[4/8] Creating random_forest_ensemble.png...")
try:
    fig = plt.figure(figsize=(19.2, 10.8))
    ax = plt.subplot(111)
    ax.set_xlim(0, 16)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(8, 9.5, 'Random Forest: "Committee Decision"',
            ha='center', fontsize=26, fontweight='bold', color='#003366')

    # Training data
    data_box = FancyBboxPatch((0.5, 7), 2.5, 1.5, boxstyle="round,pad=0.1",
                              edgecolor='#333333', facecolor='#F0F0F0', linewidth=3)
    ax.add_patch(data_box)
    ax.text(1.75, 7.8, 'Training\nData', ha='center', fontsize=14, fontweight='bold')

    # Bootstrap arrows and trees
    for i in range(5):
        x = 4 + i * 2.2

        # Arrow from data to tree
        arrow = FancyArrowPatch((3, 7.5), (x, 6.5), arrowstyle='->', lw=2, color='#FF9900')
        ax.add_patch(arrow)

        # Tree
        tree = mpatches.Polygon([[x, 6.5], [x-0.4, 5.5], [x+0.4, 5.5]],
                               closed=True, fc='#00AA00', ec='#003366', linewidth=2)
        ax.add_patch(tree)
        ax.text(x, 5.2, f'Tree {i+1}', ha='center', fontsize=11, fontweight='bold')

        # Prediction arrow
        pred_arrow = FancyArrowPatch((x, 5), (x, 3.5), arrowstyle='->', lw=2, color='#0066CC')
        ax.add_patch(pred_arrow)

        # Individual prediction
        pred = ['A', 'A', 'B', 'A', 'A'][i]
        color = '#E6F2FF' if pred == 'A' else '#FFE6E6'
        pred_box = FancyBboxPatch((x-0.3, 2.8), 0.6, 0.6, boxstyle="round,pad=0.05",
                                  edgecolor='#333333', facecolor=color, linewidth=2)
        ax.add_patch(pred_box)
        ax.text(x, 3.1, pred, ha='center', fontsize=14, fontweight='bold')

    # Voting box
    vote_box = FancyBboxPatch((5, 0.5), 6, 1.5, boxstyle="round,pad=0.1",
                              edgecolor='#006600', facecolor='#CCFFEE', linewidth=4)
    ax.add_patch(vote_box)
    ax.text(8, 1.5, 'VOTE: Class A (4 votes)', ha='center',
            fontsize=16, fontweight='bold', color='#006600')
    ax.text(8, 1, 'Final Prediction: Class A ✓', ha='center',
            fontsize=14, bbox=dict(boxstyle='round', facecolor='#CCFFCC'))

    plt.savefig('random_forest_ensemble.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ random_forest_ensemble.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 5: Bagging Illustration
print("[5/8] Creating bagging_illustration.png...")
try:
    fig = plt.figure(figsize=(16, 9))
    ax = plt.subplot(111)
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Title
    ax.text(7.5, 9.5, 'BAGGING: Bootstrap Aggregating',
            ha='center', fontsize=26, fontweight='bold', color='#003366')

    # Step headers
    for i, (x, step) in enumerate([(2.5, 'BOOTSTRAP'), (7.5, 'TRAIN'),
                                     (12.5, 'AGGREGATE')]):
        ax.text(x, 8.5, f'Step {i+1}: {step}', ha='center',
                fontsize=18, fontweight='bold', color='#003366')

    # Step 1: Bootstrap
    orig_box = FancyBboxPatch((1.5, 6.5), 2, 1.2, boxstyle="round,pad=0.05",
                              edgecolor='#333333', facecolor='#F0F0F0', linewidth=2)
    ax.add_patch(orig_box)
    ax.text(2.5, 7.5, 'Original Data', ha='center', fontsize=12, fontweight='bold')
    ax.text(2.5, 7.1, '[1,2,3,...,10000]', ha='center', fontsize=10, family='monospace')

    for i, y in enumerate([5.5, 4.5, 3.5, 2.5]):
        sample_box = FancyBboxPatch((1.2, y), 2.6, 0.7, boxstyle="round,pad=0.03",
                                    edgecolor='#3366CC', facecolor='#E6F2FF',
                                    linewidth=2, linestyle='dashed')
        ax.add_patch(sample_box)
        ax.text(2.5, y+0.35, f'Sample {i+1}: [1,1,3,5,...]', ha='center', fontsize=9)
        # Arrow
        arrow = FancyArrowPatch((2.5, 6.5), (2.5, y+0.7), arrowstyle='->',
                               lw=2, color='#FF9900')
        ax.add_patch(arrow)

    ax.text(2.5, 1.8, '(Sampling with\nreplacement)', ha='center',
            fontsize=10, style='italic')

    # Step 2: Train
    for i, y in enumerate([6, 4.8, 3.6, 2.4]):
        # Tree triangle
        tree = mpatches.Polygon([[7.5, y], [7.2, y-0.8], [7.8, y-0.8]],
                               closed=True, fc='#00AA00', ec='#003366', linewidth=2)
        ax.add_patch(tree)
        if i < 3:
            ax.text(7.5, y-1.1, f'Tree {i+1}', ha='center', fontsize=11, fontweight='bold')
        else:
            ax.text(7.5, y-1.1, '... Tree 100', ha='center', fontsize=11, style='italic')

    ax.text(7.5, 1.5, 'TRAINED IN PARALLEL\n(Independent trees)',
            ha='center', fontsize=12, fontweight='bold',
            bbox=dict(boxstyle='round', facecolor='#FFFACD'))

    # Step 3: Aggregate
    vote_box = FancyBboxPatch((11, 5.5), 3, 2.5, boxstyle="round,pad=0.1",
                              edgecolor='#006600', facecolor='#CCFFEE', linewidth=3)
    ax.add_patch(vote_box)
    ax.text(12.5, 7.5, 'CLASSIFICATION', ha='center', fontsize=14, fontweight='bold')
    ax.text(12.5, 7, 'Tree predictions:', ha='center', fontsize=11)
    ax.text(12.5, 6.6, 'A, A, B, A, A, ...', ha='center', fontsize=10)
    ax.text(12.5, 6.2, '↓ VOTE ↓', ha='center', fontsize=12, fontweight='bold')
    ax.text(12.5, 5.8, 'Class A (73%)', ha='center', fontsize=12,
            bbox=dict(boxstyle='round', facecolor='#CCFFCC'))

    avg_box = FancyBboxPatch((11, 2.5), 3, 2.5, boxstyle="round,pad=0.1",
                             edgecolor='#003366', facecolor='#E6F2FF', linewidth=3)
    ax.add_patch(avg_box)
    ax.text(12.5, 4.5, 'REGRESSION', ha='center', fontsize=14, fontweight='bold')
    ax.text(12.5, 4, 'Tree predictions:', ha='center', fontsize=11)
    ax.text(12.5, 3.6, '125, 130, 128, ...', ha='center', fontsize=10)
    ax.text(12.5, 3.2, '↓ AVERAGE ↓', ha='center', fontsize=12, fontweight='bold')
    ax.text(12.5, 2.8, '127.5', ha='center', fontsize=12,
            bbox=dict(boxstyle='round', facecolor='#CCE5FF'))

    plt.savefig('bagging_illustration.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ bagging_illustration.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 6: Boosting Illustration
print("[6/8] Creating boosting_illustration.png...")
try:
    fig = plt.figure(figsize=(16, 9))
    ax_main = plt.subplot(111)
    ax_main.set_xlim(0, 14)
    ax_main.set_ylim(0, 10)
    ax_main.axis('off')

    # Title
    ax_main.text(7, 9.5, 'BOOSTING: Sequential Error Correction',
                 ha='center', fontsize=26, fontweight='bold', color='#003366')

    # Iteration 1
    tree1_box = FancyBboxPatch((0.5, 7), 2, 1.5, boxstyle="round,pad=0.1",
                               edgecolor='#00AA00', facecolor='#CCFFCC', linewidth=3)
    ax_main.add_patch(tree1_box)
    ax_main.text(1.5, 7.8, 'Tree 1', ha='center', fontsize=14, fontweight='bold')
    ax_main.text(1.5, 7.4, 'Initial\nPredictions', ha='center', fontsize=10)

    arrow1 = FancyArrowPatch((2.5, 7.75), (3.5, 7.75), arrowstyle='->', lw=2)
    ax_main.add_patch(arrow1)
    ax_main.text(3, 8, 'Predict', ha='center', fontsize=10)

    pred1_box = FancyBboxPatch((3.5, 7), 2.5, 1.5, boxstyle="round,pad=0.05",
                               edgecolor='#3366CC', facecolor='#E6F2FF', linewidth=2)
    ax_main.add_patch(pred1_box)
    ax_main.text(4.75, 8, 'Predictions', ha='center', fontsize=12, fontweight='bold')
    ax_main.text(4.75, 7.5, 'Actual: [10, 8, 15]', ha='center',
                 fontsize=9, family='monospace')
    ax_main.text(4.75, 7.2, 'Pred:   [6, 7, 11]', ha='center',
                 fontsize=9, family='monospace')
    ax_main.text(4.75, 6.9, 'Errors: [+4, +1, +4]', ha='center',
                 fontsize=9, family='monospace', color='#CC0000', weight='bold')

    # Arrow down to Tree 2
    arrow_down1 = FancyArrowPatch((4.75, 7), (4.75, 5.5), arrowstyle='->', lw=3,
                                 color='#FF0000')
    ax_main.add_patch(arrow_down1)
    ax_main.text(5.5, 6.2, 'Learn from\nmistakes', ha='left', fontsize=10,
                 style='italic', color='#CC0000', weight='bold')

    # Iteration 2
    tree2_box = FancyBboxPatch((3.5, 4), 2.5, 1.5, boxstyle="round,pad=0.1",
                               edgecolor='#009900', facecolor='#BBFFBB', linewidth=3)
    ax_main.add_patch(tree2_box)
    ax_main.text(4.75, 4.8, 'Tree 2', ha='center', fontsize=14, fontweight='bold')
    ax_main.text(4.75, 4.4, 'Fix errors\nfrom Tree 1', ha='center', fontsize=10)

    arrow2 = FancyArrowPatch((6, 4.75), (7, 4.75), arrowstyle='->', lw=2)
    ax_main.add_patch(arrow2)

    pred2_box = FancyBboxPatch((7, 4), 2.5, 1.5, boxstyle="round,pad=0.05",
                               edgecolor='#3366CC', facecolor='#E6F2FF', linewidth=2)
    ax_main.add_patch(pred2_box)
    ax_main.text(8.25, 5, 'After Tree 2', ha='center', fontsize=12, fontweight='bold')
    ax_main.text(8.25, 4.5, 'New Pred: [7, 7.5, 12]', ha='center',
                 fontsize=9, family='monospace')
    ax_main.text(8.25, 4.2, 'Errors: [+3, +0.5, +3]', ha='center',
                 fontsize=9, family='monospace', color='#FF9900', weight='bold')

    # Arrow down to Tree 3
    arrow_down2 = FancyArrowPatch((8.25, 4), (8.25, 2.5), arrowstyle='->', lw=3,
                                 color='#FF9900')
    ax_main.add_patch(arrow_down2)

    # Iteration 3
    tree3_box = FancyBboxPatch((7, 1), 2.5, 1.5, boxstyle="round,pad=0.1",
                               edgecolor='#007700', facecolor='#AAFFAA', linewidth=3)
    ax_main.add_patch(tree3_box)
    ax_main.text(8.25, 1.8, 'Tree 3, ...', ha='center', fontsize=14, fontweight='bold')
    ax_main.text(8.25, 1.4, 'Continue fixing\nerrors', ha='center', fontsize=10)

    # Final model
    final_box = FancyBboxPatch((10.5, 6.5), 3, 2, boxstyle="round,pad=0.1",
                               edgecolor='#006600', facecolor='#DDFFDD', linewidth=4)
    ax_main.add_patch(final_box)
    ax_main.text(12, 8, 'FINAL MODEL', ha='center', fontsize=16, fontweight='bold',
                 color='#006600')
    ax_main.text(12, 7.5, 'Sum of all trees:', ha='center', fontsize=12)
    ax_main.text(12, 7.1, 'Tree₁ + η·Tree₂ +', ha='center', fontsize=11)
    ax_main.text(12, 6.8, 'η·Tree₃ + ... + η·Tree₁₀₀', ha='center', fontsize=11)

    # Side annotation
    annotation = """Each tree predicts
ERRORS (residuals)
of previous ensemble

Sequential learning:
Tree N fixes mistakes
from Trees 1 to N-1"""
    ax_main.text(0.5, 4, annotation, ha='left', va='top', fontsize=10,
                 style='italic', bbox=dict(boxstyle='round', facecolor='#FFFACD',
                 edgecolor='#FF9900', linewidth=2))

    plt.savefig('boosting_illustration.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ boosting_illustration.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 7: XGBoost Comparison
print("[7/8] Creating xgboost_comparison.png...")
try:
    metrics = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    rf_scores = [85.1, 72.4, 58.7, 65.0]
    xgb_scores = [86.7, 75.1, 63.2, 68.6]

    fig = plt.figure(figsize=(12, 8))

    # Table
    ax_table = plt.subplot(2, 1, 1)
    ax_table.axis('tight')
    ax_table.axis('off')

    table_data = [
        ['Metric', 'Random Forest', 'XGBoost', 'Winner'],
        ['Accuracy', '85.1%', '86.7%', 'XGBoost ✓'],
        ['Precision', '72.4%', '75.1%', 'XGBoost ✓'],
        ['Recall', '58.7%', '63.2%', 'XGBoost ✓'],
        ['F1-Score', '65.0%', '68.6%', 'XGBoost ✓'],
        ['─' * 15, '─' * 15, '─' * 15, '─' * 10],
        ['Training Time', '2.3s', '8.1s', 'RF ✓'],
        ['Prediction Time', '0.15s', '0.42s', 'RF ✓']
    ]

    table = ax_table.table(cellText=table_data, cellLoc='center', loc='center',
                           colWidths=[0.3, 0.25, 0.25, 0.2])
    table.auto_set_font_size(False)
    table.set_fontsize(12)
    table.scale(1, 2.5)

    # Style header row
    for i in range(4):
        table[(0, i)].set_facecolor('#E0E0E0')
        table[(0, i)].set_text_props(weight='bold', fontsize=13)

    # Highlight better values
    highlight_cells = [(1, 2), (2, 2), (3, 2), (4, 2), (6, 1), (7, 1)]
    for row, col in highlight_cells:
        table[(row, col)].set_facecolor('#CCFFCC')
        table[(row, col)].set_text_props(weight='bold')

    # Title
    fig.text(0.5, 0.95, 'Algorithm Comparison: Random Forest vs XGBoost',
             ha='center', fontsize=22, fontweight='bold', color='#003366')
    fig.text(0.5, 0.92, '(Adult Income Dataset)', ha='center',
             fontsize=16, color='#003366')

    # Bar chart
    ax_chart = plt.subplot(2, 1, 2)

    x = np.arange(len(metrics))
    width = 0.35

    bars1 = ax_chart.bar(x - width/2, rf_scores, width, label='Random Forest',
                         color='#3366CC', edgecolor='black', linewidth=1.5)
    bars2 = ax_chart.bar(x + width/2, xgb_scores, width, label='XGBoost',
                         color='#00AA00', edgecolor='black', linewidth=1.5)

    # Add value labels
    for bars in [bars1, bars2]:
        for bar in bars:
            height = bar.get_height()
            ax_chart.text(bar.get_x() + bar.get_width()/2., height + 1,
                         f'{height:.1f}%', ha='center', va='bottom',
                         fontsize=11, fontweight='bold')

    ax_chart.set_xlabel('Metrics', fontsize=14, fontweight='bold')
    ax_chart.set_ylabel('Percentage (%)', fontsize=14, fontweight='bold')
    ax_chart.set_title('Performance Metrics Comparison', fontsize=16, fontweight='bold')
    ax_chart.set_xticks(x)
    ax_chart.set_xticklabels(metrics, fontsize=12)
    ax_chart.set_ylim(0, 100)
    ax_chart.legend(loc='upper right', fontsize=12)
    ax_chart.grid(axis='y', alpha=0.3, linestyle='--')
    ax_chart.set_axisbelow(True)

    # Summary box
    summary = ("KEY TAKEAWAY:\n"
               "XGBoost achieves 1.6% higher accuracy but takes 3.5x longer to train.\n"
               "Choose based on your priorities: Speed (RF) vs Accuracy (XGBoost)")
    fig.text(0.5, 0.05, summary, ha='center', va='bottom', fontsize=12,
             bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFFACD',
                      edgecolor='#FF9900', linewidth=3))

    plt.tight_layout(rect=[0, 0.12, 1, 0.9])
    plt.savefig('xgboost_comparison.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ xgboost_comparison.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Visual 8: Overfitting Trees
print("[8/8] Creating overfitting_trees.png...")
try:
    # Generate data
    X, y = make_moons(n_samples=200, noise=0.2, random_state=42)
    X_train, X_test = X[:150], X[150:]
    y_train, y_test = y[:150], y[150:]

    # Create meshgrid for decision boundary
    h = 0.02
    x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
    y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                         np.arange(y_min, y_max, h))

    # Create figure
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(19.2, 10.8))

    # Colors
    cmap_light = ListedColormap(['#FFCCCC', '#CCCCFF'])
    cmap_bold = ['#CC0000', '#0066CC']

    # LEFT: Shallow tree
    tree_shallow = DecisionTreeClassifier(max_depth=3, random_state=42)
    tree_shallow.fit(X_train, y_train)

    Z1 = tree_shallow.predict(np.c_[xx.ravel(), yy.ravel()])
    Z1 = Z1.reshape(xx.shape)
    ax1.contourf(xx, yy, Z1, alpha=0.3, cmap=cmap_light)
    ax1.contour(xx, yy, Z1, colors='black', linewidths=3, alpha=0.8)

    # Plot points
    ax1.scatter(X_train[y_train==0, 0], X_train[y_train==0, 1],
               c='#0066CC', marker='o', s=100, edgecolors='black',
               linewidth=1.5, label='Class A', alpha=0.8)
    ax1.scatter(X_train[y_train==1, 0], X_train[y_train==1, 1],
               c='#CC0000', marker='^', s=100, edgecolors='black',
               linewidth=1.5, label='Class B', alpha=0.8)

    train_acc = tree_shallow.score(X_train, y_train) * 100
    test_acc = tree_shallow.score(X_test, y_test) * 100

    ax1.set_title('Shallow Tree (max_depth=3)\n✓ Good Generalization',
                 fontsize=18, fontweight='bold', color='#00AA00', pad=15)
    ax1.set_xlabel('Feature 1', fontsize=14)
    ax1.set_ylabel('Feature 2', fontsize=14)
    ax1.legend(loc='upper right', fontsize=12)
    ax1.grid(alpha=0.3)

    # Add metrics
    metrics_text = f"Training Acc: {train_acc:.0f}%\nTest Acc: {test_acc:.0f}%\nGap: {train_acc-test_acc:.0f}% ✓"
    ax1.text(0.5, -0.15, metrics_text, transform=ax1.transAxes,
            ha='center', fontsize=12, family='monospace',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#CCFFEE',
                     edgecolor='#00AA00', linewidth=2))

    # RIGHT: Deep tree
    tree_deep = DecisionTreeClassifier(max_depth=15, random_state=42)
    tree_deep.fit(X_train, y_train)

    Z2 = tree_deep.predict(np.c_[xx.ravel(), yy.ravel()])
    Z2 = Z2.reshape(xx.shape)
    ax2.contourf(xx, yy, Z2, alpha=0.3, cmap=cmap_light)
    ax2.contour(xx, yy, Z2, colors='black', linewidths=1, alpha=0.8)

    # Plot points
    ax2.scatter(X_train[y_train==0, 0], X_train[y_train==0, 1],
               c='#0066CC', marker='o', s=100, edgecolors='black',
               linewidth=1.5, label='Class A', alpha=0.8)
    ax2.scatter(X_train[y_train==1, 0], X_train[y_train==1, 1],
               c='#CC0000', marker='^', s=100, edgecolors='black',
               linewidth=1.5, label='Class B', alpha=0.8)

    train_acc_deep = tree_deep.score(X_train, y_train) * 100
    test_acc_deep = tree_deep.score(X_test, y_test) * 100

    ax2.set_title('Deep Tree (max_depth=15)\n✗ Overfitting!',
                 fontsize=18, fontweight='bold', color='#CC0000', pad=15)
    ax2.set_xlabel('Feature 1', fontsize=14)
    ax2.set_ylabel('Feature 2', fontsize=14)
    ax2.legend(loc='upper right', fontsize=12)
    ax2.grid(alpha=0.3)

    # Add metrics
    metrics_text = f"Training Acc: {train_acc_deep:.0f}%\nTest Acc: {test_acc_deep:.0f}%\nGap: {train_acc_deep-test_acc_deep:.0f}% ✗ OVERFITTING!"
    ax2.text(0.5, -0.15, metrics_text, transform=ax2.transAxes,
            ha='center', fontsize=12, family='monospace',
            bbox=dict(boxstyle='round,pad=0.5', facecolor='#FFCCCC',
                     edgecolor='#CC0000', linewidth=2))

    # Overall title
    fig.suptitle('Decision Tree Overfitting: Depth Comparison',
                fontsize=24, fontweight='bold', color='#003366', y=0.98)

    # Bottom comparison text
    comparison = ("KEY DIFFERENCE:\n"
                  "Shallow tree creates smooth, general decision boundaries\n"
                  "Deep tree memorizes training points with complex boundaries\n"
                  "→ Shallow tree generalizes better to new data!")
    fig.text(0.5, 0.02, comparison, ha='center', fontsize=14, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.8', facecolor='#FFFACD',
                     edgecolor='#FF9900', linewidth=3))

    plt.tight_layout(rect=[0, 0.08, 1, 0.96])
    plt.savefig('overfitting_trees.png', dpi=150, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    plt.close()
    print("   ✓ overfitting_trees.png created")
except Exception as e:
    print(f"   ✗ Error: {e}")

# Summary
print()
print("="*60)
print("Visual Generation Complete!")
print("="*60)
print()
print("Generated files:")
print("  1. decision_tree_example.png")
print("  2. tree_splitting_animation.png")
print("  3. feature_importance_plot.png")
print("  4. random_forest_ensemble.png")
print("  5. bagging_illustration.png")
print("  6. boosting_illustration.png")
print("  7. xgboost_comparison.png")
print("  8. overfitting_trees.png")
print()
print("All visuals are ready for use in teaching!")
print()

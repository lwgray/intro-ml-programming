"""
Generate the 3-panel 'Effect of Regularization on Decision Boundary' visual
for Week 4, Segment 5 (Regularization).

Key design choice: we expand the 2 raw features with high-degree POLYNOMIAL
features before fitting Logistic Regression. A plain linear model on 2 raw
features can only draw a straight-line boundary, so regularization would have
no visible effect (all panels identical). With polynomial expansion the
unregularized model has enough capacity to OVERFIT (wiggly boundary), so the
smoothing effect of L2 and the simplifying effect of L1 become visible.

Panels:
  1. No regularization   -> wiggly, overfit boundary chasing noise
  2. L2 (Ridge)          -> smooth boundary, generalizes
  3. L1 (Lasso)          -> simpler boundary, many polynomial terms zeroed out
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.pipeline import make_pipeline

# Nonlinear, noisy data so an overfit boundary actually looks different
# from a regularized one.
X, y = make_moons(n_samples=200, noise=0.30, random_state=42)

# Mesh for plotting the decision boundary
h = 0.02
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))

DEGREE = 8  # high capacity -> the unregularized model can overfit

def model(**lr_kwargs):
    return make_pipeline(
        PolynomialFeatures(degree=DEGREE, include_bias=False),
        StandardScaler(),
        LogisticRegression(max_iter=20000, **lr_kwargs),
    )

# Current sklearn API (>=1.8): control the penalty via l1_ratio, not `penalty`.
#   l1_ratio=0  -> pure L2 (Ridge)      l1_ratio=1 -> pure L1 (Lasso)
#   C=np.inf    -> effectively no regularization
models = [
    model(C=np.inf, solver='saga'),                       # No regularization
    model(C=0.05, l1_ratio=0.0, solver='saga'),           # L2 (Ridge-style)
    model(C=0.05, l1_ratio=1.0, solver='saga'),           # L1 (Lasso-style)
]

titles = ['No Regularization\n(Overfitting - wiggly)',
          'L2 Regularization\n(Smooth - generalizes)',
          'L1 Regularization\n(Simpler - drops terms)']

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for idx, (clf, title, ax) in enumerate(zip(models, titles, axes)):
    clf.fit(X, y)

    # Use probability for a soft, readable boundary surface
    Z = clf.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
    Z = Z.reshape(xx.shape)

    ax.contourf(xx, yy, Z, levels=20, alpha=0.35, cmap='RdYlBu')
    ax.contour(xx, yy, Z, levels=[0.5], colors='black', linewidths=2)

    ax.scatter(X[:, 0], X[:, 1], c=y, cmap='RdYlBu',
               edgecolors='black', s=40)

    ax.set_xlim(xx.min(), xx.max())
    ax.set_ylim(yy.min(), yy.max())
    ax.set_xlabel('Feature 1', fontsize=12)
    ax.set_ylabel('Feature 2', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')

    train_acc = clf.score(X, y)
    lr = clf.named_steps['logisticregression']
    nonzero = int(np.sum(lr.coef_ != 0))
    total = lr.coef_.size
    label = f'Train acc: {train_acc:.0%}\nNon-zero coefs: {nonzero}/{total}'
    ax.text(0.04, 0.96, label, transform=ax.transAxes, va='top', fontsize=10,
            bbox=dict(boxstyle='round', facecolor='white', alpha=0.85))

plt.suptitle('Effect of Regularization on Decision Boundary',
             fontsize=16, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('regularization_decision_boundary.png', dpi=200, bbox_inches='tight')
print('Saved regularization_decision_boundary.png')

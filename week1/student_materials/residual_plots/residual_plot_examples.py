"""
Residual Plot Examples for Week 1 Live Session
Generates good and bad residual plot examples for teaching

Used in:
- Segment 2: Quick Pipeline Demo (first viewing)
- Segment 6: Detailed Coding (detailed explanation)
- Segment 7: Pair Programming (students create their own)
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Set random seed for reproducibility
np.random.seed(42)

def create_good_residual_plot(save=False):
    """
    Create a GOOD residual plot showing random scatter
    This indicates the linear model is appropriate
    """
    # Generate data with linear relationship + random noise
    n_samples = 100
    X = np.random.uniform(0, 10, n_samples)
    y = 2 * X + 3 + np.random.normal(0, 2, n_samples)  # y = 2x + 3 + noise

    # Fit linear regression
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y)
    y_pred = model.predict(X.reshape(-1, 1))

    # Calculate residuals
    residuals = y - y_pred

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5, s=50)
    plt.axhline(y=0, color='red', linestyle='--', linewidth=2,
                label='Zero residuals (perfect predictions)')

    plt.xlabel('Predicted Values', fontsize=14)
    plt.ylabel('Residuals (Actual - Predicted)', fontsize=14)
    plt.title('GOOD Residual Plot: Random Scatter ✓', fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=12)

    # Add interpretation text
    interpretation = """
Good Signs (What we see):
✓ Random scatter around zero
✓ No clear patterns
✓ Roughly constant variance
✓ Points evenly above/below line

This means: Linear regression
is appropriate for this data!
    """

    plt.text(0.02, 0.98, interpretation, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.7))

    plt.tight_layout()

    if save:
        plt.savefig('residual_plot_good.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: residual_plot_good.png")

    plt.show()
    return residuals

def create_bad_residual_plot_funnel(save=False):
    """
    Create a BAD residual plot showing funnel pattern
    This indicates heteroscedasticity (non-constant variance)
    """
    # Generate data with increasing variance
    n_samples = 100
    X = np.random.uniform(0, 10, n_samples)
    noise = np.random.normal(0, X * 0.5, n_samples)  # Variance increases with X
    y = 2 * X + 3 + noise

    # Fit linear regression
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y)
    y_pred = model.predict(X.reshape(-1, 1))

    # Calculate residuals
    residuals = y - y_pred

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5, s=50,
                color='orange')
    plt.axhline(y=0, color='red', linestyle='--', linewidth=2)

    plt.xlabel('Predicted Values', fontsize=14)
    plt.ylabel('Residuals (Actual - Predicted)', fontsize=14)
    plt.title('BAD Residual Plot: Funnel Pattern ✗', fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)

    # Add interpretation text
    interpretation = """
Bad Signs (What we see):
✗ Funnel/cone shape
✗ Variance increases →
✗ Heteroscedasticity problem

This means: Model assumptions
violated! Consider:
• Transform the target variable
• Use different model
• Apply weighted regression
    """

    plt.text(0.02, 0.98, interpretation, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))

    plt.tight_layout()

    if save:
        plt.savefig('residual_plot_bad_funnel.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: residual_plot_bad_funnel.png")

    plt.show()
    return residuals

def create_bad_residual_plot_curve(save=False):
    """
    Create a BAD residual plot showing curved pattern
    This indicates non-linear relationship (linear model inappropriate)
    """
    # Generate data with quadratic relationship
    n_samples = 100
    X = np.random.uniform(-3, 3, n_samples)
    y = X**2 + np.random.normal(0, 1, n_samples)  # Quadratic relationship

    # Fit linear regression (wrong model!)
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y)
    y_pred = model.predict(X.reshape(-1, 1))

    # Calculate residuals
    residuals = y - y_pred

    # Create plot
    plt.figure(figsize=(10, 6))
    plt.scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5, s=50,
                color='red')
    plt.axhline(y=0, color='darkred', linestyle='--', linewidth=2)

    plt.xlabel('Predicted Values', fontsize=14)
    plt.ylabel('Residuals (Actual - Predicted)', fontsize=14)
    plt.title('BAD Residual Plot: Curved Pattern ✗', fontsize=16, fontweight='bold')
    plt.grid(True, alpha=0.3)

    # Add interpretation text
    interpretation = """
Bad Signs (What we see):
✗ Systematic U-shape curve
✗ Non-random pattern
✗ Non-linearity detected

This means: Linear regression
is NOT appropriate!
Consider:
• Polynomial regression
• Tree-based models
• Add interaction terms
    """

    plt.text(0.02, 0.98, interpretation, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.7))

    plt.tight_layout()

    if save:
        plt.savefig('residual_plot_bad_curve.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: residual_plot_bad_curve.png")

    plt.show()
    return residuals

def create_comparison_plot(save=False):
    """
    Create side-by-side comparison of all three residual plots
    """
    fig, axes = plt.subplots(1, 3, figsize=(18, 5))

    # Good plot
    X = np.random.uniform(0, 10, 100)
    y = 2 * X + 3 + np.random.normal(0, 2, 100)
    model = LinearRegression()
    model.fit(X.reshape(-1, 1), y)
    y_pred = model.predict(X.reshape(-1, 1))
    residuals = y - y_pred

    axes[0].scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5, s=40)
    axes[0].axhline(y=0, color='green', linestyle='--', linewidth=2)
    axes[0].set_xlabel('Predicted Values', fontsize=12)
    axes[0].set_ylabel('Residuals', fontsize=12)
    axes[0].set_title('✓ GOOD: Random Scatter', fontsize=14, fontweight='bold', color='green')
    axes[0].grid(True, alpha=0.3)

    # Funnel plot
    X = np.random.uniform(0, 10, 100)
    noise = np.random.normal(0, X * 0.5, 100)
    y = 2 * X + 3 + noise
    model.fit(X.reshape(-1, 1), y)
    y_pred = model.predict(X.reshape(-1, 1))
    residuals = y - y_pred

    axes[1].scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5, s=40, color='orange')
    axes[1].axhline(y=0, color='darkorange', linestyle='--', linewidth=2)
    axes[1].set_xlabel('Predicted Values', fontsize=12)
    axes[1].set_ylabel('Residuals', fontsize=12)
    axes[1].set_title('✗ BAD: Funnel Pattern', fontsize=14, fontweight='bold', color='darkorange')
    axes[1].grid(True, alpha=0.3)

    # Curve plot
    X = np.random.uniform(-3, 3, 100)
    y = X**2 + np.random.normal(0, 1, 100)
    model.fit(X.reshape(-1, 1), y)
    y_pred = model.predict(X.reshape(-1, 1))
    residuals = y - y_pred

    axes[2].scatter(y_pred, residuals, alpha=0.6, edgecolors='k', linewidth=0.5, s=40, color='red')
    axes[2].axhline(y=0, color='darkred', linestyle='--', linewidth=2)
    axes[2].set_xlabel('Predicted Values', fontsize=12)
    axes[2].set_ylabel('Residuals', fontsize=12)
    axes[2].set_title('✗ BAD: Curved Pattern', fontsize=14, fontweight='bold', color='darkred')
    axes[2].grid(True, alpha=0.3)

    plt.tight_layout()

    if save:
        plt.savefig('residual_plots_comparison.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: residual_plots_comparison.png")

    plt.show()

def create_mse_comparison_plot(save=False):
    """
    Show same scatter plot with 3 different regression lines
    Demonstrates how different lines produce different residuals and MSE

    Used to teach:
    - What residuals are (vertical distances from points to line)
    - How MSE quantifies fit quality
    - Why we want to minimize MSE
    """
    # Generate clean linear data
    np.random.seed(42)
    n_samples = 30  # Fewer points for clarity
    X = np.linspace(0, 10, n_samples)
    y_true = 2 * X + 3 + np.random.normal(0, 1.5, n_samples)

    # Three different lines:
    # 1. Poor fit (wrong slope)
    # 2. Good fit (optimal - actual linear regression)
    # 3. Better fit (optimal linear regression)

    # Fit the optimal line
    model_optimal = LinearRegression()
    model_optimal.fit(X.reshape(-1, 1), y_true)
    y_pred_optimal = model_optimal.predict(X.reshape(-1, 1))

    # Create poor fit (slope too flat)
    y_pred_poor = 1.0 * X + 5

    # Create mediocre fit (slope close but intercept off)
    y_pred_medium = 1.8 * X + 2

    # Calculate MSE for each
    mse_poor = np.mean((y_true - y_pred_poor)**2)
    mse_medium = np.mean((y_true - y_pred_medium)**2)
    mse_optimal = np.mean((y_true - y_pred_optimal)**2)

    # Create three subplots
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))

    # Plot 1: Poor Fit
    axes[0].scatter(X, y_true, color='steelblue', s=80, alpha=0.7,
                    edgecolors='black', linewidth=1, label='Actual data', zorder=3)
    axes[0].plot(X, y_pred_poor, color='red', linewidth=3,
                 label=f'Poor fit line', zorder=2)

    # Draw residuals as vertical lines
    for i in range(0, n_samples, 3):  # Every 3rd point for clarity
        axes[0].plot([X[i], X[i]], [y_true[i], y_pred_poor[i]],
                    color='red', linestyle='--', linewidth=1.5, alpha=0.6, zorder=1)

    axes[0].set_xlabel('X', fontsize=14, fontweight='bold')
    axes[0].set_ylabel('y', fontsize=14, fontweight='bold')
    axes[0].set_title('Poor Fit: Wrong Slope', fontsize=16, fontweight='bold', color='red')
    axes[0].legend(fontsize=11, loc='upper left')
    axes[0].grid(True, alpha=0.3)
    axes[0].text(0.5, 0.05, f'MSE = {mse_poor:.2f}\n(High error!)',
                transform=axes[0].transAxes, fontsize=13, fontweight='bold',
                ha='center', bbox=dict(boxstyle='round', facecolor='lightcoral', alpha=0.8))

    # Plot 2: Medium Fit
    axes[1].scatter(X, y_true, color='steelblue', s=80, alpha=0.7,
                    edgecolors='black', linewidth=1, label='Actual data', zorder=3)
    axes[1].plot(X, y_pred_medium, color='orange', linewidth=3,
                 label=f'Medium fit line', zorder=2)

    # Draw residuals
    for i in range(0, n_samples, 3):
        axes[1].plot([X[i], X[i]], [y_true[i], y_pred_medium[i]],
                    color='orange', linestyle='--', linewidth=1.5, alpha=0.6, zorder=1)

    axes[1].set_xlabel('X', fontsize=14, fontweight='bold')
    axes[1].set_ylabel('y', fontsize=14, fontweight='bold')
    axes[1].set_title('Medium Fit: Close but Not Optimal', fontsize=16, fontweight='bold', color='orange')
    axes[1].legend(fontsize=11, loc='upper left')
    axes[1].grid(True, alpha=0.3)
    axes[1].text(0.5, 0.05, f'MSE = {mse_medium:.2f}\n(Better)',
                transform=axes[1].transAxes, fontsize=13, fontweight='bold',
                ha='center', bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # Plot 3: Optimal Fit
    axes[2].scatter(X, y_true, color='steelblue', s=80, alpha=0.7,
                    edgecolors='black', linewidth=1, label='Actual data', zorder=3)
    axes[2].plot(X, y_pred_optimal, color='green', linewidth=3,
                 label=f'Optimal fit line', zorder=2)

    # Draw residuals
    for i in range(0, n_samples, 3):
        axes[2].plot([X[i], X[i]], [y_true[i], y_pred_optimal[i]],
                    color='green', linestyle='--', linewidth=1.5, alpha=0.6, zorder=1)

    axes[2].set_xlabel('X', fontsize=14, fontweight='bold')
    axes[2].set_ylabel('y', fontsize=14, fontweight='bold')
    axes[2].set_title('✓ BEST Fit: Linear Regression', fontsize=16, fontweight='bold', color='green')
    axes[2].legend(fontsize=11, loc='upper left')
    axes[2].grid(True, alpha=0.3)
    axes[2].text(0.5, 0.05, f'MSE = {mse_optimal:.2f}\n(Minimized!)',
                transform=axes[2].transAxes, fontsize=13, fontweight='bold',
                ha='center', bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

    # Add overall title
    fig.suptitle('How Residuals and MSE Show Fit Quality\n(Dashed lines = residuals | MSE = Mean Squared Error)',
                 fontsize=18, fontweight='bold', y=1.00)

    plt.tight_layout()

    if save:
        plt.savefig('mse_comparison_three_fits.png', dpi=300, bbox_inches='tight')
        print("✓ Saved: mse_comparison_three_fits.png")

    plt.show()

    # Print the actual values for teaching
    print(f"\nMSE Comparison:")
    print(f"  Poor Fit:    MSE = {mse_poor:.2f}")
    print(f"  Medium Fit:  MSE = {mse_medium:.2f}")
    print(f"  Optimal Fit: MSE = {mse_optimal:.2f}")
    print(f"\nLinear Regression finds the line that MINIMIZES MSE!")

def demo_california_housing_residual():
    """
    Create residual plot using actual California Housing data
    This is what students will see in the notebooks
    """
    from sklearn.datasets import fetch_california_housing
    from sklearn.model_selection import train_test_split

    print("\n" + "="*60)
    print("DEMO: California Housing Residual Plot")
    print("(This is what students will see in Segments 2 & 6)")
    print("="*60 + "\n")

    # Load data
    data = fetch_california_housing()
    X = data.data
    y = data.target

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Calculate residuals
    residuals = y_test - y_pred

    # Create plot
    plt.figure(figsize=(12, 6))
    plt.scatter(y_pred, residuals, alpha=0.5, edgecolors='k', linewidth=0.5)
    plt.axhline(y=0, color='red', linestyle='--', linewidth=2,
                label='Zero residuals (perfect predictions)')

    plt.xlabel('Predicted Values (median house value in $100K)', fontsize=12)
    plt.ylabel('Residuals (Actual - Predicted)', fontsize=12)
    plt.title('Residual Plot: California Housing Dataset', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    plt.legend()

    # Add interpretation text
    interpretation = f"""
Model Performance:
• R² Score: {model.score(X_test, y_test):.3f}
• Points: {len(residuals):,}

Good Signs:
✓ Random scatter around zero
✓ No clear patterns
✓ Roughly constant variance

Conclusion: Linear regression
is appropriate for this data.
"""

    plt.text(0.02, 0.98, interpretation, transform=plt.gca().transAxes,
             fontsize=10, verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))

    plt.tight_layout()
    plt.savefig('california_housing_residual_plot.png', dpi=300, bbox_inches='tight')
    print("✓ Saved: california_housing_residual_plot.png")
    plt.show()

    return model, residuals

def main():
    """Generate all residual plot examples"""
    print("="*60)
    print("RESIDUAL PLOT EXAMPLES GENERATOR")
    print("Week 1: Linear Regression - Live Session Materials")
    print("="*60 + "\n")

    print("Creating residual plot examples...\n")

    # Create MSE comparison (NEW - shows what residuals are)
    print("1. Creating MSE comparison plot (3 different fits)...")
    create_mse_comparison_plot(save=True)

    # Create good example
    print("\n2. Creating GOOD residual plot (random scatter)...")
    create_good_residual_plot(save=True)

    # Create bad examples
    print("\n3. Creating BAD residual plot (funnel pattern)...")
    create_bad_residual_plot_funnel(save=True)

    print("\n4. Creating BAD residual plot (curved pattern)...")
    create_bad_residual_plot_curve(save=True)

    # Create comparison
    print("\n5. Creating side-by-side comparison...")
    create_comparison_plot(save=True)

    # Create California Housing example
    print("\n6. Creating California Housing example...")
    demo_california_housing_residual()

    print("\n" + "="*60)
    print("✅ ALL RESIDUAL PLOTS CREATED SUCCESSFULLY!")
    print("="*60)
    print("\nFiles created:")
    print("  • mse_comparison_three_fits.png          [NEW!]")
    print("  • residual_plot_good.png")
    print("  • residual_plot_bad_funnel.png")
    print("  • residual_plot_bad_curve.png")
    print("  • residual_plots_comparison.png")
    print("  • california_housing_residual_plot.png")
    print("\nUse these in:")
    print("  - Segment 4: LR Theory (mse_comparison_three_fits.png)")
    print("  - Segment 2: Quick Pipeline Demo")
    print("  - Segment 6: Detailed Coding")
    print("  - Segment 7: Pair Programming (for reference)")

if __name__ == "__main__":
    main()

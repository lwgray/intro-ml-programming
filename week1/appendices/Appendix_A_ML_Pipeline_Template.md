# Appendix A: Complete ML Pipeline Template (sklearn)

**Purpose:** A reusable template for machine learning projects using scikit-learn

**When to use:** Reference this template for all weeks and your final projects

---

## 📋 The Standard ML Pipeline

Every machine learning project follows this structure:

```
1. Load Data
2. Split Data (BEFORE preprocessing!)
3. Preprocess
4. Train Model
5. Evaluate
6. Interpret
```

---

## 🔧 Complete Code Template

```python
# =============================================================================
# STEP 0: IMPORTS
# =============================================================================

# Data handling
import numpy as np
import pandas as pd

# Sklearn components
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression  # Change based on algorithm
from sklearn.metrics import mean_squared_error, r2_score  # Change based on task

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Settings
import warnings
warnings.filterwarnings('ignore')
np.random.seed(42)

print("✅ Imports complete!")


# =============================================================================
# STEP 1: LOAD DATA
# =============================================================================

# Option A: Load from sklearn dataset
from sklearn.datasets import fetch_california_housing
data = fetch_california_housing()
X = data.data
y = data.target
feature_names = data.feature_names

# Option B: Load from CSV
# df = pd.read_csv('your_data.csv')
# X = df.drop('target_column', axis=1)
# y = df['target_column']

# Option C: Load from other source (database, API, etc.)
# X, y = load_your_data()

print(f"✅ Data loaded!")
print(f"   X shape: {X.shape}")
print(f"   y shape: {y.shape}")


# =============================================================================
# STEP 2: EXPLORATORY DATA ANALYSIS (EDA)
# =============================================================================

# Check for missing values
print(f"\nMissing values in X: {pd.DataFrame(X).isnull().sum().sum()}")
print(f"Missing values in y: {pd.Series(y).isnull().sum()}")

# Check data types
print(f"\nData types:")
print(pd.DataFrame(X).dtypes)

# Basic statistics
print(f"\nBasic statistics:")
print(pd.DataFrame(X).describe())

# Visualize target distribution
plt.figure(figsize=(8, 4))
plt.hist(y, bins=50, edgecolor='k')
plt.xlabel('Target Variable')
plt.ylabel('Frequency')
plt.title('Distribution of Target Variable')
plt.show()


# =============================================================================
# STEP 3: SPLIT DATA (BEFORE PREPROCESSING!)
# =============================================================================

# ⚠️ CRITICAL: Split BEFORE any preprocessing to prevent data leakage

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,        # 80% train, 20% test
    random_state=42,      # For reproducibility
    # stratify=y          # Uncomment for classification to preserve class distribution
)

print(f"\n✅ Data split complete!")
print(f"   Training samples: {len(X_train)}")
print(f"   Test samples: {len(X_test)}")
print(f"   Split ratio: {len(X_train)/len(X):.1%} train, {len(X_test)/len(X):.1%} test")


# =============================================================================
# STEP 4: PREPROCESSING
# =============================================================================

# 4A: Feature Scaling (for algorithms sensitive to scale)
# Note: Fit on TRAIN only, then transform both train and test

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)  # Fit on train
X_test_scaled = scaler.transform(X_test)        # Transform test using train stats

print(f"\n✅ Scaling complete!")
print(f"   Mean of scaled training data: {X_train_scaled.mean():.4f}")
print(f"   Std of scaled training data: {X_train_scaled.std():.4f}")

# 4B: Handle Missing Values (if any)
# from sklearn.impute import SimpleImputer
# imputer = SimpleImputer(strategy='mean')
# X_train_imputed = imputer.fit_transform(X_train)
# X_test_imputed = imputer.transform(X_test)

# 4C: Encode Categorical Variables (if any)
# from sklearn.preprocessing import OneHotEncoder
# encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
# X_train_encoded = encoder.fit_transform(X_train_categorical)
# X_test_encoded = encoder.transform(X_test_categorical)


# =============================================================================
# STEP 5: TRAIN MODEL
# =============================================================================

# Create model instance
model = LinearRegression()  # Change based on your algorithm

print(f"\n✅ Training {model.__class__.__name__}...")

# Train the model
model.fit(X_train_scaled, y_train)  # Use scaled data if you scaled

print(f"   Training complete!")

# Display learned parameters (if applicable)
if hasattr(model, 'coef_'):
    print(f"   Number of features: {len(model.coef_)}")
    print(f"   Intercept: {model.intercept_:.4f}")


# =============================================================================
# STEP 6: MAKE PREDICTIONS
# =============================================================================

# Predict on training set (to check for overfitting)
y_train_pred = model.predict(X_train_scaled)

# Predict on test set (final evaluation)
y_test_pred = model.predict(X_test_scaled)

print(f"\n✅ Predictions complete!")
print(f"   Train predictions shape: {y_train_pred.shape}")
print(f"   Test predictions shape: {y_test_pred.shape}")


# =============================================================================
# STEP 7: EVALUATE MODEL
# =============================================================================

# Calculate metrics on BOTH train and test (to detect overfitting)

# Training set metrics
train_mse = mean_squared_error(y_train, y_train_pred)
train_rmse = np.sqrt(train_mse)
train_r2 = r2_score(y_train, y_train_pred)

# Test set metrics
test_mse = mean_squared_error(y_test, y_test_pred)
test_rmse = np.sqrt(test_mse)
test_r2 = r2_score(y_test, y_test_pred)

# Display results
print("\n" + "="*60)
print("MODEL EVALUATION METRICS")
print("="*60)
print(f"\nTraining Set:")
print(f"  MSE:  {train_mse:.4f}")
print(f"  RMSE: {train_rmse:.4f}")
print(f"  R²:   {train_r2:.4f}")

print(f"\nTest Set:")
print(f"  MSE:  {test_mse:.4f}")
print(f"  RMSE: {test_rmse:.4f}")
print(f"  R²:   {test_r2:.4f}")

print("\n" + "="*60)

# Check for overfitting
print(f"\n⚠️  Overfitting Check:")
print(f"   R² difference (train - test): {train_r2 - test_r2:.4f}")
if train_r2 - test_r2 > 0.1:
    print(f"   ⚠️  Warning: Possible overfitting detected!")
else:
    print(f"   ✓ No significant overfitting detected")


# =============================================================================
# STEP 8: VISUALIZE RESULTS
# =============================================================================

# 8A: Predicted vs Actual Plot
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.scatter(y_test, y_test_pred, alpha=0.5, edgecolors='k', linewidth=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         'r--', lw=2, label='Perfect predictions')
plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title('Predicted vs Actual Values')
plt.legend()
plt.grid(True, alpha=0.3)

# 8B: Residual Plot
residuals = y_test - y_test_pred

plt.subplot(1, 2, 2)
plt.scatter(y_test_pred, residuals, alpha=0.5, edgecolors='k', linewidth=0.5)
plt.axhline(y=0, color='red', linestyle='--', linewidth=2, label='Zero residuals')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals (Actual - Predicted)')
plt.title('Residual Plot')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()


# =============================================================================
# STEP 9: INTERPRET MODEL (For Linear Models)
# =============================================================================

if hasattr(model, 'coef_') and hasattr(data, 'feature_names'):
    print("\n" + "="*60)
    print("FEATURE IMPORTANCE (COEFFICIENT MAGNITUDES)")
    print("="*60)

    # Create feature importance dataframe
    feature_importance = pd.DataFrame({
        'feature': feature_names,
        'coefficient': model.coef_,
        'abs_coefficient': np.abs(model.coef_)
    }).sort_values('abs_coefficient', ascending=False)

    print("\nTop 5 Most Important Features:")
    print(feature_importance.head())

    # Visualize feature importance
    plt.figure(figsize=(10, 6))
    plt.barh(feature_importance['feature'], feature_importance['abs_coefficient'])
    plt.xlabel('Absolute Coefficient Value')
    plt.title('Feature Importance (by coefficient magnitude)')
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()


# =============================================================================
# STEP 10: SAVE MODEL (Optional)
# =============================================================================

# Option A: Save with pickle
# import pickle
# with open('model.pkl', 'wb') as f:
#     pickle.dump(model, f)

# Option B: Save with joblib (recommended for sklearn)
# from joblib import dump
# dump(model, 'model.joblib')

# To load:
# from joblib import load
# loaded_model = load('model.joblib')

print("\n✅ Pipeline complete!")
```

---

## 📝 Quick Reference: Common Modifications

### For Classification Tasks

Change these components:

```python
# Imports
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Model
model = LogisticRegression()

# Metrics
accuracy = accuracy_score(y_test, y_test_pred)
precision = precision_score(y_test, y_test_pred)
recall = recall_score(y_test, y_test_pred)
f1 = f1_score(y_test, y_test_pred)

print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1 Score:  {f1:.4f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_test_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('Confusion Matrix')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()
```

### For Tree-Based Models (Week 3)

```python
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(
    n_estimators=100,
    max_depth=10,
    random_state=42
)

# Feature importance (built-in)
importances = model.feature_importances_
```

### For Neural Networks (Week 6)

```python
import torch
import torch.nn as nn

# Will use PyTorch instead of sklearn
# Different pipeline structure - covered in Week 6
```

---

## ⚠️ Common Pitfalls to Avoid

| Mistake | Consequence | Fix |
|---------|-------------|-----|
| **Fitting scaler on all data** | Data leakage | Fit on train only, transform both |
| **Not checking for missing values** | Errors or silent NaN propagation | Check and handle before split |
| **Not setting random_state** | Non-reproducible results | Always set random_state |
| **Only evaluating on test set** | Can't detect overfitting | Evaluate on both train and test |
| **Forgetting to scale test data** | Poor predictions | Always transform test with fitted scaler |

---

## 🎯 Pipeline Checklist

Use this checklist for every project:

- [ ] Imports complete
- [ ] Data loaded and inspected
- [ ] Missing values handled
- [ ] Data split (80/20 or 70/30)
- [ ] Preprocessing done (fit on train only!)
- [ ] Model trained
- [ ] Predictions made on both train and test
- [ ] Metrics calculated and displayed
- [ ] Overfitting checked
- [ ] Residual plot created (regression) or confusion matrix (classification)
- [ ] Results interpreted
- [ ] Model saved (optional)

---

## 📚 Additional Resources

- **sklearn Pipeline Documentation:** https://scikit-learn.org/stable/modules/compose.html
- **Best Practices:** https://scikit-learn.org/stable/common_pitfalls.html
- **Cross-Validation:** Will cover in Week 4

---

**This template will evolve as we learn more techniques in upcoming weeks!**

**Bookmark this page - you'll reference it constantly.**

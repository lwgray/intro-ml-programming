# Week 1: sklearn Cheat Sheet - Linear Regression

**Quick Reference for Week 1**

**Purpose:** Copy-pasteable code snippets for the most common Week 1 tasks
**Scope:** Only what you need for Week 1 (not comprehensive sklearn)

---

## 📋 Table of Contents

1. [Essential Imports](#essential-imports)
2. [Loading Data](#loading-data)
3. [Splitting Data](#splitting-data)
4. [Training Linear Regression](#training-linear-regression)
5. [Making Predictions](#making-predictions)
6. [Evaluating Models](#evaluating-models)
7. [Visualizations](#visualizations)
8. [Complete Pipeline Template](#complete-pipeline-template)
9. [Common Errors & Fixes](#common-errors--fixes)
10. [External Cheat Sheet Links](#external-cheat-sheet-links)

---

## Essential Imports

### Week 1 Standard Imports

```python
# Data and splitting
from sklearn.datasets import fetch_california_housing, load_diabetes
from sklearn.model_selection import train_test_split

# Model
from sklearn.linear_model import LinearRegression

# Metrics
from sklearn.metrics import mean_squared_error, r2_score

# Visualization
import matplotlib.pyplot as plt

# Math operations
import numpy as np

# Jupyter notebook setting (optional - ensures plots display)
%matplotlib inline
```

**Copy-paste this at the start of every notebook!**

---

## Loading Data

### Built-in Datasets

#### California Housing Dataset

```python
# Load California Housing data
data = fetch_california_housing()

# Extract features and target
X = data.data
y = data.target

# Explore
print(f"Shape of X: {X.shape}")  # (20640, 8)
print(f"Shape of y: {y.shape}")  # (20640,)
print(f"Features: {data.feature_names}")
```

**Output:**
- 20,640 samples
- 8 features: `['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']`
- Target: Median house value in $100,000s

---

#### Diabetes Dataset

```python
# Load Diabetes data
data = load_diabetes()

# Extract features and target
X = data.data
y = data.target

# Explore
print(f"Shape of X: {X.shape}")  # (442, 10)
print(f"Shape of y: {y.shape}")  # (442,)
print(f"Features: {data.feature_names}")
```

**Output:**
- 442 samples
- 10 features: `['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']`
- Target: Disease progression one year after baseline

---

### Loading Your Own Data

#### From CSV file

```python
import pandas as pd

# Load CSV
df = pd.read_csv('your_data.csv')

# Separate features and target
X = df.drop('target_column_name', axis=1).values
y = df['target_column_name'].values

# Check shapes
print(f"X shape: {X.shape}")
print(f"y shape: {y.shape}")
```

---

## Splitting Data

### Basic Train/Test Split

```python
from sklearn.model_selection import train_test_split

# Split: 80% training, 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 20% for testing
    random_state=42      # For reproducibility
)

# Verify split
print(f"Training samples: {len(X_train)}")
print(f"Test samples: {len(X_test)}")
```

**Key parameters:**
- `test_size`: Proportion for testing (0.2 = 20%)
- `random_state`: Set to any number for reproducible splits

---

### Different Split Ratios

```python
# 70/30 split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 90/10 split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42
)
```

**Common ratios:** 80/20, 70/30, 90/10

---

## Training Linear Regression

### Basic Model

```python
from sklearn.linear_model import LinearRegression

# Step 1: Create the model
model = LinearRegression()

# Step 2: Fit (train) the model
model.fit(X_train, y_train)

# Model is now trained!
print("✅ Model trained successfully")
```

---

### Accessing Model Parameters

```python
# Intercept (β₀)
intercept = model.intercept_
print(f"Intercept: {intercept:.4f}")

# Coefficients (β₁, β₂, ...)
coefficients = model.coef_
print(f"Coefficients: {coefficients}")

# Show coefficients with feature names
for feature, coef in zip(data.feature_names, model.coef_):
    print(f"{feature:12s}: {coef:8.4f}")
```

**Example output:**
```
MedInc      :   0.4367
HouseAge    :   0.0095
AveRooms    :  -0.1073
...
```

---

## Making Predictions

### Predict on Test Set

```python
# Make predictions
y_pred = model.predict(X_test)

# Check shape
print(f"Predictions shape: {y_pred.shape}")
# Should match y_test.shape

# View first 5 predictions vs actuals
for i in range(5):
    print(f"Predicted: {y_pred[i]:.2f}, Actual: {y_test[i]:.2f}")
```

---

### Predict on New Data

```python
# Create new sample (same number of features as training data)
new_house = np.array([[8.3252, 41., 6.98, 1.02, 322., 2.55, 37.88, -122.23]])

# Predict
prediction = model.predict(new_house)
print(f"Predicted price: ${prediction[0] * 100000:,.0f}")
```

**Important:** New data must have the same number of features as training data!

---

## Evaluating Models

### R² Score (Coefficient of Determination)

```python
from sklearn.metrics import r2_score

# Calculate R² on test set
r2 = r2_score(y_test, y_pred)

print(f"R² Score: {r2:.4f}")
print(f"Interpretation: Model explains {r2*100:.1f}% of variance")
```

**Scale:**
- 0 = terrible (no better than predicting the mean)
- 1 = perfect (100% accuracy)
- Typical: 0.3 - 0.9 (depends on domain)

**Alternative:** Use `.score()` method
```python
r2 = model.score(X_test, y_test)  # Same as r2_score
```

---

### MSE (Mean Squared Error)

```python
from sklearn.metrics import mean_squared_error

# Calculate MSE
mse = mean_squared_error(y_test, y_pred)

print(f"MSE: {mse:.4f}")
```

**Interpretation:** Lower is better
**Problem:** Units are squared (hard to interpret)

---

### RMSE (Root Mean Squared Error)

```python
import numpy as np
from sklearn.metrics import mean_squared_error

# Calculate RMSE
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

print(f"RMSE: {rmse:.4f}")
print(f"Average error: {rmse:.2f} units")
```

**Interpretation:** Average prediction error in original units
**Advantage:** Same units as target variable (easier to interpret)

---

### All Metrics at Once

```python
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

# Calculate all three
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Display nicely
print("=" * 50)
print("MODEL EVALUATION")
print("=" * 50)
print(f"R² Score:  {r2:.4f} ({r2*100:.1f}% variance explained)")
print(f"MSE:       {mse:.4f}")
print(f"RMSE:      {rmse:.4f} (average error)")
print("=" * 50)
```

---

## Visualizations

### Residual Plot (Most Important!)

```python
import matplotlib.pyplot as plt

# Calculate residuals
residuals = y_test - y_pred

# Create residual plot
plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.5, edgecolors='k', linewidth=0.5)
plt.axhline(y=0, color='red', linestyle='--', linewidth=2)
plt.xlabel('Predicted Values')
plt.ylabel('Residuals (Actual - Predicted)')
plt.title('Residual Plot')
plt.grid(True, alpha=0.3)
plt.show()
```

**What to look for:**
- ✅ Random scatter around zero = good
- ❌ Curved pattern = nonlinear relationship
- ❌ Funnel shape = heteroscedasticity

---

### Predictions vs Actuals

```python
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5, edgecolors='k', linewidth=0.5)

# Perfect prediction line (45-degree)
min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val],
         'r--', linewidth=2, label='Perfect Prediction')

plt.xlabel('Actual Values')
plt.ylabel('Predicted Values')
plt.title(f'Predictions vs Actuals (R² = {r2:.3f})')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
```

**Interpretation:** Points closer to red line = better predictions

---

### Feature Coefficients Bar Plot

```python
import matplotlib.pyplot as plt

# Create bar plot of coefficients
plt.figure(figsize=(10, 6))
plt.barh(data.feature_names, model.coef_)
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.title('Feature Coefficients')
plt.grid(True, alpha=0.3, axis='x')
plt.tight_layout()
plt.show()
```

**Use:** Visualize which features have the largest impact

---

## Complete Pipeline Template

### Copy-Paste Ready Pipeline

```python
# ========================================
# COMPLETE ML PIPELINE FOR LINEAR REGRESSION
# ========================================

# 1. IMPORTS
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
import numpy as np

# 2. LOAD DATA
data = fetch_california_housing()
X = data.data
y = data.target

print(f"✅ Data loaded: {X.shape[0]} samples, {X.shape[1]} features")

# 3. SPLIT DATA (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"✅ Data split: {len(X_train)} train, {len(X_test)} test")

# 4. TRAIN MODEL
model = LinearRegression()
model.fit(X_train, y_train)

print(f"✅ Model trained")

# 5. MAKE PREDICTIONS
y_pred = model.predict(X_test)

print(f"✅ Predictions made")

# 6. EVALUATE MODEL
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

print("\n" + "=" * 60)
print("MODEL EVALUATION")
print("=" * 60)
print(f"R² Score:  {r2:.4f} ({r2*100:.1f}% variance explained)")
print(f"MSE:       {mse:.4f}")
print(f"RMSE:      {rmse:.4f}")
print("=" * 60)

# 7. RESIDUAL PLOT
residuals = y_test - y_pred

plt.figure(figsize=(10, 6))
plt.scatter(y_pred, residuals, alpha=0.5, edgecolors='k', linewidth=0.5)
plt.axhline(y=0, color='red', linestyle='--', linewidth=2)
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.grid(True, alpha=0.3)
plt.show()

print("✅ Pipeline complete!")
```

**This is the pattern you'll use every time!**

---

## Common Errors & Fixes

### Error 1: "X has Y features but model was trained with Z features"

```python
ValueError: X has 8 features but LinearRegression is expecting 6 features
```

**Cause:** Feature mismatch between training and prediction

**Fix:**
```python
# Ensure same features
print(f"Training features: {X_train.shape[1]}")
print(f"Test features: {X_test.shape[1]}")
# These must match!
```

---

### Error 2: "Expected 2D array, got 1D array instead"

```python
ValueError: Expected 2D array, got 1D array instead
```

**Cause:** Passing a 1D array when sklearn expects 2D

**Fix:**
```python
# If predicting one sample
new_sample = [[value1, value2, value3]]  # Double brackets!
# OR
new_sample = np.array([value1, value2, value3]).reshape(1, -1)

prediction = model.predict(new_sample)
```

---

### Error 3: "y should be a 1d array, got 2d array instead"

```python
ValueError: y should be a 1d array, got 2d array instead
```

**Cause:** Target variable y has wrong shape

**Fix:**
```python
# If y is DataFrame column
y = df['target'].values  # Use .values to get 1D array

# If y is 2D, flatten it
y = y.ravel()  # or y.flatten()
```

---

### Error 4: ImportError

```python
ImportError: cannot import name 'fetch_california_housing'
```

**Cause:** sklearn not installed or outdated version

**Fix:**
```bash
# Install sklearn
pip install scikit-learn

# Upgrade to latest
pip install --upgrade scikit-learn
```

---

### Warning: "DataConversionWarning"

```python
DataConversionWarning: A column-vector y was passed...
```

**Cause:** y has shape (n, 1) instead of (n,)

**Fix:**
```python
# Flatten y
y = y.ravel()
```

---

## External Cheat Sheet Links

### Official sklearn Documentation

**Linear Regression API Reference:**
https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

**What to bookmark:**
- Constructor parameters
- Methods: `.fit()`, `.predict()`, `.score()`
- Attributes: `.coef_`, `.intercept_`

---

### DataCamp Cheat Sheets

#### sklearn Cheat Sheet
**Link:** https://www.datacamp.com/cheat-sheet/scikit-learn-cheat-sheet-python-machine-learning

**What to focus on:**
- "Supervised Learning" section
- train_test_split
- Model evaluation metrics

**Download:** PDF available for printing

---

#### matplotlib Cheat Sheet
**Link:** https://www.datacamp.com/cheat-sheet/matplotlib-cheat-sheet-plotting-in-python

**What to focus on:**
- Scatter plots
- Line plots
- Labels and titles

**Use:** For creating residual plots and visualizations

---

### Quick Reference Cards (Printable)

#### sklearn Algorithm Cheat Sheet
**Link:** https://scikit-learn.org/stable/tutorial/machine_learning_map/index.html

**What it is:** Decision tree for choosing algorithms

**When to use:** "Which algorithm should I use for my problem?"

---

### Interactive Resources

#### sklearn Examples Gallery
**Link:** https://scikit-learn.org/stable/auto_examples/index.html

**Search for:** "Linear Regression"

**What you'll find:**
- Complete working examples
- Visualizations
- Different use cases

---

## Quick Command Reference

### Most-Used Commands

```python
# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluate
r2 = model.score(X_test, y_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)

# Get parameters
intercept = model.intercept_
coefficients = model.coef_

# Calculate residuals
residuals = y_test - y_pred
```

---

## Keyboard Shortcuts (Jupyter)

```
Shift + Enter    : Run cell and move to next
Ctrl + Enter     : Run cell (stay in cell)
Esc              : Command mode
A                : Insert cell above (command mode)
B                : Insert cell below (command mode)
DD               : Delete cell (command mode)
M                : Change to markdown (command mode)
Y                : Change to code (command mode)
```

---

## Tips & Best Practices

### ✅ Do This

- Always set `random_state` for reproducibility
- Check data shapes after every step
- Create residual plots to validate assumptions
- Use meaningful variable names
- Comment your code
- Test on small datasets first

### ❌ Avoid This

- Don't preprocess before splitting (data leakage!)
- Don't skip train/test split
- Don't rely only on R² (check residual plots!)
- Don't predict without checking feature count
- Don't forget to import required libraries

---

## Week 1 Workflow Checklist

```
□ Import libraries
□ Load data
□ Explore data (shapes, features)
□ Split data (BEFORE preprocessing!)
□ Create model
□ Train model (fit)
□ Make predictions
□ Calculate metrics (R², MSE, RMSE)
□ Create residual plot
□ Interpret results
```

---

## Need More Help?

**Official Documentation:**
- sklearn: https://scikit-learn.org/
- NumPy: https://numpy.org/
- matplotlib: https://matplotlib.org/

**Video Tutorials:**
- StatQuest (YouTube): Linear Regression explained
- Corey Schafer: sklearn tutorial series

**Q&A:**
- Stack Overflow: Search "sklearn linear regression"
- Course discussion forum

---

**Save this cheat sheet for quick reference during Week 1!** 📌

**Remember:** The more you practice this pipeline, the more automatic it becomes!

---

*Last Updated: 2025-11-26*

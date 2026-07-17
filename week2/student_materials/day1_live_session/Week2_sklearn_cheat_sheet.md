# Week 2: sklearn Classification Cheat Sheet

**Purpose:** Quick reference for all sklearn commands needed in Week 2
**Format:** Copy-paste ready code snippets with explanations

---

## Table of Contents
1. [Imports](#imports)
2. [Data Loading](#data-loading)
3. [Train/Test Split](#traintestsplit)
4. [Preprocessing](#preprocessing)
5. [Model Training](#model-training)
6. [Making Predictions](#making-predictions)
7. [Evaluation Metrics](#evaluation-metrics)
8. [Visualization](#visualization)

---

## Imports

### Essential Imports for Week 2

```python
# Data handling
import numpy as np
import pandas as pd

# sklearn - data
from sklearn.datasets import load_breast_cancer

# sklearn - preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# sklearn - model
from sklearn.linear_model import LogisticRegression

# sklearn - metrics (ALL classification metrics!)
from sklearn.metrics import (
    accuracy_score,           # Overall correctness
    confusion_matrix,         # TP, TN, FP, FN
    classification_report,    # Comprehensive summary
    precision_score,          # Positive prediction accuracy
    recall_score,             # Positive detection rate
    f1_score,                 # Balance of precision & recall
    roc_curve,                # For ROC curve plotting
    roc_auc_score            # Area under ROC curve
)

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns

# Jupyter magic command
%matplotlib inline
```

---

## Data Loading

### Load Built-in Dataset

```python
# Load breast cancer dataset
data = load_breast_cancer()

# Extract features and target
X = data.data          # Features (30 measurements)
y = data.target        # Target (0=malignant, 1=benign)

# Optional: Get feature names and target names
feature_names = data.feature_names
target_names = data.target_names  # ['malignant', 'benign']
```

### Load from CSV

```python
# Load data from CSV
df = pd.read_csv('data.csv')

# Separate features and target
X = df.drop('target_column', axis=1).values  # Features
y = df['target_column'].values               # Target

# Or keep as DataFrame (useful for column names)
X = df.drop('target_column', axis=1)
y = df['target_column']
```

### Quick Data Exploration

```python
# Check shapes
print(f"Features shape: {X.shape}")  # (n_samples, n_features)
print(f"Target shape: {y.shape}")    # (n_samples,)

# Check class distribution
unique, counts = np.unique(y, return_counts=True)
print(f"Class distribution: {dict(zip(unique, counts))}")

# Check for missing values (if DataFrame)
print(df.isnull().sum())
```

---

## Train/Test Split

### Standard Split (80/20)

```python
# Split data: 80% train, 20% test
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,       # 20% for testing
    random_state=42      # For reproducibility
)

print(f"Training set: {X_train.shape}")
print(f"Test set: {X_test.shape}")
```

### Split with Stratification (Important for Imbalanced Data!)

```python
# Stratified split - maintains class proportions
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42,
    stratify=y          # Maintains class balance in both sets
)

# Verify stratification worked
print(f"Train class distribution: {np.bincount(y_train) / len(y_train)}")
print(f"Test class distribution: {np.bincount(y_test) / len(y_test)}")
```

**⚠️ Remember:** Always split BEFORE preprocessing!

---

## Preprocessing

### Feature Scaling with StandardScaler

```python
# Create scaler
scaler = StandardScaler()

# Fit on training data and transform
X_train_scaled = scaler.fit_transform(X_train)

# Transform test data (using training statistics!)
X_test_scaled = scaler.transform(X_test)

# Verify scaling worked
print(f"Mean before: {X_train[:, 0].mean():.2f}")
print(f"Mean after: {X_train_scaled[:, 0].mean():.2f}")  # Should be ~0
print(f"Std after: {X_train_scaled[:, 0].std():.2f}")    # Should be ~1
```

**⚠️ Critical Rules:**
- Fit on training data only (`fit_transform`)
- Transform test data using training statistics (`transform` only)
- Never `fit` on test data (causes data leakage!)

---

## Model Training

### Create and Train Logistic Regression

```python
# Create model
model = LogisticRegression(
    max_iter=10000,      # Maximum iterations (increase if convergence warning)
    random_state=42      # For reproducibility
)

# Train model
model.fit(X_train_scaled, y_train)

print("✅ Model trained!")
```

### Access Model Parameters

```python
# Get coefficients (one per feature)
coefficients = model.coef_[0]

# Get intercept
intercept = model.intercept_[0]

# Number of iterations taken
n_iterations = model.n_iter_[0]

# Display feature importance (top 5)
feature_importance = pd.DataFrame({
    'feature': feature_names,
    'coefficient': np.abs(coefficients)
}).sort_values('coefficient', ascending=False)
print(feature_importance.head())
```

---

## Making Predictions

### Hard Predictions (Class Labels)

```python
# Predict class labels (0 or 1)
y_pred = model.predict(X_test_scaled)

print(f"Predictions: {y_pred[:10]}")  # First 10 predictions
print(f"Shape: {y_pred.shape}")
```

### Soft Predictions (Probabilities)

```python
# Predict probabilities for each class
y_pred_proba = model.predict_proba(X_test_scaled)

# Show first 5 probability predictions
print("Probability predictions [P(class 0), P(class 1)]:")
print(y_pred_proba[:5])

# Extract probability of positive class only
prob_positive_class = y_pred_proba[:, 1]
print(f"P(class 1): {prob_positive_class[:5]}")
```

### Custom Threshold Predictions

```python
# Use custom threshold (default is 0.5)
threshold = 0.3  # Lower threshold → more positive predictions

# Get probabilities
y_pred_proba = model.predict_proba(X_test_scaled)

# Apply custom threshold
y_pred_custom = (y_pred_proba[:, 1] >= threshold).astype(int)

print(f"Default predictions (threshold=0.5): {y_pred[:10]}")
print(f"Custom predictions (threshold=0.3): {y_pred_custom[:10]}")
```

---

## Evaluation Metrics

### Accuracy

```python
# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f} ({accuracy*100:.1f}%)")

# Alternative: use model.score()
accuracy_alt = model.score(X_test_scaled, y_test)
```

### Confusion Matrix

```python
# Generate confusion matrix
cm = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(cm)

# Extract individual values
tn, fp, fn, tp = cm.ravel()
print(f"TN: {tn}, FP: {fp}, FN: {fn}, TP: {tp}")

# Pretty print with labels
cm_df = pd.DataFrame(
    cm,
    index=['Actual Negative', 'Actual Positive'],
    columns=['Predicted Negative', 'Predicted Positive']
)
print(cm_df)
```

### Precision, Recall, F1-Score

```python
# Calculate individual metrics
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print(f"Precision: {precision:.3f}")
print(f"Recall:    {recall:.3f}")
print(f"F1-Score:  {f1:.3f}")
```

### Classification Report (All Metrics at Once!)

```python
# Comprehensive report
report = classification_report(
    y_test,
    y_pred,
    target_names=['Malignant', 'Benign']  # Optional: class names
)
print(report)

# Get as dictionary for programmatic access
report_dict = classification_report(
    y_test,
    y_pred,
    target_names=['Malignant', 'Benign'],
    output_dict=True
)
print(f"Benign F1-score: {report_dict['Benign']['f1-score']:.3f}")
```

### ROC Curve and AUC

```python
# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1])

# Calculate AUC score
auc = roc_auc_score(y_test, y_pred_proba[:, 1])

print(f"AUC Score: {auc:.3f}")
```

---

## Visualization

### Confusion Matrix Heatmap

```python
# Create confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Visualize as heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    cm,
    annot=True,          # Show numbers
    fmt='d',             # Integer format
    cmap='Blues',        # Color scheme
    xticklabels=['Malignant', 'Benign'],
    yticklabels=['Malignant', 'Benign'],
    cbar_kws={'label': 'Count'}
)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix: Breast Cancer Classification')
plt.tight_layout()
plt.show()
```

### ROC Curve Plot

```python
# Calculate ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_pred_proba[:, 1])
auc = roc_auc_score(y_test, y_pred_proba[:, 1])

# Plot ROC curve
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2,
         label=f'ROC curve (AUC = {auc:.3f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--',
         label='Random guessing (AUC = 0.5)')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate (Recall)')
plt.title('ROC Curve')
plt.legend(loc="lower right")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Probability Distribution Plot

```python
# Plot distribution of predicted probabilities for each class
plt.figure(figsize=(10, 6))

# Get probabilities for positive class
prob_positive = y_pred_proba[:, 1]

# Separate by actual class
prob_class_0 = prob_positive[y_test == 0]
prob_class_1 = prob_positive[y_test == 1]

# Plot histograms
plt.hist(prob_class_0, bins=30, alpha=0.5, label='Actual Class 0 (Malignant)', color='red')
plt.hist(prob_class_1, bins=30, alpha=0.5, label='Actual Class 1 (Benign)', color='blue')

# Add threshold line
plt.axvline(x=0.5, color='black', linestyle='--', linewidth=2, label='Default Threshold (0.5)')

plt.xlabel('Predicted Probability of Class 1')
plt.ylabel('Frequency')
plt.title('Distribution of Predicted Probabilities')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()
```

### Class Distribution Bar Plot

```python
# Visualize class distribution
unique, counts = np.unique(y, return_counts=True)

plt.figure(figsize=(8, 5))
plt.bar(['Class 0\n(Malignant)', 'Class 1\n(Benign)'], counts, color=['red', 'blue'], alpha=0.7)
plt.ylabel('Count')
plt.title('Class Distribution in Dataset')
plt.grid(axis='y', alpha=0.3)

# Add percentage labels
for i, count in enumerate(counts):
    percentage = count / len(y) * 100
    plt.text(i, count, f'{count}\n({percentage:.1f}%)', ha='center', va='bottom')

plt.tight_layout()
plt.show()
```

---

## Complete Pipeline Template

### Copy-Paste Ready Full Pipeline

```python
# ===== IMPORTS =====
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, confusion_matrix, classification_report,
    precision_score, recall_score, f1_score,
    roc_curve, roc_auc_score
)
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ===== LOAD DATA =====
data = load_breast_cancer()
X = data.data
y = data.target

# ===== SPLIT DATA =====
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ===== PREPROCESS =====
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# ===== TRAIN MODEL =====
model = LogisticRegression(max_iter=10000, random_state=42)
model.fit(X_train_scaled, y_train)

# ===== MAKE PREDICTIONS =====
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)

# ===== EVALUATE =====
# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.3f}")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(f"\\nConfusion Matrix:\\n{cm}")

# Precision, Recall, F1
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
print(f"\\nPrecision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1-Score: {f1:.3f}")

# AUC
auc = roc_auc_score(y_test, y_pred_proba[:, 1])
print(f"\\nAUC: {auc:.3f}")

# Classification Report
print(f"\\n{classification_report(y_test, y_pred, target_names=data.target_names)}")

# ===== VISUALIZE =====
# Confusion Matrix Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
            xticklabels=data.target_names,
            yticklabels=data.target_names)
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.tight_layout()
plt.show()

# ROC Curve
fpr, tpr, _ = roc_curve(y_test, y_pred_proba[:, 1])
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, lw=2, label=f'AUC = {auc:.3f}')
plt.plot([0, 1], [0, 1], 'k--', lw=2, label='Random')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC Curve')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("\\n✅ Pipeline complete!")
```

---

## Common Patterns & Tricks

### Calculate All Metrics from Confusion Matrix

```python
# Get confusion matrix
cm = confusion_matrix(y_test, y_pred)
tn, fp, fn, tp = cm.ravel()

# Calculate all metrics manually
accuracy = (tp + tn) / (tp + tn + fp + fn)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * (precision * recall) / (precision + recall)
specificity = tn / (tn + fp)
fpr = fp / (fp + tn)

print(f"Accuracy: {accuracy:.3f}")
print(f"Precision: {precision:.3f}")
print(f"Recall: {recall:.3f}")
print(f"F1-Score: {f1:.3f}")
print(f"Specificity: {specificity:.3f}")
print(f"FPR: {fpr:.3f}")
```

### Compare Multiple Thresholds

```python
# Test different thresholds
thresholds_to_test = [0.3, 0.5, 0.7]
y_pred_proba = model.predict_proba(X_test_scaled)

for threshold in thresholds_to_test:
    y_pred_threshold = (y_pred_proba[:, 1] >= threshold).astype(int)
    precision = precision_score(y_test, y_pred_threshold)
    recall = recall_score(y_test, y_pred_threshold)
    f1 = f1_score(y_test, y_pred_threshold)

    print(f"\\nThreshold: {threshold}")
    print(f"  Precision: {precision:.3f}")
    print(f"  Recall: {recall:.3f}")
    print(f"  F1: {f1:.3f}")
```

### Get Prediction Confidence

```python
# Get probabilities
y_pred_proba = model.predict_proba(X_test_scaled)

# Calculate confidence (max probability)
confidence = np.max(y_pred_proba, axis=1)

# Find low-confidence predictions
low_confidence_idx = np.where(confidence < 0.6)[0]
print(f"Low confidence predictions: {len(low_confidence_idx)}")
print(f"Samples: {low_confidence_idx[:5]}")
```

---

## Troubleshooting

### Common Errors and Fixes

**Error:** `ConvergenceWarning: lbfgs failed to converge`
```python
# Fix: Increase max_iter
model = LogisticRegression(max_iter=10000)  # Default is 100
```

**Error:** `ValueError: could not convert string to float`
```python
# Fix: Encode categorical variables or check for non-numeric data
# Check for non-numeric columns
print(df.dtypes)
# Encode if needed
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['category'] = le.fit_transform(df['category'])
```

**Error:** Metrics return unexpected values
```python
# Check: Make sure positive class is what you think it is!
print(f"Positive class (1): {data.target_names[1]}")

# If needed, reverse labels
y = 1 - y  # Swap 0 and 1
```

**Warning:** Poor performance
```python
# Check 1: Did you scale features?
# Check 2: Is data balanced?
print(f"Class distribution: {np.bincount(y)}")
# Check 3: Did you split before preprocessing?
# Check 4: Are you using the right metric for your problem?
```

---

## Quick Command Reference

```python
# LOAD
data = load_breast_cancer()
X, y = data.data, data.target

# SPLIT
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SCALE
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# TRAIN
model = LogisticRegression(max_iter=10000, random_state=42)
model.fit(X_train_scaled, y_train)

# PREDICT
y_pred = model.predict(X_test_scaled)
y_pred_proba = model.predict_proba(X_test_scaled)

# EVALUATE
accuracy = accuracy_score(y_test, y_pred)
cm = confusion_matrix(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
auc = roc_auc_score(y_test, y_pred_proba[:, 1])
```

---

**Bookmark this page for quick reference during Week 2!** 🎓

---

*Week 2 sklearn Cheat Sheet v1.0 | December 2025*

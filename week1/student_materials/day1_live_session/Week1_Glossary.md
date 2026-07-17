# Week 1 Glossary - Linear Regression

**Purpose:** Key terms and concepts from Week 1 defined clearly
**Format:** Alphabetically organized with examples and cross-references

---

## How to Use This Glossary

- **Bold terms** are defined in this glossary
- *Italicized terms* are related concepts
- 📌 indicates especially important terms to memorize
- → indicates "see also" cross-references

---

## A

### Algorithm
A step-by-step procedure for solving a problem. In machine learning, an algorithm is the method used to learn patterns from data.

**Example:** Linear regression is an algorithm that learns to predict continuous values.

→ See also: *Model*, *Linear Regression*

---

### Assumption
A condition that must be true for a model to work correctly. Linear regression makes several assumptions about data.

**Key assumptions for linear regression:**
1. Linearity (relationship is linear)
2. Independence (samples are independent)
3. Homoscedasticity (constant variance)
4. Normality (residuals are normally distributed)

→ See also: *Residual Plot*

---

## C

### Coefficient 📌
The weight (slope) assigned to each feature in a linear regression model. Represented as β₁, β₂, etc.

**Mathematical representation:**
```
y = β₀ + β₁X₁ + β₂X₂ + ...
      ↑    ↑    ↑
   coefficients
```

**Example:** If the coefficient for square feet is 150, each additional square foot increases the house price by $150 (holding other features constant).

**Python access:**
```python
model.coef_  # Array of coefficients
```

→ See also: *Intercept*, *Feature*, *Partial Effect*

---

### Continuous Variable
A variable that can take any value within a range (not limited to whole numbers or categories).

**Examples:**
- House price: $250,000.37
- Temperature: 72.5°F
- Height: 5.83 feet

**Contrast with:** *Categorical Variable* (discrete categories like "red", "blue", "green")

→ See also: *Target Variable*, *Regression*

---

### Convergence
The point at which an iterative algorithm stops improving and reaches a stable solution.

**Context:** Gradient descent converges when it finds the minimum error.

→ See also: *Gradient Descent*, *Learning Rate*

---

### Cross-Validation
(Preview for Week 4) A technique for validating models by splitting data into multiple folds. Not covered in Week 1, but mentioned for future reference.

---

## D

### Data Leakage 📌
When information from the test set "leaks" into the training process, causing overly optimistic performance estimates.

**How it happens:** Preprocessing before splitting (e.g., scaling using statistics from entire dataset including test set).

**How to prevent:** Always split BEFORE any preprocessing!

**Analogy:** Studying for a test using questions from the actual test - you'll score great on that test but haven't actually learned.

→ See also: *Train-Test Split*, *Preprocessing*

---

### Dataset
A collection of data samples used for training and evaluating machine learning models.

**Week 1 datasets:**
- **California Housing:** 20,640 samples, 8 features, predicting median house value
- **Diabetes:** 442 samples, 10 features, predicting disease progression

→ See also: *Feature*, *Sample*, *Target Variable*

---

## E

### Error
The difference between a predicted value and the actual value.

**Formula:** `Error = Actual - Predicted`

**Also called:** Residual

→ See also: *Residual*, *MSE*, *RMSE*

---

### Evaluation
The process of measuring how well a model performs on unseen data.

**Week 1 evaluation metrics:**
- R² (percentage of variance explained)
- MSE (mean squared error)
- RMSE (root mean squared error)

→ See also: *Metrics*, *Test Set*

---

## F

### Feature 📌
An input variable used to make predictions. Also called an independent variable or predictor.

**Example (California Housing):**
- Features: MedInc, HouseAge, AveRooms, etc.
- Target: Median house value

**Python representation:** Columns of X matrix

→ See also: *Target Variable*, *X*, *y*

---

### Feature Engineering
The process of creating new features or transforming existing ones to improve model performance.

**Examples:**
- Creating polynomial features (X²)
- Combining features (e.g., total_rooms = bedrooms + bathrooms)
- Transforming variables (log, sqrt)

**Preview:** Week 4 covers this in depth.

---

### Fit
The process of training a model by learning parameters from training data.

**Python:**
```python
model.fit(X_train, y_train)
```

**What happens:** The model calculates coefficients (β values) that minimize error on the training data.

→ See also: *Train*, *.fit()*, *Parameters*

---

## G

### Generalization
A model's ability to perform well on new, unseen data (not just training data).

**Good generalization:** Train R² = 0.75, Test R² = 0.72 (similar performance)
**Poor generalization:** Train R² = 0.95, Test R² = 0.45 (overfitting!)

→ See also: *Overfitting*, *Test Set*

---

### Gradient Descent
An iterative optimization algorithm that finds the best model parameters by taking small steps in the direction that reduces error.

**Analogy:** Walking downhill in the dark by feeling which direction is steeper.

**Key parameter:** Learning rate (step size)

**Note:** sklearn's `LinearRegression` uses the Normal Equation, not gradient descent, but you'll see gradient descent in Week 6 (neural networks).

→ See also: *Learning Rate*, *Optimization*, *Normal Equation*

---

## H

### Heteroscedasticity
When the variance of residuals is not constant across all levels of predicted values.

**Visual:** Funnel shape in residual plot (variance increases with predictions)

**Problem:** Violates linear regression assumptions; predictions less reliable for some ranges.

**Contrast with:** Homoscedasticity (constant variance - what we want)

→ See also: *Residual Plot*, *Assumptions*

---

### Homoscedasticity
When the variance of residuals is constant across all levels of predicted values.

**What we want:** Residuals have similar spread for low, medium, and high predicted values.

**Visual:** Uniform scatter in residual plot (no funnel)

→ See also: *Heteroscedasticity*, *Residual Plot*

---

### Hyperparameter
A setting you choose BEFORE training that controls how the algorithm learns.

**Examples:**
- Learning rate (for gradient descent)
- Number of iterations
- test_size (proportion for test set)
- random_state (for reproducibility)

**Contrast with:** *Parameters* (learned during training, like coefficients)

→ See also: *Learning Rate*, *Parameters*

---

## I

### Independent Variable
Another name for a feature or input variable.

**Why "independent":** Features are assumed to be independent from each other (though this assumption can be violated - see *Multicollinearity*).

→ See also: *Feature*, *Dependent Variable*

---

### Inference
Drawing conclusions about the relationship between features and target, often using statistical tests.

**Example:** "Is the relationship between square feet and price statistically significant?"

**Week 1 focus:** Prediction, not inference (we care more about accurate predictions than statistical significance).

---

### Intercept 📌
The y-value when all features equal zero. Represented as β₀ in the linear equation.

**Mathematical representation:**
```
y = β₀ + β₁X₁ + β₂X₂ + ...
    ↑
 intercept
```

**Example:** In house price prediction, the intercept might be $50,000 (base price before considering features).

**Python access:**
```python
model.intercept_
```

→ See also: *Coefficient*, *y-intercept*

---

## L

### Learning Rate
A hyperparameter that controls the step size in gradient descent.

**Too small:** Slow convergence (many iterations needed)
**Too large:** May overshoot minimum and diverge
**Just right:** Fast, stable convergence

**Note:** Not used in sklearn's `LinearRegression` (only in `SGDRegressor`).

→ See also: *Gradient Descent*, *Hyperparameter*

---

### Least Squares
The method used by linear regression to find the best-fit line by minimizing the sum of squared errors.

**Formula to minimize:**
```
Σ(actual - predicted)²
```

**Why "squared":** Makes errors positive and penalizes large errors more.

→ See also: *MSE*, *Loss Function*

---

### Linear Regression 📌
A supervised learning algorithm that models the relationship between features and a continuous target as a linear equation.

**Equation:**
```
y = β₀ + β₁X₁ + β₂X₂ + ... + βₚXₚ
```

**Use cases:** Predicting house prices, temperatures, sales, etc.

**Week 1 focus algorithm!**

→ See also: *Regression*, *Supervised Learning*

---

### Loss Function
A mathematical function that measures how wrong a model's predictions are. The goal of training is to minimize this function.

**For linear regression:** Mean Squared Error (MSE)

**Formula:**
```
MSE = (1/n) Σ(actual - predicted)²
```

→ See also: *MSE*, *Optimization*

---

## M

### Machine Learning (ML)
The science of getting computers to learn patterns from data without being explicitly programmed.

**Types:**
- Supervised learning (Week 1-4: regression, classification)
- Unsupervised learning (Week 5: clustering)
- Deep learning (Week 6: neural networks)

---

### Mean Squared Error (MSE) 📌
A metric that measures the average squared difference between predicted and actual values.

**Formula:**
```
MSE = (1/n) Σ(yᵢ - ŷᵢ)²
```

**Interpretation:** Lower is better
**Problem:** Units are squared (hard to interpret)
**Solution:** Use RMSE instead

**Python:**
```python
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
```

→ See also: *RMSE*, *Loss Function*, *Metrics*

---

### Metrics
Measurements used to evaluate model performance.

**Week 1 metrics:**
- **R²:** Percentage of variance explained (0 to 1, higher is better)
- **MSE:** Mean squared error (lower is better)
- **RMSE:** Root mean squared error (lower is better, same units as target)

→ See also: *Evaluation*, *R²*, *MSE*, *RMSE*

---

### Model 📌
A mathematical representation learned from data that can make predictions.

**In sklearn:**
```python
model = LinearRegression()  # Create model
model.fit(X_train, y_train)  # Train model
y_pred = model.predict(X_test)  # Use model
```

→ See also: *Algorithm*, *Training*, *Prediction*

---

### Multicollinearity
When features are highly correlated with each other, making it difficult to determine their individual effects.

**Example:** Including both "square feet" and "square meters" as features (perfect correlation).

**Problem:** Coefficients become unstable and uninterpretable.

**Solution:** Remove one of the correlated features or use regularization (Week 4).

→ See also: *Feature*, *Coefficient*

---

### Multiple Linear Regression
Linear regression with more than one feature.

**Equation:**
```
y = β₀ + β₁X₁ + β₂X₂ + β₃X₃ + ...
```

**Contrast with:** Simple linear regression (only one feature: y = β₀ + β₁X)

---

## N

### Nonlinear
A relationship that cannot be represented by a straight line.

**Examples:**
- Exponential growth (population)
- Logarithmic (diminishing returns)
- Polynomial (curved relationships)

**Problem for linear regression:** LR assumes linear relationships!

**Solution:** Transform variables, add polynomial features, or use nonlinear algorithms (trees, neural nets).

→ See also: *Linear Regression*, *Residual Plot*

---

### Normal Equation
A mathematical formula that directly calculates the optimal coefficients for linear regression without iteration.

**Formula:** β = (X^T X)^(-1) X^T y

**What sklearn uses:** For most datasets (unless very large).

**Advantage:** Exact solution, no hyperparameters
**Disadvantage:** Slow for very large datasets

→ See also: *Gradient Descent*, *Coefficients*

---

### NumPy
A Python library for numerical computing, especially array/matrix operations.

**Week 1 usage:**
```python
import numpy as np
rmse = np.sqrt(mse)  # Calculate square root
```

---

## O

### Optimization
The process of finding model parameters that minimize the loss function.

**Methods:**
- Normal Equation (direct calculation)
- Gradient Descent (iterative)

→ See also: *Loss Function*, *Gradient Descent*

---

### Outlier
A data point that is very different from other observations.

**Example:** A $10M mansion in a dataset of $200K-$500K houses.

**Impact on linear regression:** Can distort the model (squared errors magnify outliers).

**What to do:** Investigate - is it a data error or a legitimate rare event?

→ See also: *Residual Plot*, *Robust Regression*

---

### Overfitting 📌
When a model performs very well on training data but poorly on test data because it has memorized noise instead of learning true patterns.

**Signs:**
- Train R² >> Test R²
- Very complex model for simple problem

**Prevention:**
- Use train/test split
- Regularization (Week 4)
- Cross-validation (Week 4)

**Contrast with:** Underfitting (model too simple, poor performance on both train and test)

→ See also: *Generalization*, *Train-Test Split*

---

## P

### Parameters 📌
Values learned by the model during training.

**For linear regression:** Coefficients (β₁, β₂, ...) and intercept (β₀)

**Contrast with:** *Hyperparameters* (set before training, like learning rate)

→ See also: *Coefficient*, *Intercept*, *Training*

---

### Partial Effect
The change in the target variable when one feature increases by one unit, holding all other features constant.

**What coefficients represent!**

**Example:** If β₁ = 150 for square feet, adding 1 sq ft increases price by $150, assuming bedrooms, age, etc. stay the same.

→ See also: *Coefficient*

---

### Prediction 📌
Using a trained model to estimate the target value for new, unseen data.

**Python:**
```python
y_pred = model.predict(X_test)
```

→ See also: *Model*, *Target Variable*

---

### Preprocessing
Transforming raw data before training a model.

**Examples:**
- Scaling features (standardization, normalization)
- Handling missing values
- Encoding categorical variables

**CRITICAL RULE:** Split data BEFORE preprocessing to prevent data leakage!

→ See also: *Data Leakage*, *Train-Test Split*

---

## R

### R² (R-squared) 📌
The coefficient of determination - a metric representing the percentage of variance in the target explained by the model.

**Formula:**
```
R² = 1 - (SS_residual / SS_total)
```

**Scale:** 0 (terrible) to 1 (perfect)
**Interpretation:** R² = 0.58 means model explains 58% of variance

**Python:**
```python
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
# OR
r2 = model.score(X_test, y_test)
```

→ See also: *Metrics*, *Variance*

---

### random_state 📌
A hyperparameter that sets the random seed for reproducibility.

**Usage:**
```python
train_test_split(X, y, test_size=0.2, random_state=42)
```

**What it does:** Ensures the same random split every time you run the code.

**Why 42?** Arbitrary! Reference to "Hitchhiker's Guide to the Galaxy" (answer to everything). Could be any number.

**ALWAYS SET THIS** for reproducibility in coursework!

→ See also: *Reproducibility*, *Train-Test Split*

---

### Regression
A type of supervised learning where the target variable is continuous (can take any numerical value).

**Examples:** Predicting house prices, temperatures, stock prices

**Contrast with:** *Classification* (predicting categories)

→ See also: *Linear Regression*, *Target Variable*

---

### Reproducibility
The ability to get the same results when running code multiple times.

**How to ensure:** Set `random_state` in all operations involving randomness.

→ See also: *random_state*

---

### Residual 📌
The difference between the actual value and the predicted value. Same as error.

**Formula:**
```
Residual = Actual - Predicted = y - ŷ
```

**Positive residual:** Model underestimated (predicted too low)
**Negative residual:** Model overestimated (predicted too high)

**Python:**
```python
residuals = y_test - y_pred
```

→ See also: *Error*, *Residual Plot*

---

### Residual Plot 📌
A scatter plot of predicted values (x-axis) vs. residuals (y-axis) used to validate linear regression assumptions.

**What to look for:**
- ✅ **Good:** Random scatter around zero (no patterns)
- ❌ **Bad:** Curved pattern (nonlinear relationship)
- ❌ **Bad:** Funnel shape (heteroscedasticity)
- ❌ **Bad:** Clusters (missing categorical features)

**Python:**
```python
residuals = y_test - y_pred
plt.scatter(y_pred, residuals)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.show()
```

→ See also: *Residual*, *Assumptions*, *Validation*

---

### RMSE (Root Mean Squared Error) 📌
The square root of MSE - represents average prediction error in the same units as the target.

**Formula:**
```
RMSE = √MSE = √[(1/n) Σ(yᵢ - ŷᵢ)²]
```

**Advantage over MSE:** Same units as target (easier to interpret)

**Example:** RMSE = 0.73 for California Housing means average error is $73,000 (since target is in $100K units: 0.73 × $100,000)

**Python:**
```python
import numpy as np
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
```

→ See also: *MSE*, *Metrics*

---

## S

### Sample
A single observation (row) in a dataset.

**Example:** One house with its features (square feet, bedrooms, age) and target (price).

**Python:** Rows of X matrix

→ See also: *Dataset*, *Feature*

---

### scikit-learn (sklearn) 📌
The primary Python library for machine learning used in this course.

**Installation:**
```bash
pip install scikit-learn
```

**Week 1 usage:**
```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
```

---

### Slope
The rate of change - how much y changes per unit change in x.

**In linear regression:** The coefficients (β₁, β₂, ...) are slopes.

→ See also: *Coefficient*

---

### Supervised Learning 📌
A type of machine learning where the training data includes both features (X) and the target variable (y).

**The model learns:** How to map X → y

**Types:**
- Regression (continuous target)
- Classification (categorical target)

**Week 1 focus:** Supervised learning for regression

**Contrast with:** Unsupervised learning (no target variable - Week 5)

→ See also: *Regression*, *Classification*, *Training*

---

## T

### Target Variable 📌
The variable we're trying to predict. Also called the dependent variable or output.

**Example:** House price, temperature, disease progression

**Python representation:** y vector

**Requirements for linear regression:** Must be continuous (not categorical)

→ See also: *Feature*, *y*, *Regression*

---

### Test Set 📌
The portion of data held back and used ONLY for evaluating model performance on unseen data.

**Typical size:** 20-30% of total data

**Critical rule:** Never train on test data! It must remain "unseen" to measure generalization.

**Python:**
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

→ See also: *Train Set*, *Train-Test Split*, *Generalization*

---

### Training 📌
The process of a model learning patterns from data by adjusting parameters to minimize error.

**For linear regression:** Finding coefficients that minimize MSE

**Python:**
```python
model.fit(X_train, y_train)  # This is training!
```

→ See also: *Fit*, *Parameters*, *Model*

---

### Train Set 📌
The portion of data used to train the model (learn parameters).

**Typical size:** 70-80% of total data

**Python:**
```python
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# test_size=0.2 means 80% for training
```

→ See also: *Test Set*, *Train-Test Split*

---

### Train-Test Split 📌
Dividing data into separate training and test sets to evaluate generalization.

**Why necessary:** Prevents overfitting and gives realistic performance estimate.

**CRITICAL TIMING:** Split BEFORE any preprocessing!

**Python:**
```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% for testing
    random_state=42     # For reproducibility
)
```

→ See also: *Train Set*, *Test Set*, *Data Leakage*

---

## U

### Underfitting
When a model is too simple to capture the underlying patterns in data, resulting in poor performance on both training and test sets.

**Example:** Using simple linear regression for highly nonlinear data.

**Contrast with:** *Overfitting* (too complex, memorizes training data)

→ See also: *Overfitting*, *Model Complexity*

---

## V

### Validation
The process of checking whether a model performs well on data it hasn't seen during training.

**Week 1 method:** Train-test split

**Week 4 method:** Cross-validation (more robust)

→ See also: *Test Set*, *Evaluation*

---

### Variance (in statistics)
A measure of how spread out data is.

**Formula:** Average of squared differences from the mean

**Context for R²:** R² measures how much of the target's variance is explained by the model.

---

### Variance (in ML - bias-variance tradeoff)
(Preview for later weeks) A model's sensitivity to small changes in training data. High variance models overfit.

---

## X

### X 📌
Conventional notation for the feature matrix (inputs).

**Shape:** (n_samples, n_features)

**Example:**
```python
X = data.data  # All features
print(X.shape)  # (20640, 8) for California Housing
```

→ See also: *Feature*, *y*

---

## Y

### y 📌
Conventional notation for the target vector (output).

**Shape:** (n_samples,) - one value per sample

**Example:**
```python
y = data.target  # Target variable
print(y.shape)  # (20640,) for California Housing
```

→ See also: *Target Variable*, *X*

---

### y-intercept
Another name for the intercept (β₀) - the value of y when all X values are zero.

→ See also: *Intercept*

---

### ŷ (y-hat)
Notation for predicted values.

**Pronounced:** "y-hat"

**Example:**
```python
y_pred = model.predict(X_test)  # y_pred is ŷ
```

→ See also: *Prediction*, *y*

---

## Additional Resources

### For More Definitions

**sklearn Glossary:**
https://scikit-learn.org/stable/glossary.html

**Statistics Glossary:**
https://www.statology.org/statistics-glossary/

**Machine Learning Glossary (Google):**
https://developers.google.com/machine-learning/glossary

---

## Quick Reference: Week 1 Key Terms

### Must Memorize

1. **Linear Regression** - Algorithm for predicting continuous values using linear equation
2. **Train-Test Split** - Dividing data into train and test sets
3. **Coefficient** - Weight for each feature (β₁, β₂, ...)
4. **Intercept** - Baseline value when all features are zero (β₀)
5. **R²** - Percentage of variance explained (0 to 1)
6. **MSE** - Mean squared error (average squared difference)
7. **RMSE** - Root mean squared error (in original units)
8. **Residual** - Difference between actual and predicted (error)
9. **Residual Plot** - Diagnostic plot to validate assumptions
10. **Data Leakage** - When test info leaks into training (split BEFORE preprocessing!)

### sklearn API Terms

1. **.fit()** - Train the model
2. **.predict()** - Make predictions
3. **.score()** - Calculate R² on test set
4. **.coef_** - Access coefficients
5. **.intercept_** - Access intercept

---

**Study tip:** Review this glossary before homework and exams. Knowing these terms will help you understand lecture content and documentation!

---

*Last Updated: 2025-11-26*

⸻

# Neural Network Loss + Activation Cheat Sheet

| Problem Type                     | Output Meaning                          | Activation Function        | Loss Function                     | When to Use                                      | Key Caveats |
|----------------------------------|----------------------------------------|----------------------------|-----------------------------------|--------------------------------------------------|-------------|
| Binary Classification            | Single probability (0–1)               | Sigmoid                    | Binary Cross-Entropy (BCE)         | Spam detection, yes/no tasks                     | Avoid MSE → poor gradients near 0/1 |
| Multi-Class (Exclusive)          | Probability distribution (sum = 1)     | Softmax                    | Categorical Cross-Entropy (CCE)    | Digit classification, image labels               | Classes must be mutually exclusive |
| Multi-Class (Sparse Labels)      | Same as above (integer labels)         | Softmax                    | Sparse Categorical Cross-Entropy   | Same as above, memory-efficient                  | Same caveat as CCE |
| Multi-Label Classification       | Independent probabilities per class    | Sigmoid (per output)       | Binary Cross-Entropy (BCE)         | Tags, object detection labels                   | Do NOT use softmax |
| Regression (Standard)            | Continuous value                      | Linear (no activation)     | Mean Squared Error (MSE)           | Predicting prices, demand                       | Sensitive to outliers |
| Regression (Robust)              | Continuous value                      | Linear                     | Mean Absolute Error (MAE)          | Noisy data, outliers present                    | Less smooth gradients |
| Regression (Hybrid)              | Continuous value                      | Linear                     | Huber Loss                         | Balance of MSE + MAE                            | Requires tuning delta |
| Imbalanced Classification        | Probability                           | Sigmoid / Softmax          | Focal Loss                         | Rare events (fraud, defects)                    | Extra hyperparameter (gamma) |
| Distribution Prediction          | Full probability distribution         | Softmax                    | KL Divergence                      | Forecasting distributions, generative models     | Asymmetric (direction matters) |
| Margin-Based Classification      | Distance from decision boundary       | Linear / None              | Hinge Loss                         | SVM-style classifiers                           | Not probabilistic |


⸻

🔥 The Pairing Patterns (Memorize This)

1. Probabilities → Cross-Entropy Family
	•	Sigmoid → BCE
	•	Softmax → CCE

👉 Why:
	•	These losses are derived from log-likelihood
	•	They match probability theory → better gradients

⸻

2. Continuous Values → Distance-Based Loss
	•	Linear → MSE / MAE / Huber

👉 Why:
	•	You’re measuring distance between numbers

⸻

3. Independent vs Competing Outputs

Case	Activation	Loss
Independent labels	Sigmoid	BCE
Competing classes	Softmax	CCE

👉 This is one of the most important distinctions in ML

⸻

⚠️ Common Mistakes (High-Value)

❌ Mistake 1: Softmax for multi-label
	•	Forces probabilities to sum to 1
	•	Breaks independent predictions

⸻

❌ Mistake 2: MSE for classification
	•	Leads to slow / unstable training
	•	Especially bad with sigmoid

⸻

❌ Mistake 3: Ignoring outliers with MSE
	•	Large errors dominate loss
	•	Model overfits rare extreme cases

⸻

❌ Mistake 4: Using BCE with Softmax
	•	Assumes independence when outputs are dependent

⸻

🧠 Mental Shortcut (What you should think in practice)

When designing a model, ask:
	1.	What is my output?
	•	Probability? → Cross-entropy
	•	Number? → MSE/MAE
	2.	Are outputs independent or competing?
	•	Independent → Sigmoid
	•	Competing → Softmax
	3.	Do I have outliers or imbalance?
	•	Yes → MAE / Huber / Focal

⸻

💡 Teaching Insight (for your courses / Blue River)

If you want a one-liner for students:

Activation defines the output space.
Loss defines how mistakes are measured in that space.

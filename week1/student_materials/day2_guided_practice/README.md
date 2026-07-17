# Week 1 - Day 2: Guided Practice Materials

**Duration:** 1 hour
**Format:** Deep dive + guided practice + assessment

---

## 📁 Contents

### Main Exercise

1. **`week1_boston_housing_guided.ipynb`** - Boston Housing Prediction
   - Guided in-class exercise (20 minutes)
   - Instructor codes, students follow along
   - 506 houses, 13 features
   - Apply Day 1 pipeline to new dataset
   - Interpret residual plots with Day 2 knowledge

### Additional Practice (Take-Home)

2. **`week1_auto_mpg_practice.ipynb`** - Auto MPG Prediction ✅
   - Car fuel efficiency prediction (398 cars from 1970s-1980s)
   - Different domain from housing (automotive vs. real estate)
   - Same 8-step pipeline structure
   - Solutions provided (expandable at end)

3. **`week1_bonus_polynomial.ipynb`** - Polynomial Features
   - Handling nonlinear relationships
   - Extends Deep Dive learning
   - Shows how to fix curved residual patterns

### Assessment

4. **`Week1_Self_Assessment.md`** - Review questions and reflections

### Solutions

5. **`week1_postclass_solutions.ipynb`** - Solutions for Boston Housing

---

## 🎯 Learning Objectives (Day 2)

By the end of Day 2, students will:
- Understand the 4 assumptions of linear regression
- Map residual patterns to assumption violations
- Know solutions for each pattern type
- Recognize when linear regression is inappropriate
- Complete a full regression pipeline with guidance
- Assess own understanding through quiz

---

## ⏱️ Day 2 Timeline

```
0:00-0:05  Welcome & Day 1 Recap
0:05-0:25  Deep Dive: Statistical Foundations (20 min)
           - 4 assumptions: Linearity, Independence,
             Homoscedasticity, Normality
           - Why residual patterns matter
           - Solutions for each violation
           - When NOT to use linear regression

0:25-0:45  Guided Practice: Boston Housing (20 min)
           - Apply pipeline to new dataset
           - Focus on residual interpretation
           - Compare to Day 1 results

0:45-0:55  Assessment Quiz (10 min)
           - 8 questions on Deep Dive content
           - Immediate review of answers

0:55-1:00  Week 2 Preview & Take-Home Assignment
```

---

## 📊 Key Concepts Covered (Day 2)

### The 4 Assumptions

1. **Linearity** - Relationship between X and y is linear
   - Violated by: Curved residual pattern
   - Fix: Polynomial features, transformations, nonlinear models

2. **Independence** - Observations independent of each other
   - Violated by: Time series, spatial data
   - Fix: Specialized methods (ARIMA, mixed-effects)

3. **Homoscedasticity** - Constant variance of residuals
   - Violated by: Funnel-shaped residuals
   - Fix: Log transform target, weighted least squares

4. **Normality** - Residuals approximately normal
   - Violated by: Heavy tails, extreme skew
   - Fix: Least critical for prediction, transformations help

### Pattern → Solution Mapping

| Pattern | Assumption | Solution |
|---------|------------|----------|
| Random scatter ✓ | None | Use model! |
| Curve | Linearity | Add X², transform |
| Funnel | Homoscedasticity | log(y) |
| Clusters | Missing features | Add categories |
| Outliers | Investigate | Check data |

### When NOT to Use LR

- ❌ Categorical targets (classification)
- ❌ Time series (violates independence)
- ❌ p >> n (too many features)
- ❌ Severe nonlinearity

---

## 🚀 After Day 2

**What You Should Know:**
- ✅ Visual residual pattern recognition (Day 1)
- ✅ Statistical foundations (Day 2)
- ✅ Solutions for each pattern
- ✅ When to use/not use linear regression

**Take-Home Practice:**
- Complete Auto MPG exercise (when provided)
- Explore Bonus: Polynomial Features
- Review Deep Dive materials if needed

**Week 2 Preview:**
- Classification with Logistic Regression
- Spam detection, product recommendations
- Confusion matrices, precision, recall

---

## 💡 Tips for Day 2

1. **Connect to Day 1** - You already know WHAT patterns look like, now learn WHY
2. **Focus on assumptions** - They explain everything about residual plots
3. **Practice pattern → solution** - See curve? Add polynomial features.
4. **Remember classification rule** - NEVER use LR for yes/no targets
5. **Take the quiz seriously** - It shows what you've mastered

---

## 📝 Assessment Quiz Topics

**Expect questions on:**
- Which assumption is violated by specific patterns?
- What to try first for each pattern type?
- When NOT to use linear regression?
- Identifying overfitting (train vs test R²)
- What homoscedasticity means

**Passing:** 5+/8 correct (60%)

---

## 🔗 Related Materials

- **Day 1 Materials:** `day1_live_session/`
- **Teaching Guide:** `teaching_guide/DAY2_DEEP_DIVE_TEACHING_GUIDE.md`
- **Quick Reference:** `teaching_guide/DAY2_QUICK_REFERENCE.md`
- **Quiz:** `teaching_guide/DAY2_QUIZ.md`
- **Deep Dives (Background):** `instructor_materials/deep_dives/`

---

## ❓ Common Questions

**Q: "Do I need to memorize the 4 assumptions?"**
A: Understand, not memorize. Know that LR makes assumptions and residual plots reveal violations.

**Q: "What if my Boston Housing results differ from others?"**
A: Random split causes slight variations. R² between 0.70-0.75 is expected.

**Q: "Should I do the bonus polynomial exercise?"**
A: Highly recommended! It shows how to handle curved residual patterns.

**Q: "When will we use logistic regression?"**
A: Week 2! You'll revisit classification problems with the RIGHT algorithm.

---

*If you're returning after a break: This folder contains all Day 2 (second hour) materials.*

# Appendix F: Model Saving & Loading Guide

## Keras 3.x Format (.keras)

### Saving Complete Model
```python
model.save('my_model.keras')
```
**Saves:** Architecture + weights + optimizer state + compilation config

### Loading Model
```python
from keras.models import load_model
model = load_model('my_model.keras')
```
**Ready for:** Immediate predictions, continued training

## Legacy Formats

### HDF5 Format (.h5) - Keras 2.x
```python
model.save('model.h5')  # Old format
model = load_model('model.h5')
```
**Note:** Still works but .keras preferred for Keras 3.x

## Saving Only Weights
```python
model.save_weights('weights.weights.h5')
model.load_weights('weights.weights.h5')
```
**Use when:** Need to reload weights into same architecture

## Best Practices

1. **Always use .keras extension** for Keras 3.x
2. **Include version** in filename: model_v1.keras
3. **Save after training** before evaluation  
4. **Test loading** immediately after saving
5. **Version control** model files separately

## Common Issues

**Issue:** "Unable to load model"
**Fix:** Check Keras version matches

**Issue:** "Model architecture changed"
**Fix:** Can't load into different architecture, must retrain

**Issue:** Custom layers/losses
**Fix:** Provide custom_objects parameter

## Deployment Workflow

1. Train model → 2. Save as .keras → 3. Test load → 4. Deploy  

*Appendix F | Version 1.0 | February 2026*

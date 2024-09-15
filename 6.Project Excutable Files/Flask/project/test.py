
import pickle

# Load the model
with open('credit.pkl', 'rb') as handle:
    model = pickle.load(handle)

# Print out the coefficients and feature names
if hasattr(model, 'coef_') and hasattr(model, 'intercept_'):
    print("Model Coefficients:", model.coef_)
    print("Model Intercept:", model.intercept_)
else:
    print("Model does not have coefficients and intercepts attributes.")

# Assuming feature names were set during training
if hasattr(model, 'feature_names_in_'):
    print("Feature Names:", model.feature_names_in_)
else:
    print("Model does not have feature names attribute.")

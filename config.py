"""
Configuration constants for the ANN for Antenna Design project.
"""

import os

# Path Constants
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_FILE = os.path.join(ROOT_DIR, "antenna_dataset.csv")
MODEL_FILE = os.path.join(ROOT_DIR, "antenna_model.pkl")
SCALER_FILE = os.path.join(ROOT_DIR, "scaler.pkl")

# Physical Constants
C0 = 299792458  # Speed of light in m/s

# Default Parameter Ranges (mm)
PARAM_RANGES = {
    'W': (20.0, 60.0),
    'L': (20.0, 60.0),
    'h': (0.5, 3.2),
    'er': (2.2, 10.2)
}

# Model Hyperparameters
MLP_CONFIG = {
    'hidden_layer_sizes': (128, 64, 32),
    'activation': 'relu',
    'solver': 'adam',
    'max_iter': 500,
    'random_state': 42
}

# Optimization Config
OPTIM_BOUNDS = [(10.0, 100.0), (10.0, 100.0)]  # [W, L]

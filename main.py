import argparse
import os
import logging
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
from typing import Optional, Tuple
from sklearn.model_selection import train_test_split, KFold, cross_val_score
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from generator import generate_antenna_data
from model import build_ann_model
from optimizer import run_inverse_design
from config import DATA_FILE, MODEL_FILE, SCALER_FILE

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def train(use_cv: bool = False) -> None:
    """
    Handles the end-to-end training pipeline:
    1. Data Loading/Generation
    2. Preprocessing (Scaling)
    3. Model Training (with optional Cross-Validation)
    4. Evaluation and Serialization
    """
    logger.info("Initializing Training Pipeline... PHASE 1/4")
    
    if not os.path.exists(DATA_FILE):
        logger.info("Dataset not found. Generating new synthetic antenna data...")
        generate_antenna_data(num_samples=2000)
    
    df = pd.read_csv(DATA_FILE)
    X = df[['W_mm', 'L_mm', 'h_mm', 'er']].values
    y = df['fr_GHz'].values
    
    # Preprocessing
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    if use_cv:
        logger.info("Executing 5-Fold Cross Validation... PHASE 2/4")
        model_cv = build_ann_model()
        # Note: cross_val_score doesn't return the fitted model, just scores
        scores = cross_val_score(model_cv, X_scaled, y, cv=5, scoring='neg_mean_squared_error')
        mse_scores = -scores
        logger.info(f"CV MSE Scores: {mse_scores}")
        logger.info(f"Mean MSE: {mse_scores.mean():.6f} (+/- {mse_scores.std():.6f})")
    
    # Train-Test Split for the final model
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    logger.info("Training the Final MLP Model... PHASE 3/4")
    model = build_ann_model()
    model.fit(X_train, y_train)
    
    # Evaluation
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    print("\n" + "="*40)
    print("  [MODEL PERFORMANCE METRICS]")
    print("="*40)
    print(f" MSE:  {mse:.6f}")
    print(f" MAE:  {mae:.6f}")
    print(f" R²:   {r2:.6f}")
    print("="*40 + "\n")
    
    # Saving
    joblib.dump(model, MODEL_FILE)
    joblib.dump(scaler, SCALER_FILE)
    logger.info(f"Model saved to {MODEL_FILE}")
    logger.info(f"Scaler saved to {SCALER_FILE}")
    
    # Visualization: Residual Plot
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred, alpha=0.5, color='#3498db', label='Predictions')
    plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], '#e74c3c', lw=2, linestyle='--', label='Ideal Fit')
    plt.title('Error Analysis: Actual vs. Predicted Resonance Frequency', fontsize=12)
    plt.xlabel('Actual Frequency (GHz)')
    plt.ylabel('Predicted Frequency (GHz)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig('prediction_plot.png', dpi=300)
    logger.info("Performance plot saved as 'prediction_plot.png'")

def predict(W: float, L: float, h: float, er: float) -> None:
    """
    Performs a single frequency prediction for given physical parameters.
    """
    if not os.path.exists(MODEL_FILE) or not os.path.exists(SCALER_FILE):
        logger.error("No trained model found. Please run with --train first.")
        return

    model = joblib.load(MODEL_FILE)
    scaler = joblib.load(SCALER_FILE)
    
    inputs = np.array([[W, L, h, er]])
    inputs_scaled = scaler.transform(inputs)
    
    prediction = model.predict(inputs_scaled)[0]
    
    print("\n" + "="*40)
    print("  [RESONANCE FREQUENCY ESTIMATE]")
    print("="*40)
    print(f" Parameters: W={W}, L={L}, h={h}, er={er}")
    print(f" Predicted f_r: {prediction:.4f} GHz")
    print("="*40 + "\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ANN for Antenna Design CLI - Professional Engineering Tool")
    parser.add_argument("--train", action="store_true", help="Execute model training pipeline")
    parser.add_argument("--cv", action="store_true", help="Perform 5-fold cross-validation")
    parser.add_argument("--predict", action="store_true", help="Predict frequency for a specific design")
    parser.add_argument("--inverse", action="store_true", help="Perform inverse design (Frequency -> Dimensions)")
    parser.add_argument("--target_f", type=float, default=2.4, help="Target resonance frequency (GHz)")
    parser.add_argument("--W", type=float, default=40.0, help="Width (mm)")
    parser.add_argument("--L", type=float, default=40.0, help="Length (mm)")
    parser.add_argument("--H", type=float, default=1.6, help="Substrate Height (mm)")
    parser.add_argument("--ER", type=float, default=4.4, help="Dielectric Constant (er)")
    
    args = parser.parse_args()
    
    if args.train:
        train(use_cv=args.cv)
    elif args.predict:
        predict(args.W, args.L, args.H, args.ER)
    elif args.inverse:
        run_inverse_design(args.target_f, args.H, args.ER)
    else:
        parser.print_help()

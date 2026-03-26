import numpy as np
import joblib
import logging
import os
import matplotlib.pyplot as plt
from typing import Dict, List
from config import MODEL_FILE, SCALER_FILE

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class SensitivityAnalyzer:
    """
    Analyzes the sensitivity of the antenna's resonance frequency 
    with respect to its physical parameters (W, L, h, er).
    """

    def __init__(self, model_path: str = MODEL_FILE, scaler_path: str = SCALER_FILE):
        if not os.path.exists(model_path) or not os.path.exists(scaler_path):
            raise FileNotFoundError("Model or Scaler not found.")
        
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)

    def analyze(self, baseline: List[float] = [40.0, 40.0, 1.6, 4.4], delta: float = 0.05) -> Dict[str, float]:
        """
        Performs a perturbation-based sensitivity analysis.
        
        Calculates Δf_r / ΔParam for each parameter.
        """
        params_names = ['W_mm', 'L_mm', 'h_mm', 'er']
        baseline_pred = self.model.predict(self.scaler.transform([baseline]))[0]
        
        sensitivities = {}
        
        for i, name in enumerate(params_names):
            # Perturb parameter i by +delta%
            perturbed = list(baseline)
            perturbed[i] *= (1 + delta)
            
            perturbed_pred = self.model.predict(self.scaler.transform([perturbed]))[0]
            
            # Sensitivity = abs(change in output / percent change in input)
            sensitivity = abs((perturbed_pred - baseline_pred) / delta)
            sensitivities[name] = sensitivity
            
        return sensitivities

def plot_sensitivity():
    """
    Runs sensitivity analysis and saves a professional bar chart.
    """
    logger.info("Performing Sensitivity Analysis...")
    try:
        analyzer = SensitivityAnalyzer()
        results = analyzer.analyze()
        
        names = list(results.keys())
        values = list(results.values())
        
        # Sort results
        idx = np.argsort(values)
        names = [names[i] for i in idx]
        values = [values[i] for i in idx]
        
        plt.figure(figsize=(10, 6))
        plt.barh(names, values, color='#2ecc71', alpha=0.8)
        plt.title('Design Sensitivity Analysis: Impact on Resonance Frequency', fontsize=14)
        plt.xlabel('Sensitivity (Normalized |Δf_r / 5% ΔParam|)', fontsize=12)
        plt.grid(axis='x', linestyle='--', alpha=0.6)
        
        plt.tight_layout()
        plt.savefig('sensitivity_analysis.png', dpi=300)
        logger.info("Sensitivity analysis plot saved as 'sensitivity_analysis.png'")
        
        print("\n" + "="*40)
        print("  [SENSITIVITY ANALYSIS RESULTS]")
        print("="*40)
        for name, val in results.items():
            print(f" {name:10}: {val:.4f}")
        print("="*40 + "\n")
        
    except Exception as e:
        logger.error(f"Sensitivity analysis failed: {e}")

if __name__ == "__main__":
    plot_sensitivity()

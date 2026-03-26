import joblib
import numpy as np
import logging
from scipy.optimize import minimize, OptimizeResult
import os
from typing import Tuple, Optional, List
from config import MODEL_FILE, SCALER_FILE, OPTIM_BOUNDS

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

class AntennaInverseOptimizer:
    """
    A class to handle inverse design of antennas using a pre-trained ANN model.

    This optimizer finds the optimal physical dimensions (W, L) that result in a 
    target resonance frequency, given fixed substrate parameters (h, er).
    """

    def __init__(self, model_path: str = MODEL_FILE, scaler_path: str = SCALER_FILE):
        """
        Initializes the optimizer with a trained model and scaler.

        Args:
            model_path (str): Path to the .pkl model file.
            scaler_path (str): Path to the .pkl scaler file.
        """
        if not os.path.exists(model_path) or not os.path.exists(scaler_path):
            logger.error("Model or Scaler not found. Run training first.")
            raise FileNotFoundError(f"Missing files: {model_path} or {scaler_path}")
        
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        logger.info("Optimizer: Model and Scaler loaded successfully.")

    def _cost_function(self, params: np.ndarray, target_f: float, h: float, er: float) -> float:
        """
        Calculates the squared error between target frequency and predicted frequency.

        Args:
            params (np.ndarray): Array [W, L] to optimize.
            target_f (float): Desired frequency (GHz).
            h (float): Fixed substrate height (mm).
            er (float): Fixed dielectric constant.

        Returns:
            float: The cost value.
        """
        W, L = params
        # Prepare input for mapping (W, L, h, er)
        input_data = np.array([[W, L, h, er]])
        input_scaled = self.scaler.transform(input_data)
        
        predicted_f = self.model.predict(input_scaled)[0]
        return float((target_f - predicted_f)**2)

    def optimize(self, target_f: float, h: float, er: float, initial_guess: List[float] = [40.0, 40.0]) -> np.ndarray:
        """
        Executes the optimization algorithm (L-BFGS-B).

        Args:
            target_f (float): Target frequency in GHz.
            h (float): Substrate height in mm.
            er (float): Relative permittivity.
            initial_guess (List[float]): Starting W and L [mm].

        Returns:
            np.ndarray: Optimized [W, L] dimensions.
        """
        logger.info(f"Finding optimal dimensions for f_r = {target_f} GHz...")

        result: OptimizeResult = minimize(
            self._cost_function, 
            initial_guess, 
            args=(target_f, h, er),
            bounds=OPTIM_BOUNDS,
            method='L-BFGS-B'
        )
        
        if result.success:
            logger.info(f"Optimization converged. Loss: {result.fun:.6e}")
            return result.x  # [W_opt, L_opt]
        else:
            logger.warning(f"Optimization warning: {result.message}")
            return result.x

def run_inverse_design(target_f: float, h: float, er: float) -> Optional[Tuple[float, float]]:
    """
    Helper function to run inverse design through the CLI.
    """
    try:
        optimizer = AntennaInverseOptimizer()
        w_opt, l_opt = optimizer.optimize(target_f, h, er)
        
        # Validation
        val_input = np.array([[w_opt, l_opt, h, er]])
        val_scaled = optimizer.scaler.transform(val_input)
        predicted_f = optimizer.model.predict(val_scaled)[0]
        
        print("\n" + "="*40)
        print(f"  [DESIGN SOLUTION FOUND]")
        print("="*40)
        print(f" Target Frequency:  {target_f:.4f} GHz")
        print(f" Resulting Width:   {w_opt:.4f} mm")
        print(f" Resulting Length:  {l_opt:.4f} mm")
        print(f" Predicted f_r:     {predicted_f:.4f} GHz")
        print(f" Design Error:      {abs(target_f - predicted_f):.6f} GHz")
        print("="*40 + "\n")
        
        return float(w_opt), float(l_opt)
    except Exception as e:
        logger.error(f"Inverse design aborted: {e}")
        return None

if __name__ == "__main__":
    # Test call
    run_inverse_design(2.4, 1.6, 4.4)

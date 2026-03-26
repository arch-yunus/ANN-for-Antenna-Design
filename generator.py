import numpy as np
import pandas as pd
import logging
from typing import Optional
from config import DATA_FILE, C0, PARAM_RANGES

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def generate_antenna_data(num_samples: int = 1000, filename: str = DATA_FILE) -> str:
    """
    Generates synthetic data for a microstrip patch antenna using the Transmission Line Model.

    The resonant frequency (fr) is calculated using the physical dimensions (W, L), 
    substrate height (h), and dielectric constant (er).

    Args:
        num_samples (int): Number of synthetic data points to generate.
        filename (str): The output CSV filename.

    Returns:
        str: The path to the generated CSV file.
    """
    logger.info(f"Generating {num_samples} antenna data samples...")

    # Randomly sample physical parameters within specified ranges
    W = np.random.uniform(*PARAM_RANGES['W'], num_samples)
    L = np.random.uniform(*PARAM_RANGES['L'], num_samples)
    h = np.random.uniform(*PARAM_RANGES['h'], num_samples)
    er = np.random.uniform(*PARAM_RANGES['er'], num_samples)

    # 1. Calculate effective dielectric constant (er_eff)
    # This accounts for the fringing fields at the edges of the patch.
    er_eff = (er + 1) / 2 + (er - 1) / 2 * (1 + 12 * h / W)**-0.5

    # 2. Calculate Resonant Frequency (fr) in GHz
    # Formula: fr = c0 / (2 * L * sqrt(er_eff))
    # We convert L from mm to meters (* 1e-3) and final result to GHz (* 1e-9)
    fr = (C0 / (2 * (L * 1e-3) * np.sqrt(er_eff))) * 1e-9

    # 3. Add simulated measurement noise (Gaussian)
    # In real-world EM solvers (like HFSS or CST), results vary slightly due to mesh density.
    noise = np.random.normal(0, 0.02, num_samples)  # Reduced noise for better educational clarity
    fr += noise

    # Create DataFrame
    df = pd.DataFrame({
        'W_mm': W,
        'L_mm': L,
        'h_mm': h,
        'er': er,
        'fr_GHz': fr
    })

    # Save to CSV
    df.to_csv(filename, index=False)
    logger.info(f"Dataset successfully saved to: {filename}")
    
    return filename

if __name__ == "__main__":
    generate_antenna_data()

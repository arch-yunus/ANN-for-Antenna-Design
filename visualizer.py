import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import os
import logging
from typing import Optional
from config import MODEL_FILE, SCALER_FILE

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')
logger = logging.getLogger(__name__)

def visualize_3d_parameter_surface(h_fixed: float = 1.6, er_fixed: float = 4.4, save_path: str = '3d_parameter_surface.png'):
    """
    Generates a professional 3D surface plot showing the interaction between 
    Width (W) and Length (L) on the resonance frequency (fr).

    Args:
        h_fixed (float): Substrate height to fix for the 2D slice.
        er_fixed (float): Dielectric constant to fix for the 2D slice.
        save_path (str): Path to save the output image.
    """
    if not os.path.exists(MODEL_FILE) or not os.path.exists(SCALER_FILE):
        logger.error("No trained model found. Please run 'python main.py --train' first.")
        return

    logger.info(f"Generating 3D parameter surface for h={h_fixed}, er={er_fixed}...")
    
    model = joblib.load(MODEL_FILE)
    scaler = joblib.load(SCALER_FILE)

    # Create high-resolution grid for W and L
    w_range = np.linspace(20, 60, 100)
    l_range = np.linspace(20, 60, 100)
    W_grid, L_grid = np.meshgrid(w_range, l_range)
    
    # Prepare input batch for prediction
    grid_points = np.column_stack([
        W_grid.ravel(), 
        L_grid.ravel(), 
        np.full_like(W_grid.ravel(), h_fixed), 
        np.full_like(W_grid.ravel(), er_fixed)
    ])
    
    # Scale and predict
    grid_points_scaled = scaler.transform(grid_points)
    fr_pred = model.predict(grid_points_scaled)
    fr_grid = fr_pred.reshape(W_grid.shape)

    # Plotting using high-authority aesthetics
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Use 'plasma' or 'viridis' for high-contrast engineering plots
    surface = ax.plot_surface(
        W_grid, L_grid, fr_grid, 
        cmap='plasma', 
        edgecolor='none', 
        alpha=0.9,
        antialiased=True
    )
    
    # Labeling with LaTeX-style formatting for professional look
    ax.set_title(fr'Antenna Parameter Topology: $f_r(W, L)$ @ $h={h_fixed}, \epsilon_{{r}}={er_fixed}$', fontsize=16, pad=30)
    ax.set_xlabel('Width ($W$) [mm]', fontsize=12, labelpad=15)
    ax.set_ylabel('Length ($L$) [mm]', fontsize=12, labelpad=15)
    ax.set_zlabel('Resonances ($f_r$) [GHz]', fontsize=12, labelpad=15)
    
    # Add a color bar
    cbar = fig.colorbar(surface, ax=ax, shrink=0.5, aspect=10, pad=0.1)
    cbar.set_label('Frequency [GHz]', rotation=270, labelpad=20)
    
    # Adjust view angle for best perception
    ax.view_init(elev=30, azim=225)
    
    plt.tight_layout()
    plt.savefig(save_path, dpi=300)
    logger.info(f"3D visualization saved as '{save_path}'")
    plt.close()

if __name__ == "__main__":
    visualize_3d_parameter_surface()

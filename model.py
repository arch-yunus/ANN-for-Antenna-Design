from sklearn.neural_network import MLPRegressor
from config import MLP_CONFIG

def build_ann_model() -> MLPRegressor:
    """
    Builds a Multilayer Perceptron (MLP) for frequency prediction using Scikit-learn.

    The model is initialized with a robust architecture (128, 64, 32) and L2 regularization
    (alpha) to prevent overfitting on the synthetic data.

    Returns:
        MLPRegressor: An un-fitted Scikit-learn MLP Regressor object.
    """
    model = MLPRegressor(
        hidden_layer_sizes=MLP_CONFIG['hidden_layer_sizes'],
        activation=MLP_CONFIG['activation'],
        solver=MLP_CONFIG['solver'],
        max_iter=MLP_CONFIG['max_iter'],
        random_state=MLP_CONFIG['random_state']
    )
    return model

if __name__ == "__main__":
    # Test initialization
    m = build_ann_model()
    print("Scikit-learn MLPRegressor initialized successfully.")

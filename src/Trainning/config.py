"""
Configuration centralisée pour l'entraînement et l'application AI-Sketch.
"""

# Liste exacte des 7 classes présentes dans le dossier data/raw/
CLASSES = [
    "apple",
    "crown",
    "diamond",
    "door",
    "airplane",
    "cat",
    "hammer",
]

# Hyperparamètres d'entraînement
BATCH_SIZE = 64
EPOCHS = 10
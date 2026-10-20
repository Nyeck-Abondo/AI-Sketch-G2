from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # aucune fenêtre : les graphiques sont enregistrés
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

keras = tf.keras
layers = tf.keras.layers

# Noms des fichiers Quick, Draw! (en anglais) pour les classes en français
FR_TO_EN = {
    "pomme": "apple",
    "couronne": "crown",
    "diamant": "diamond",
    "porte": "door",
    "avion": "full_numpy_bitmap_airplane",
    "airplane": "full_numpy_bitmap_airplane",
    "chat": "full_numpy_bitmap_cat",
    "cat": "full_numpy_bitmap_cat",
    "marteau": "hammer",
}

from config import CLASSES, BATCH_SIZE, EPOCHS

ROOT = Path(__file__).resolve().parent.parent.parent  # racine du projet

# Définition directe des dossiers de sortie et du modèle
OUT_DIR = ROOT / "output"
MODEL_PATH = ROOT / "models" / "sketch_classifier.keras"

SAMPLES_PER_CLASS = 10000
SEED = 42
def find_npy(class_name):
    fname = FR_TO_EN.get(class_name.lower(), class_name.lower()) + ".npy"
    for folder in (ROOT / "data" / "raw", ROOT / "data"):
        path = folder / fname
        if path.exists():
            return path
    raise FileNotFoundError(f"{fname} introuvable dans data/raw/ ni dans data/")


def load_data():
    """Retourne x (N,28,28,1) normalisé entre 0 et 1, et y (N,) entiers."""
    xs, ys = [], []
    for label, name in enumerate(CLASSES):
        arr = np.load(find_npy(name), mmap_mode="r")
        n = min(SAMPLES_PER_CLASS, len(arr))
        xs.append(np.array(arr[:n]))
        ys.append(np.full(n, label, dtype=np.int64))
        print(f"{name} : {n} dessins")
    x = np.concatenate(xs).reshape(-1, 28, 28, 1).astype("float32") / 255.0
    y = np.concatenate(ys)
    return x, y


# --- Modèle ------------------------------------------------------------------
def build_model(num_classes):
    model = keras.Sequential([
        layers.Input(shape=(28, 28, 1)),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dropout(0.3),
        layers.Dense(num_classes, activation="softmax"),
    ])
    model.compile(optimizer="adam",
                  loss="sparse_categorical_crossentropy",
                  metrics=["accuracy"])
    return model


# --- Graphiques pour le rapport ----------------------------------------------
def save_curves(history):
    fig, axes = plt.subplots(1, 2, figsize=(10, 4))
    for ax, key, title in zip(axes, ("accuracy", "loss"), ("Précision", "Perte")):
        ax.plot(history.history[key], label="entraînement")
        ax.plot(history.history["val_" + key], label="validation")
        ax.set_title(title)
        ax.set_xlabel("époque")
        ax.legend()
    fig.tight_layout()
    fig.savefig(OUT_DIR / "courbes_entrainement.png", dpi=150)
    plt.close(fig)


def save_confusion(y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred)
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.imshow(cm, cmap="Blues")
    ax.set_xticks(range(len(CLASSES)))
    ax.set_yticks(range(len(CLASSES)))
    ax.set_xticklabels(CLASSES, rotation=45, ha="right")
    ax.set_yticklabels(CLASSES)
    ax.set_xlabel("Prédit")
    ax.set_ylabel("Réel")
    ax.set_title("Matrice de confusion")
    for i in range(len(CLASSES)):
        for j in range(len(CLASSES)):
            ax.text(j, i, cm[i, j], ha="center", va="center",
                    color="white" if cm[i, j] > cm.max() / 2 else "black")
    fig.tight_layout()
    fig.savefig(OUT_DIR / "matrice_confusion.png", dpi=150)
    plt.close(fig)


# --- Programme principal -------------------------------------------------------
def train():
    np.random.seed(SEED)
    tf.random.set_seed(SEED)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)

    x, y = load_data()
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, stratify=y, random_state=SEED)
    print(f"Entraînement : {len(x_train)} | Test : {len(x_test)}")

    model = build_model(len(CLASSES))
    model.summary()

    history = model.fit(
        x_train, y_train,
        epochs=EPOCHS, batch_size=BATCH_SIZE, validation_split=0.1,
        callbacks=[keras.callbacks.EarlyStopping(
            patience=2, restore_best_weights=True)],
    )

    loss, acc = model.evaluate(x_test, y_test, verbose=0)
    print(f"\nTest : précision = {acc:.4f} | perte = {loss:.4f}")

    y_pred = np.argmax(model.predict(x_test, verbose=0), axis=1)
    report = classification_report(y_test, y_pred, target_names=CLASSES)
    print(report)
    (OUT_DIR / "rapport_classification.txt").write_text(
        f"Précision test : {acc:.4f}\n\n{report}", encoding="utf-8")
    save_curves(history)
    save_confusion(y_test, y_pred)

    model.save(str(MODEL_PATH))
    print(f"Modèle sauvegardé : {MODEL_PATH}")

    

if __name__ == "__main__":
    train()
    
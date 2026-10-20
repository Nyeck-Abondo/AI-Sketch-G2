import os
import numpy as np
from sklearn.model_selection import train_test_split
import tensorflow as tf

def load_and_process_data(data_dir="data/raw", objects=None, image_nbn=5000):
    """
    Charge, prepare et divise le dataset quickDraw
    """

    objects = ["apple", "crown", "diamond", "door", "hammer"]
    x_list = []
    y_list = []

    for label_index, category in enumerate(objects):
        filepath = os.path.join(data_dir, f"{category}.npy")

        if not os.path.exists(filepath):
            raise FileNotFoundError(f"Le fichier {filepath} est introuvable")

        #chargement partiel

        info = np.load(filepath)
        info = info[:image_nbn]

       # creation d'etiquettes
        label = np.full(shape=(info.shape[0],), fill_value=label_index)

        x_list.append(info)
        y_list.append(label)

    #CONCATENATION DES OBJETS
    X = np.concatenate(x_list, axis=0)
    y = np.concatenate(y_list, axis=0)

    #normalisation
    X = X.astype('float32') / 255.0
    X = X.reshape(-1, 28, 28, 1)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print(f"Dataset pret !")
    print(f"X_train : {X_train.shape}, y_train : {y_train.shape}")
    print(f"X_test  : {X_test.shape}, y_test  : {y_test.shape}")

    return (X_train, y_train), (X_test, y_test), objects

if __name__ == '__main__':
    Object = ["apple", "crown", "diamond", "door", "hammer"]
    (X_train, y_train), (X_test, y_test), class_names = load_and_process_data(data_dir="data/raw", objects=Object, image_nbn=5000)
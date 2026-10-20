import numpy as np

def qimage_to_tensor(qimage):
    """
    Convertit la QImage en un tenseur (1, 28, 28, 1) normalisé.
    Assure que le fond est NOIR (0.0) et les traits BLANCS (1.0).
    """
    width = qimage.width()
    height = qimage.height()

    ptr = qimage.bits()
    ptr.setsize(height * width)
    arr = np.array(ptr, dtype=np.uint8).reshape(height, width)

    # Si le fond de votre QImage est blanc (valeurs élevées ~255), on inverse l'image
    if np.mean(arr) > 127:
        arr = 255 - arr

    # Normalisation entre 0.0 et 1.0
    arr = arr.astype("float32") / 255.0

    return np.expand_dims(arr, axis=(0, -1))
import sys
import numpy as np
import tensorflow as tf
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QScrollArea

from styles import APP_STYLESHEET
from section import HeaderSection
from zonedessin import DrawingPanel
from reconnaissance import RecognitionPanel
from action import ActionButtons

# Emplacement du modèle et des classes
ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))
MODEL_PATH = ROOT / "models" / "sketch_classifier.keras"

from src.Trainning.config import CLASSES
from utils import qimage_to_tensor

# Dictionnaire de traduction optionnel pour l'affichage
EN_TO_FR = {
    "apple": "Pomme",
    "crown": "Couronne",
    "diamond": "Diamant",
    "door": "Porte",
    "airplane": "Avion",
    "cat": "Chat",
    "hammer": "Marteau",
}


class SketchRecognitionUI(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("SketchAI - Reconnaissance de dessin")
        self.resize(1000, 900)
        self.setMinimumSize(700, 650)
        self.setStyleSheet(APP_STYLESHEET)

        # chargement du modele
        self.model = None
        if MODEL_PATH.exists():
            try:
                self.model = tf.keras.models.load_model(str(MODEL_PATH))
                print("Modèle chargé avec succès.")
            except Exception as e:
                print(f"Erreur lors du chargement du modèle : {e}")
        
        self.build_ui()
        self.connect_actions()

    def build_ui(self):
        # Zone défilante pour les petites fenêtres
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.setCentralWidget(scroll)

        page = QWidget()
        scroll.setWidget(page)

        root = QVBoxLayout(page)
        root.setContentsMargins(24, 22, 24, 24)
        root.setSpacing(16)

        # En-tête
        self.header = HeaderSection()
        root.addWidget(self.header)

        # Zone de dessin et outils
        self.drawing_panel = DrawingPanel()
        root.addWidget(self.drawing_panel, 3)

        # Résultats de reconnaissance
        self.recognition_panel = RecognitionPanel()
        root.addWidget(self.recognition_panel, 2)

        # Boutons inférieurs
        self.action_buttons = ActionButtons()
        root.addWidget(self.action_buttons)

    def connect_actions(self):
        drawing = self.drawing_panel
        actions = self.action_buttons

        drawing.pen_button.clicked.connect(self.select_pen)
        drawing.eraser_button.clicked.connect(self.select_eraser)
        drawing.undo_button.clicked.connect(self.undo_drawing)

        actions.clear_button.clicked.connect(self.clear_drawing)
        actions.recognize_button.clicked.connect(self.recognize_drawing)

    def select_pen(self):
        self.drawing_panel.pen_button.setChecked(True)
        self.drawing_panel.eraser_button.setChecked(False)

        self.drawing_panel.canvas.set_tool("pen")

    def select_eraser(self):
        self.drawing_panel.eraser_button.setChecked(True)
        self.drawing_panel.pen_button.setChecked(False)

        self.drawing_panel.canvas.set_tool("eraser")

    def undo_drawing(self):
        canvas = self.drawing_panel.canvas

        canvas.undo()
        self.drawing_panel.update_drawing_count()

    def clear_drawing(self):
        canvas = self.drawing_panel.canvas
        panel = self.recognition_panel

        # Effacer le contenu du canevas
        canvas.clear()
        self.drawing_panel.update_drawing_count()

        # Réinitialiser le panneau IA
        panel.status_label.setText("✧   En attente d'un dessin...")

        self.header.ready_badge.setText("●  Prêt à dessiner")

        for card in panel.suggestion_cards:
            card.reset()
            card.hide()

    def recognize_drawing(self):
        canvas = self.drawing_panel.canvas
        panel = self.recognition_panel

        if not canvas.has_drawing():
            panel.status_label.setText("Dessine d'abord un objet dans la zone blanche.")
            return

        if self.model is None:
            panel.status_label.setText("Modèle introuvable. Veuillez exécuter train.py.")
            return

        # 1. Obtension du tenseur normailisé
        qimg = canvas.get_qimage_28x28()
        tensor = qimage_to_tensor(qimg)

        # 2. Exécuter la prédiction
        predictions = self.model.predict(tensor, verbose=0)[0]

        # 3. Récupérer les 3 meilleures propositions
        top3_indices = np.argsort(predictions)[::-1][:3]

        panel.status_label.setText("✧   Résultats de l'analyse :")
        self.header.ready_badge.setText("●  Dessin analysé")

        # 4. Mettre à jour les cartes SuggestionCard
        for rank, idx in enumerate(top3_indices):
            if rank < len(panel.suggestion_cards):
                card = panel.suggestion_cards[rank]
                
                class_en = CLASSES[idx]
                class_fr = EN_TO_FR.get(class_en, class_en.capitalize())
                prob_pct = predictions[idx] * 100

                card.set_result(class_fr, prob_pct)
                card.show()

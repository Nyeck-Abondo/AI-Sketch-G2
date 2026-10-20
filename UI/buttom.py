from PyQt6.QtWidgets import (
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QProgressBar
)


class SuggestionCard(QFrame):
    """Carte affichant une proposition de reconnaissance."""

    def __init__(self, rank, parent=None):
        super().__init__(parent)

        self.setObjectName("suggestionCard")

        self.setStyleSheet("""
            QFrame#suggestionCard {
                background-color: #FFFFFF;
                border: 1px solid #E5EAF0;
                border-radius: 10px;
            }
        """)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 10, 12, 10)
        layout.setSpacing(7)

        header = QHBoxLayout()

        self.rank_label = QLabel(f"#{rank}")
        self.rank_label.setStyleSheet("""
            color: #7D8B9B;
            font-weight: bold;
        """)

        self.object_label = QLabel("En attente")
        self.object_label.setStyleSheet("""
            color: #26364A;
            font-weight: 600;
        """)

        self.confidence_label = QLabel("--")
        self.confidence_label.setStyleSheet("""
            color: #526D87;
            font-weight: bold;
        """)

        header.addWidget(self.rank_label)
        header.addWidget(self.object_label, 1)
        header.addWidget(self.confidence_label)

        layout.addLayout(header)

        self.progress = QProgressBar()
        self.progress.setRange(0, 100)
        self.progress.setValue(0)
        self.progress.setTextVisible(False)
        self.progress.setFixedHeight(6)

        layout.addWidget(self.progress)

    def set_result(self, name, confidence):
        """Actualise la carte avec un résultat fourni par l'IA."""
        confidence = max(0, min(100, int(confidence)))

        self.object_label.setText(name)
        self.confidence_label.setText(f"{confidence}%")
        self.progress.setValue(confidence)

    def reset(self):
        """Réinitialise la carte."""
        self.object_label.setText("En attente")
        self.confidence_label.setText("--")
        self.progress.setValue(0)
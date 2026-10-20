from PyQt6.QtWidgets import (
    QLabel,
    QFrame,
    QVBoxLayout
)

from interface import SuggestionCard


class RecognitionPanel(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("panel")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 18, 20, 18)
        layout.setSpacing(14)

        title = QLabel("Reconnaissance IA")
        title.setObjectName("sectionTitle")

        description = QLabel(
            "L'objet reconnu et les propositions apparaîtront ici."
        )
        description.setObjectName("subtitle")
        description.setWordWrap(True)

        layout.addWidget(title)
        layout.addWidget(description)

        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet(
            "background-color: #E2E7ED; max-height: 1px;"
        )

        layout.addWidget(separator)

        self.status_label = QLabel(
            "✧   En attente d'un dessin..."
        )
        self.status_label.setObjectName("subtitle")
        self.status_label.setWordWrap(True)

        layout.addWidget(self.status_label)

        self.suggestion_cards = []

        for rank in range(1, 4):
            card = SuggestionCard(rank)
            card.hide()

            self.suggestion_cards.append(card)
            layout.addWidget(card)
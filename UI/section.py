from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QHBoxLayout
)


class HeaderSection(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)

        top = QHBoxLayout()

        title = QLabel("SketchAI")
        title.setObjectName("appTitle")

        self.ready_badge = QLabel("●  Prêt à dessiner")
        self.ready_badge.setObjectName("readyBadge")
        self.ready_badge.setAlignment(
            Qt.AlignmentFlag.AlignCenter
        )

        top.addWidget(title)
        top.addStretch()
        top.addWidget(self.ready_badge)

        layout.addLayout(top)

        subtitle = QLabel(
            "Dessine un objet, l'IA essaiera de le reconnaître."
        )
        subtitle.setObjectName("subtitle")
        subtitle.setWordWrap(True)

        layout.addWidget(subtitle)
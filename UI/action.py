from PyQt6.QtWidgets import (
    QWidget,
    QPushButton,
    QHBoxLayout
)


class ActionButtons(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(14)

        self.recognize_button = QPushButton("Reconnaître")
        self.recognize_button.setObjectName("primaryButton")
        self.recognize_button.setMinimumHeight(76)

        self.clear_button = QPushButton("Effacer")
        self.clear_button.setObjectName("clearButton")
        self.clear_button.setMinimumHeight(76)

        layout.addWidget(self.recognize_button, 1)
        layout.addWidget(self.clear_button, 1)
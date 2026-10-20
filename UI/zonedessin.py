from PyQt6.QtWidgets import (
    QLabel,
    QPushButton,
    QFrame,
    QVBoxLayout,
    QHBoxLayout,
    QSizePolicy
)

from drawing import DrawingCanvas


class DrawingPanel(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setObjectName("panel")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 18, 18, 18)
        layout.setSpacing(13)

        header = QHBoxLayout()

        title = QLabel("Zone de dessin")
        title.setObjectName("sectionTitle")

        self.drawing_count = QLabel("0 dessin")
        self.drawing_count.setObjectName("muted")

        header.addWidget(title)
        header.addStretch()
        header.addWidget(self.drawing_count)

        layout.addLayout(header)

        self.canvas = DrawingCanvas()
        layout.addWidget(self.canvas, 1)

        toolbar = QHBoxLayout()
        toolbar.setSpacing(10)

        self.pen_button = QPushButton("✏️  Crayon")
        self.pen_button.setCheckable(True)
        self.pen_button.setChecked(True)

        self.undo_button = QPushButton("↶  Annuler")

        self.eraser_button = QPushButton("Gomme")
        self.eraser_button.setCheckable(True)

        for button in (
            self.pen_button,
            self.undo_button,
            self.eraser_button
        ):
            button.setMinimumHeight(52)
            button.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Fixed
            )

        toolbar.addWidget(self.pen_button)
        toolbar.addWidget(self.undo_button)
        toolbar.addWidget(self.eraser_button)

        layout.addLayout(toolbar)

    def update_drawing_count(self):
        count = len(self.canvas.strokes)

        if count == 1:
            self.drawing_count.setText("1 trait")
        else:
            self.drawing_count.setText(f"{count} traits")
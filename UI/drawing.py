from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPainter, QPen, QColor
from PyQt6.QtWidgets import QWidget, QSizePolicy


class DrawingCanvas(QWidget):
    """Zone de dessin à la souris."""

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setMinimumSize(300, 240)
        self.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)

        # stocker les traits dessinnees et en cours
        self.strokes = []
        self.current_stroke = None

        #configuration du crayon
        self.tool = "pen"
        self.pen_color = QColor("#26364A")
        self.pen_width = 4
        self.eraser_width = 24

        self.setCursor(Qt.CursorShape.CrossCursor)    # curseur en forme de croix lors du survol sur la zone de dessib
        self.setStyleSheet("""
            background-color: #FFFFFF;
            border: 1px solid #E2E7ED;
            border-radius: 14px;
        """)

    def set_tool(self, tool):
        self.tool = tool

        if tool == "pen":
            self.setCursor(Qt.CursorShape.CrossCursor)
        else:
            self.setCursor(Qt.CursorShape.PointingHandCursor)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.current_stroke = {
                "points": [event.position()],
                "color": (
                    QColor("#FFFFFF")
                    if self.tool == "eraser"
                    else QColor(self.pen_color)
                ),
                "width": (self.eraser_width if self.tool == "eraser" else self.pen_width  )
            }
            self.update()

    def mouseMoveEvent(self, event):
        if self.current_stroke is not None:
            self.current_stroke["points"].append(event.position())
            self.update()

    def mouseReleaseEvent(self, event):
        if (
            event.button() == Qt.MouseButton.LeftButton
            and self.current_stroke is not None
        ):
            self.strokes.append(self.current_stroke)
            self.current_stroke = None
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        painter.fillRect(self.rect(), QColor("#FFFFFF"))

        strokes = list(self.strokes)

        if self.current_stroke is not None:
            strokes.append(self.current_stroke)

        for stroke in strokes:
            points = stroke["points"]

            if not points:
                continue

            pen = QPen(
                stroke["color"],
                stroke["width"],
                Qt.PenStyle.SolidLine,
                Qt.PenCapStyle.RoundCap,
                Qt.PenJoinStyle.RoundJoin
            )

            painter.setPen(pen)

            if len(points) == 1:
                painter.drawPoint(points[0])
            else:
                for index in range(1, len(points)):
                    painter.drawLine(
                        points[index - 1],
                        points[index]
                    )

        painter.end()

    def undo(self):
        """Supprime le dernier trait."""
        if self.current_stroke is not None:
            self.current_stroke = None
        elif self.strokes:
            self.strokes.pop()

        self.update()

    def clear(self):
        """Efface entièrement le dessin."""
        self.strokes.clear()
        self.current_stroke = None
        self.update()

    def has_drawing(self):
        """Indique si le canevas contient un dessin."""
        return bool(self.strokes or self.current_stroke)
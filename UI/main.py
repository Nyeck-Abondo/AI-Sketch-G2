import sys

from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QFont

from main_window import SketchRecognitionUI


def main():
    app = QApplication(sys.argv)
    app.setFont(QFont("Segoe UI", 11))

    window = SketchRecognitionUI()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
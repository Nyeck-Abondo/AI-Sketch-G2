APP_STYLESHEET = """
QMainWindow {
    background-color: #F0F3F8;
}

QWidget {
    color: #26364A;
    font-family: "Segoe UI";
    font-size: 11pt;
}

QLabel#appTitle {
    font-size: 30px;
    font-weight: 700;
    color: #203249;
}

QLabel#subtitle {
    color: #687789;
    font-size: 17px;
}

QLabel#sectionTitle {
    font-size: 19px;
    font-weight: 650;
    color: #29394D;
}

QLabel#muted {
    color: #8995A5;
}

QFrame#panel {
    background-color: #FFFFFF;
    border: 1px solid #DCE3EB;
    border-radius: 17px;
}

QLabel#readyBadge {
    background-color: #D9F3E4;
    color: #16804A;
    border-radius: 18px;
    padding: 8px 15px;
    font-weight: 600;
}

QPushButton {
    background-color: #E7EDF5;
    color: #344B65;
    border: none;
    border-radius: 12px;
    padding: 12px 16px;
    font-size: 15px;
}

QPushButton:hover {
    background-color: #DCE5F0;
}

QPushButton:checked {
    background-color: #D4E3F6;
    color: #285C9D;
    border: 1px solid #B5CBE8;
}

QPushButton#primaryButton {
    background-color: #526F89;
    color: white;
    border: none;
    border-radius: 12px;
    padding: 17px 15px;
    font-size: 19px;
    font-weight: 650;
}

QPushButton#primaryButton:hover {
    background-color: #405D77;
}

QPushButton#clearButton {
    background-color: #E1E8F1;
    color: #344B65;
    border-radius: 12px;
    padding: 17px 15px;
    font-size: 19px;
    font-weight: 650;
}

QPushButton#clearButton:hover {
    background-color: #D5DFEB;
}

QProgressBar {
    background-color: #EDF1F5;
    border: none;
    border-radius: 3px;
}

QProgressBar::chunk {
    background-color: #6D94C3;
    border-radius: 3px;
}

QScrollArea {
    border: none;
    background: transparent;
}
"""
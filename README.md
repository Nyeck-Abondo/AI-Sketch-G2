# 🎨 SketchAI - Reconnaissance de Croquis par IA

**SketchAI (AI-Sketch-G2)** est une application desktop interactive développée en **Python** et **PyQt6**, propulsée par un réseau de neurones convolutif (**CNN TensorFlow/Keras**). L'application permet de dessiner à la main sur un canevas vectoriel et d'obtenir en temps réel la classification de l'objet parmi 7 catégories, avec une précision globale supérieure à **95 %**.

---

## 🌟 Fonctionnalités

* 🖌️ **Zone de Dessin Vectorielle** : Outils Crayon, Gomme, Annuler (*Undo*) et Effacer (*Clear*).
* 🧠 **Classification par IA** : Modèle CNN entraîné sur le jeu de données officiel Google *Quick, Draw!* (140 000 images au total).
* 📊 **Affichage Top-3** : Cartes de propositions dynamiques affichant le podium des prédictions avec barres de progression et pourcentages de confiance.
* ⚡ **Prétraitement Intelligent** : Conversion vectorielle $28 \times 28$ pixels et inversion automatique du contraste (fond noir / traits blancs) pour s'aligner parfaitement sur le format du modèle.
* 🎨 **Interface Moderne** : UI ergonomique et responsive stylisée avec PyQt6 (QSS).

---

## 🏷️ Classes Reconnues

L'application est entraînée pour reconnaître 7 classes d'objets :

1. 🍎 **Pomme** (`apple`)
2. 👑 **Couronne** (`crown`)
3. 💎 **Diamant** (`diamond`)
4. 🚪 **Porte** (`door`)
5. ✈️ **Avion** (`airplane`)
6. 🐱 **Chat** (`cat`)
7. 🔨 **Marteau** (`hammer`)

---

## 🛠️ Pile Technique & Dépendances

* **Langage** : Python 3.12+
* **Deep Learning** : TensorFlow 2.17.0, Keras
* **Interface Graphique** : PyQt6
* **Traitement d'Images & Matrice** : NumPy 1.26.4, OpenCV (headless)
* **Évaluation & Visualisation** : Scikit-Learn, Matplotlib

---

## 📂 Arborescence du Projet

```text
AI-Sketch-G2/
├── data/
│   └── raw/                          # Fichiers binaires Quick, Draw! (.npy)
├── models/
│   └── sketch_classifier.keras       # Modèle CNN entraîné sauvegardé
├── output/
│   ├── courbes_entrainement.png      # Graphique des époques (Loss/Accuracy)
│   ├── matrice_confusion.png         # Matrice de confusion scikit-learn
│   └── rapport_classification.txt    # Rapport détaillé de précision/rappel
├── src/
│   ├── Trainning/
│   │   ├── config.py                 # Hyperparamètres et liste des classes
│   │   ├── dataset.py                # Chargement optimisé mmap_mode
│   │   └── train.py                  # Script d'entraînement avec EarlyStopping
│   └── UI/
│       ├── action.py                 # Boutons "Reconnaître" et "Effacer"
│       ├── buttom.py / interface.py  # Cartes de suggestion (SuggestionCard)
│       ├── drawing.py                # Canevas DrawingCanvas & export QImage 28x28
│       ├── main_window.py            # Contrôleur principal et intégration IA
│       ├── reconnaissance.py         # Panneau des résultats de reconnaissance
│       ├── section.py                # En-tête de l'application
│       ├── styles.py                 # Feuille de style QSS globale
│       ├── utils.py                  # Normalisation & inversion de contraste
│       └── zonedessin.py             # Panneau avec barre d'outils (Crayon/Gomme)
├── .gitignore                        # Configuration d'exclusion Git
├── check_versions.py                 # Script de vérification des bibliothèques
├── main.py                           # Point d'entrée de l'application
├── Rapport_Technique_AI_Sketch.docx # Rapport complet Word
└── requirements.txt                  # Dépendances pip
```

---

## 🚀 Installation & Configuration

### 1. Cloner le Dépôt Git
```bash
git clone https://github.com/votre-compte/AI-Sketch-G2.git
cd AI-Sketch-G2
```

### 2. Créer et Activer l'Environnement Virtuel

* **Sous Windows (PowerShell) :**
  ```powershell
  python -m venv venv_tf217
  .\venv_tf217\Scripts\Activate.ps1
  ```
* **Sous Linux / macOS :**
  ```bash
  python3 -m venv venv_tf217
  source venv_tf217/bin/activate
  ```

### 3. Installer les Dépendances
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## 📥 Préparation des Données & Entraînement

### 1. Téléchargement des Données Quick, Draw!
Placez les 7 fichiers binaire `.npy` correspondants dans le dossier `data/raw/` :
* `apple.npy`
* `crown.npy`
* `diamond.npy`
* `door.npy`
* `full_numpy_bitmap_airplane.npy`
* `full_numpy_bitmap_cat.npy`
* `hammer.npy`

### 2. Lancer l'Entraînement du Modèle
Pour exécuter le pipeline d'apprentissage ($20\ 000$ images par classe, soit $140\ 000$ échantillons) :

```bash
python src/Trainning/train.py
```

À la fin de l'entraînement :
* Le modèle sera sauvegardé dans `models/sketch_classifier.keras`.
* Les métriques et courbes seront générées dans le dossier `output/`.

---

## 🎮 Lancement de l'Application

Exécutez le fichier `main.py` à la racine du projet :

```bash
python main.py
```

### Guide d'Utilisation :
1. **Dessiner** : Utilisez le crayon pour tracer un objet au centre du canevas blanc.
2. **Ajuster** : Utilisez la gomme ou le bouton **Annuler** pour corriger un trait.
3. **Reconnaître** : Cliquez sur le bouton bleu **Reconnaître** pour lancer la prédiction IA.
4. **Réinitialiser** : Cliquez sur **Effacer** pour réinitialiser le canevas et tester un nouveau dessin.

---

## 💡 Conseils pour de Meilleurs Résultats de Reconnaissance

* **Tête de marteau** : Dessinez une tête rectangulaire fine et allongée (en « T ») plutôt qu'une grande boîte fermée pour éviter toute confusion avec une **Porte**.
* **Avion** : Tracez un fuselage central net avec deux ailes latérales distinctes.
* **Traits lisibles** : Évitez les traits trop fins ou trop collés aux bords de la zone de dessin.

---

## 📜 Licence

Ce projet est réalisé dans le cadre académique du cours **ANI-2083**. Librement réutilisable à des fins pédagogiques.
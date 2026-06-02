# Notes_1_juin.md

# 1 juin 2026 – Adaptation du pipeline de Lorène Jeantet aux tortues

## Objectif

Comprendre le pipeline de classification acoustique et réussir à générer des spectrogrammes de tortues marines à partir de mes propres annotations.

---

# Étape 1 – Création du Dataset_Example

Structure créée :

Dataset_Example/

├── Audio/

├── Annotations/

├── DataFiles/

└── Datasets/

Fichier audio utilisé :

IMB_05_08h10_08h20.wav

Scripts créés :

* create_turtle_dataset_example.py
* create_svl_from_mastertable.py

Résultat :

* création automatique des dossiers ;
* copie du fichier wav ;
* création des fichiers train.txt, val.txt et test.txt ;
* création du fichier .svl à partir de la master table.

---

# Étape 2 – Création du fichier .svl

Source :

master_table.xlsx

Feuille :

selections updated

Segment testé :

IMB_05

08h10_08h20

Résultat :

IMB_05_08h10_08h20.svl

Nombre d’annotations :

49 lignes dans la master table

48 pulses finalement extraits par le pipeline

---

# Étape 3 – Ouverture du notebook de Lorène

Notebook utilisé :

Notebook de création des datasets.

---

# Étape 4 – Exécution des imports

```python
import sys
from pathlib import Path

for _candidate in [Path().resolve().parent / "src", Path().resolve() / "src"]:
    if _candidate.exists() and str(_candidate) not in sys.path:
        sys.path.insert(0, str(_candidate))
        break

from preprocess import Preprocessing
from settings import Config
from config_species import get_settings

import matplotlib.pyplot as plt
import numpy as np
import pickle
```

---

# Étape 5 – Chargement de la configuration

```python
selected_species = "gibbon"

settings = get_settings(selected_species)

config = Config(settings)

config.data.species_folder = r"C:\Users\cheva\Desktop\github_projects\acoustic_classifier_seaturtles\juliana_tests\Dataset_Example"
```

Remarque :

Même si la configuration "gibbon" est utilisée, le dossier de travail est remplacé par le Dataset_Example des tortues.

---

# Étape 6 – Création de l'objet preprocess

```python
preprocess = Preprocessing(
    **config.preprocessing.dict(),
    species_folder=config.data.species_folder,
    positive_class=config.data.positive_class,
    negative_class=config.data.negative_class,
)
```

---

# Étape 7 – Génération du dataset

IMPORTANT :

La version avec augmentation ne fonctionne pas.

```python
data_augmentation=True
```

provoque une erreur car une seule classe ("pulse") est présente.

La commande qui fonctionne est :

```python
X_calls, Y_calls = preprocess.create_dataset(
    "train",
    data_augmentation=False
)

print("OK")
print(len(X_calls))
print(len(Y_calls))
```

Résultat :

```text
Processing: IMB_05_08h10_08h20

Found file IMB_05_08h10_08h20

Nb of labels
(array(['pulse']), array([48]))

OK

48

48
```

---

# Étape 8 – Vérification du dataset

```python
print(X_calls.shape)
```

Résultat :

```text
(48, 128, 76)
```

Interprétation :

* 48 spectrogrammes
* 128 bandes Mel
* 76 pas temporels

---

# Étape 9 – Affichage du premier spectrogramme

```python
plt.imshow(
    X_calls[0],
    origin="lower"
)

plt.show()
```

---

# Étape 10 – Création de la planche envoyée à Lorène

```python
fig, axes = plt.subplots(
    4,
    4,
    figsize=(12,12)
)

for i, ax in enumerate(axes.flatten()):
    ax.imshow(
        X_calls[i],
        origin="lower",
        aspect="auto"
    )
    ax.set_title(f"{i+1}")
    ax.axis("off")

plt.tight_layout()

plt.show()
```

---

# Problèmes rencontrés

* Difficulté à comprendre l'organisation du dépôt GitHub.
* Difficulté à comprendre le fonctionnement des notebooks Jupyter.
* Plusieurs redémarrages de VS Code.
* Problèmes de kernel Python.
* Erreur liée à resampy/librosa.
* Apprentissage du format .svl de Sonic Visualiser.
* Première utilisation du pipeline de Lorène.

---

# Retour de Lorène

"Merci pour les spectrogrammes, ils ne sont pas très jolies ;D

on va devoir regarder ça de plus près."

Rendez-vous avancé :

2 juin 2026

15h

---

# Questions pour demain

1. Les spectrogrammes obtenus correspondent-ils à ce qui est attendu ?

2. Une fenêtre de 4 secondes est-elle adaptée à des pulses d'environ 0,2 seconde ?

3. Le fait qu'il s'agisse de Mel-spectrogrammes influence-t-il fortement leur apparence ?

4. Quels paramètres doivent être adaptés aux tortues ?

* segment_duration
* n_fft
* hop_length
* n_mels
* f_min
* f_max

5. Comment adapter les paramètres sans casser le reste du pipeline ?



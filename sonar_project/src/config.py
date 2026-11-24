# -*- coding: utf-8 -*-
"""Configuration centrale : chemins (indépendants du dossier courant), graine, résultats du papier."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
PROCESSED = DATA / "processed"
LOGS = ROOT / "results" / "logs"
FIGURES = ROOT / "results" / "figures"

SEED = 42
N_FOLDS = 13

# Gorman & Sejnowski (1988) - accuracy moyenne, écart-type (%)
PAPIER_EXP1 = {
    "Perceptron (0 hidden)": (77.1, 8.3), "MLP (2 hidden)": (81.9, 6.2),
    "MLP (3 hidden)": (82.0, 7.3), "MLP (6 hidden)": (83.5, 5.6),
    "MLP (12 hidden)": (84.7, 5.7), "MLP (24 hidden)": (84.5, 5.7),
}
PAPIER_EXP2 = {0: (73.1, 4.8), 2: (85.7, 6.3), 3: (87.6, 3.0),
               6: (89.3, 2.4), 12: (90.4, 1.8), 24: (89.2, 1.4)}

for _d in (PROCESSED, LOGS, FIGURES):
    _d.mkdir(parents=True, exist_ok=True)

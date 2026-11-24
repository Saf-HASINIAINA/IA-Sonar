#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Expérience 1 - Validation croisée stratifiée K=13 (indépendant de l'angle)."""
import time
import pandas as pd
from .config import LOGS, N_FOLDS, PAPIER_EXP1
from .evaluation import cv_scores
from .model import get_models_exp1
from .utils import load_xy, compare_papier


def run():
    print("=" * 60 + "\nEXPÉRIENCE 1 - VALIDATION CROISÉE K=13\n" + "=" * 60)
    X, y = load_xy()
    rows = {}
    for nom, modele in get_models_exp1().items():
        t = time.time()
        s = cv_scores(modele, X, y)
        rows[nom] = [s.mean(), s.std(), time.time() - t, *s]
        msg = f"{nom:24} {s.mean():.4f} (+/- {s.std():.4f})"
        if nom in PAPIER_EXP1:
            msg += "  " + compare_papier(s.mean() * 100, PAPIER_EXP1[nom])
        print(msg)
    df = pd.DataFrame(rows).T
    df.columns = ["moyenne", "ecart_type", "temps"] + [f"fold_{i+1}" for i in range(N_FOLDS)]
    df.to_csv(LOGS / "experience1_complete.csv")
    with open(LOGS / "experience1_resume.txt", "w", encoding="utf-8") as f:
        f.write("EXPÉRIENCE 1 - RÉSULTATS\n\n")
        for nom, r in df.iterrows():
            f.write(f"{nom:25} -> {r['moyenne']:.4f} (+/- {r['ecart_type']:.4f})\n")
    return df


if __name__ == "__main__":
    run()

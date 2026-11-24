#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Expérience 2 - Split angle-dépendant, 10 runs (graines différentes) par architecture."""
import time
import numpy as np
import pandas as pd
from .config import LOGS, PAPIER_EXP2
from .experience2_parsing import create_experiment2_split
from .model import make_mlp, make_perceptron
from .utils import load_xy, compare_papier

ARCHS, N_RUNS = [0, 2, 3, 6, 12, 24], 10


def run():
    print("=" * 60 + "\nEXPÉRIENCE 2 - SPLIT ANGLE-DÉPENDANT\n" + "=" * 60)
    X, y = load_xy()
    tr, te = create_experiment2_split()
    rows = {}
    for u in ARCHS:
        scores, t = [], time.time()
        for r in range(N_RUNS):
            m = make_perceptron(r) if u == 0 else make_mlp(u, r)
            scores.append(m.fit(X[tr], y[tr]).score(X[te], y[te]))
        rows[u] = {"moyenne": np.mean(scores), "ecart_type": np.std(scores),
                   "temps_moyen": (time.time() - t) / N_RUNS,
                   **{f"run_{i+1}": s for i, s in enumerate(scores)}}
        print(f"Units {u:2d}: {np.mean(scores):.4f} (+/- {np.std(scores):.4f})  "
              + compare_papier(np.mean(scores) * 100, PAPIER_EXP2[u]))
    df = pd.DataFrame(rows).T
    df.to_csv(LOGS / "experience2_complete.csv")
    with open(LOGS / "experience2_resume.txt", "w", encoding="utf-8") as f:
        f.write("EXPÉRIENCE 2 - RÉSULTATS\n\n")
        for u, r in rows.items():
            f.write(f"Units {u:2d}: {r['moyenne']:.4f} (+/- {r['ecart_type']:.4f})\n")
    return df


if __name__ == "__main__":
    run()

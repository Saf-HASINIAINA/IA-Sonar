#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Split de l'expérience 2 (angle-dépendant, 104 train / 104 test).

Roches : les 97 vecteurs de sonar.rocks.txt sont ASSOCIÉS aux lignes du CSV par
égalité des valeurs (et non par position supposée). Les marqueurs '*' = train.
Mines : sonar.mines n'est pas fourni -> 49 mines tirées au hasard (graine fixe) en train,
les 62 autres en test (approximation documentée).
"""
import re
import numpy as np
from .config import DATA, PROCESSED, SEED
from .utils import load_xy

N_TRAIN = 104


def parse_rock_file():
    text = (DATA / "sonar.rocks.txt").read_text()
    X, y = load_xy()
    train, test = [], []
    for m in re.finditer(r"(\*?)CR\d+:\s*\{([^}]*)\}", text):
        vec = np.array(m.group(2).split(), dtype=float)
        d = np.abs(X - vec).sum(axis=1)
        d[y == 1] = np.inf  # roches seulement
        idx = int(d.argmin())
        if d[idx] > 1e-3:
            raise ValueError(f"Aucune correspondance dans le CSV pour un vecteur de roche (d={d[idx]:.4f})")
        (train if m.group(1) else test).append(idx)
    if len(set(train + test)) != 97:
        raise ValueError("Correspondance roches/CSV non bijective")
    return sorted(train), sorted(test)


def create_experiment2_split(save=True):
    _, y = load_xy()
    mine_idx = np.where(y == 1)[0]
    rock_train, rock_test = parse_rock_file()
    n_mine_train = N_TRAIN - len(rock_train)
    # Tirage aléatoire (graine fixe) : les mines du CSV sont ordonnées par cible/angle,
    # prendre les premières créerait un fort décalage de distribution train/test.
    perm = np.random.RandomState(SEED).permutation(mine_idx)
    train = sorted(list(perm[:n_mine_train]) + rock_train)
    test = sorted(list(perm[n_mine_train:]) + rock_test)
    assert len(train) == N_TRAIN and len(test) == 208 - N_TRAIN
    assert not set(train) & set(test)
    print(f"Split: train={len(train)} ({len(rock_train)} roches), test={len(test)} ({len(rock_test)} roches)")
    if save:
        np.save(PROCESSED / "exp2_train_indices.npy", train)
        np.save(PROCESSED / "exp2_test_indices.npy", test)
    return train, test


if __name__ == "__main__":
    create_experiment2_split()

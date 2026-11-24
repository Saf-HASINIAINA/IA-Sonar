# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from .config import DATA


def load_xy():
    """Données brutes (non normalisées) : X (208,60), y (0=R, 1=M)."""
    df = pd.read_csv(DATA / "sonar.all-data.csv", header=None)
    return df.iloc[:, :60].values.astype(float), (df.iloc[:, 60] == "M").astype(int).values


def compare_papier(moy_pct, papier):
    return f"vs Papier: {papier[0]:.1f}% (+/- {papier[1]:.1f}) [Diff: {moy_pct - papier[0]:+.2f}%]"

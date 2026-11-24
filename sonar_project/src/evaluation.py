# -*- coding: utf-8 -*-
import numpy as np
from sklearn.model_selection import StratifiedKFold, cross_val_score
from .config import N_FOLDS, SEED


def cv_scores(model, X, y):
    cv = StratifiedKFold(n_splits=N_FOLDS, shuffle=True, random_state=SEED)
    return cross_val_score(model, X, y, cv=cv, scoring="accuracy", n_jobs=-1)


def summarize(scores):
    return float(np.mean(scores)), float(np.std(scores))

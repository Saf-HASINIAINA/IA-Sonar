# -*- coding: utf-8 -*-
"""Fabrique de modèles. Le scaler est DANS le pipeline : il est donc ajusté
uniquement sur les données d'entraînement de chaque fold (pas de fuite de données)."""
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from .config import SEED


def make_mlp(units, seed=SEED):
    # Ancien réglage learning_rate_init=2.0 : divergence -> prédiction de la classe majoritaire.
    return make_pipeline(StandardScaler(), MLPClassifier(
        hidden_layer_sizes=(units,), activation="logistic", solver="adam",
        learning_rate_init=0.01, alpha=1e-2, max_iter=2000, random_state=seed))


def make_perceptron(seed=SEED):
    return make_pipeline(StandardScaler(), Perceptron(max_iter=1000, tol=1e-3, random_state=seed))


def get_models_exp1(seed=SEED):
    models = {"Perceptron (0 hidden)": make_perceptron(seed)}
    for k in (1, 3, 5):
        models[f"KNN (k={k})"] = make_pipeline(StandardScaler(), KNeighborsClassifier(n_neighbors=k))
    for u in (2, 3, 6, 12, 24):
        models[f"MLP ({u} hidden)"] = make_mlp(u, seed)
    models["SVM (RBF)"] = make_pipeline(StandardScaler(), SVC(C=10, gamma="scale"))
    models["Random Forest"] = RandomForestClassifier(n_estimators=300, random_state=seed)
    return models

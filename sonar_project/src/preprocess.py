#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
preprocess.py
Prétraitement des données Sonar
Auteur: Personne 1
"""

import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
import joblib
import os
from .config import PROCESSED

def preprocess_data(data, save=True):
    """
    Normalise les features et encode les labels
    
    Args:
        data: DataFrame avec les données (doit avoir une colonne 'label')
        save: booléen pour sauvegarder ou non
    
    Returns:
        X_scaled: features normalisées
        y_encoded: labels encodés (0 pour R, 1 pour M)
        scaler: le scaler utilisé
        encoder: l'encoder utilisé
    """
    print("\n🔧 Prétraitement des données...")
    
    # Séparer features et labels
    X = data.drop('label', axis=1).values
    y = data['label'].values
    
    # Encoder les labels (R=0, M=1)
    encoder = LabelEncoder()
    y_encoded = encoder.fit_transform(y)
    print(f"   Encodage: {dict(zip(encoder.classes_, encoder.transform(encoder.classes_)))}")
    print(f"   Distribution: 0={sum(y_encoded==0)}, 1={sum(y_encoded==1)}")
    
    # Normaliser les features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    print(f"   Normalisation: moyenne ~ {X_scaled.mean():.3f}, écart-type ~ {X_scaled.std():.3f}")
    
    # Sauvegarder si demandé
    if save:
        PROCESSED.mkdir(parents=True, exist_ok=True)
        np.save(PROCESSED / 'X_scaled.npy', X_scaled)
        np.save(PROCESSED / 'y_encoded.npy', y_encoded)
        joblib.dump(scaler, PROCESSED / 'scaler.pkl')
        joblib.dump(encoder, PROCESSED / 'label_encoder.pkl')
        print("✅ Données sauvegardées dans data/processed/")
    
    return X_scaled, y_encoded, scaler, encoder

def load_processed_data():
    """
    Charge les données déjà prétraitées
    
    Returns:
        X: features normalisées
        y: labels encodés
    """
    X_path = PROCESSED / 'X_scaled.npy'
    y_path = PROCESSED / 'y_encoded.npy'
    
    if os.path.exists(X_path) and os.path.exists(y_path):
        X = np.load(X_path)
        y = np.load(y_path)
        print(f"✅ Données chargées: X={X.shape}, y={y.shape}")
        return X, y
    else:
        print("⚠️ Données non trouvées dans data/processed/")
        return None, None

if __name__ == "__main__":
    # Test du module
    from load_data import load_sonar_data
    data = load_sonar_data()
    X, y, scaler, encoder = preprocess_data(data)
    print(f"\n✅ Test réussi! X: {X.shape}, y: {y.shape}")
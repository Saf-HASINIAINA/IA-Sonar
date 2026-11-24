#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
load_data.py
Chargement des données Sonar
Auteur: Personne 1
"""

import pandas as pd
from .config import DATA

def load_sonar_data():
    """
    Charge le fichier sonar.all-data
    
    Returns:
        DataFrame avec 60 features + 1 colonne 'label'
    """
    filepath = DATA / 'sonar.all-data.csv'
    print(f"Chargement de {filepath}...")
    
    # Charger sans en-tête
    data = pd.read_csv(filepath, header=None)
    
    # Nommer les colonnes
    feature_cols = [f'freq_{i+1}' for i in range(60)]
    data.columns = feature_cols + ['label']
    
    print(f"✅ Données chargées: {data.shape[0]} échantillons, {data.shape[1]-1} features")
    print(f"   Classes: {data['label'].value_counts().to_dict()}")
    
    return data

def load_mine_file():
    """Charge le fichier sonar.mines pour l'expérience 2"""
    print("Fonction à compléter par Personne 4")
    pass

def load_rock_file():
    """Charge le fichier sonar.rocks pour l'expérience 2"""
    print("Fonction à compléter par Personne 4")
    pass

if __name__ == "__main__":  # python -m src.load_data
    # Test
    data = load_sonar_data()
    print("\nAperçu des données:")
    print(data.head())
    print(f"\nTypes de données:\n{data.dtypes}")
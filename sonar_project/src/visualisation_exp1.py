#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
visualisation_exp1.py
Visualisation des résultats de l'expérience 1
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Charger les résultats
df = pd.read_csv('results/logs/experience1_complete.csv', index_col=0)

# 1. Boxplot comparatif
plt.figure(figsize=(14, 6))
data_to_plot = [df.loc[nom, [f'fold_{i+1}' for i in range(13)]].values 
                for nom in df.index]
plt.boxplot(data_to_plot, tick_labels=df.index)
plt.title('Comparaison des performances (Expérience 1)', fontsize=14)
plt.ylabel('Accuracy')
plt.xticks(rotation=45, ha='right')
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.savefig('results/figures/boxplot_exp1.png')
plt.close()

# 2. Bar chart avec barres d'erreur
plt.figure(figsize=(12, 6))
x = np.arange(len(df.index))
plt.bar(x, df['moyenne'], yerr=df['ecart_type'], capsize=5, alpha=0.7)
plt.xticks(x, df.index, rotation=45, ha='right')
plt.ylabel('Accuracy')
plt.title('Performances des modèles avec écart-type')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('results/figures/barres_exp1.png')
plt.close()

# 3. Comparaison avec le papier
papier = {
    'Perceptron (0 hidden)': 77.1,
    'MLP (2 hidden)': 81.9,
    'MLP (3 hidden)': 82.0,
    'MLP (6 hidden)': 83.5,
    'MLP (12 hidden)': 84.7,
    'MLP (24 hidden)': 84.5
}

modeles_communs = [m for m in papier.keys() if m in df.index]
nos_valeurs = [df.loc[m, 'moyenne']*100 for m in modeles_communs]
papier_valeurs = [papier[m] for m in modeles_communs]

plt.figure(figsize=(10, 6))
x = np.arange(len(modeles_communs))
width = 0.35
plt.bar(x - width/2, nos_valeurs, width, label='Nos résultats', alpha=0.7)
plt.bar(x + width/2, papier_valeurs, width, label='Papier original', alpha=0.7)
plt.xlabel('Modèles')
plt.ylabel('Accuracy (%)')
plt.title('Comparaison avec les résultats du papier')
plt.xticks(x, modeles_communs, rotation=45, ha='right')
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('results/figures/comparaison_papier.png')
plt.close()

print("✅ Graphiques sauvegardés dans results/figures/")

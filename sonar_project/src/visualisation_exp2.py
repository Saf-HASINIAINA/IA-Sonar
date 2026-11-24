#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
visualisation_exp2.py
Visualisation des résultats de l'expérience 2
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Charger les résultats
df = pd.read_csv('results/logs/experience2_complete.csv', index_col=0)

print("="*60)
print("VISUALISATION EXPÉRIENCE 2")
print("="*60)
print(df[['moyenne', 'ecart_type', 'temps_moyen']])

# 1. Bar chart avec barres d'erreur
plt.figure(figsize=(10, 6))
x = np.arange(len(df.index))
plt.bar(x, df['moyenne'], yerr=df['ecart_type'], capsize=5, alpha=0.7)
plt.xticks(x, [f'{int(u)} units' for u in df.index])
plt.ylabel('Accuracy')
plt.title('Expérience 2 - Performance par architecture')
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('results/figures/barres_exp2.png')
plt.close()

# 2. Comparaison avec le papier
papier = {0: 73.1, 2: 85.7, 3: 87.6, 6: 89.3, 12: 90.4, 24: 89.2}
units = [int(u) for u in df.index]
nos_valeurs = df['moyenne'].values * 100
papier_valeurs = [papier[u] for u in units]

plt.figure(figsize=(10, 6))
x = np.arange(len(units))
width = 0.35
plt.bar(x - width/2, nos_valeurs, width, label='Nos résultats', alpha=0.7)
plt.bar(x + width/2, papier_valeurs, width, label='Papier original', alpha=0.7)
plt.xlabel('Hidden Units')
plt.ylabel('Accuracy (%)')
plt.title('Expérience 2 - Comparaison avec le papier')
plt.xticks(x, units)
plt.legend()
plt.grid(True, alpha=0.3, axis='y')
plt.tight_layout()
plt.savefig('results/figures/comparaison_exp2.png')
plt.close()

print("✅ Graphiques sauvegardés dans results/figures/")
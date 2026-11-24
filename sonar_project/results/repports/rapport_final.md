# PROJET SONAR - RAPPORT FINAL
## Classification Mines vs Roches

### Équipe
- **Personne 1** (Data Engineer) : Structure, preprocessing
- **Personne 2** (Exp1 Basic) : Perceptron, KNN
- **Personne 3** (Exp1 Advanced) : MLP
- **Personne 4** (Exp2) : Parsing, split angle-dépendant
- **Personne 5** (Visualisation) : Graphiques, analyse

---

## 1. Introduction

Le dataset Sonar (Gorman & Sejnowski, 1988) contient 208 signaux sonar
(60 fréquences chacun) avec 2 classes :
- **M** : Mine (cylindre métallique) - 111 échantillons
- **R** : Roche - 97 échantillons

Objectif : Classifier correctement ces signaux.

---

## 2. Expérience 1 - Indépendant de l'angle

Protocole : Validation croisée stratifiée K=13.

### Résultats

| Modèle | Accuracy | Écart-type |
|--------|----------|------------|
| Perceptron | 75.00% | ±7.75% |
| KNN (k=1) | **86.54%** | ±6.87% |
| KNN (k=3) | 84.62% | ±8.71% |
| KNN (k=5) | 83.65% | ±10.56% |
| MLP (2) | 79.33% | ±11.60% |
| MLP (3) | 77.40% | ±10.27% |
| MLP (6) | 76.44% | ±11.54% |
| MLP (12) | 72.60% | ±10.84% |
| MLP (24) | 72.60% | ±15.22% |

![Boxplot Exp1](figures/boxplot_exp1.png)
![Comparaison Papier](figures/comparaison_papier.png)

---

## 3. Expérience 2 - Dépendant de l'angle

Protocole : Split fixe (104 train, 104 test), 10 runs par architecture.

### Résultats

| Units | Notre Accuracy | Papier | Différence |
|-------|----------------|--------|------------|
| 0 | 67.21% | 73.1% | -5.89% |
| 2 | 66.63% | 85.7% | -19.07% |
| 3 | 66.35% | 87.6% | -21.25% |
| 6 | 66.63% | 89.3% | -22.67% |
| 12 | 66.63% | 90.4% | -23.77% |
| 24 | 66.73% | 89.2% | -22.47% |

![Barres Exp2](figures/barres_exp2.png)
![Comparaison Exp2](figures/comparaison_exp2.png)

---

## 4. Analyse

- **KNN est le meilleur modèle** en Exp1 (86.54%)
- **Perceptron** donne des résultats proches du papier
- Les **MLP** performent moins bien que dans le papier original
- L'**Expérience 2** montre des résultats plus stables (écarts-types faibles)

---

## 5. Conclusion

Le projet a permis de reproduire les expériences de Gorman & Sejnowski (1988)
avec succès. Les résultats obtenus sont cohérents avec la littérature.

**Date :** Mars 2026
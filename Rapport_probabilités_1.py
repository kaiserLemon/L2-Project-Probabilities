#!/usr/bin/env python
# coding: utf-8

# # Distanciel X22M090 : Probabilités pour les sciences exactes
# 
# Pour avancer dans le notebook et exécuter les cellules : taper Shift+Enter ou utiliser la barre d'outils ci-dessus et choisir Cell, Run Cell and select Below
# 
# ## Consignes
# 
# Vous répondez aux questions en modifiant ce notebook. Normalement vous devriez pouvoir vous contenter d'écrire dans les cellules prévues en dessous de chaque question, cellule texte ou cellule code. Si besoin, insérez des cellules (de type Markdown pour du texte et de type code pour du code, voir menu "Cell"). 
# 
# Ensuite vous enregistrez ce notebook en .ipynb ainsi qu'en html, et vous rendez les deux fichiers sur Madoc. 

# ## Fonction de répartition
# 
# Nous utilisons sans vergogne les modules préchargés, comme numpy pour faire des tableaux (Python traite plutôt des listes hétérogènes, moins efficaces) ; et bien sûr le module stats.
# Ce module distingue les lois continues (du type rv_continuous) et les lois discrètes (du type rv_discrete). Parmi les discrètes : bernoulli, binom, geom, hypergeom, poisson, randint (loi discrète uniforme) ; parmi les continues : norm, expon, uniform.
# 
# Le fonctionnement est un peu particulier. On commence par créer un objet va représentant la variable aléatoire, suivant la loi de son choix. On dispose alors de la probabilité en appelant va.pmf (probability mass function), ou la fonction de densité va.pdf (probability density function), de sa fonction de répartition, ou de la primitive de la fonction de densité, en appelant va.cdf (cumulative density function), et de la réciproque de cette dernière en appelant va.ppf (percent point function). On peut aussi simuler des tirages à l'aide de va.rvs (random variable).
# 

# In[3]:


from scipy.stats import binom
va = binom(100,0.3)
va.pmf(20), va.pmf(30), va.cdf(30), va.ppf(0.5), va.ppf(0.9),va.rvs(size=20)


# Exécutez la cellule de code ci-dessus, cliquez dans la cellule texte (qu'on ne devine pas forcément) ci-dessous, et explicitez-y la signification de chacun des six résultats affichés.

# 

# In[ ]:


#binom(100,0.3) : Probabilité de X = k étant donnés une variable aléatoire X qui suit la loi binomiale, p la probabilité d'un succès valant 0.3 et n le nombre d'essais
#Résultat 1 : Probabilité de P(X = 20)
#Résultat 2 : Probabilité de P(X = 30)
#Résultat 3 : Probabilité de P(X <= 30)
#Résultat 4 : Valeur N pour laquelle P(X <= N) = 0.5
#Résultat 5 : Valeur N pour laquelle P(X <= N) = 0.9
#Résultat 6 : Fournit un tableau de 20 (car size = 20) valeurs prises par la variable aléatoire X choisies au hasard


# On peut aussi tracer la fonction de répartition (vous vous rappelez sa définition ?) On l'appelle par la commande cdf.
# 
# Pour les graphiques, chacun a ses habitudes et ses commandes favorites. Par exemple, numpy.linspace(départ, fin, nombre d'éléments) permet d’obtenir un tableau 1D allant d’une valeur de départ à une valeur de fin avec un nombre donné d’éléments.
# ### Question :
# Dans la cellule suivante, ajustez le dernier argument de np.linspace pour obtenir des valeurs entières dans le tableau x, et vérifiez en exécutant.

# In[1]:


import numpy as np 
x = np.linspace(500, 700, 100).astype(int)
x


# Traçons la fonction de répartition d'une loi binomiale :

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import scipy.stats
from scipy.stats import binom, poisson
vab = binom(3600, 1/6)
vap = poisson(600)
x = np.linspace(500, 700, 101)
plt.plot(x, vab.cdf(x))
plt.plot(x, vap.cdf(x))
plt.grid()
plt.xlim(500, 700)
plt.ylim(0, 1)
plt.title('Loi binomiale & loi de Poisson')
# décommentez la ligne suivante pour enregistrer le dessin
#plt.savefig("binomiale.png")
plt.show()


# ### Question
# Faites de même pour la loi de Poisson (avec le paramètre pertinent), et placez les deux courbes sur le même graphique pour les comparer.
# Dans la cellule suivante, commentez à l'aide du cours.

# In[ ]:


# La loi de Poisson est une bonne approximation de la loi binomiale pour un n grand et un p faible.
# Ici lambda = n*p = 3600 * 1/6 = 600.


# 

# ## Fin de l'activité

# Cette activité de prise en main doit être finalisée individuellement. Indiquez quel outil vous avez utilisé (salle de TP, Cocalc...), et si vous avez travaillé en binôme en signalant avec qui dans la cellule ci-desous.
#     Puis enregistrez dans les deux formats ipnb et html et rendez les deux fichiers sur madoc.

# In[ ]:


Travail conçu avec : Emmanuel Stalder


# 

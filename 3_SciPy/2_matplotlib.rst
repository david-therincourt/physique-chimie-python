==============================
Les graphiques avec Matplotlib
==============================

Matplotlib est une librairie Python pour la visualisation de courbes.

Site Web officiel de Matplotlib : https://matplotlib.org/

Référence de l'API de la collection *pyplot* de la librairie  *matplotlib* :

https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot



Tracer une courbe à partir de données
=====================================

Les bases
~~~~~~~~~

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.array([0,1.01,2.02,2.99,3.98])     # Données en abscisse
   y = np.array([10.02,7.96,6.03,4.04,2.01]) # Données en ordonnée

   plt.plot(x,y)       # Tracé de la courbe
   plt.show()          # Affichage de la courbe
   
.. image:: images/Matplotlib_Courbe_1.png
   :width: 515 px
   :height: 349 px
   :scale: 70 %
   :alt: alternate text
   :align: center


* La collection ``pyplot`` du module ``matplotlib`` est importée avec l'alias ``plt``.
* La fonction ``plot()`` trace la courbe ``y=f(x)`` à partir des tableaux ``x`` et ``y``.
* La fonction ``show()`` appelée en dernier affiche la fenêtre graphique.

Ajouter un titre, une légende, une grille
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.array([0,1.01,2.02,2.99,3.98])     # Données en abscisse
   y = np.array([10.02,7.96,6.03,4.04,2.01]) # Données en ordonnée
   
   plt.plot(x,y,'x')       # Tracé de la courbe
   plt.title('Mom titre')  # Ajout d'un titre
   plt.xlabel('x')         # Nom de la grandeur en abscisse
   plt.ylabel('y')         # Nom de la grandeur en ordonnée
   plt.grid()              # Ajout d'une grille
   plt.show()              # Affichage



.. image:: images/Matplotlib_Courbe_2.png
   :width: 515 px
   :height: 349 px
   :scale: 70 %
   :alt: alternate text
   :align: center

* Le paramètre ``x`` dans ``plot()`` met en évidence les points par des croix sans les relier par des segments de droite.
* Les fonctions ``title()``, ``xlabel`` et ``ylabel()`` pour ajouter une titre et les légendes sur les axes.
* La fonction ``grid()`` ajoute une grille.

Définir l'échelle
~~~~~~~~~~~~~~~~~



.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   
   x = np.array([0,1.01,2.02,2.99,3.98])     # Données en abscisse
   y = np.array([10.02,7.96,6.03,4.04,2.01]) # Données en ordonnée
   
   
   plt.plot(x,y,'x')       # Tracé de la courbe
   plt.title('Mon titre')  # Ajout d'un titre
   plt.xlabel('x')         # Nom de la grandeur en abscisse
   plt.xlim(0,4)           # Echelle sur l'axe des x
   plt.ylabel('y')         # Nom de la grandeur en ordonnée
   plt.ylim(0,11)          # Echelle sur l'axe des y
   plt.grid()              # Ajout d'une grille
   plt.show()              # Affichage

.. image:: images/Matplotlib_Courbe_3.png
   :width: 515 px
   :height: 349 px
   :scale: 70 %
   :alt: alternate text
   :align: center

Tracer une courbe à partir d'une fonction
=========================================

Cas d'une sinusoïde
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.linspace(0,10,100)   # Création d'un tableau de valeurs pour x
   y = 10*np.sin(x)            # Calcul de y à partir de la fonction mathématique
   
   plt.plot(x,y)                        # Tracé de la courbe
   plt.title("A partir d'une fonction") # Titre
   plt.xlabel('x')                      # Légende abscisse
   plt.ylabel('y')                      # Légende ordonnée
   plt.grid()                           # Ajout d'une grille
   plt.show()                           # Affichage

.. image:: images/Matplotlib_Courbe_10.png
   :width: 515 px
   :height: 349 px
   :scale: 70 %
   :alt: alternate text
   :align: center

Cas de deux sinusoïdes avec légende
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.linspace(1,10,100)   # Création d'un tableau de valeurs pour x
   y1 = 10*np.sin(x)           # Calcul de y1
   y2 =  6*np.sin(x-1)         # Calcul de y2
   
   plt.plot(x,y1,label='10.sin(x)')   # Tracé de la courbe y1 avec texte légende
   plt.plot(x,y2,label='6.sin(x-1)')  # Tracé de la courbe y1 avec texte légende
   plt.title('Ma première courbe')    # Titre
   plt.xlabel('x')                    # Légende abscisse
   plt.ylabel('y')                    # Légende ordonnée
   plt.legend()                       # Ajout de la légende
   plt.grid()                         # Ajout d'une grille
   plt.show()                         # Affichage

.. image:: images/Matplotlib_Courbe_11.png
   :width: 515 px
   :height: 349 px
   :scale: 70 %
   :alt: alternate text
   :align: center

* Dans la fonction ``plot()``, le paramètre ``label='...'`` permet d'ajouter une étiquette dans la légende.

Tracer un histogramme
=====================

Le module **matplolib** propose la fonction ``hist()`` pour l'affichage d'un **histogramme** à partir d'un tableau de mesures.
La documentation officielle de cette fonction se trouve `ici <https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.hist.html>`_

Histogramme seul
~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt

   x = [5,6,4,7,6,7,6,8,6,5,6,5,3,9,4,6,5,8,7,6]

   plt.hist(x,range=(0,10),bins=10,rwidth = 0.8, align='left')
   plt.show()

:Résultats:

.. image:: images/ultrason_histogramme_2.png
   :width: 507 px
   :height: 349 px
   :scale: 70 %
   :alt: alternate text
   :align: center

Dans la fonction ``hist()`` :

* ``range=(0,10)`` fixe les limites de la plage d'étude du tableau de données.
* ``bins=10`` est le nombre d'intervalles dans la plage d'étude.
* ``rwidth = 0.95`` fixe la largeur des barres à 95% pour une meilleure visibilité.
* ``align='left'`` permet de centrer les barres.

Histogramme, valeurs et fréquences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt

   x = [5,6,4,7,6,7,6,8,6,5,6,5,3,9,4,6,5,8,7,6]

   freq,valx,opt = plt.hist(x,range=(0,10),bins=10,rwidth = 0.8, align='left')
   plt.show()

   print("Valeur moyenne = ", np.mean(x))
   print("Ecart type = ",np.std(x).round(2))
   print('frequence = ',freq)
   print('valeurs x = ',valx)

:Résultats:

.. image:: images/ultrason_histogramme_2.png
   :width: 507 px
   :height: 349 px
   :scale: 70 %
   :alt: alternate text
   :align: center

.. code-block:: python

   Valeur moyenne =  5.95
   Ecart type =  1.4309
   frequence =  [0. 0. 0. 1. 2. 4. 7. 3. 2. 1.]
   valeurs x =  [ 0.  1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]

* Les fonctions du module Numpy ``mean()`` est ``std()`` calculent respectivement la valeur moyenne et l'écart type.

.. note::

   Le module ``scipy.stats`` fournit un grand nombre de lois de probabilités (Bernoulli, binomiale, normale, ...) et diverses méthodes de calcul (moyenne, médiane, variance, écart type, ...).

   Voir la page `Python pour le calcul scientifique/Statistiques <https://fr.wikibooks.org/wiki/Python_pour_le_calcul_scientifique/Statistiques>`_ sur WikiBooks

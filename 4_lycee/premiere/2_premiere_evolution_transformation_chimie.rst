===============================
Évolution d'un système chimique
===============================

.. topic:: Programme de première générale - Enseignement de spécialité - 2019

   "Déterminer la composition de l’état final d’un système siège d’une transformation chimique totale à l’aide d’un langage de programmation.

Méthode algébrique
==================

.. code-block:: python

   import numpy as np
   import matplotlib.pyplot as plt


   a,b,c,d = 1,2,1,2           # Nombres stoechiométriques
   niA,niB,niC,niD = 4,4,0,0   # quantité de matière initiale de l'espèce chimique A

   # Calcul de l'avancement maximal xMax
   xMax1 = niA/a
   xMax2 = niB/b
   if (xMax1<xMax2):
       xMax = xMax1
       print("L'espèce A est la réactif limitant donc xmax = ", xMax, " mol")
   elif (xMax2<xMax1):
       xMax = xMax2
       print("L'espèce B est la réactif limitant donc xmax = ", xMax, " mol")
   else:
       xMax = xMax1
       print("Les espèces A et B sont tous les deux réactifs limitant donc xmax = ", xMax, " mol")
       print("Les espèces A et B sont en proportion stoechiométrique !")

   # Tracé de l'évolution du système chimique

   x = np.linspace(0,xMax,10)
   nA = niA-a*x
   nB = niB-b*x
   nC = niC+c*x
   nD = niD+d*x

   plt.title("Evolution d'une réaction chimique")
   plt.xlabel("Avancement x (mol)")
   plt.xlim(0,xMax)
   plt.ylabel("Quantité de matière (mol)")
   plt.ylim(0,4)
   plt.plot(x,nA,label = "Réactif A")
   plt.plot(x,nB,label = "Réactif B")
   plt.plot(x,nC,label = "Produit C")
   plt.plot(x,nD,label = "Produit D")
   plt.legend()
   plt.grid()
   plt.show()

:Résultats:

.. code::

   L'espèce B est la réactif limitant donc xmax =  2.0  mol

.. image:: images/Chimie_Evolution_Systeme.png
   :width: 539 px
   :height: 385px
   :scale: 100 %
   :alt: alternate text
   :align: center




Méthode itérative
=================

On considère la réaction totale entre l’hydrogène sulfureux (H 2 S) et le dioxyde de soufre (SO 2 ) qui produit du
soufre et de l’eau et modélisée par l’équation :

.. math::

   2 H_2S + SO_2 -> 3 S + 2 H_2O

Etape 1 : sans courbe
---------------------

.. code-block:: python

   a = 2 # coefficient stoechiométrique de H2S
   b = 1
   c = 3
   d = 2

   n0_H2S = float(input("Donne le nombre de moles de H2S : "))
   n0_SO2 = float(input("Donne le nombre de moles de SO2 : "))
   n0_S   = float(input("Donne le nombre de moles de S : "))
   n0_H2O = float(input("Donne le nombre de moles de H2O : "))

   n_H2S, n_SO2, n_S, n_H2O = n0_H2S, n0_SO2, n0_S, n0_H2O

   dx = 0.01
   x = 0

   while n_H2S>0 and n_SO2>0:
       x = x + dx
       n_H2S = n0_H2S - a*x
       n_SO2 = n0_SO2 - b*x
       n_S   = n0_S   + c*x
       n_H2O = n0_H2O + d*x


   print('Avancement final = ',x, ' mol')
   print('n(H2S) = ', n_H2S)
   print('n(SO2) = ', n_SO2)
   print('n(S) = ', n_S)
   print('n(H2O) = ', n_H2O)

Etape 2 : avec courbe
---------------------

.. code-block:: python

   import matplotlib.pyplot as plt

   a = 2 # coefficient stoechiométrique de H2S
   b = 1
   c = 3
   d = 2

   n0_H2S = float(input("Donne le nombre de moles de H2S : "))
   n0_SO2 = float(input("Donne le nombre de moles de SO2 : "))
   n0_S   = float(input("Donne le nombre de moles de S : "))
   n0_H2O = float(input("Donne le nombre de moles de H2O : "))

   n_H2S, n_SO2, n_S, n_H2O = [n0_H2S], [n0_SO2], [n0_S], [n0_H2O]

   dx = 0.1
   x = [0]

   while n_H2S[-1]>0 and n_SO2[-1]>0:
       x.append(x[-1] + dx)
       n_H2S.append(n_H2S[-1] - a*dx)
       n_SO2.append(n_SO2[-1] - b*dx)
       n_S.append(n_S[-1]   + c*dx)
       n_H2O.append(n_H2O[-1] + d*dx)

   xMax = max(x)

   plt.title("Evolution d'une réaction chimique")
   plt.xlabel("Avancement x (mol)")
   plt.xlim(0,xMax)
   plt.ylabel("Quantité de matière (mol)")
   plt.ylim(0,2)
   plt.plot(x,n_H2S,label = "Réactif H2S")
   plt.plot(x,n_SO2,label = "Réactif SO2")
   plt.plot(x,n_S,label = "Produit S")
   plt.plot(x,n_H2O,label = "Produit H2O")
   plt.legend()
   plt.grid()
   plt.show()

:résultats:

.. code-block:: python

   Donne le nombre de moles de H2S : 1
   Donne le nombre de moles de SO2 : 1
   Donne le nombre de moles de S : 0
   Donne le nombre de moles de H2O : 0
   xMax=  0.5000000000000002

.. image:: images/Chimie_Evolution_Systeme_2.png
   :width: 556 px
   :height: 386 px
   :scale: 100 %
   :alt: alternate text
   :align: center

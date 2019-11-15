===============================
Évolution d'un système chimique
===============================

.. topic:: Programme de première générale - Enseignement de spécialité - 2019

   "Déterminer la composition de l’état final d’un système siège d’une transformation chimique totale à l’aide d’un langage de programmation.

:Script Python:

.. code:: python

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

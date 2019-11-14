==============================
Les graphiques avec Matplotlib
==============================

Matplotlib est une librairie Python pour la visualisation de courbes.

Site Web officiel de Matplotlib :

https://matplotlib.org/

Référence de l'API de la collection *pyplot* de la librairie  *matplotlib* :

https://matplotlib.org/api/_as_gen/matplotlib.pyplot.html#module-matplotlib.pyplot



Tracer une courbe à partir de données
=====================================

Les bases
~~~~~~~~~


:Code Python:

.. code:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.array([0,1.01,2.02,2.99,3.98])
   y = np.array([10.02,7.96,6.03,4.04,2.01])

   plt.plot(x,y)
   plt.show()
   
.. image:: images/Matplotlib_Courbe_1.png
   :width: 515 px
   :height: 349 px
   :scale: 100 %
   :alt: alternate text
   :align: center


* La collection ``pyplot`` du module ``matplotlib`` est importée avec l'alias ``plt``.
* La fonction ``plot()`` trace la courbe ``y=f(x)`` à partir des tableaux ``x`` et ``y``.
* La fonction ``show()`` appelée en dernier affiche la fenêtre graphique.

Ajouter un titre, une légende, une grille
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Code Python:

.. code:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.array([0,1.01,2.02,2.99,3.98])
   y = np.array([10.02,7.96,6.03,4.04,2.01])
   
   plt.plot(x,y,'x')
   plt.title('Mom titre')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.grid()
   plt.show()



.. image:: images/Matplotlib_Courbe_2.png
   :width: 515 px
   :height: 349 px
   :scale: 100 %
   :alt: alternate text
   :align: center

* Le paramètre ``x`` dans ``plot()`` met en évidence les points par des croix sans les relier par des segments de droite.
* Les fonctions ``title()``, ``xlabel`` et ``ylabel()`` pour ajouter une titre et les légendes sur les axes.
* La fonction ``grid()`` ajoute une grille.

Définir l'échelle
~~~~~~~~~~~~~~~~~

:Code Python:

.. code:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   
   x = np.array([0,1.01,2.02,2.99,3.98])
   y = np.array([10.02,7.96,6.03,4.04,2.01])
   
   
   plt.plot(x,y,'x')
   plt.title('Mon titre')
   plt.xlabel('x')
   plt.xlim(0,4)    # Echelle sur l'axe des x
   plt.ylabel('y')
   plt.ylim(0,11)   # Echelle sur l'axe des y
   plt.grid()
   plt.show()

.. image:: images/Matplotlib_Courbe_3.png
   :width: 515 px
   :height: 349 px
   :scale: 100 %
   :alt: alternate text
   :align: center

Tracer une courbe à partir d'une fonction
=========================================

:Code Python:

.. code:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.linspace(0,10,100)
   y = 10*np.sin(x)
   
   plt.plot(x,y)
   plt.title("A partir d'une fonction")
   plt.xlabel('x')
   plt.ylabel('y')
   plt.grid()
   plt.show()

.. image:: images/Matplotlib_Courbe_10.png
   :width: 515 px
   :height: 349 px
   :scale: 100 %
   :alt: alternate text
   :align: center

:Code Python:

.. code:: python

   import numpy as np
   import matplotlib.pyplot as plt
   
   x = np.linspace(1,10,100)
   y1 = 10*np.sin(x)
   y2 =  6*np.sin(x-1)
   
   plt.plot(x,y1,label='10.sin(x)')
   plt.plot(x,y2,label='6.sin(x-1)')
   plt.title('Ma première courbe')
   plt.xlabel('x')
   plt.ylabel('y')
   plt.legend()
   plt.grid()
   plt.show()

.. image:: images/Matplotlib_Courbe_11.png
   :width: 515 px
   :height: 349 px
   :scale: 100 %
   :alt: alternate text
   :align: center



* Dans la fonction ``plot()``, le paramètre ``label='...'`` permet d'ajouter une étiquette dans la légende.

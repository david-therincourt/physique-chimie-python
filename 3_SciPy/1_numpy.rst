=======================
Les tableaux avec Numpy
=======================

Le module Numpy  permet la création et la manipulation de tableaux (vecteurs) dans Python.

Site Web officiel de Numpy : https://www.numpy.org/

Documentation de Numpy : https://docs.scipy.org/doc/

Importation du module Numpy
===========================

.. code-block:: python

   >>> import numpy as np

* Le module ``numpy`` est importé avec l'alias ``np`` qui est plus rapide à écrire à fois !


Création de tableaux
====================

A partir d'une liste
~~~~~~~~~~~~~~~~~~~~



.. code-block:: python

   >>> a = np.array([1,2,3,4])
   >>> a
   array([1, 2, 3, 4])
   >>> print(a)
   [1 2 3 4]

* Il est possible de créer un tableau (ici à 1 dimension) à partir d'une liste.


A partir d'un intervalle et du nombre de d'éléments
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


.. code-block:: python

   >>> a = np.linspace(1,7,3)
   >>> a
   array([1., 4., 7.])

* La fonction ``linspace(start,end, nb)`` génère ``n`` valeurs entre ``start`` et ``end``.


A partir d'un intervalle et d'un pas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   >>> a = np.arange(1,2,0.2)
   >>> print(a)
   [1.  1.2 1.4 1.6 1.8]

* La fonction ``arange(a,b,p)`` construit un tableau Numpy de ``a`` à ``b`` (non compris) avec un pas de ``p``.

Créer un tableau vide
~~~~~~~~~~~~~~~~~~~~~

Il est parfois utile de créer un tableau vide (rempli de zéros) dont les valeurs pourront être modifiées par la suite.

.. code-block:: python

   >>> a = np.zeros(5)
   >>> print(a)
   [0. 0. 0. 0. 0.]


Manipulation de tableaux
========================



.. code-block:: python

   >>> a = np.array([1,2,3,4])
   >>> a*3
   array([ 3,  6,  9, 12])
   >>> a**2
   array([ 1,  4,  9, 16])

* Les opérations mathématiques se font **itérativement** sur les tableaux de type Numpy.



.. code-block:: python

   >>> l=[1,2,3,4]
   >>> l*3
   [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

* Ce n'est pas le cas avec les listes !



.. code-block:: python

   >>> a = np.array([1,2,3,4])
   >>> b = np.array([5,6,3,8])
   >>> 3*a+b
   array([ 8, 12, 12, 20])
   >>> a==b
   array([False, False,  True, False])

* La plupart des opérateurs sont disponibles avec les tableaux Numpy !



.. code-block:: python

   >>> a = np.array([1,2,3,4])
   >>> import math
   >>> math.sqrt(a)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: only size-1 arrays can be converted to Python scalars

* Par contre, il n'est pas possible d'appliquer les fonctions mathématiques du module ``math``.



.. code-block:: python

   >>> np.sqrt(a)
   array([1.        , 1.41421356, 1.73205081, 2.        ])
   >>> np.exp(a)
   array([ 2.71828183,  7.3890561 , 20.08553692, 54.59815003])

* Le module Numpy intégre ses propres fonctions mathématiques.



Importation et exportation de données
=====================================

Fichier CSV
~~~~~~~~~~~

La plupart des logiciels de traitement de données (ex. tableur, Regressi, Latis, ...) donne la possibilité d'importer ou d'exporter des données dans un **fichier texte au format CSV** avec l'extension ``.csv`` ou ``.txt``.



Le tableau de données suivant :

   == == ==
   x  y  z
   == == ==
   1  5  7
   2  10 6
   3  15 5
   4  20 4
   == == ==

s'écrit comme ci-dessous dans un fichier texte au format CSV nommé par exemple ``data.txt`` :

.. code::

   x,y,z
   1,5,7
   2,10,6
   3,15,5
   4,20,4

* les données sont rangées en colonne ;
* les valeurs sont séparées par une virgule, un point virgule ou une tabulation ;
* la première ligne renseigne sur les noms des variables.


Importer un fichier CSV
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   >>> import numpy as np
   >>> np.loadtxt('data.txt',delimiter=',',skiprows=1,unpack=True)
   array([[  1.,   2.,   3.,   4.],
       [  5.,  10.,  15.,  20.],
       [  7.,   6.,   5.,   4.]])

* La fonction ``loadtxt()`` importe les données d'un fichier CSV et renvoie un tableau Numpy.
* ``delimiter=','`` pour signifier que les virgules séparent les valeurs.
* ``skiprows=1`` pour indiquer que la première ligne ne contient pas de données.
* L'option ``unpack=True`` transpose le tableau pour être dans le bon sens.



.. code-block:: python

   >>> import numpy as np
   >>> x,y,z = np.loadtxt('data.txt',delimiter=',',skiprows=1,unpack=True)
   >>> x
   array([1., 2., 3., 4.])
   >>> y
   array([ 5., 10., 15., 20.])
   >>> z
   array([7., 6., 5., 4.])


* Une affectation multiple (utilisation d'un tuple) permet d'obtenir toutes les variables d'un coup.

Export dans un fichier CSV
~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import numpy as np
   a = np.array([1,2,3,4])         # Données de la variable a
   b = np.array([5,6,7,8])         # Données de la variable b
   data = np.transpose([a,b])      # Transposition des données
   np.savetxt('data2.txt',data,delimiter=',',header='a,b',comments='')  # Création du fichier CSV


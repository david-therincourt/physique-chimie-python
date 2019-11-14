===========
Les modules
===========

Le langage Python est fourni avec des fonctions de base. Mais leur nombre est bien souvent insuffisant. Il est alors souvent utile d'utiliser des fonctions écrites par d'autres personnes de la communauté Python. C'est ce qu'apportent les librairies ou modules.

Par exemple, il n'est pas possible d'effectuer une racine carrée à moins d'importer la fonction ``sqrt()`` inclue dans le module ``math`` !

https://docs.python.org/3/library/math.html

:Exemple:

.. code:: python

   >>> import math
   >>> sqrt(2)
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   NameError: name 'sqrt' is not defined
   >>> math.sqrt(2)
   1.4142135623730951

* Le mot clé ``import`` charge la librairie ``math`` ;
* La fonction racine carrée n'est accessible qu'avec la syntaxe ``math.sqrt()`` signifiant que ``sqrt()`` est une fonction du module ``math``.
* Toutes les autres fonctions mathématiques du module ``math`` sont ainsi disponibles de cette manière.

:Exemple:

Si le nom du module est trop long à écrire à chaque fois !

.. code:: python

   >>> import math as mt
   >>> mt.sqrt(2)
   1.4142135623730951
   >>> mt.exp(1)
   2.718281828459045

* ``mt`` est un alias de ``math``.

:Exemples: autres façons d'appeler une librairie.

.. code:: python

   >>> from math import sqrt
   >>> sqrt(2)
   1.4142135623730951

* Seule la fonction ``sqrt()`` a été importée ;
* Son appel se fait directement.


.. code:: python

   >>> from math import *
   >>> sqrt(3)
   1.7320508075688772
   >>> exp(1)
   2.718281828459045

* La présence du caractère ``*`` importe toutes les fonctions du module ``math`` ;
* Mauvaise pratique. **À éviter** ! 

.. note::

   Quelques modules souvent rencontrés en sciences physiques : ``math``, ``numpy``, ``matplotlib``, ``scipy``, ...

   :Exemple:

   .. code:: python
   
      >>> import numpy as np
      >>> import matplotlib.pyplot as plt
      >>> from scipy.stats import linregress

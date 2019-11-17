=============
Les fonctions
=============

En programmation, un fonctionne **réalise un traitement** puis **renvoie  la résultat** de ce traitement.

.. code-block:: python

   >>> def aireCarre(a):
   ...     aire = a*a
   ...     return aire
   ...
   >>> aireCarre(5)
   25

* Le mot clé ``def`` est toujours utilisé pour définir une fonction.
* ``aireCarre`` est le **nom de la fonction**.
* La variable ``a`` est un **paramètre** (ou argument) de la fonction.
* Après le caractère ``:``, toutes instructions de la fonction sont **indentés**.
* Le mot clé ``return`` est utilisé pour **renvoyer le résultat** de la fonction.
* Le nom de la fonction est utilisé pour **l'appel** de la fonction.

.. code-block:: python

   >>> def aireRectangle(l,L):
   ...     aire = l*L
   ...     return aire
   ...
   >>> aireRectangle(4,5)
   20

Une fonction peuvent admettre aucun, un ou plusieurs arguments

**Application :** calcul d'énergie mécanique

Dans un script Python :

.. code-block:: python

   def Epp(m,h):
       return m*9.81*h

   def Ecc(m,v):
       return 0.5*m*v**2

   def Em(m,h,v):
       return Epp(m,h)+Ecc(m,v)

Résultats dans la console Python :

.. code-block:: Python

   >>> Epp(50,10)
   4905.0
   >>> Ecc(50,13)
   4225.0
   >>> Em(50,10,13)
   9130.0

Une fonction peut appeler d'autres fonctions !

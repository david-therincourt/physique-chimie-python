=============
Les fonctions
=============

Principe
========

En programmation, un fonctionne **réalise un traitement** puis **renvoie le résultat** de ce traitement.

.. code-block:: python

   >>> def aireCarre(a):
   ...     aire = a*a
   ...     return aire
   ...
   >>> aireCarre(5)
   25

* Le mot clé ``def`` est toujours utilisé pour définir une fonction.
* Ici ``aireCarre`` est le **nom de la fonction**.
* La variable ``a`` est un **paramètre** (ou argument) de la fonction.
* Après le caractère ``:``, toutes instructions appartenant à la fonction doivent-être **indentées**.
* Le mot clé ``return`` est utilisé pour **renvoyer le résultat** de la fonction.
* Le nom de la fonction est utilisé lors de **l'appel** de la fonction.

.. code-block:: python

   >>> def aireRectangle(l,L):
   ...     aire = l*L
   ...     return aire
   ...
   >>> aireRectangle(4,5)
   20

* Une fonction peuvent admettre aucun, un ou plusieurs arguments

Exemple 1 : calcul d'une énergie potentielle
============================================

**Définition** de la fonction calculant l'énergie potentielle de pesanteur dans un script Python :

.. code-block:: python

   def Epp(m,h):
       return m*9.81*h

.. warning:: Ne pas oublier d'exécuter le script Python pour que la fonction soit prise en compte !

**Appel** de la fonction dans l'interpréteur Python :

.. code-block:: Python

   >>> Epp(50,10)
   4905.0

* Les variables ``m`` et ``h`` sont locales. Elles n'existent que dans la fonction !

Exemple 2 : calcul d'une énergie mécanique
==========================================

Définitions des fonctions :

.. code-block:: python

   def Epp(m,h):
       return m*9.81*h

   def Ec(m,v):
       return 0.5*m*v**2

   def Em(m,h,v):
       return Epp(m,h)+Ec(m,v)

Résultats :

.. code-block:: Python

   >>> Epp(50,10)
   4905.0
   >>> Ec(50,13)
   4225.0
   >>> Em(50,10,13)
   9130.0

* La fonction ``Em()`` fait appel aux deux autres fonctions ``Epp()`` et ``Ec()`` !
* Pour chaque fonction, la variable ``m`` n'est pas la même. C'est toujours un variable locale.

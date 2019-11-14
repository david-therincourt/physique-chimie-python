=================
Les types évolués
=================

Les listes
----------
En sciences physiques, l'utilisation des tableaux de données est monnaie courante. En langage Python, les tableaux peuvent-être représentés par les listes.

:Exemple:

.. code:: python

   >>> l = [0,'a',4.13]
   >>> print(l)
   [0, 'a', 4.13]

* Une liste est **délimitée** par des crochés ``[]`` ;
* Les éléments d'une liste sont **séparés** par des virgules ;
* Une liste peut contenir des  **types différents**.

:Exemple:

.. code:: python

   >>> l[0]
   0
   >>> l[1]
   'a'
   >>> l[2]
   4.13
   >>> l[3]
   Traceback (most recent call last):
   File "<stdin>", line 1, in <module>
   IndexError: list index out of range

* Les éléments d'une liste sont repérés par un **indice**.
* En programmation, l'indice du premier élément est toujours 0 !

:Exemple:

.. code:: python

   >>> l[1]=3
   >>> print(l)
   [0, 3, 4.13]



* Les éléments d'une liste peuvent-être **modifiés**.

:Exemple:

.. code:: python

   >>> x = [0,1,2,3,4,5,6]
   >>> x[2:]
   [2, 3, 4, 5, 6]
   >>> x[:3]
   [0, 1, 2]
   >>> x[2:5]
   [2, 3, 4]

* Le caractère ``:`` permet de **sélectionner** une partie de la liste.

:Exemple:

.. code:: python

   >>> y = [0,1,2,6,5,4,3]
   >>> y.sort()
   >>> print(y)
   [0, 1, 2, 3, 4, 5, 6]
   >>> len(y)
   7

* La fonction ``sort()`` trie une liste dans l'ordre croissant.
* La fonction ``len()`` donne le nombre d'éléments dans une liste.

Les tuples
----------

Un tuple est un tableau **non-modifiable**.

:Exemple:

.. code:: python

   >>> t = (1,2,3)
   >>> t[1]
   2
   >>> t[1] = 4
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'tuple' object does not support item assignment

* Un tuple est une **série de valeurs** entre parenthèses ``()`` séparées par des virgules.
* Les éléments d'un tuple sont **non modifiables**.

:Exemple:

.. code:: python

   >> t = 1,2,3
   >>> t
   (1, 2, 3)

* Il est possible d'omettre les parenthèses !

:Exemple:

.. code:: python

   >>> a,b,c = 4,"azerty",4.56
   >>> print(a)
   4
   >>> print(b)
   azerty
   >>> print(c)
   4.56

* En Python, les tuples permettent l'**affectation multiple** (sur une même ligne).

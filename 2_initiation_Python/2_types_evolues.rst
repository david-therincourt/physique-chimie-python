=================
Les types évolués
=================

Les listes
----------

En sciences physiques, l'utilisation des tableaux de données est monnaie courante. En langage Python, les **tableaux sont représentés par les listes**.

.. code-block:: python

   >>> l = [0,'a',4.13]
   >>> print(l)
   [0, 'a', 4.13]

* Une liste est **délimitée** par des crochés ``[]`` ;
* Les éléments d'une liste sont **séparés** par des virgules ;
* Une liste peut contenir des  **types différents**.

.. code-block:: python

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

* Chaque élément d'une liste est repéré par un **indice** (position dans la liste).
* L'indice du premier élément est toujours 0 !

.. code-block:: python

   >>> l[-1]
   4.13
   >>> l[-2]
   'a'
   >>> l[-4]
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   IndexError: list index out of range

* Les indices négatifs permettent de parcourir la liste depuis la fin.
* L'indice ``-1`` étant le dernier élément de la liste !

.. code-block:: python

   >>> l[1]=3
   >>> print(l)
   [0, 3, 4.13]

* Les éléments d'une liste peuvent-être **modifiés**.


.. code-block:: python

   >>> x = [0,1,2,3,4,5,6]
   >>> x[2:]
   [2, 3, 4, 5, 6]
   >>> x[:3]
   [0, 1, 2]
   >>> x[2:5]
   [2, 3, 4]

* Le caractère ``:`` permet de **sélectionner** une partie de la liste.

.. code-block:: python

   >>> y = [0,1,2,6,5,4,3]
   >>> len(y)
   7

* La fonction ``len()`` donne le nombre d'éléments dans une liste.

.. code-block:: python

   >>> y = [0,1,2,6,5,4,3]
   >>> y.append(9)
   >>> y
   [0, 1, 2, 6, 5, 4, 3, 9]
   >>> y.sort()
   >>> print(y)
   [0, 1, 2, 3, 4, 5, 6, 9]

* La méthode ``append()`` ajoute un élément à la fin de la liste.
* La méthode ``sort()`` trie une liste dans l'ordre croissant.
* Application de ces deux méthodes modifient la liste sur laquelle elles sont appliquées !

Les tuples
----------

Un tuple est un tableau **non-modifiable**.


.. code-block:: python

   >>> t = (1,2,3)
   >>> t[1]
   2
   >>> t[1] = 4
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: 'tuple' object does not support item assignment

* Un tuple est une **série de valeurs** entre parenthèses ``()`` séparées par des virgules.
* Les éléments d'un tuple sont **non modifiables**.


.. code-block:: python

   >>> t = 1,2,3
   >>> t
   (1, 2, 3)

* Il est possible d'omettre les parenthèses (quand c'est possible) avec les tuples !


.. code-block:: python

   >>> a,b,c = 4,"azerty",4.56
   >>> print(a)
   4
   >>> print(b)
   azerty
   >>> print(c)
   4.56

* En Python, les **tuples permettent l'affectation multiple** (sur une même ligne).

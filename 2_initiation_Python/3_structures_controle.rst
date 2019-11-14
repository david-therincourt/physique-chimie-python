==========================
Les structures de contrôle
==========================

Les conditionnelles
===================

Les structures conditionnelles permettent de faire des tests. ::

   SI <condition>
   ALORS
      <bloc d'instruction(s) pour condition vraie>
   SINON
      <bloc d'instruction(s) pour condition fausse>

:Exemple:

.. code:: python

   >>> if True :
   ...     print("Vrai")
   ... else :
   ...     print("Faux")
   ... 
   Vrai

   >>> if False :
   ...     print("Vrai")
   ... else :
   ...     print("Faux")
   ... 
   Faux

* Une condition ne peut-être que vrai (``True``) ou fausse (``False``).
* Le caractère ``:`` signifie le **début d'un bloc d'instructions**.
* Un bloc d'instructions est toujours **indenté** (décalé du même nombre de caractères pour chaque ligne).
* Les caractères ``...`` est un **prompt secondaire** signifiant que des instructions sont écrites sur plusieurs lignes.
* Le mot clé ``else`` peut-être omis si rien ne doit-être fait pour une condition fausse.


:Exemple:

.. code:: python

   >>> a = 3
   >>> b = 5
   >>> if (a>b):
   ...     print("a strictement plus grand que b !")
   ... else:
   ...     print("a plus petit ou égal à b !")
   ... 
   a plus petit ou égal à b !
   >>> a>b
   False

* Une condition s'obtient à partir d'une **expression** dont le résultat est du type booléen (``True`` ou ``False``)



Les boucles
===========

En programmation, une **boucle** permet de répéter plusieurs fois ou indéfiniment des instructions.

En Python, la structure suivante est souvent rencontrée : ::

   POUR <variable> DANS <liste> FAIRE
      <bloc d'instructions>

:Exemple:

.. code:: python

   >>> for i in [1,2,3]:
   ...     print(i)
   ... 
   1
   2
   3

* La variable ``i`` prend itérativement les valeurs 1, 2 et 3 dans la liste ;
* Le nombre d'itération d'une boucle de type ``for`` est toujours connu à l'avance !



:Exemple: la fonction ``range()``.

.. code:: python

   >>> list(range(5))
   [0, 1, 2, 3, 4]
   >>> for i in range(5):
   ...     print(i)
   ... 
   0
   1
   2
   3
   4

* La fonction ``range(n)`` facilite la création de boucle.
* La fonction ``range(n)`` renvoie un itérateur de 0 à n-1



:Exemple:

.. code:: python

   >>> for i in range(2,5):
   ...     print(i)
   ... 
   2
   3
   4
   >>> for i in range(2,9,3):
   ...     print(i)
   ... 
   2
   5
   8

* D'autres formes de la fonction ``range()`` existent !

.. note::
   La structure itérative ``while`` n'est pas abordée ici.

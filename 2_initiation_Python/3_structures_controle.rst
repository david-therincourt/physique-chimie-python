==========================
Les structures de contrôle
==========================

Les conditionnelles
===================

Les structures conditionnelles permettent de faire des tests.

.. code::

   SI <condition>
   ALORS
      <bloc instruction(s) pour condition vraie>
   SINON
      <bloc instruction(s) pour condition fausse>

.. warning::

   Dans les exemples qui suivent, les caractères ``...`` composent un **prompt secondaire** de la console Python signifiant que des instructions sont écrites sur plusieurs lignes. Ces caractères n'apparaissent jamais dans un script Python.

.. code-block:: python

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
* Le mot clé ``else`` peut-être omis si rien ne doit-être fait pour une condition fausse.






.. code-block:: python

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

Une condition s'obtient à partir d'une **expression** dont le résultat est du type booléen (``True`` ou ``False``)

Les boucles
===========

En programmation, une **boucle** permet de répéter plusieurs fois ou indéfiniment des instructions.

La boucle FOR
-------------

.. code::

   POUR <variable> DANS <liste> FAIRE
      <bloc instructions>

La boucle POUR s'utilise lors que le **nombre d'itérations est connu à l'avance**.

Il s'agit d'une **boucle bornée**.

.. code-block:: python

   >>> for i in [1,2,3]:
   ...     print(i)
   ... 
   1
   2
   3

* La variable ``i`` prend itérativement les valeurs 1, 2 et 3 dans la liste ;
* Le nombre d'itération d'une boucle de type ``for`` est toujours connu à l'avance !

.. code-block:: python

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
* La fonction ``range(n)`` renvoie un itérateur de ``0`` à ``n-1``.
* La variable ``i`` est un **compteur**.

.. code-block:: python

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

* Il existe d'autres formes de la fonction ``range()``.

**Application :** Calcul d'une moyenne d'une liste de notes.

En parcourant la liste :

.. code-block:: python

   listeNote = [12,15,14,16,13,15]
   nbNote = len(listeNote)
   somme = 0
   for note in listeNote:
       somme = somme + note
   moyenne = somme/nbNote
   print(moyenne)

Avec un compteur :

.. code-block:: python

   listeNote = [12,15,14,16,13,15]
   nbNote = len(listeNote)
   somme = 0
   for i in range(nbNote):
       somme = somme + listeNote[i]
   moyenne = somme/nbNote
   print(moyenne)

La boucle While
---------------

.. code::

   TANT QUE <condition> FAIRE
      <bloc instructions>

La boucle TANT QUE est utilisée quand le **nombre d'itérations n'est pas connu à l'avance**.

.. code-block:: python

   reponse = ''
   while reponse != 'blanc':
       reponse = input("Quelle est la couleur du cheval blanc d'Henry IV ? ")
   print("Bonne réponse !")

La boucle s'effectue indéfiniment tant que la réponse est fausse !

.. code-block:: python

   from random import random
   x=0
   while x<10:
       x=x+3*random()
       print(x)

* La fonction ``random()`` renvoie un nombre au hasard entre 0 et 1 (exclu).
* Le nombre d'itération varie à chaque exécution du programme !




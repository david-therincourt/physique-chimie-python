==========================
Variables et types de base
==========================

Qu'est-ce qu'une variable ?
---------------------------

Une variable est un **emplacement  mémoire** dans l'ordinateur prévu pour contenir des données ;



:Exemple:

.. code:: python

   >>> a = 3
   >>> nom = "Newton"

* Une variable **identifiée** par un nom ;
* Le signe ``=`` permet l'**affection** d'une valeur à une variable.
* Son contenu est **modifiable** pendant l'exécution du programme.





Affichage d'une variable
------------------------

:Exemple:

.. code:: python

   >>> a = 3
   >>> print(a)
   3
   >>> nom = "Newton"
   >>> print(nom)
   Newton
   >>> print(nom, a, "Bonjour")
   Newton 3 Bonjour

* La fonction ``print()`` affiche le contenu d'une variable.


Les types d'une variable
------------------------

Contrairement à d'autres langage de programmation, il n'est pas nécessaire de donner le type d'une variable à sa déclaration en Python.

Les entiers
~~~~~~~~~~~

:Exemple:

.. code:: python

   >>> type(10)
   <class 'int'>
   >>> a = 10
   >>> type(a)
   <class 'int'>

* La fonction ``type()`` donne le type d'une expression ou d'une variable.
* ``int`` pour `integer` (entier).

.. code:: python

   >>> b = 3
   >>> a+b
   13
   >>> a/b
   3.3333333333333335
   >>> a//b
   3
   >>> a%b
   1


* Les **opérateurs mathématiques** s'appliquent normalement.
* L'opérateur ``//`` donne le **quotient** de la division entière.
* L'opérateur ``%`` (modulo) donne le **reste** de la division entière.

   ====== ===============================
   Opérateurs mathématiques
   --------------------------------------
   ``+``  Addition
   ``-``  Soustraction
   ``*``  Multiplication
   ``/``  Division
   ``//`` Quotient de la division entière
   ``%``  Reste de la division entière
   ``**`` Elever à la puissance
   ====== ===============================

Les flottants
~~~~~~~~~~~~~

Un flottant est un **nombre à virgule**.

:Exemple:

.. code:: python

   >>> type(9.80665)
   <class 'float'>

* Le type ``float`` pour les nombres à virgule flottante.

.. code:: python

   >>> g = 9.80665
   >>> round(g,2)  
   9,81
   >>> m = 25
   >>> P = m*g
   >>> print(P)
   245.16625

* La fonction ``round(x,n)`` arrondie la valeur flottante ``x`` à ``n`` chiffres après le virgule.

Les booléens
~~~~~~~~~~~~

Les valeurs ``True`` (vrai) ou ``False`` (faux).

:Exemple:

.. code:: python

   >> type(True)
   <class 'bool'>
   >>> type(False)
   <class 'bool'>

:Exemple:

.. code:: python

   >>> 3>2
   True
   >>> 3<=2
   False
   >>> 3 == 2
   False

* Les opérateurs de comparaison renvoient un booléen (``True`` ou ``False``)

   ====== =====================
   Opérateurs de comparaison
   ----------------------------
   ``>``  Strictement supérieur
   ``<``  Strictement inférieur
   ``<=`` Inférieur ou  égal
   ``>=`` Supérieur ou  égal
   ``==`` Égal à
   ``!=`` Différent de
   ====== =====================

:Exemple:


.. code:: python

   >>> True and True
   True
   >>> True and False
   False
   >>> not False
   True

* Quelques opérateurs booléens.



   =======  ===================
   Opérateurs booléens
   ----------------------------
   ``and``  ET logique
   ``or``   OU logique
   ``not``  NON logique
   =======  ===================

Les chaines de caractères
~~~~~~~~~~~~~~~~~~~~~~~~~

Les chaines de caractères sont délimitées par les caractères ``'`` ou ``"``.

:Exemple:

.. code:: python

   >>> type("Bonjour")
   <class 'str'>
   >>> ch1 = "Bonjour"
   >>> print(ch1)
   Bonjour

* Le type ``str`` pour *string* (chaine de caractères).

.. code:: python

   >>> ch2 = "Paul"
   >>> ch1 + ch2
   'BonjourPaul'
   >>> ch3 = ch1 + " " +  ch2
   >>> print(ch3)
   Bonjour Paul

* Ici l'opérateur ``+`` réalise la **concaténation** de chaines de caractères.

:Exemple:

.. code:: python

   >>> m = 50
   >>> g = 9.81
   >>> P = m*g
   >>> print('Une masse de ' + str(m) + ' kg a un poids de ' + str(P) + ' N sur Terre !')
   Une masse de 50 kg a un poids de 490.5 N sur Terre !


   

* Ici la fonction ``str()`` permet la **conversion** de tout type en chaine de caractères (``string``).

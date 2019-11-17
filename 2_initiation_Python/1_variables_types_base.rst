==========================
Variables et types de base
==========================

Qu'est-ce qu'une variable ?
---------------------------

Une variable est un **emplacement  mémoire** dans l'ordinateur prévu pour contenir des données.

.. code-block:: python

   >>> a = 3
   >>> nom = "Newton"

* Une variable est **identifiée** par un nom ;
* Le signe ``=`` permet **l'affection** d'une valeur à une variable.
* Le contenu d'une variable est **modifiable pendant l'exécution** du programme.

Affichage d'une variable
------------------------

.. code-block:: python

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

Contrairement à d'autres langage de programmation comme C/C++ (ex. Arduino), il n'est **pas nécessaire de préciser le type d'une variable** lors de sa déclaration en Python.

Les entiers
~~~~~~~~~~~

.. code-block:: python

   >>> type(10)
   <class 'int'>
   >>> a = 10
   >>> type(a)
   <class 'int'>

* La fonction ``type()`` donne le type d'une expression ou d'une variable.
* Le mot clé ``int`` pour `integer` signifie que la variable contient un entier.

.. code-block:: python

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
   Opérateurs mathématiques en Python
   --------------------------------------
   ``+``  Addition
   ``-``  Soustraction
   ``*``  Multiplication
   ``/``  Division
   ``//`` Quotient de la division entière
   ``%``  Reste de la division entière
   ``**`` Élever à la puissance
   ====== ===============================

Les flottants
~~~~~~~~~~~~~

Un flottant est un **nombre à virgule** (nombre décimal).

.. code-block:: python

   >>> type(9.80665)
   <class 'float'>

Le type ``float`` pour les nombres à virgule flottante.

.. code-block:: python

   >>> g = 9.80665
   >>> round(g,2)  
   9.81
   >>> m = 25
   >>> P = m*g
   >>> print(P)
   245.16625

La fonction ``round(x,n)`` arrondie la valeur flottante ``x`` à ``n`` chiffres après le virgule.

Les booléens
~~~~~~~~~~~~

Un booléen est un type de variable logique à deux états : vrai ou faux.

.. code-block:: python

   >>> type(True)
   <class 'bool'>
   >>> type(False)
   <class 'bool'>

Un booléen prend les valeurs ``True`` (vrai) ou ``False`` (faux).

.. code-block:: python

   >>> 3>2
   True
   >>> 3<=2
   False
   >>> 3 == 2
   False

Les opérateurs de comparaison renvoient un booléen (``True`` ou ``False``)

   ====== =====================
   Opérateurs de comparaison en Python
   ----------------------------
   ``>``  Strictement supérieur
   ``<``  Strictement inférieur
   ``<=`` Inférieur ou  égal
   ``>=`` Supérieur ou  égal
   ``==`` Égal à
   ``!=`` Différent de
   ====== =====================

.. code-block:: python

   >>> True and True
   True
   >>> True and False
   False
   >>> not False
   True

Les mots clés ``and`` et ``not`` sont des opérateurs logiques.

   =======  ===================
   Opérateurs logiques en Python
   ----------------------------
   ``and``  ET logique
   ``or``   OU logique
   ``not``  NON logique
   =======  ===================

Les chaines de caractères
~~~~~~~~~~~~~~~~~~~~~~~~~

Une chaine de caractères est un **ensemble de caractères**.

.. code-block:: python

   >>> type("Bonjour")
   <class 'str'>
   >>> ch1 = "Bonjour"
   >>> print(ch1)
   Bonjour

* Le type ``str`` pour *string* (chaine de caractères).
* Les chaines de caractères sont toujours délimitées par les caractères ``'`` ou ``"``.

.. code-block:: python

   >>> ch2 = "Paul"
   >>> ch1 + ch2
   'BonjourPaul'
   >>> ch3 = ch1 + " " +  ch2
   >>> print(ch3)
   Bonjour Paul

L'opérateur ``+`` réalise la **concaténation** de chaines de caractères.

.. code-block:: python

   m = 50
   >>> g = 9.81
   >>> P = m*g
   >>> reponse = 'Une masse de ' + m + ' kg a un poids de ' + P + ' N sur Terre !'
   Traceback (most recent call last):
     File "<stdin>", line 1, in <module>
   TypeError: can only concatenate str (not "int") to str
   >>> reponse = 'Une masse de ' + str(m) + ' kg a un poids de ' + str(P) + ' N sur Terre !'
   >>> reponse
   'Une masse de 50 kg a un poids de 490.5 N sur Terre !'

* Il n'est pas possible de concaténer des chaines de caractères avec d'autres types !
* La fonction ``str()`` permet la **conversion** de tout type en chaine de caractères (``string``).

.. code-block:: python

   >>> m = 50
   >>> g = 9.81
   >>> P = m*g
   >>> print('Une masse de ', m, ' kg a un poids de ', P, ' N sur Terre !')
   Une masse de  50  kg a un poids de  490.5  N sur Terre !

* La fonction ``print()`` permet l'affichage de tout type en texte.
* Les différents types sont séparés par une virgule ``,``.
* A l'affichage, un espace est ajouté pour chaque virgule.

Saisir le contenu d'une variable
--------------------------------

En python, il est possible de demander à l'utilisateur du programme de saisir un texte au clavier.

.. code-block:: python

   >>> rep = input()
   Bonjour
   >>> rep
   'Bonjour'

* La fonction ``input()`` renvoie la chaine de caractères saisie au clavier par l'utilisateur.
* Le chaine de caractère est affectée à la variable ``rep``.

.. code-block:: python

   >>> mon = input('Quel est votre nom ? ')
   Quel est votre nom ? David
   >>> mon
   'David'

Il est possible d'ajouter un texte lors de la saisie par l'utilisateur.

.. code-block:: python

   >>> n = input('Entrer un entier : ')
   Entrer un entier : 5
   >>> n
   '5'
   >>> n*3
   '555'

Attention, la fonction ``input()`` en **renvoie qu'une chaine de caractères** !

.. code-block:: python

   >>> rep = input('Entrer un entier : ')
   Entrer un entier : 5
   >>> rep
   '5'
   >>> n = int(rep)
   >>> n
   5
   >>> n*3
   15

La fonction ``int()`` convertit nombre entier sous la forme d'une chaine de caractères en type entier.

.. code-block:: python

   >>> n = int(input('Entrer un entier : '))
   Entrer un entier : 5
   >>> n
   5
   >>> n*3
   15


Il est possible de combiner les fonctions ``int()`` et ``input()`` sur la même ligne.

.. note::

   De la même manière, la fonction ``float()`` permet la conversion en type flottant.

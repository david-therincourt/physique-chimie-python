=====================
Introduction à Python
=====================

Qu'est-ce que Python ?
======================

Créer en 1991 par Guido van Rossum, Python est un langage de programmation très proche du langage algorithme (langage naturel). Cette particularité fait de Python un langage simple à apprendre et à utiliser. Performant, multiplateforme et sous licence libre, il est devenu le langage le plus utilisé au monde (devant C, C++, JAVA, ...) aussi bien dans l'éducation, la recherche et l'industrie.

L'environnement Python est très riche. En plus du langage de base, il existe une multitudes de **librairies** (modules) qui lui ajoutent des fonctionnalités dans des domaines très variés. Par exemple, avec les trois modules **Numpy**, **Matplotlib** et **Scypi**, Python est devenu une sérieuse alternative à des langages scientifiques comme Matlab ou Scilab.

Python 3.7 est la dernière version stable.

.. warning::
    Il y eu quelques changements notables au passage de Python 2 à Python 3, ce qui fait que ces deux versions ne sont pas compatibles.



Quelle distribution Python choisir ?
====================================

Il existe une multitude de distribution Python : Anaconda, WinPython, Portable Python, Tiny Python, ...





**Anaconda Python** reste le choix le plus judicieux pour plusieurs raisons :

    * multiplateforme (Windows, Linux, Mac OSX) ;
    * complet (bibliothèque étoffée) ;
    * possède des outils performants (l'éditeur Spyder et bien d'autres).



.. image:: images/anaconda_logo-1024x512.png
   :width: 1024 px
   :height: 512px
   :scale: 30 %
   :alt: alternate text
   :align: center

`<https://www.anaconda.com/distribution/>`_

Programmer Python en ligne :

https://www.onlinegdb.com/online_python_compiler

Présentation d'Anaconda Python
==============================

Anaconda est livré avec l'environnement intégré de développement (IDE) **Spyder**.


.. image:: images/spyder_fenetre.png
   :width: 1067 px
   :height: 812px
   :scale:  60 %
   :alt: alternate text
   :align: center

L'outil **Spyder** est composé de plusieurs fenêtres dont les deux suivantes :

   * une **console** IPython (en bas à droite) dans laquelle les instructions Python vont être interprétées ;
   * un **éditeur** de texte (à gauche) dans lequel les instructions sont écrites puis enregistrées avec l'extension ``.py``. Ce type de fichier s'appelle un **script** Python.



Premier pas
===========

.. Un programme Python est une suite d'instructions écrites dans une syntaxe qui lui est propre.

Voici une première instruction Python :

.. code:: python

   print('Bonjour')


Cette instruction peut-être exécutée de deux façons.



Directement dans la console
---------------------------

.. image:: images/spyder_fenetre_console.png
   :width:  467 px
   :height: 284 px
   :scale:  100 %
   :alt: alternate text
   :align: center

* La console (**interpréteur**) choisie dans Spyder est IPython.

* ``In [1]:`` est une entrée numérotée  de la console.

* ``Out[1]:`` est la sortie donnant le résultat de l'interprétation de l'entrée ``In[1]:``.

.. note::
   Cette technique est pratique pour faire des tests d'instruction(s) ou pour débugger un programme.


A partir d'un script
--------------------



.. image:: images/spyder_fenetre_editeur.png
   :width:  492 px
   :height: 263 px
   :scale:  100 %
   :alt: alternate text
   :align: center

* Les instructions Python sont écrites séquentiellement dans un **fichier texte**.
* Ce type  de fichier enregistré avec l'extension ``.py`` est appelé **script** Python.
* Le script sera exécuté dans la console IPython à partir du menu ``Exécution > Exécution`` ou en appuyant sur la touche ``F5`` du clavier.

.. note::
   Un script sera préféré pour élaborer un programme Python.










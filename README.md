# Test stage 20233AGENC002
Ce dépôt Git a été créé dans le cadre d’un test de stage de développeur backend. Il consiste en une succession d'étapes permettant la communication avec une base de données afin de retranscrire les informations présentes dans celle-ci.
## Objectif :
Ce test a pour objectif de mettre en pratique les connaissances et compétences du postulant sur le développement d’application dorsale (backend).
## Tâche :
Le dépôt comprend les fichiers ainsi que les étapes nécessaires afin d’accomplir la tâche suivante : Créer une application dorsale en Python en utilisant le cadre d’application Flask exposant une interface de programmation.
## Étape 1 : Création du dépôt Git
Ce fichier README a été créé et mis à jour suite à la finalisation du projet.
## Étape 2 : Installation des bibliothèques
Pour réaliser ce travail, j’ai installer les bibliothèques nécessaires tel que flask, psycopg2 et dotenv. Pour cela il faut effectuer les commandes suivantes dans le terminal du projet :
*	pip install flask
*	pip install psycopg2
*	pip install python-dotenv
  
Flask correspond au cadre d’application spécifié pour ce test, psycopg2 est nécessaire pour la connexion à la base de données PostgreSQL et dotenv permet d’accéder aux données présentes dans le ficher .env comportant les informations de connexion.
## Étape 3 : connexion à la base de données
La connexion est réalisée via une méthode de la bibliothèque psycopg2. Elle prend en paramètres les différentes informations de connexion présentes dans le fichier .env (host, port, user, password et name).

## Étape 4 : Requête et résultat
La route de l’app prend en compte le topn afin d’adapté la requête. Suite à la connexion et le placement du curseur, on fait la requête où l’on récupère le score et les information de la table crawl des topn éléments via entity_id lié au score. Après avoir été classés, les résultats sont stockés dans une variable qui va être découpée pour ne garder que les informations désirées. Cette variable finale est enfin retournée sur notre app flask en JSON.

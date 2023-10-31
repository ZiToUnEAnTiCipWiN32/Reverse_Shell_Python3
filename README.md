# Reverse Shell Python3

## Projet Obfuscation/Déobfuscation de Scripts

Ce projet contient trois scripts Python conçus pour générer, obfusquer et déobfusquer un script modèle. Chaque script a un objectif spécifique dans le processus d'obfuscation et de déobfuscation .

### 1. Générateur de Script Modèle (`generateur_script_modele.py`)

Ce script a pour but de générer un script modèle, l'enregistrer localement et l'exécuter. Il établit une connexion réseau avec un serveur distant, permet d'exécuter des commandes à distance.

### Fonctionnalités

- **Génération du Script Modèle :** Le script génère un modèle de script en Python avec des fonctionnalités spécifiques pour la connexion à un serveur distant.
- **Connexion au Serveur :** Il tente de se connecter à un serveur distant à l'adresse "127.0.0.1" sur le port "1234".
- **Exécution de Commandes à Distance :** Le script permet d'exécuter des commandes à distance sur le serveur connecté.
- **Suppression de Fichiers Locaux :** Le script supprime des fichiers locaux en fonction de certains critères.

### 2. Obfuscateur de Script (`obfuscate_script.py`)

L'objectif de ce script est d'obfusquer le contenu du script modèle. Il utilise un mécanisme de décalage de caractères pour modifier le script modèle et ajouter une couche d'obfuscation.

### Fonctionnalités

- **Génération de Valeurs Aléatoires :** Le script génère des valeurs aléatoires pour un décalage de caractères.
- **Lecture du Script Modèle :** Le script lit le contenu du script modèle à obfusquer.
- **Obfuscation du Script :** Il applique un mécanisme d'obfuscation en modifiant le script modèle avec des décalages de caractères.
- **Mise à Jour du Script de Déobfuscation :** Il met à jour le script de déobfuscation avec la nouvelle version obfusquée du script modèle.

### Notes Additionnelles

- Ce script nécessite l'existence du fichier `generateur_script_modele.py` pour lire et obfusquer son contenu. Veuillez vous assurer que ce fichier est présent dans le même répertoire que le script d'obfuscation.

### 3. Déobfuscateur de Script (`deobfuscate_script.py`)

Ce script a pour but de déobfusquer un script modèle obfusqué. Il restaure le contenu original du script à partir de sa version obfusquée en utilisant une méthode de décalage de caractères.

### Fonctionnalités

- **Recherche de Nombres Premiers :** Le script effectue une recherche de nombres premiers dans une plage spécifiée.
- **Déobfuscation du Script :** Il restaure le contenu original du script modèle à partir de sa version obfusquée, utilisant une méthode de décalage de caractères.
- **Enregistrement du Modèle Déobfusqué :** Il enregistre le modèle déobfusqué dans un nouveau fichier dans le répertoire courant.
- **Exécution du Modèle Déobfusqué :** Une fois le modèle déobfusqué créé, le script l'exécute en fonction du système d'exploitation.

### Notes Additionnelles

- Le script nécessite l'existence du fichier obfusqué du script modèle pour le restaurer. Assurez-vous d'avoir préalablement obfusqué le script avant d'utiliser ce déobfuscateur.

### Avertissement

Ces scripts sont destinés à des fins éducatives ou de recherche pour démontrer les concepts d'obfuscation et de déobfuscation de scripts. L'utilisation inappropriée ou non autorisée peut être illégale. Assurez-vous d'avoir l'autorisation adéquate avant d'utiliser ces scripts.

![POC](Screenshot_1.png)

[POC](https://youtu.be/_92vQwMH-Ak)
Explications :
Fonction scan_ip : Essaie de se connecter à une adresse IP sur un port donné (par défaut 80). Si la connexion réussit, l'hôte est actif.

Fonction scan_network : Scanne une plage d'adresses IP (par exemple, 192.168.1.1 à 192.168.1.255) en utilisant des threads pour accélérer le processus.

Threads : Utilisés pour paralléliser les scans et réduire le temps d'exécution.

Résultat : Liste les adresses IP actives trouvées sur le réseau.

Prérequis :
Python 3.x installé.

Exécutez ce script avec des privilèges administrateur si nécessaire (sur certains systèmes).

Remplacez network par le préfixe de votre réseau local (par exemple, "192.168.0" ou "10.0.0").

Utilisation :
Sauvegardez le code dans un fichier, par exemple scan80.py

Exécutez-le avec : python scan80.py

Attendez les résultats. Le script affiche les appareils détectés.

Limitations :
Ce scanner est basique et ne détecte que les appareils répondant sur le port spécifié (par défaut 80).



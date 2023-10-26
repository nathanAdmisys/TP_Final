# TP_Final

# TP de fin de formation

Le but de ce TP est de consolider toutes les notions vues depuis le niveau 1

## Définition du besoin

Nous avons à notre disposition une application python utilisant flask à déployer sur nos deux machines.

Cette application est plutôt simple, il s'agit d'une application web écrite en flask.

## Reset des VMs

Afin de n'avoir aucune interférence, nous allons réinitialiser les machines 1 et 2

Dans le dossier de machine1 et machine2, lancer les 2 commandes suivantes :

```
vagrant destroy -f
vagrant up --provision
```

## Analyse des fichiers fournis

Etudier le code de l'application python dans le dossier my-app.

Etudier le fichier de service fourni.

## Ecriture du playbook

Ecrire le playbook avec les 6 tâches suivantes : 

* On s'assure que les dépendances soient installées (python3-flask)
* On s'assure que /home/vagrant/my-app est bien un dossier
* On s'assure que le fichier app.py soit bien présent dans /home/vagrant/m-app/
* On s'assure que le fichier my-app.service soit bien dans /etc/systemd/system/
* On s'assure de recharger systemd
* On s'assure que le service my-app soit démarré.

Pour écrire ce playbook, voici la liste des modules nécessaires

- package
- file
- copy
- systemd
- service

## Création d'un template de job

Dans AWX, créer le projet et le template pour exécuter ce playbook.

Lancer le job depuis l'interface pour vérifier que tout fonctionne.

Le serveur flask doit écouter sur le port 8080, vérifier depuis votre navigateur que l'application fonctionne.

## Lancement du template depuis AWX KIT

Ecrire les commandes awx pour lancer et monitorer le déploiement.



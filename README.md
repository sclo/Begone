# Begone — Liste de blocage — France

## Prérequis

Avant de commencer, assurez-vous d'avoir installé l'application
[Begone][begone] sur votre iPhone. Une fois l'application installée, lancez-la
et suivez les instructions pour l'activer comme application de blocage d'appels
sur iOS.

## Installation

Ouvrez cette page sur votre iPhone et suivez les instructions ci-dessous :

> [!IMPORTANT]
> [**fr-all.xml**](https://raw.githubusercontent.com/danroc/begone-fr-list/refs/heads/main/dist/fr-all.xml)

1. Installez l'application [Begone](https://apps.apple.com/fr/app/id1596818195)
   sur votre iPhone.

2. Appouyez et maintenez le lien `fr-all.xml` ci-dessus et sélectionnez
   **Télécharger le fichier lié**.

3. Ouvrez l'application Begone et sélectionnez **Importer de nouveaux
   numéros**.

4. Sélectionnez **Fichiers**.

5. Importez le fichier `fr-all.xml` que vous venez de télécharger.

## Contribution

### Configurer l'environnement de développement

1. Créez un nouvel environnement virtuel Python.

   ```bash
    python3 -m venv venv
    ```

2. Activez l'environnement virtuel.

    ```bash
     source venv/bin/activate
     ```

3. Installez les dépendances nécessaires.

    ```bash
    pip install -r requirements.txt
    ```

### Ajouter de nouveaux numéros à la liste de blocage

1. Mettez à jour le fichier `data/numbers.yaml` avec les nouveaux numéros que
   vous souhaitez bloquer.

2. Exécutez `make` pour générer le nouveau fichier `dist/fr-all.xml`.

[begone]: https://apps.apple.com/fr/app/id1596818195

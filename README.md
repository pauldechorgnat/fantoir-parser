# FANTOIR parser

Ce repository contient un fichier pour extraire les données du **Fichier ANnuaire TOpographique Initialisé Réduit** (FANTOIR). En effet, le format de ce fichier n'est pas le plus classique et la documentation peut être un peu complexe.

## Description des fichiers

- `fantoir_parser.py`: fichier utilisé pour parser le fichier FANTOIR1022
- `utils.py`: fichier contenant les fonctions utilisées dans `fantoir_parser.py`
- `files`:
    - `Descriptif ...`: fichier de documentation du FANTOIR dont sont issues les fichiers de référence (au format json) ainsi que les règles de parsing du fichier.
- `data`:
    - `code_voie_references.json`: référence pour les nature de voies qui sont encodées sur quelques caractères (`AV` -> `AVENUE`)
    - `type_voie_references.json`: référence pour les types de voies
    - `libelle_voies.csv`: fréquences calculées par mes soins des libellés des voies (hors lieu-dit et ensembles immobiliers)
    - `type_voies.csv`: fréquences calculeées par mes soins des natures des voies (incluant les lieu-dits)

- `notebooks`:
    - `01_analysis.ipynb`: contient le code utilisé pour calculer les fichiers de fréquences des libellés et des natures des voies.

## Utilisation de `fantoir_parser.py`

Le fichier `fantoir_parser` permet de récupérer les informations principales contenues dans un fichier FANTOIR. **Attention**, le code n'a été testé que sur le fichier datant de novembre 2022. Il vous faut en premier lieu télécharger le fichier depuis la page d'[OpenDataGouv](https://www.data.gouv.fr/fr/datasets/fichier-fantoir-des-voies-et-lieux-dits/).

```sh
python3 fantoir_parser.py \
 --input-file data/FANTOIR1022 \
 --output-file data/parsed_{object_type}.json \
 --limit 10000 \
 --departements \
 --communes \
 --voies \
 --verbose 

```

On peut afficher l'aide avec `python3 fantoir_parser.py --help` mais je redonne ici la signification des différents arguments:

- `-i INPUT_FILE` ou `--input-file INPUT_FILE`: nom du fichier FANTOIR
- `-o OUTPUT_FILE` ou `--output-file OUTPUT_FILE`: nom des fichiers dans lesquels seront stockés les objets parsés (on pourra utiliser un `{object_type}` pour générer automatiquement les noms en fonction des objets).
- `--departements`: si précisé, le script parsera les départements (directions)
- `--communes`: si précisé, le script parsera les communes
- `--voies`: si précisé, le script parsera les voies
- `-l LIMIT` ou `--limit LIMIT`: permet de limiter le nombre d'objets parsés
- `-v` ou `--verbose`: si précisé, des informations sont imprimées dans la sortie standard

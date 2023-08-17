import csv


def get_data(
    string: str,
    reference: list[dict],
    include_keys: bool = True,
):
    data = {}
    for feature in reference:
        data[feature["name"]] = string[
            feature["start"] - 1 : feature["end"] 
        ].strip()
    if include_keys:
        return data
    return list(data.values())


def write_data(
    path: str,
    data: dict,
    keys: list,
):
    with open(path, "w", encoding="utf-8") as file:
        csv_writer = csv.writer(
            file,
            delimiter=",",
            escapechar="\\",
            quotechar='"',
        )
        csv_writer.writerow(keys)
        csv_writer.writerows(data)


COMMUNES_REFERENCE = [
    {
        "start": 1,
        "end": 2,
        "length": 2,
        "name": "Code département",
        "short_name": "code_departement",
    },
    {
        "start": 3,
        "end": 3,
        "length": 1,
        "name": "Code direction",
        "short_name": "code_direction",
    },
    {
        "start": 4,
        "end": 6,
        "length": 3,
        "name": "Code commune",
        "short_name": "code_commune",
    },
    {
        "start": 11,
        "end": 11,
        "length": 1,
        "name": "Clé RIVOLI",
        "short_name": "cle_rivoli",
    },
    {
        "start": 12,
        "end": 41,
        "length": 30,
        "name": "Libellé Commune",
        "short_name": "libelle_commune",
    },
    {
        "start": 43,
        "end": 43,
        "length": 1,
        "name": "Type de la commune",
        "short_name": "type_commune",
    },
    {
        "start": 46,
        "end": 46,
        "length": 1,
        "name": "Caractère RUR",
        "short_name": "caractere_rur",
    },
    {
        "start": 50,
        "end": 50,
        "length": 1,
        "name": "Caractère de population",
        "short_name": "caractere_population",
    },
    {
        "start": 53,
        "end": 59,
        "length": 7,
        "name": "Population réelle",
        "short_name": "population_reelle",
    },
    {
        "start": 60,
        "end": 66,
        "length": 7,
        "name": "Population à part",
        "short_name": "population_a_part",
    },
    {
        "start": 67,
        "end": 73,
        "length": 7,
        "name": "Population fictive",
        "short_name": "population_fictive",
    },
    {
        "start": 74,
        "end": 74,
        "length": 1,
        "name": "Caractère d’annulation",
        "short_name": "caractere_annulation",
    },
    {
        "start": 75,
        "end": 81,
        "length": 7,
        "name": "Date d’annulation",
        "short_name": "date_annulation",
    },
    {
        "start": 82,
        "end": 88,
        "length": 7,
        "name": "Date de création de l’article",
        "short_name": "date_creation",
    },
]

VOIES_REFERENCE = [
    {
        "start": 1,
        "end": 2,
        "length": 2,
        "name": "Code département",
        "short_name": "code_departement",
    },
    {
        "start": 3,
        "end": 3,
        "length": 1,
        "name": "Code direction",
        "short_name": "code_direction",
    },
    {
        "start": 4,
        "end": 6,
        "length": 3,
        "name": "Code commune",
        "short_name": "code_commune",
    },
    {
        "start": 7,
        "end": 10,
        "length": 4,
        "name": "Identifiant de la voie dans la commune",
        "short_name": "identifiant_voie",
    },
    {
        "start": 11,
        "end": 11,
        "length": 1,
        "name": "Clé RIVOLI",
        "short_name": "cle_rivoli",
    },
    {
        "start": 12,
        "end": 15,
        "length": 4,
        "name": "Code nature de voie",
        "short_name": "code_nature_voie",
    },
    {
        "start": 16,
        "end": 41,
        "length": 26,
        "name": "Libellé voie",
        "short_name": "libelle_voie",
    },
    {
        "start": 43,
        "end": 43,
        "length": 1,
        "name": "Type de la commune N : rurale, R : recensée",
        "short_name": "type_commune",
    },
    {
        "start": 46,
        "end": 46,
        "length": 1,
        "name": "Caractère RUR 3 : pseudo-recensée, blanc sinon",
        "short_name": "caractere_rur",
    },
    {
        "start": 49,
        "end": 49,
        "length": 1,
        "name": "Caractère de voie",
        "short_name": "caractere_voie",
    },
    {
        "start": 50,
        "end": 50,
        "length": 1,
        "name": "Caractère de population",
        "short_name": "caractere_population",
    },
    {
        "start": 60,
        "end": 66,
        "length": 7,
        "name": "Population à part",
        "short_name": "population_a_part",
    },
    {
        "start": 67,
        "end": 73,
        "length": 7,
        "name": "Population fictive",
        "short_name": "population_fictive",
    },
    {
        "start": 74,
        "end": 74,
        "length": 1,
        "name": "Caractère d’annulation",
        "short_name": "caractere_annulation",
    },
    {
        "start": 75,
        "end": 81,
        "length": 7,
        "name": "Date d’annulation",
        "short_name": "date_annulation",
    },
    {
        "start": 82,
        "end": 88,
        "length": 7,
        "name": "Date de création de l’article",
        "short_name": "date_annulation",
    },
    {
        "start": 104,
        "end": 108,
        "length": 5,
        "name": "Code identifiant MAJIC de la voie",
        "short_name": "code_identifiant_majic",
    },
    {
        "start": 109,
        "end": 109,
        "length": 1,
        "name": "Type de voie",
        "short_name": "type_voie",
    },
    {
        "start": 110,
        "end": 110,
        "length": 1,
        "name": "Caractère du lieu-dit",
        "short_name": "caractere_lieu_dit",
    },
    {
        "start": 113,
        "end": 120,
        "length": 8,
        "name": "Dernier mot entièrement alphabétique du libellé de la voie",
        "short_name": "dernier_mot",
    },
]


DEPARTEMENTS_REFERENCE = [
    {
        "start": 1,
        "end": 2,
        "length": 2,
        "name": "Code département",
        "short_name": "code_departement",
    },
    {
        "start": 3,
        "end": 3,
        "length": 1,
        "name": "Code direction",
        "short_name": "code_direction",
    },
    {
        "start": 12,
        "end": 41,
        "length": 30,
        "name": "Libellé Direction",
        "short_name": "libelle_direction",
    },
]

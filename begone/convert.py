import plistlib
import re
from typing import Annotated

import requests
import typer
import yaml

app = typer.Typer()

TagGroups = dict[str, list[dict[str, str]]]

ALL_GROUP_TAG = "all"

CATEGORY_BLOCKED = "0"
CATEGORY_ALLOWED = "1"
CATEGORY_DIRECTORY = "2"

def extract_common_beginning(tranche_debut, tranche_fin):
    # Trouver la longueur de la partie commune au début
    common_length = 0
    for i in range(min(len(tranche_debut), len(tranche_fin))):
        if tranche_debut[i] == tranche_fin[i]:
            common_length += 1
        else:
            break

    # Extraire la partie commune et ajouter des dièses pour le reste
    common_part = tranche_debut[:common_length]
    formatted_tranche = common_part + '#' * (len(tranche_debut) - common_length)

    # Remplacer le premier '0' par '+33'
    if formatted_tranche.startswith('0'):
        formatted_tranche = '+33' + formatted_tranche[1:]

    return formatted_tranche

def get_numbers_from_arcep(mnemo: str) -> list[str]:
    resource_id = "90e8bdd0-0f5c-47ac-bd39-5f46463eb806"
    url = f"https://tabular-api.data.gouv.fr/api/resources/{resource_id}/data/?Mn%C3%A9mo__exact={mnemo}"

    all_formatted_numbers = []

    while url:
        response = requests.get(url)
        data = response.json()

        # Extraire et formater les tranches
        formatted_numbers = [
            extract_common_beginning(entry["Tranche_Debut"], entry["Tranche_Fin"])
            for entry in data["data"]
        ]

        all_formatted_numbers.extend(formatted_numbers)

        # Mettre à jour l'URL pour la page suivante
        url = data["links"].get("next")

    return all_formatted_numbers

def sanitize_number(number: str) -> str:
    return re.sub(r"[^+0-9#]", "", number)


def load_numbers(input_file: str) -> TagGroups:
    with open(input_file) as f:
        entries = yaml.safe_load(f)

    groups: TagGroups = {}
    for entry in entries:
        group = []
        for number in entry.get("numbers", []):
            group.append({
                "title": entry["title"],
                "addNational": "true",
                "category": CATEGORY_BLOCKED,
                "number": sanitize_number(number),
            })

        for asn in entry.get("asn", []):
            for number in get_numbers_from_arcep(asn):
                group.append({
                    "title": entry["title"],
                    "addNational": "true",
                    "category": CATEGORY_BLOCKED,
                    "number": sanitize_number(number),
                })

        for tag in entry.get("tags", []):
            if tag == ALL_GROUP_TAG:
                continue
            groups.setdefault(tag, []).extend(group)
        groups.setdefault(ALL_GROUP_TAG, []).extend(group)

    return groups


def main(
    input_file: Annotated[str, typer.Argument(help="Input YAML numbers file")],
    output_file: Annotated[str, typer.Argument(help="Output Begone XML file")],
    tags: Annotated[list[str], typer.Argument(help="Tags to include")],
) -> None:
    groups = load_numbers(input_file)
    output = []
    for tag in tags:
        output.extend(groups.get(tag, []))

    with open(output_file, "wb") as f:
        plistlib.dump(output, f)


def run() -> None:
    typer.run(main)


if __name__ == "__main__":
    run()

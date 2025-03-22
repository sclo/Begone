import plistlib
import re
from typing import Annotated

import requests
import typer
import yaml

app = typer.Typer()

# Type alias for the groups of tagged numbers
TagGroups = dict[str, list[dict[str, str]]]

# Constants for special tags and categories
ALL_GROUP_TAG = "all"
CATEGORY_BLOCKED = "0"

def extract_common_beginning(tranche_debut: str, tranche_fin: str) -> str:
    """Extracts the common beginning of two number ranges and formats it."""
    common_length = next((i for i, (a, b) in enumerate(zip(tranche_debut, tranche_fin)) if a != b), len(tranche_debut))
    common_part = tranche_debut[:common_length]
    formatted_tranche = common_part + '#' * (len(tranche_debut) - common_length)
    return '+33' + formatted_tranche[1:] if formatted_tranche.startswith('0') else formatted_tranche

def is_number_included(number: str, existing_ranges: set) -> bool:
    """Checks if a number is included in any of the existing ranges."""
    number = number.replace("#", "")
    return any(range_start <= number <= range_end for range_start, range_end in existing_ranges)

def fetch_numbers_from_arcep(mnemo: str) -> list[str]:
    """Fetches and formats number ranges from the ARCEP API."""
    resource_id = "90e8bdd0-0f5c-47ac-bd39-5f46463eb806"
    url = f"https://tabular-api.data.gouv.fr/api/resources/{resource_id}/data/?Mn%C3%A9mo__exact={mnemo}"
    all_formatted_numbers = []

    while url:
        response = requests.get(url)
        data = response.json()
        formatted_numbers = [extract_common_beginning(entry["Tranche_Debut"], entry["Tranche_Fin"]) for entry in data["data"]]
        all_formatted_numbers.extend(formatted_numbers)
        url = data["links"].get("next")

    return all_formatted_numbers

def sanitize_number(number: str) -> str:
    """Sanitizes a number by removing unwanted characters."""
    return re.sub(r"[^+0-9#]", "", number)

def process_entry_numbers(entry: dict, existing_ranges: set) -> list[dict[str, str]]:
    """Processes numbers from a single entry."""
    group = []
    for number in entry.get("numbers", []):
        sanitized_number = sanitize_number(number)
        if not is_number_included(sanitized_number, existing_ranges) :
            group.append({
                "title": entry["title"],
                "addNational": "true",
                "category": CATEGORY_BLOCKED,
                "number": sanitized_number,
            })
            existing_ranges.add((sanitized_number.replace("#", "0"), sanitized_number.replace("#", "9")))
    return group

def process_entry_asn(entry: dict, existing_ranges: set) -> list[dict[str, str]]:
    """Processes ASN numbers from a single entry."""
    group = []
    for asn in entry.get("asn", []):
        for number in fetch_numbers_from_arcep(asn):
            sanitized_number = sanitize_number(number)
            if len(sanitized_number) > 4 and not is_number_included(sanitized_number, existing_ranges):
                group.append({
                    "title": entry["title"],
                    "addNational": "true",
                    "category": CATEGORY_BLOCKED,
                    "number": sanitized_number,
                })
                existing_ranges.add((sanitized_number.replace("#", "0"), sanitized_number.replace("#", "9")))
    return group

def load_numbers(input_file: str) -> TagGroups:
    """Loads and processes numbers from a YAML file."""
    with open(input_file) as f:
        entries = yaml.safe_load(f)

    groups: TagGroups = {}
    existing_ranges = set()

    for entry in entries:
        group = process_entry_numbers(entry, existing_ranges) + process_entry_asn(entry, existing_ranges)

        for tag in entry.get("tags", []):
            if tag == ALL_GROUP_TAG:
                continue
            groups.setdefault(tag, []).extend(group)
        groups.setdefault(ALL_GROUP_TAG, []).extend(group)

    for tag, group in groups.items():
        group.sort(key=lambda x: (x["title"], x["number"]))

    return groups

def main(
        input_file: Annotated[str, typer.Argument(help="Input YAML numbers file")],
        output_file: Annotated[str, typer.Argument(help="Output Begone XML file")],
        tags: Annotated[list[str], typer.Argument(help="Tags to include")],
) -> None:
    """Main function to process numbers and save them to an output file."""
    groups = load_numbers(input_file)
    output = [item for tag in tags for item in groups.get(tag, [])]

    with open(output_file, "wb") as f:
        plistlib.dump(output, f)

def run() -> None:
    typer.run(main)

if __name__ == "__main__":
    run()

import plistlib
from typing import Annotated

import typer
import yaml

app = typer.Typer()

CATEGORY_BLOCK = "0"


def sanitize_number(number: str) -> str:
    return number.replace(" ", "").replace("-", "").replace(".", "")


TagGroups = dict[str, list[dict[str, str]]]

ALL_GROUP_TAG = "all"


def load_numbers(input_file: str) -> TagGroups:
    with open(input_file) as f:
        entries = yaml.safe_load(f)

    groups: TagGroups = {}
    for entry in entries:
        group = []
        for number in entry["numbers"]:
            group.append({
                "title": entry["title"],
                "addNational": "true",
                "category": CATEGORY_BLOCK,
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
    entries = [entry for tag in tags for entry in groups.get(tag, [])]
    with open(output_file, "wb") as f:
        plistlib.dump(entries, f)


if __name__ == "__main__":
    typer.run(main)

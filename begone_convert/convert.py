import plistlib

import typer
import yaml

app = typer.Typer()


def main(input_file: str, output_file: str) -> None:
    with open(input_file) as f:
        entries = yaml.safe_load(f)

    plist = []
    for entry in entries:
        for number in entry['numbers']:
            plist.append({
                'title': entry['title'],
                'addNational': 'true',
                'category': '0',
                'number': number.replace(' ', ''),
            })

    with open(output_file, 'wb') as f:
        plistlib.dump(plist, f)


if __name__ == '__main__':
    typer.run(main)

# Begone: Blocking List :fr:

This repository contains blocking lists of unwanted numbers for France,
to be used with the [Begone][begone-app] application on iOS.

## Prerequisites

Before you begin, ensure you have installed the [Begone][begone-app]
application on your iPhone. Once the application is installed, launch it
and follow the instructions to activate it as a call blocking application
on iOS.

## Installation

Open [this page](#installation) on your iPhone and follow the instructions
below:

1. Long press on the link of the desired list below and select
   **Download Linked File**.

   - [Spam Numbers][list-spam] (recommended)
   - [VOIP Numbers][list-voip]
      - [OnOff Numbers][list-onoff]
      - [Ubicentrex Numbers][list-ubicentrex]
      - [Aircall Numbers][list-aircall]
      - [BJT Partners Numbers][list-bjt]
      - [Kavkom Numbers][list-kavkom]
   - [Prepaid Numbers][list-prepaid]
     - [Lyca Numbers][list-lyca]
   - [Complete List][list-all]

2. Open the Begone application and select **Import New Numbers**.

3. Select **Files**.

4. Import the file you just downloaded.

## Contribution

### Setting Up the Development Environment

1. Create a new Python virtual environment and install the necessary
   dependencies.

   ```bash
   uv venv
   uv sync
   # or run 'make init'
   ```

2. Activate the virtual environment.

   ```bash
   source .venv/bin/activate
   ```

### Adding New Numbers to the Blocking List

1. Update the `data/numbers.yaml` file with the new numbers you wish to block.

2. Run `make` to generate the new lists in the `dist` folder.

[begone-app]: https://apps.apple.com/fr/app/id1596818195
[list-all]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-tout.xml
[list-spam]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-demarchage.xml
[list-voip]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-voip.xml
[list-onoff]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-onoff.xml
[list-ubicentrex]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-ubicentrex.xml
[list-aircall]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-aircall.xml
[list-bjt]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-bjt.xml
[list-kavkom]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-kavcom.xml
[list-prepaid]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-prepaid.xml
[list-lyca]: https://raw.githubusercontent.com/Fluyd-Cloud/Begone/refs/heads/main/dist/begone-fr-lyca.xml
# Begone — French numbers blocklist

## Installation

Open this page on your iPhone and follow the instructions below:

> [!IMPORTANT]
> [**fr-all.xml**](https://raw.githubusercontent.com/danroc/begone-fr-list/refs/heads/main/dist/fr-all.xml)

1. Touch and hold the `fr-all.xml` link above and select **Download Linked File**.

2. Open the Begone app and select **Import New Numbers**.

3. Select **Files**.

4. Import the `fr-all.xml` file you just downloaded.

## Contributing

### Set up the development environment

1. Create a new Python virtual environment.

   ```bash
    python3 -m venv venv
    ```

2. Activate the virtual environment.

    ```bash
     source venv/bin/activate
     ```

3. Install the required dependencies.

    ```bash
    pip install -r requirements.txt
    ```

### Add new numbers to the blocklist

1. Update the `data/numbers.yaml` file with the new numbers you want to block.
2. Run `make` to generate the new `dist/fr-all.xml` file.

import os
import tomli
import sys

# Gets the absolute path of the config.toml file
current_dir = os.path.dirname(__file__)
config_path = os.path.join(current_dir, 'config.toml')

try:
    # Opens the TOML file in binary mode
    with open(config_path, 'rb') as f:
        config = tomli.load(f)
    print("TOML file loaded successfully!")
except FileNotFoundError:
    print(f"Error: The file '{config_path}' was not found.")
    print("Please make sure the config.toml file exists in the correct directory.")
    sys.exit(1)
except tomli.TOMLDecodeError as e:
    print(f"Error: Failed to parse TOML file: {e}")
    print("Please ensure the file is correctly formatted according to the TOML specification.")
    sys.exit(1)
except Exception as e:
    print(f"Unexpected error while loading the TOML file: {e}")
    sys.exit(1)

# Checks if the 'observationSource' field is present and prints it
observation_source = config.get("observationSource")
if observation_source:
    print("Content of 'observationSource':")
    print(observation_source)
else:
    print("Error: Field 'observationSource' not found in the TOML file.")
    print("Please add an 'observationSource' entry in config.toml.")
    sys.exit(1)


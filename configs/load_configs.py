import yaml
import os


class Configs:
    """Represents a configuration object."""

    def __init__(self, data):
        """Initializes the Config object from a dictionary."""
        self.update(data)

    def update(self, data):
        """Updates the Config object with a dictionary."""
        for key, value in data.items():
            if isinstance(value, dict):
                setattr(self, key, Configs(value))  # Recursive Config creation
            else:
                setattr(self, key, value)

    def __repr__(self):
        """Provides a string representation of the Config object."""
        return str(self.__dict__)
    

def load_configs(yaml_file):
    """
    Loads a YAML file and replaces environment variables within it.

    Args:
        yaml_file (str): Path to the YAML file.

    Returns:
        dict: A dictionary representing the loaded configuration, with environment variables replaced.
    """

    def is_int(s):
        try:
            int(s)
            return True
        except ValueError:
            return False

    def replace_env_vars(data):
        """Recursively replaces environment variables in a nested data structure."""
        if isinstance(data, str):
            # Check for environment variable placeholders like ${MY_VAR}
            if "${" in data and "}" in data:
              start = data.find("${") + 2
              end = data.find("}")
              env_var_name = data[start:end]
              env_var_value = os.environ.get(env_var_name)
              if env_var_value is not None:
                if is_int(env_var_value):
                    return int(env_var_value)
                return data.replace(f"${{{env_var_name}}}", env_var_value)
              else:
                return data #return the original string if the env var doesn't exist.
            else:
                return data
        elif isinstance(data, dict):
            return {key: replace_env_vars(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [replace_env_vars(item) for item in data]
        else:
            return data
        
    with open(yaml_file, 'r') as f:
        config = yaml.safe_load(f)

    return Configs(replace_env_vars(config))

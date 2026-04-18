from pathlib import Path
from typing import Any
from classes.TireWayException import ConfigError
import yaml

class Config:
    """Loads and Reads the Config File"""

    def __init__(self, config_path:str) -> None:
        """Initializes the Config object"""
        self.config_path: str = config_path
        self.raw_config: dict[str, Any] = {}
        self._load_config()

    def _load_config(self) -> None:
        """Loads the config file and stores the data in raw_config"""

        if not Path(self.config_path).exists():
            raise ConfigError(f"Config file not found: {self.config_path}")

        with open(self.config_path, 'r') as configFile:
            self.raw_config = yaml.safe_load(configFile)
        
        if not isinstance(data, dict):
            raise ConfigError("config cant be loaded, because it is not a dict")
        
        if "location" not in data:
            raise ConfigError("config cant be loaded, because location is missing")
        
        self.raw_config = data
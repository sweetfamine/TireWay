import folium
from classes.Config import Config
from classes.OSMLoader import OSMLoader

class MapRenderer:
    """..."""
    
    def __init__(self, config: Config, loader: OSMLoader) -> None:
        self.config = config
        self.loader = loader

    def render(self) -> None:
        """Renders the map and saves it as HTML"""
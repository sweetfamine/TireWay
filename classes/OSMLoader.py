import osmnx as ox
from pathlib import Path
from classes.Config import Config
from classes.TireWayException import LoaderError
import geopandas as gpd
from networkx import MultiDiGraph

class OSMLoader:
    """ Class to load OSM data from OSMNX"""

    def __init__(self, config: Config) -> None:
        self.config: Config = config
        self.graph: MultiDiGraph | None = None              # streets as graph from osmnx
        self.edges: gpd.GeoDataFrame | None = None          # streets as table from osmnx
        self.nodes: gpd.GeoDataFrame | None = None          # notes as table from osmnx
        self._load()

    def _load(self) -> None:
        """Loads the data from OSM or from the cache file"""
        if self._cache_exists():
            self._load_from_cache()
        else:
            self._load_from_osm()
        
    def _cache_exists(self) -> bool:
        """Checks if the cache file exists"""
        return
    
    def _load_from_cache(self) -> None:
        """Loads the data from the cache file"""
        return

    def _load_from_osm(self) -> None:
        """Loads the data from OSM and saves it to the cache file"""

        try: 
            self.graph = ox.graph_from_place(
                self.config.raw_config["location"]["name"],
                network_type="drive"
            )
            
            self.nodes, self.edges = ox.graph_to_gdfs(self.graph)
        except Exception as e:
            raise LoaderError(f"Failed to load from OSM: {e}")
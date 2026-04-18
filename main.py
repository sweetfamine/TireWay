from classes.Config import Config
from classes.OSMLoader import OSMLoader

def main():
    print("Start")
    
    cfg = Config("config.yaml")
    print(f"City: {cfg.raw_config['location']['name']}")
    
    print("Loading street data from OSM...")
    loader = OSMLoader(cfg)
    
    print(f"intersections: {len(loader.nodes)}")
    print(f"streets: {len(loader.edges)}")

if __name__ == "__main__":
    main()

import yaml
from pprint import pprint

with open("docker-compose.yml", "r") as stream:
    try:
        pprint(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)

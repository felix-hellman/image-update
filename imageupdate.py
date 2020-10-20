import yaml
import sys


path = sys.argv[1]
tag = sys.argv[2]

with open(path, "r") as file:
    deployment = yaml.load(file, Loader=yaml.FullLoader)
    image = deployment['items'][0]['spec']['template']['spec']['containers'][0]['image']
    split = image.split(':')
    image = split[0] + ":" + tag
    deployment['items'][0]['spec']['template']['spec']['containers'][0]['image'] = image
    with open(path, "w") as write_file:
        yaml.dump(deployment, write_file, default_flow_style=False)



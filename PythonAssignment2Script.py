import yaml
import os
import argparse
import matplotlib.pyplot as plt
import pandas as pd

parser = argparse.ArgumentParser(description='Dataset analysis script')
parser.add_argument('--gridalpha', 
                    '-g',
                    type=float,
                    default=0.3,
                    help='float number to set for alpha')
# parser.add_argument('configfile', 
#                     type=str, 
#                     default='userconfig.yml', 
#                     help='Path to the configuration file')

args = parser.parse_args()

# print(f'Enter config file path: {args.config}')
# print(args.configfile)
# print(f'Enter grid alpha: {args.grid}')
print(args.gridalpha)

config_paths = 'userconfig.yml'
# config_paths += args.configfile

config = {}

for path in [config_paths]:
    with open(path, 'r') as f:
        this_config = yaml.safe_load(f)
        config.update(this_config)

print(config)

# print(os.environ) 
print(config['dataset'])
print(config['plot_config']['title'])

iris_data = pd.read_csv(config['dataset'])

plt.scatter(iris_data['sepal_length'], iris_data['sepal_width'],
            marker='s',
            facecolor='#fb1',
            edgecolor='k',
            label='Sepal Width')

plt.subplot().set_title(config['plot_config']['title'])
plt.subplot().set_xlabel(config['plot_config']['xlabel'])
plt.subplot().set_ylabel(config['plot_config']['ylabel'])
plt.subplot().grid(alpha=(args.gridalpha))
plt.subplot().legend()
plt.savefig('iris_scatter.png')
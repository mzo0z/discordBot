import os

paths = [
    'discord',
    'quart',
    'quart-discord',
    'requests',
    'dhooks',
]

for i in paths:
    os.system(f"pip install {i}")
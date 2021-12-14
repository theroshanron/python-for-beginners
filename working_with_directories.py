from pathlib import Path

# Absolute path is any path from root of the hard_disk whereas relative path is current path

x=Path()

print(x.exists())


for file in x.glob('*'):
    print(file)
print(x)
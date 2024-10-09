import tarfile
import os

# Path to the 102flowers.tgz file
tar_file_path = '102flowers.tgz'
extracted_dir = 'flowers_dataset\splitlowers_dataset\split'

# Extract the tar file
with tarfile.open(tar_file_path, 'r:gz') as tar:
    tar.extractall(path=extracted_dir)

print(f"Images extracted to {extracted_dir}")


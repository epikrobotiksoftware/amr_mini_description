import subprocess
from ament_index_python.packages import get_package_share_directory

pkg_dir = get_package_share_directory('amr_mini_description')
# Execute a terminal command
with open("requirements.txt", "r") as f:
    # Read the entire contents of the file
    contents = f.read()

subprocess.call(contents, shell=True)

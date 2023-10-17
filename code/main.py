import os
import subprocess

# Get the directory where main.py is located
current_dir = os.path.dirname(os.path.abspath(__file__))

# List of script filenames in the desired execution order
script_files = [
    "removebg.py",
    "overlaying.py",
    "centroid.py",
    "major_axis.py",
    "perimeter.py",
    "smallcircle.py",
    "tsurfacearea.py"
]

def run_scripts():
    for script in script_files:
        script_path = os.path.join(current_dir, script)
        subprocess.run(["python", script_path])

if __name__ == "__main__":
    run_scripts()

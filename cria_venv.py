import sys
import subprocess

if len(sys.argv) < 2:
    print("Falta 1")
    sys.exit()

env_name = sys.argv[1]

subprocess.run(["python", "-m", "venv", env_name])

print("Criou o venv")

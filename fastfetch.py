import subprocess
from pathlib import Path

script = Path(__file__).parent / "fastfetch.sh"

subprocess.run(["bash", str(script)])
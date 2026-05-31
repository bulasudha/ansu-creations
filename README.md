import os
from pathlib import Path
from zipfile import ZipFile
from textwrap import dedent

# Setup directories
current_dir = Path.cwd()
base = current_dir / "Ansu_Dimension_Premium"
base.mkdir(exist_ok=True)

assets = base / "assets"
assets.mkdir(exist_ok=True)

import shutil
from pathlib import Path

src_root = Path("/Users/ajoe01/Documents/tim/code-prep-2025")

for item in src_root.iterdir():
    if item.is_dir() and not item.name.startswith('.'):
        shutil.rmtree(item)
        print(f"Deleted folder: {item}")
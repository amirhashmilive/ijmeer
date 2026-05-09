import os
import subprocess
import sys

def install_pillow():
    print("Checking for Pillow...")
    try:
        import PIL
        print("Pillow is already installed.")
    except ImportError:
        print("Pillow not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
        print("Pillow installed successfully.")

install_pillow()

from PIL import Image

def convert_to_webp(directory):
    converted_files = []
    for root, dirs, files in os.walk(directory):
        if 'scratch' in root or '.git' in root or '.gemini' in root or 'node_modules' in root:
            continue
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                filepath = os.path.join(root, file)
                try:
                    with Image.open(filepath) as img:
                        webp_path = os.path.splitext(filepath)[0] + '.webp'
                        img.save(webp_path, 'webp')
                        converted_files.append((filepath, webp_path))
                        print(f"CONVERTED|{filepath}|{webp_path}")
                except Exception as e:
                    print(f"Error converting {filepath}: {e}")
    return converted_files

if __name__ == "__main__":
    convert_to_webp('.')

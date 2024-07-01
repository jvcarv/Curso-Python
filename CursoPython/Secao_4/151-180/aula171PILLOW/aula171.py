# Pillow: redimensionando imagens com Python
# Essa biblioteca é o Photoshop do Python 😂
from PIL import Image
from pathlib import Path

ROOT_FOLDER = Path(__file__).parent
ORIGINAL = ROOT_FOLDER / 'ceu.jpg'
IMAGE_FOLDER = ROOT_FOLDER / 'new.jpg'

pil_image = Image.open(ORIGINAL)
width, height = pil_image.size
exif = pil_image.info['exif']

# conta para que  a imagem não fique desproporcional
# width  ---- new_width
# height ---- new_height
# o resultado da conta deve ser sempre round

new_width = 640
new_height = round(height * new_width / width)


new_image = pil_image.resize(size=(new_width, new_height))
new_image.save(
    IMAGE_FOLDER,
    optimize=True,
    quality=100,
    exif=exif
)

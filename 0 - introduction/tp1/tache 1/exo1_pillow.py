from pathlib import Path
from PIL import Image

folder = Path(__file__).parent
junia = Image.open(folder/"junia.png")

box = (940, 130, 1436, 564)

junia_crop = junia.crop(box)

junia_crop.show()
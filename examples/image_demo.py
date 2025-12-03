import os
from pathlib import Path
from PIL import Image
from dataproc.images import preprocess as prep

BASE_DIR = Path(__file__).resolve().parent
OUTPUT_DIR = BASE_DIR / "output"
INPUT_PATH = BASE_DIR / "input.jpg"


def ensure_input_image(path: Path) -> None:
    if path.exists():
        return
    img = Image.new("RGB", (512, 512), color=(255, 0, 0))
    img.save(path, format="JPEG")


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    ensure_input_image(INPUT_PATH)
    img = Image.open(INPUT_PATH)

    resized = prep.resize_image(img, (256, 256))
    prep.save_image(resized, OUTPUT_DIR / "resized_256x256.jpg")

    gray = prep.grayscale_image(img)
    prep.save_image(gray, OUTPUT_DIR / "gray.jpg")

    rotated = prep.rotate_image(img, angle=45)
    prep.save_image(rotated, OUTPUT_DIR / "rotated_45.jpg")

    blurred = prep.blur_image(img, radius=2.0)
    prep.save_image(blurred, OUTPUT_DIR / "blurred.jpg")

    print("demo done: outputs saved to", OUTPUT_DIR)


if __name__ == "__main__":
    main()

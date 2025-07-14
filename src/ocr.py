from pathlib import Path
from loguru import logger
from PIL import Image
import pytesseract


def extract_text_from_image(image_path: Path) -> str:
    logger.info(f"Обработка изображения: {image_path}")

    if not image_path.exists():
        logger.error(f"Файл не найден: {image_path}")
        raise FileNotFoundError(f"{image_path} не найден")

    img = Image.open(image_path)
    text = pytesseract.image_to_string(img, lang="rus+eng")

    logger.debug(f"Распознанный текст:\n{text}")
    return text
if __name__ == "__main__":
    img_path = Path(__file__).parent.parent / "data" / "output" / "test_blueprint.png"
    extract_text_from_image(img_path)

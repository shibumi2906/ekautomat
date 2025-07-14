from pdf2image import convert_from_path
from pathlib import Path
from loguru import logger
import os

# путь к poppler
os.environ["PATH"] += os.pathsep + r"C:\tools\poppler-24.08.0\poppler-24.08.0\Library\bin"

def convert_pdf_to_png(pdf_path: Path, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    images = convert_from_path(str(pdf_path.resolve()), dpi=300)

    if not images:
        logger.error(f"Не удалось конвертировать: {pdf_path}")
        raise ValueError("Пустой PDF")

    output_path = output_dir / (pdf_path.stem + ".png")
    images[0].save(output_path, "PNG")
    logger.debug(f"Сконвертировано в PNG: {output_path}")
    return output_path

# ручной запуск
if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    pdf_path = root / "data" / "input" / "test_blueprint.pdf"
    output_dir = root / "data" / "output"
    convert_pdf_to_png(pdf_path, output_dir)




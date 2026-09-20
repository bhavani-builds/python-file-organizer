import sys
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).parent.parent / "src")
)

from organizer import get_category, get_unique_path


def test_image_category():
    file_path = Path("photo.jpg")

    assert get_category(file_path) == "Images"


def test_document_category():
    file_path = Path("resume.pdf")

    assert get_category(file_path) == "Documents"


def test_python_category():
    file_path = Path("program.py")

    assert get_category(file_path) == "Python"


def test_unknown_category():
    file_path = Path("unknown.xyz")

    assert get_category(file_path) == "Others"


def test_case_insensitive_extension():
    file_path = Path("PHOTO.PNG")

    assert get_category(file_path) == "Images"


def test_unique_path(tmp_path):
    original = tmp_path / "photo.jpg"

    original.touch()

    unique_path = get_unique_path(original)

    assert unique_path != original
    assert unique_path.name == "photo_1.jpg"

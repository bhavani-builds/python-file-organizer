from pathlib import Path
import shutil

from config import FILE_CATEGORIES


def get_category(file_path):
    extension = file_path.suffix.lower()

    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category

    return "Others"


def get_unique_path(destination):
    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )

        new_path = destination.parent / new_name

        if not new_path.exists():
            return new_path

        counter += 1


def organize_directory(directory):
    directory = Path(directory)

    if not directory.exists():
        raise FileNotFoundError(
            f"Directory not found: {directory}"
        )

    if not directory.is_dir():
        raise NotADirectoryError(
            f"Not a directory: {directory}"
        )

    moved_files = []

    for file_path in directory.iterdir():

        if not file_path.is_file():
            continue

        category = get_category(file_path)

        category_folder = directory / category
        category_folder.mkdir(exist_ok=True)

        destination = category_folder / file_path.name
        destination = get_unique_path(destination)

        shutil.move(
            str(file_path),
            str(destination)
        )

        moved_files.append({
            "file": file_path.name,
            "category": category,
            "destination": str(destination)
        })

    return moved_files

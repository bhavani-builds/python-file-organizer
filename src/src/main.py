from organizer import organize_directory


def show_results(results):
    if not results:
        print("\nNo files were found to organize.")
        return

    print("\n===== ORGANIZATION RESULTS =====")

    for result in results:
        print(
            f"{result['file']}  →  "
            f"{result['category']}"
        )

    print(f"\nTotal files organized: {len(results)}")


def main():
    print("=" * 50)
    print("          PYTHON FILE ORGANIZER")
    print("=" * 50)

    directory = input(
        "\nEnter the folder path to organize: "
    ).strip()

    if not directory:
        print("Folder path cannot be empty.")
        return

    try:
        results = organize_directory(directory)

        show_results(results)

        print("\nOrganization completed successfully!")

    except FileNotFoundError:
        print("\nError: The specified folder does not exist.")

    except NotADirectoryError:
        print("\nError: The specified path is not a folder.")

    except PermissionError:
        print("\nError: Permission denied.")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()

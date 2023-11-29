def read_file(file_path: str) -> str:
    """Читает содержимое файла.

    Args:
        file_path (str): Путь к файлу.

    Returns:
        str: Содержимое файла в виде строки.

    """
    with open(file_path, "r") as file:
        return file.read()


def save_content(file_path: str, content: str) -> None:
    """Сохраняет содержимое в файл.

    Args:
        file_path (str): Путь к файлу.
        content (str): Содержимое для сохранения.

    Raises:
        Exception: В случае ошибки при сохранении.

    """
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Content successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving content to {file_path}: {e}")

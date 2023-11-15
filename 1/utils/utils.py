def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def save_content(file_path, content):
    try:
        with open(file_path, "w") as file:
            file.write(content)
        print(f"Content successfully saved to {file_path}")
    except Exception as e:
        print(f"Error saving content to {file_path}: {e}")

import os


def get_size(file_path):
    size = os.path.getsize(file_path)
    units = ['Б', 'КБ', 'МБ']
    unit_index = 0

    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024
        unit_index += 1
    return f"{round(size)}{units[unit_index]}"


def get_sizes_in_current_folder():
    current_folder = os.getcwd()
    files = [f for f in os.listdir(current_folder) if os.path.isfile(os.path.join(current_folder, f))]

    for file in files:
        file_path = os.path.join(current_folder, file)
        size = get_size(file_path)
        print(f"{file}: {size}")


get_sizes_in_current_folder()

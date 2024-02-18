import os
import humanize


def get_dir_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            total_size += os.path.getsize(os.path.join(root, file))
    return total_size


def get_top_10_largest_dirs(path):
    dir_sizes = {}
    for root, dirs, files in os.walk(path):
        dir_sizes[root] = get_dir_size(root)

    sorted_dir_sizes = sorted(dir_sizes.items(), key=lambda x: x[1], reverse=True)
    return sorted_dir_sizes[:10]


path = input("Enter the path to the directory: ")
top_10_largest_dirs = get_top_10_largest_dirs(path)

for dir, size in top_10_largest_dirs:
    print(f"{dir} - {humanize.naturalsize(size)}")

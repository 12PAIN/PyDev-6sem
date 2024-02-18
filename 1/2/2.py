import zipfile
import humanize


def print_zip_structure(zip_file):
    with zipfile.ZipFile(zip_file) as z:
        for info in z.infolist():
            if info.is_dir():
                print(f"  {info.filename}")
            else:
                print(f"    {info.filename}  {humanize.naturalsize(info.file_size)}")


zip_file = 'files/input.zip'
print_zip_structure(zip_file)

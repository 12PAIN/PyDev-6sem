import zipfile
import json


def count_people_in_moscow(zip_file):
    count = 0
    for info in zip_file.infolist():
        if info.filename.endswith(".json"):
            with zip_file.open(info) as json_file:
                data = json.load(json_file)
            if data["city"] == "Moscow":
                count += 1
    return count


if __name__ == "__main__":
    zip_file_path = "files/jsons.zip"

    with zipfile.ZipFile(zip_file_path) as zip_file:
        count = count_people_in_moscow(zip_file)

    print(f"The number of people in Moscow is: {count}")

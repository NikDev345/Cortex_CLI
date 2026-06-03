import re
import json


def extract_info(text):

    name = None
    age = None
    city = None

    name_match = re.search(r"([A-Z][a-z]+)", text)

    if name_match:
        name = name_match.group(1)

    age_match = re.search(r"(\d+)", text)

    if age_match:
        age = int(age_match.group(1))

    city_match = re.search(r"lives in ([A-Za-z ]+)", text)

    if city_match:
        city = city_match.group(1).strip()

    result = {
        "name": name,
        "age": age,
        "city": city
    }

    return json.dumps(result, indent=4)
import requests


REQUEST_API = "http://127.0.0.1:8000/api/nx-part-requests/"
GENERATED_API = "http://127.0.0.1:8000/api/nx-generated-parts/"


def generate_from_django_api():
    response = requests.get(REQUEST_API)

    if response.status_code != 200:
        print("Failed to connect Django API")
        return

    parts = response.json()

    if len(parts) == 0:
        print("No NX part requests found")
        return

    latest_part = parts[-1]

    part_name = latest_part["part_name"]
    diameter = latest_part["diameter"]
    length = latest_part["length"]
    material = latest_part["material"]

    print("NX AUTOMATION SERVICE STARTED")
    print("-----------------------------")
    print("Part Name:", part_name)
    print("Diameter:", diameter)
    print("Length:", length)
    print("Material:", material)
    print("-----------------------------")

    generated_data = {
        "part_name": part_name,
        "nx_file": f"{part_name}.prt",
        "step_file": f"{part_name}.step",
        "pdf_file": f"{part_name}.pdf"
    }

    save_response = requests.post(GENERATED_API, json=generated_data)

    if save_response.status_code == 201:
        print("NX Model Generated Successfully")
        print("Generated Part Saved to Django Database")
    else:
        print("Generated Part Save Failed")
        print(save_response.text)


if __name__ == "__main__":
    generate_from_django_api()
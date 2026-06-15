def create_bolt(part_name, diameter, length, material):
    bolt_data = {
        "part_name": part_name,
        "diameter": diameter,
        "length": length,
        "material": material,
        "status": "NX Part Request Created"
    }

    return bolt_data
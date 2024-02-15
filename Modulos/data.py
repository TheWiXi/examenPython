import json


def dataDownload():
    with open('Modulos/datos.json', 'r') as data:
        datos = list(json.load(data))
    return datos


def dataUpload(datos: list):
    with open('Modulos/datos.json', 'w') as data:
        json.dump(datos, data, indent=4)
        input("✅✅")
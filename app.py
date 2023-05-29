from flask import Flask, request

app = Flask(__name__)

areas = [{
    'id': 1,
    'nombre': 'Marketing',
    'piso': 2
},
    {
    'id': 2,
    'nombre': 'Sistemas',
    'piso': 3
},
    {
    'id': 3,
    'nombre': 'Contabilidad',
    'piso': 1
}]

empleados = [
    {
        'id': 1,
        'nombre': 'Jose',
        'apellido': 'Rodriguez',
        'email': 'jose@gmail.com',
        'area_id': 1
    }
]

@app.route('/areas', methods=['GET'])
def devolverAreas():
    if request.method == 'GET':
        areas_existentes = []
        for area in areas:
            if area is None:
                continue
            areas_existentes.append(area)

        return {
            'message': 'Las areas son',
            'content': areas_existentes
        }


@app.route('/area', methods=['POST'])
def crearArea():
    if request.method == 'POST':
        id = len(areas) + 1
        data = request.json
        data['id'] = id
        areas.append(data)

        return {
            'message': 'Area creada exitosamente'
        }


@app.route('/area/<int:id>', methods=['GET'])
def devolverAreaId(id):
    print(id)
    resultado = None
    for area in areas:
        if area is None:
            continue
        if area['id'] == id:
            resultado = area
            break

    if resultado is None:
        return {
            'message': 'No se encontro el area a buscar'
        }

    if request.method == 'GET':
        return {
            'message': 'El area es',
            'content': resultado
        }


@app.route('/empleado', methods=['POST'])
def crearEmpleado():
    if request.method == 'POST':
        id = len(empleados) + 1
        data = request.json
        data['id'] = id
        empleados.append(data)

        return {
            'message': 'Empleado creado exitosamente'
        }


@app.route('/empleados', methods=['GET'])
def devolverEmpleados():
    if request.method == 'GET':
        empleados_existentes = []
        for empleado in empleados:
            if empleado is None:
                continue
            empleados_existentes.append(empleado)

        return {
            'message': 'Los empleados son',
            'content': empleados_existentes
        }


if __name__ == "__main__":
    app.run(debug=True)

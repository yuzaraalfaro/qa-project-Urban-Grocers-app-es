import sender_stand_request
import data


# Cambiar el valor del parámetro name en kit_body
def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

# Prueba positiva para kit_name
def positive_assert(kit_name):
    kit_body = get_kit_body(kit_name)
    kit_response = sender_stand_request.post_new_kit(kit_body)

    assert kit_response.status_code == 201

    # comprueba si el campo "name" en el cuerpo de la respuesta coincide con el campo "name" en el cuerpo de la solicitud
    assert kit_response.json()["name"] == kit_body["name"]


# Prueba negativa para error de carácteres en el nombre
def negative_assert_symbol(kit_name):
    kit_body = get_kit_body(kit_name)
    response = sender_stand_request.post_new_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "El nombre debe contener solo letras latino," \
                                         " un espacio y un guión. De 2 a 15 caracteres."


# Prueba negativa para cuando falta un parámetro
def negative_assert_no_kit_name(kit_body):

    response = sender_stand_request.post_new_kit(kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "No se han aprobado todos los parámetros requeridos"


# Prueba 1, 1 letra en el nombre
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert(data.name_one_letter)


# Prueba 2, 511 letras en el nombre

def test_create_kit_511_letters_in_name_get_success_response():
    positive_assert(data.name_511_letters)


# Prueba 3. nombre vacio
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_kit_name(kit_body)


# Prueba 4 	El número de caracteres en el nombre es mayor que la cantidad permitida (512)
def test_create_kit_512_letters_in_name_get_error_response():
    negative_assert_symbol(data.name_512_letters)


# Prueba 5, nombre con caracteres especiales
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert(data.name_special_symbol)


# Prueba 6, nombre con espacios
def test_create_kit_name_with_spaces_get_success_response():
    positive_assert(data.name_with_spaces)


# Prueba 7, números en el nombre
def test_create_kit_numbers_on_the_name_get_success_response():
    positive_assert(data.name_numbers)


# Prueba 8, parámetro vacio en la solicitud
def test_create_kit_empty_name_get_error_response():
    kit_body = get_kit_body(" ")
    negative_assert_no_kit_name(kit_body)

# Prueba 9, tipo de parámetro en name : número
def test_create_kit_number_type_in_name_get_error_response():
    kit_body = get_kit_body(123)
    response = sender_stand_request.post_new_kit(kit_body)

    assert response.status_code == 400

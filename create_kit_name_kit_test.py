import sender_stand_request
import data
# Función para obtener el token de autorización con la creación de un usuario nuevo.
def get_user_auth_token():
    # El resultado de la solicitud para crear un nuevo usuario o usuaria se guarda en la variable.
    user_response = sender_stand_request.post_new_user(data.user_body, data.headers)
    # Comprueba si el código de estado es 201.
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor.
    assert user_response.json()["authToken"] != ""
    # Se devuelve el token de autorización.
    return user_response.json()["authToken"]
# Función para obtener los headers necesarios.
def get_headers(auth_token):
    # Los headers son almacenados en la variable desde data.py.
    headers = data.headers.copy()
    # Se agrega el header de autorización.
    headers["Authorization"] = "Bearer " + str(auth_token)
    # Se devuelven los headers.
    return headers
# Función de prueba positiva
def positive_assert(kit_body):
    # El token de autorización se guarda en la variable.
    auth_token = get_user_auth_token()
    # Los headers necesarios se guardan en la variable.
    headers = get_headers(auth_token)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable.
    kit_response = sender_stand_request.post_create_kit(kit_body, headers)
    # Comprueba si el código de estado es 201.
    assert kit_response.status_code == 201
    # Comprueba que el campo name en el cuerpo coincide con el campo name del cuerpo de la solicitud.
    assert kit_response.json()["name"] == kit_body["name"]
# Función de prueba nagativa
def negative_assert(kit_body):
    # El token de autorización se guarda en la variable.
    auth_token = get_user_auth_token()
    # Los headers necesarios se guardan en la variable.
    headers = get_headers(auth_token)
    # El resultado de la solicitud para crear un nuevo kit se guarda en la variable.
    kit_response = sender_stand_request.post_create_kit(kit_body, headers)
    # Comprueba si el código de estado es 400.
    assert kit_response.status_code == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert (kit_response.json()["message"] == "No se han aprobado todos los parámetros requeridos"/
            "El nombre debe contener sólo letras latino, un espacio y un guión. De 2 a 15 caracteres")

# Prueba 1. Kit creado con éxito. El parámetro name contiene 1 carácter.
def test_create_kit_1_letter_long_name_get_success_response():
    positive_assert(data.kit_body_1_letter_long_name)

# Prueba 2. Kit creado con éxito. El parámetro name contiene 511 carácteres.
def test_create_kit_511_letters_long_name_get_success_response():
    positive_assert(data.kit_body_511_letters_long_name)

# Prueba 3. Error. El parámetro name contiene 0 carácteres.
def test_create_kit_0_letters_name_get_error_response():
    negative_assert(data.kit_body_0_letters_long_name)

# Prueba 4. Error. El parámetro name contiene 512 carácteres.
def test_create_kit_512_letters_long_name_get_error_response():
    negative_assert(data.kit_body_512_letters_long_name)

# Prueba 5. Kit creado con éxito. El parámetro name contiene carácteres especiales.
def test_create_kit_special_symbols_in_name_get_success_response():
    positive_assert(data.kit_body_special_symbols_in_name)

# Prueba 6. Kit creado con éxito. El parámetro name contiene espcios en blanco.
def test_create_kit_space_in_name_get_success_response():
    positive_assert(data.kit_body_space_in_name)

# Prueba 7. Kit creado con éxito. El parámetro name contiene carácteres numéricos.
def test_create_kit_numbers_in_name_get_success_response():
    positive_assert(data.kit_body_numbers_in_name)

# Prueba 8. Error. El parámetro name está vacio.
def test_create_kit_empty_name_get_error_response():
    negative_assert(data.kit_body_empty)

# Prueba 9. Error. El tipo del parámetro name: número.
def test_create_kit_number_type_name_get_error_response():
    negative_assert(data.kit_body_number_type_name)

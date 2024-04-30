# Proyecto Urban Grocers 
# Pruebas automatizadas para APIs con pytest: Creación de usuario y pruebas de requerimiento en el nombre de un kit

## Descripción


Se realizó el siguiente archivo utilizando todo lo anteriormente aprendido y estudiado. Primero realicé la creacion del usuario de donde se sacó el token para generar un kit.
Una vez ya creado el kit, se procedió a realizar la ejecución de 9 pruebas. Estas tenian que probar si los requerimientos mencionados en la lista de comprobación estaban correctos o de lo contrario fallaban.

  **A continuación se detallan las pruebas realizadas:**

    1. **El número permitido de caracteres (1):**
       - `kit_body = { "name": "a"}`
  
    2. **El número permitido de caracteres (511):**
       - `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a"}`
  
    3. **El número de caracteres es menor que la cantidad permitida (0):**
       - `kit_body = { "name": "" }`
  
    4. **El número de caracteres es mayor que la cantidad permitida (512):**
       - `kit_body = { "name":"El valor de prueba para esta comprobación será inferior a” }`
  
    5. **Se permiten caracteres especiales:**
       - `kit_body = { "name": ""№%@"," }`
  
    6. **Se permiten espacios:**
       - `kit_body = { "name": " A Aaa " }`
  
    7. **Se permiten números:**
       - `kit_body = { "name": "123" }`
  
    8. **El parámetro no se pasa en la solicitud:**
       - `kit_body = { }`
  
    9. **Se ha pasado un tipo de parámetro diferente (número):**
       - `kit_body = { "name": 123 }`

## Conclusiones

De las 9 pruebas realizadas, 4 pruebas fallaron mientras que las restantes se ejecutaron exitosamente. Las pruebas que fallaron fueron las siguientes:

- test_create_kit_no_name_get_error_response
- test_create_kit_512_letters_in_name_get_error_response
- test_create_kit_empty_name_get_error_response
- test_create_kit_number_type_in_name_get_error_response

En conclusión, se recomienda revisar y corregir las pruebas que fallaron para garantizar el correcto funcionamiento de la API. Es fundamental abordar las correcciones necesarias para que la API pueda operar de manera exitosa en todos los aspectos.

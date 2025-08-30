def check_vowels():
    # Código a implementar utilizando input.


    # Para verificar este ejercicio ejecutar el comando
    # `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`
    nombre = input("Ingrese su nombre: ")
    nombre = nombre.lower()
    print(f"Contiene a: {'a' in nombre or 'A' in nombre}")
    print(f"Contiene e: {'e' in nombre or 'E' in nombre}")
    print(f"Contiene i: {'i' in nombre or 'í' in nombre}")
    print(f"Contiene o: {'o' in nombre or 'O' in nombre}")
    print(f"Contiene u: {'u' in nombre or 'U' in nombre}")
check_vowels()
import random, string

caracteres = string.ascii_letters + string.punctuation + string.digits
print(caracteres)
senha = "".join(random.choices(caracteres, k=10))
print(f"A senha gerada foi: {senha}")
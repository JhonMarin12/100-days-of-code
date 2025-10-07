import random

# Amigos comiendo juntos
amigos = ["Alicia", "Juan", "Carlos", "David", "Emanuel"]
quien_paga = random.choice(amigos)

# ¿Quien debe pagar la cuenta?
print(f"La cuenta la debe pagar: {quien_paga}")

# sin usar random.choice
index_amigo = random.randint(0, len(amigos) - 1)
print(f"La cuenta la debe pagar: {amigos[index_amigo]}")

n = 3  # Número de discos
origem, destino, auxiliar = 'A', 'C', 'B'  # Nomes dos pinos

passo = 0  # Contador de passos

# Estado inicial
print(f"Estado Inicial: Peça pequena em cima, Peça média no meio, Peça grande embaixo - Pino {origem}")

# Primeiro passo: Mover a peça pequena para o pino C
origem, destino = origem, destino
print(f"Move peça pequena de {origem} para {destino}")
passo += 1

# Segundo passo: Mover a peça média para o pino B
origem, destino = origem, auxiliar
print(f"Move peça média de {origem} para {destino}")
passo += 1

# Terceiro passo: Mover a peça pequena para o pino B
origem, destino, auxiliar = destino, origem, auxiliar
print(f"Move peça pequena de {origem} para {destino}")
passo += 1

# Quarto passo: Mover a peça grande para o pino C
origem, destino = auxiliar, destino
print(f"Move peça grande de {origem} para {destino}")
passo += 1

# Quinto passo: Mover a peça média para o pino C
origem, destino, auxiliar = origem, destino, auxiliar
print(f"Move peça média de {origem} para {destino}")
passo += 1

# Sexto passo: Mover a peça pequena para o pino C
origem, destino, auxiliar = auxiliar, origem, destino
print(f"Move peça pequena de {origem} para {destino}")
passo += 1

# Estado final
print(f"\nEstado Final: Peça pequena em cima, Peça média no meio, Peça grande embaixo - Pino {destino}")
print(f"\nTotal de passos: {passo}")

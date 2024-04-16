valor_produto = float(input("Digite o valor do produto: "))
forma_pagamento = int(input("Digite codigo de pagamento: "))
desconto = 0
juros = 0

if forma_pagamento == 1: desconto = valor_produto * 0.10
elif forma_pagamento == 2: desconto = valor_produto * 0.15
elif forma_pagamento == 3: juros = 0
elif forma_pagamento == 4: juros = valor_produto * 0.10
elif forma_pagamento == 5: juros = valor_produto * 0.20
else: print("Forma de pagamento invalida")

valor_final = valor_produto - desconto

if forma_pagamento == 3: valor_final = valor_produto + juros
elif forma_pagamento == 4: valor_final = valor_produto + juros
elif forma_pagamento == 5: valor_final = valor_produto + juros

print("O valor a ser pago é: ", "R$", valor_final)
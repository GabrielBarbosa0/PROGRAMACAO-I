# # Desenvolva um sistema de Marketing Multinível (MMN) em Python. Você já possui um sistema de vendas que inclui um campo de cadastro com a opção "Indicado por:". Nesse campo, um usuário pode ser identificado pelo seu ID e nome. Qualquer usuário indicado por outro deve receber comissão, e essa comissão deve continuar sendo paga até que o cliente indicado cancele sua associação.

# # Além disso, o sistema deve permitir configurar o valor da comissão. Também é necessário implementar um ranking dos usuários com base no número de indicações feitas. Os três principais usuários desse ranking devem receber classificações de bronze, prata e ouro. Cada classificação tem uma bonificação associada, e esses valores devem ser configuráveis. Por exemplo, Ouro = R$300, Prata = R$200 e Bronze = R$100.

# # O sistema deve ter uma função que permita a configuração desses valores de bonificação. Ao mesmo tempo, deve calcular e exibir o ranking atualizado dos usuários e suas classificações, possibilitando a identificação dos três principais em cada ciclo.

# eu preciso que tenha um menu para que eu possa adicionar ou não usuario novos e se foram ou não indicados por alguem, refaça o codigo com base nessas alterações
# o menu deve pedir o id do usuario, nome e o ID do usuário que indicou (se não houver, deixe em branco)


class Usuario:
    def __init__(self, id, nome, indicado_por=None):
        self.id = id
        
        self.nome = nome
        self.indicado_por = indicado_por
        self.indicacoes = []  # Lista para armazenar os usuários indicados por este usuário
        self.bonificacao = 0  # Inicialmente sem bonificação

    def adicionar_indicacao(self, usuario):
        self.indicacoes.append(usuario)  # Adiciona um usuário à lista de indicações deste usuário


class SistemaMMN:
    def __init__(self, valor_comissao, bonificacao_ouro, bonificacao_prata, bonificacao_bronze):
        self.valor_comissao = valor_comissao
        self.bonificacao_ouro = bonificacao_ouro
        self.bonificacao_prata = bonificacao_prata
        self.bonificacao_bronze = bonificacao_bronze
        self.usuarios = []  # Lista para armazenar todos os usuários cadastrados no sistema

    def cadastrar_usuario(self):
        id = input("Digite o ID do usuário: ")
        nome = input("Digite o nome do usuário: ")
        indicado_por_id = input("Digite o ID do usuário que indicou (se não houver, deixe em branco): ")
        indicado_por = None
        for usuario in self.usuarios:
            if usuario.id == indicado_por_id:
                indicado_por = usuario
                break
        usuario = Usuario(id, nome, indicado_por)
        self.usuarios.append(usuario)
        if indicado_por:
            indicado_por.adicionar_indicacao(usuario)
        print(f"Usuário {nome} cadastrado com sucesso!")

    def calcular_ranking(self):
        ranking = sorted(self.usuarios, key=lambda x: len(x.indicacoes), reverse=True)
        return ranking

    def distribuir_bonificacao(self):
        ranking = self.calcular_ranking()
        for i, usuario in enumerate(ranking[:3]):
            if i == 0:
                usuario.bonificacao = self.bonificacao_ouro
            elif i == 1:
                usuario.bonificacao = self.bonificacao_prata
            elif i == 2:
                usuario.bonificacao = self.bonificacao_bronze


sistema = SistemaMMN(valor_comissao=100, bonificacao_ouro=300, bonificacao_prata=200, bonificacao_bronze=100)

while True:
    print("\nMENU:")
    print("1. Cadastrar novo usuário")
    print("2. Calcular comissões")
    print("3. Calcular ranking")
    print("4. Distribuir bonificações")
    print("5. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        sistema.cadastrar_usuario()
    elif escolha == "2":
        for usuario in sistema.usuarios:
            comissao = usuario.calcular_comissao(sistema.valor_comissao)
            print(f"Comissão de {usuario.nome}: R$ {comissao}")
    elif escolha == "3":
        ranking = sistema.calcular_ranking()
        print("Ranking:")
        for i, usuario in enumerate(ranking):
            print(f"{i + 1}. {usuario.nome} - Indicações: {len(usuario.indicacoes)}")
    elif escolha == "4":
        sistema.distribuir_bonificacao()
        print("Bonificações distribuídas com sucesso!")
    elif escolha == "5":
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")


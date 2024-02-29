#definir listas

lista_clientes = []
lista_vendas=[]
produtos = {}

#classes
class Produtos():
    def __init__(self,nome_produto:str,preco:float,codigo:str,quantidade:int) -> None:
        self.nome_produto=nome_produto
        self.preco=preco
        self.codigo=codigo
        self.quantidade=quantidade
    # def __str__(self):
    #     return f"{self.nome_produto} (Código: {self.codigo}, Preço: {self.preco}, Quantidade: {self.quantidade})"
    def criar_produto(self,produtos):
        while True:
            codigo = input("Digite o codigo do produto: ")
            if codigo not in self.produtos_em_estoque:
                nome_produto = input("Nome produto: ")
                preco = int(input("Preço do produto: "))
                quantidade = int(input("Digite a quantidade desse produto que ja tem no estoque:"))
                novo_produto = Produtos(nome_produto, preco, codigo, quantidade)
                self.produtos[codigo] = novo_produto
                break
            else:
                print("Esse codigo de produto já existe, por favor insira outro.")
    #exivir as propriedades da venda
    def __str__(self):
        return f"{self.nome_produto} (Código: {self.codigo}, Preço: {self.preco}, Quantidade: {self.quantidade})"
        

class Cliente():
    def __init__(self,nome_cliente:str,cpf:str,historico_compras:dict,lista_clientes:list) -> None:
        self.nome_cliente=nome_cliente
        self.cpf=cpf
        self.historico_compras=historico_compras
        self.lista_clientes= lista_clientes

    def criar_cliente(self):
        novo_cliente= Cliente(
            input("Nome: "),
            input("Cpf: "),
            {},
            self.lista_clientes
        )
        self.lista_clientes.append(novo_cliente)
   
    def logar_cliente(self):
        senha_digitada = input("digite sua senha:")
        for cliente in lista_clientes:
            if cliente.cpf == senha_digitada:
                print(f"Acesso permitido!\n Bem-vindo, {cliente.nome_cliente}.")
                return cliente
            if cliente.cpf != senha_digitada:
                print("Acesso negado.")
                continue
       

class Venda():
    def __init__(self, produtos_vendidos:list, quantidades:list, cliente:Cliente, lista_vendas:list) -> None:
        self.produtos_vendidos = produtos_vendidos
        self.quantidades = quantidades
        self.cliente = cliente
        self.valor_total = sum([self.produtos_vendidos[i].preco * self.quantidades[i] for i in range(len(self.produtos_vendidos))])
        self.lista_vendas = lista_vendas
    def imprimir_venda(self):
        produtos = ", ".join([str(produto) for produto in self.produtos_vendidos])
        print(f"Venda para {self.cliente.nome_cliente} inclui os seguintes produtos: {produtos}. Valor total: {self.valor_total}")

    def criar_nova_venda(self, produtos):
        print("Insira os códigos dos produtos vendidos, separados por vírgulas.")
        produtos_vendidos_codigos = input().split(',')
        print("Insira as quantidades correspondentes, separadas por vírgulas.")
        quantidades = list(map(int, input().split(',')))
        cliente = Cliente.logar_cliente(self)
        if cliente is None:
            return None
        # Converta os códigos dos produtos em objetos Produto
        produtos_vendidos = [produtos[codigo] for codigo in produtos_vendidos_codigos]
        novo = Venda(produtos_vendidos, quantidades, cliente, self.lista_vendas)
        self.lista_vendas.append(novo)
        for i in range(len(produtos_vendidos)):
            produtos_vendidos[i].quantidade -= quantidades[i]
        



class CarrinhoDeCompras:
    def __init__(self, cliente: Cliente):
        self.produtos_no_carrinho = []
        self.cliente_associado = cliente
    def adicionar_produto(self, produtos):
        codigo_produto = input("Insira o código do produto que deseja adicionar: ")
        produto = produtos.get(codigo_produto)
        if produto:
            self.produtos_no_carrinho.append(produto)
            print(f"Produto {produto.nome_produto} adicionado ao carrinho.")
        else:
            print("Produto não encontrado.")

    def remover_produto(self, produtos):
        codigo_produto = input("Insira o código do produto que deseja remover: ")
        produto = produtos.get(codigo_produto)
        if produto and produto in self.produtos_no_carrinho:
            self.produtos_no_carrinho.remove(produto)
            print(f"Produto {produto.nome_produto} removido do carrinho.")
        else:
            print("Este produto não está no carrinho.")


class Mercadinho():
    def __init__(self,produtos:dict) -> None:
        self.produtos=produtos

    def adicionar_estoque(self):
        codigo_produto=input("digite o codigo do produto: ")
        quantidade= int(input("digite a quantidade do produto a ser adicionado "))
        if codigo_produto in self.produtos:
            self.produtos[codigo_produto].quantidade += quantidade
        else:
            print("Produto não encontrado no estoque.")

    def lista_estoque(self):
        for codigo_produto, produto in self.produtos.items():
            print(f"Nome do produto: {produto.nome_produto}, Quantidade: {produto.quantidade}, Preço: {produto.preco}, Código do produto: {produto.codigo}")

    def remover_estoque(self):
        codigo_produto=input("digite o codigo do produto: ")
        quantidade= int(input("digite a quantidade do produto a ser removido "))
        if codigo_produto in self.produtos:
            self.produtos[codigo_produto].quantidade -= quantidade
        else:
            print("Produto não encontrado no estoque.")
        
    def adicionar_produto(self):
        while True:
            codigo = input("Digite o codigo do produto: ")
            if codigo not in self.produtos:
                nome_produto = input("Nome produto: ")
                preco = float(input("Preço do produto: "))
                quantidade = int(input("Digite a quantidade desse produto que ja tem no estoque:"))
                novo_produto = Produtos(nome_produto, preco, codigo, quantidade)
                self.produtos[codigo] = novo_produto
                break
            else:
                print("Esse codigo de produto já existe, por favor insira outro.")




    def remover_produto(self):
        produto_deletado = input("Digite o codigo do produto a ser deletado: ")
        if produto_deletado in self.produtos:
            del self.produtos[produto_deletado]  # Alterado para 'produto_deletado'
        else:
            print("Produto não encontrado no estoque.")
    def imprimir_vendas(self):
        for venda in lista_vendas:
            venda.imprimir_venda()
def interface():
    print("Bem-vindo ao Mercadinho!")
    while True:
        #Opções de escolha
        print("Escolha uma opção:")
        print("1. Adicionar produto")
        print("2. Remover produto")
        print("3. Adicionar estoque")
        print("4. Remover estoque")
        print("5. Listar estoque")
        print("6. Criar cliente")
        print("7. Comprar")
        print("8. Sair")
        opcao = input()
        if opcao == "1":
            mercadinho.adicionar_produto()
        elif opcao == "2":
            mercadinho.remover_produto()
        elif opcao == "3":
            mercadinho.adicionar_estoque()
        elif opcao == "4":
            mercadinho.remover_estoque()
        elif opcao == "5":
            mercadinho.lista_estoque()
        elif opcao == "6":
            cliente1.criar_cliente()
        elif opcao == "7":
            venda1.criar_nova_venda(produtos)
            mercadinho.imprimir_vendas()

        elif opcao == "8":
            break
        else:
            print("Opção inválida. Tente novamente.")

cliente1   = Cliente("Erivelter","1234567890",{},lista_clientes)   
venda1= Venda([],[],cliente1,lista_vendas)
lista_clientes.append(cliente1)
lista_vendas.append(venda1)
produtos = {
    "1": Produtos("queijo", 10, "1", 5),
    "2": Produtos("café", 20, "2", 3),
    # etc.
}

mercadinho = Mercadinho(produtos)


interface()





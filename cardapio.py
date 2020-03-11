print("|||||CARDÁPIO VIRTUAL|||||")

def cadastro:
    nome = input("Digite seu nome: ")
    while len(nome) == 0:
        nome = input("Digite seu nome: ")
        
    email = input("Digite seu e-mail: ")
    
    telefone = input("Digite seu telefone: ")

    print("Usuário cadastrado com sucesso!")
    

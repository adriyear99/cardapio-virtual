import register

print("|||||CARDÁPIO VIRTUAL|||||")

def Register():
	while (True):
		name = input("Digite seu nome: ")
		email = input("Digite seu e-mail: ")
		password = input("Digite sua senha: ")
		cell_number = input("Digite seu telefone: ")
		if (register.Register(email, password, name, cell_number)):
			print("Registrado com sucesso!")
			return
		print("Falha no registro de conta. Tente novamente")

def Login():
	while (True):
		email = input("Digite seu e-mail: ")
		password = input("Digite sua senha: ")
		if (register.Login(email, password)):
			print("Logado com sucesso!")
			return
		print("Falha no login. Tente novamente")

while (True):
	choice = int(input("1 para registrar e 2 para logar: "))

	if (choice == 1):
		print("--------------Registro----------------")
		Register()
	if (choice == 2):
		print("----------------Login-----------------")
		Login()

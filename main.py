# Mostrando o menu principal.

print("\nBem vindo ao menu!\n")       
print("1. Estudantes")
print("2. Professores")
print("3. Disciplinas")
print("4. Turmas")
print("5. Matriculas")
print("0. Sair\n")

# Coletar opção escolhida pelo usuário.

opcao = int(input("Digite uma opção válida: "))

print("\n------------------\n")

# Mostrando o menu secundário.

print(f"\nMenu de operações - opcao {opcao}\n")
print("1. Cadastrar")
print("2. Listar")
print("3. Atualizar")
print("4. Excluir")
print("5. Voltar ao menu principal\n")

# Coletar informação do menu secundário.

opcao_secundaria = int(input("Digite uma opção válida: "))

print("\n------------------\n")

# Caso a opção esteja entre 1 e 5 retornará uma mensagem de opção válida, caso contrário, 
# retornará uma mensagem informando que a opção selecionada é inválida.

if 1 >= opcao <= 5:
    print(f"Você escolheu uma opção **valida** {opcao}.")
else:
    print("Você não digitou uma opção válida.")


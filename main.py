opcao = 1
opcao_secundaria = 2

estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []

while opcao != 0:
   try:
   
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
    def opcao_valida(opcao):
        if opcao_valida:True
        opcoes_validas = [1, 2, 3, 4, 5]
        return opcao in opcoes_validas

    
    if opcao != 0:
        print("\n------------------\n")

         # Mostrando o menu secundário.

        print(f"\nMenu de operações - opcao {opcao}\n")
        print("1. Cadastrar")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Excluir")
        print("5. Voltar ao menu principal\n")

            # Coletar informação do menu secundário.

        if opcao_secundaria : 1

        while opcao_secundaria != 5:
        
    

            opcao_secundaria = int(input("Digite uma opção válida: "))

            if opcao_secundaria == 1:
                
                if opcao == 1:
                    estudanteId = int(input("Informe o codigo do estudante: "))
                    nome = input("Informe o nome do estudante: ")
                    cpf = input("Informe o cpf do estudante: ")
                    estudantes.append({"estudanteId": estudanteId, "nome": nome, "cpf": cpf})
                    
                if opcao == 2:
                    professorId = input("Informe o codigo do professor : ")
                    nome  = input("Informe materia do professor : ")
                    cpf  = input("Informe o CPF do professor : ")
                    professores.append({ "id": id, "nome": nome, "cpf": cpf}) 
                
                if  opcao == 3:
                    disciplinaId = input("Informe o codigo da disciplina : ")
                    nome = input("Informe o nome da disciplina : ")
                    disciplinas.append({ "id": id, "nome": nome}) 
                
                if  opcao == 4:
                    turmaId = input("Informe o codigo da turma : ")
                    professorId  = input("Informe o codigo do professor : ")
                    disciplinaId  = input("Informe o codigo da disciplina : ")
                    turmas.append({ "turmaId": turmaId, "professorId": professorId, "disciplinaId": disciplinaId}) 
                
                if  opcao == 5:
                    turmaId= input("Informe o ano de matricula : ")
                    estudanteId  = input("Informe curso de matricula : ")
                    matriculas.append({ " turmaId":  turmaId, " estudanteId": estudanteId}) 
                

            if opcao_secundaria == 2:  

                if len(estudantes) > 0 :
                    for estudante in estudantes : 
                        print(estudante)  
                else:
                    print("Não há estudantes cadastrados")

                if len(professores) > 0 :
                    for professor in professores :
                        print(professor)
                else:
                     print("Não há professores cadastrados")
                
                if len(disciplinas) > 0 :
                    for disciplina in disciplinas :
                        print(disciplina)
                else:
                     print("Nao há disciplinas cadastradas")

                if len(turmas) > 0 :
                    for turma in turmas :
                        print(turma)
                else:
                     print("Nao há turmas cadastradas")
                
                if len(matriculas) > 0 :
                    for matricula in matriculas :
                        print(matricula)
                else:
                     print("Não há matriculas cadastrados")
                
                
            if opcao_secundaria == 3:
                
                if opcao == 1 :
                    estudanteId = int(input("Informe o código do estudante a ser atualizado: "))
                    novo_estudanteId = int(input("Informe o novo código do estudante: "))
                    novo_nome = input("Informe o novo nome do estudante: ")
                    novo_cpf = input("Informe o novo CPF do estudante: ")
                   
                for estudante in estudantes:
                    if (estudante["estudanteId"] == estudanteId):
                        estudante["estudanteId"] = novo_estudanteId
                        estudante["nome"] = novo_nome
                        estudante["cpf"] = novo_cpf
                
                if opcao == 2 :
                     professorId = int(input("Informe o código do professor a ser atualizado: "))
                     novo_professorId = int(input("Informe o novo código do professor: "))
                     novo_nome = input("Informe o novo nome do professor: ")
                     novo_cpf = input("Informe o novo CPF do professor ")

                for professor in professores:
                     if (professor["professorId"] == professorId):
                        professor["professorId"] = novo_professorId
                        professor["nome"] = novo_nome
                        professor["cpf"] = novo_cpf 
               
                if opcao == 3 :
                    disciplinaId = int(input("Informe o código da disciplina a ser atualizada: "))
                    nova_disciplinaId = int(input("Informe o novo código da disciplina: "))
                    novo_nome = input("Informe o novo nome da disciplina: ")

                for disciplina in disciplinas:
                    if (disciplina["disciplinaId"] == professorId):
                        disciplina["disciplinaId"] = nova_disciplinaId
                        disciplina["nome"] = novo_nome
                         
                if opcao == 4 :
                    turmaId = int(input("Informe o código da turma a ser atualizada: "))
                    nova_turmaId = int(input("Informe o novo código da turma: "))
                    novo_estudanteId = input("Informe o novo nome do estudante: ")
                
                for turma in turmas:
                     if (turma["turmaId"] == turmaId):
                        turma["turmaId"] = nova_turmaId
                        estudante["estudanteId"] = novo_estudanteId
                         
                if opcao == 5 :
                    matriculaId = int(input("Informe o código da matricula a ser atualizada: "))
                    turmaId = int(input("Informe o novo código da turma "))
                    estudanteId = input("Informe o novo nome do estudante: ")
               
                for matricula in matriculas:
                     if (turma["turmaId"] == turmaId):
                        estudante["estudanteId"] = novo_estudanteId
                        
            if opcao_secundaria == 4:
                if opcao == 1 :
                   estudanteId = int(input("Informe o código do estudante a ser excluído: "))

                for estudante in estudantes:
                       if (estudante["estudanteId"] == estudanteId):
                        estudantes.remove(estudante)

                if opcao == 2 :
                    professorId = int(input("Informe o código do professor a ser excluído: "))

                for professor in professores:
                    if (professor["professorId"] == professorId):
                        professores.remove(professor)              
  
                if opcao == 3 :
                    disciplinaId = int(input("Informe o código da disciplina a ser excluído: "))

                for  disciplina in  disciplinas:
                    if ( disciplina[" disciplinaId"] ==  disciplinaId):
                         disciplinas.remove( disciplina)
                
                if opcao == 4 :
                    turmaId = int(input("Informe o código da turma a ser excluído: "))

                for turma in turmas:
                    if (turma["turmaId"] == turmaId):
                        turmas.remove(turma)                     

                if opcao == 5 :
                    matriculaId = int(input("Informe o código dda matricula a ser excluído: "))

                for matricula in matriculas:
                    if (matricula["matriculaId"] == matriculaId):
                        matriculas.remove(matricula)
                        
            # Caso a opção esteja entre 1 e 5 retornará uma mensagem de opção válida, caso contrário, 
            # retornará uma mensagem informando que a opção selecionada é inválida.

            if 1 >= opcao <= 5:
                print(f"Você escolheu uma opção **valida** {opcao}.")
                pass
            else:
                  print("Opção inválida. Por favor, escolha uma opção válida.")
   except ValueError:
    print("Entrada inválida. Por favor, digite um número inteiro para a opção.")
print("O programa foi encerrado.")


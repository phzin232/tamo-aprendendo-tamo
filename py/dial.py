while True:
    print("1 - Adicionar nota")
    print("2 - pesquisar aluno")
    print("3 - ver notas")
    print("4 - ver media por materia")
    print("5 - sair")

    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome: ")
        materia = input("Matéria: ")
        atividade = input("Atividade: ")
        nota = float(input("Nota: "))

        with open("notas.txt","a") as arquivo:
            arquivo.write(f"{nome}, {materia}, {atividade}, {nota}")
        print("Nota salva!")

    elif op == "2":
        nome_busca = input("Nome do aluno: ")


        with open("notas.txt", "r") as arquivo:
            for linha in arquivo:
                nome, materia, atividade, nota = linha.strip().split(",")
                if nome == nome_busca:
                    print("Nome: ",nome)
                    print("Matéria:", materia)
                    print("Atividade:", atividade)
                    print("Nota:", nota)


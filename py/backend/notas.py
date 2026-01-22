import os
import py.gui as gui

base_dir = os.path.dirname(os.path.abspath(__file__))
pathn = os.path.join(base_dir,"..","..", "infos", "notas.txt")

def load_names():
    nomes_set = set()
    salas_set = set()
    materias_set = set()
    aluno_sala = {}

    with open(pathn, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(",")
            if len(partes) != 5:
                continue           
            nome,sala,materia,_,_ = partes

            nomes_set.add(nome)
            salas_set.add(sala)
            materias_set.add(materia)

            if nome not in aluno_sala:
                aluno_sala[nome] = []
            if sala not in aluno_sala[nome]:
                aluno_sala[nome].append(sala)

    return list(nomes_set), list(salas_set), list(materias_set), aluno_sala


#Adinicionar nota
def add_grade (nome, sala, materia, atividade, nota):
    
    with open(pathn, "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{sala},{materia},{atividade},{nota}\n")
        return True

#Pesquisar Aluno
def search_aluno():
        print("1 - Nota geral do Aluno")
        print("2 - Nota por matéria")
        print("3 - Voltar")

        sub = input("Escolha: ")
        #Nota Geral do aluno
def geral_gradeb():
    

    total = 0
    quantidade = 0
    encontrado = False
    
    with open(pathn, encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.strip().split(",")
            if len(partes) != 5:
                continue

            nome, sala, materia, atividade, nota = partes



            total += float(nota)
            quantidade += 1


            

    if quantidade > 0:
        total / quantidade
    
    if not encontrado:
        print("Aluno não encontrado.")
        #Nota por matéria
        def grade_per_subject():
            nome_busca = input("Nome do aluno: ")
            sala_busca = input("Sala do aluno: ")
            materia_busca = input("Nome da matéria: ")

            total = 0
            quantidade = 0

            nome_encontrado = False
            materia_encontrado = False
            sala_encontrado = False

            linha_encontrado = False

            with open(pathn, encoding="utf-8") as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(",")
                    if len(partes) !=5:
                        continue
                    nome, sala, materia, atividade, nota = partes
                    
                    if nome == nome_busca:
                        nome_encontrado = True
                    
                    if materia == materia_busca:
                        materia_encontrado = True
                    if sala == sala_busca:
                        sala_encontrado = True

                    if  nome == nome_busca and materia == materia_busca and sala == sala_busca:
                        print("Nome: ", nome, sala)
                        print("Atividade", atividade)
                        print("Nota: ", nota)
                        print("----")

                        total += float(nota)
                        quantidade +=1

                for linha in arquivo:
                    nome, sala, materia, atividade, nota = linha.strip().split(",")
                    if nome == nome_busca and sala == sala_busca and materia == materia_busca:
                        linha_encontrado = True

            if quantidade > 0 : 
                print(f"Média por materia: {materia} {total / quantidade:.2f} ".format)

            if not linha_encontrado:
                print("Aluno não encontrado")

            if not materia_encontrado:
                print("Matéria não encontrada")
                
            if not nome_encontrado:
                print("Nome não encontrado")

            if not sala_encontrado:
                print("Sala não encontrada.")
        #Voltar                 

#Ver notas por Sala
def consult_grade ():
    while True:
        print("1 - Visão geral")
        print("2 - Visão detalhada")
        print("3 - Voltar")

        sub = input("Escolha: ")
        #Visão geral
        if sub == "1":

            sala_busca = input("Digite a sala: ")

            total = 0
            quantidade = 0
            encontrado = False

            notas_por_aluno = {}

            with open(pathn, encoding="utf-8") as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(",")
                    if len(partes) != 5:
                                continue

                    nome, sala, materia, atividade, nota = partes


                    if sala == sala_busca:
                        encontrado = True

                        if nome in notas_por_aluno and sala == sala_busca:
                            if nome not in notas_por_aluno:
                                notas_por_aluno[nome] = []
                            notas_por_aluno[nome].append(float(nota))
                        else:
                            notas_por_aluno[nome] = [float(nota)]

            if not encontrado:
                print("Sala não encontrada.")

            else:
                for aluno in notas_por_aluno:
                    media = sum(notas_por_aluno[aluno]) / len(notas_por_aluno[aluno])
                    print(f"{aluno}, ->, {media:.2f}")
        #Visão detalhada
        elif sub == "2":
            sala_busca = input("Digite a sala: ")
            
            total = 0
            quantidade = 0
            encontrado = False

            detalhes_por_aluno = {}

            with open(pathn, encoding="utf-8") as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(",")
                    if len(partes) != 5:
                                continue
                    nome, sala, materia, atividade, nota = partes 
                    
                    if sala == sala_busca:
                        encontrado = True

                    if sala == sala_busca:
                        if nome not in detalhes_por_aluno:
                            detalhes_por_aluno[nome] = []
                        detalhes_por_aluno[nome].append((materia,atividade,float(nota)))
                for aluno, lista_atividades in detalhes_por_aluno.items():
                    print(f"\nAluno: {aluno}")
                    print("Atividades: ")
                    
                    for materia, atividade, nota in lista_atividades:
                        print(f"- {materia}: {atividade} → Nota: {nota:.2f}")
                if not encontrado:
                    print("Sala não encontrada.")
        #voltar
        elif sub == "3":
            break
#Ver médias por materia
def average_per_subject():
    while True:
        print("1 - Média por matéria geral")
        print("2 - Média por matéria da sala ")
        print("3 - Voltar")

        sub = input("Escolha: ")

        #media por materia geral
        if sub == "1":
            materia_busca = input("Nome da matéria: ")

            total = 0
            quantidade = 0
            encontrado = False

            with open(pathn, encoding="utf-8") as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(",")
                    if len(partes) != 5:
                        continue
                    nome, sala, materia, atividade, nota = partes

                    if materia == materia_busca:
                        encontrado = True

                    if materia == materia_busca:
                        total += float(nota)
                        quantidade += 1

            if quantidade > 0:
                print(f"Média geral:, {total / quantidade:.2f}")
            if not encontrado:
                print("Nenhuma nota encontrada para essa matéria")
        #media por materia da sala
        elif sub == "2":
            sala_busca = input("Sala: ")
            materia_busca = input("Matéria: ")

            total = 0
            quantidade = 0
            sala_encontrado = False
            materia_encontrado = False

            with open(pathn, encoding="utf-8") as arquivo:
                for linha in arquivo:
                    partes = linha.strip().split(",")
                    if len(partes) != 5:
                        continue
                    nome, sala, materia, atividade, nota = partes

                    if sala == sala_busca:
                        sala_encontrado = True
                    
                    if materia == materia_busca:
                        materia_encontrado = True

                    if sala == sala_busca and materia == materia_busca:
                        total += float(nota)
                        quantidade +=1
                        

                if quantidade > 0:
                    print(f"Média da matéria:  {materia_busca}  {total / quantidade:.2f}")

                if not materia_encontrado:
                    print("Matéria não encontrada.")

                if not sala_encontrado:
                    print("Sala não encontrada.")
        #voltar
        elif sub == "3":
            break
#sair

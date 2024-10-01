while True:
    try:
        colab = int(input("Informe o número de colaboradores: ")) #Input para que o usuário informe o número de votantes/colaboradores
        print("O número de colaboradores é {}".format(colab))
        break

    #Input é mostrado novamente caso o usuário não escolha uma das opções apresentadas     
    except ValueError:
        print("Valor incorreto. Informe um número inteiro por favor")

#Variable para armazenar o número de votos de cada dia da semana
votos = {
    "segunda-feira": 0,
    "terça-feira": 0,
    "quarta-feira": 0,
    "quinta-feira": 0,
    "sexta-feira": 0
}

for i in range(colab):
    while True:
        voto = input("Escolha um dia da semana. As opções são as seguintes (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira): ")
        
        if voto.lower() in votos:
            votos[voto.lower()] += 1
            break

        #Input é mostrado novamente caso o usuário não escolha uma das opções apresentadas        
        else:
            print("Voto não computado. Escolha entre uma das opções válidas")

max_votos = max(votos.values()) #Determina o número máximo de votos na mesma opção
dias_empatados = [dia for dia, quantidade in votos.items() if quantidade == max_votos] #Determina que houve empate caso a variável quantidade tenha o mesmo valor que o número máximo de votos na mesma opção
dia_vencedor = dias_empatados[0]

if len(dias_empatados) > 1:
    print("Houve empate entre: ", dias_empatados)

else:
    print("O dia com mais votos é:",dia_vencedor, "com",max_votos,"votos")
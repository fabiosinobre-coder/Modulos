import statisticalAnalysis



def main():

    numberEntered = []

    while True:
        userInput = input("Digite um número ou 'sair': ").strip().lower()

        if userInput == "sair":
            break
        try:
            ### Converte a entreda para float
            number = float(userInput)
            numberEntered.append(number)
        except ValueError:
            print("X Entrada inválida! Digite um número ou 'sair: '")
        
    ### verifica se a lista não está vázia antes de enviar para lista.
    if len(numberEntered) > 0:
        finalAverage = statisticalAnalysis.arithmeticMean(numberEntered)

        print("\n #### Resultados ####")
        print(f"Números digitados: {numberEntered}")
        print(f"Média aritmética: {finalAverage:.2f}")
    else:
        print("\n Nenhum numero foi digitado. O programa será encerrado.")


if __name__ == "__main__":
    main()


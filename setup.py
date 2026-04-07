def menu():
    print("\n=== URNA ELETRÔNICA ===")
    print("1 - Votar")
    print("2 - Ver resultados")
    print("3 - Sair")

votos = {
    "Branco": 0,
    "Nulo": 0,
    "Candidato_A": 0,
    "Candidato_B": 0,
    "Candidato_C": 0
}

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            print("Digite seu voto:")
            print("0 - Branco")
            print("1 - Nulo")
            print("2 - Candidato A")
            print("3 - Candidato B")
            print("4 - Candidato C")

            voto =  input("Seu voto: ")

            match voto:
                case "0":
                    votos["Branco"] =+ 1
                    print("Voto branco confirmado!")
                case "1":
                    votos["Nulo"] =+ 1
                    print("Voto nulo confirmado!")
                case "2":
                    votos["Candidato_A"] =+ 1
                    print("Voto no Candidato A confirmado!")
                case "3":
                    votos["Candidato_B"] =+ 1
                    print("Voto no Candidato B confirmado!")
                case "4":
                    votos["CandidatoC"] =+ 1
                    print("Voto no Confirmado C confirmado!")
                case _:
                    print("Voto inválido")

        case "2":
            print("\n=== RESULTADOS ===")
            print(votos)

        case "3":
            print("Encerrando...")
            break

        case _:
            print("opção inválida!")
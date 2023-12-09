message = input("Olá, essa é a calculadora de empréstimo Fortuna. Iremos calcular qualquer valor que não exceda o valor de 5 vezes sua renda e seja parcelado no período máximo de 12 meses. Clique Enter para começarmos.")
input_user = input("Gostaria de fazer uma simulaçao?(Sim ou Nao): ")

if input_user.lower() == "Nao":
    print('Sem problemas, estaremos sempre a disposiçao')

if input_user.lower() == "sim":
    print("Poderia informar qual sua renda familiar?") # criar sequencia Validação de Renda: Os usuários inserirão informações sobre sua renda mensal.

    lower_bound = 2000.00
    upper_bound = 10000.00

    renda = float(input("Insira o total da renda, até seus decimais")) # A aplicação verificará se a renda inserida é válida e está dentro de um limite específico. Valor entre 2000 até 10.000

    if lower_bound <= renda <= upper_bound:
        print("Sua renda foi aprovada para seguirmos.")

        emprestimo = float(input("Qual o valor desejado para empréstimo? ")) # Cálculo de Empréstimo:Após a validação bem-sucedida da renda, os usuários poderão inserir o valor do empréstimo desejado (Valor máximo de 5x a renda)

        if emprestimo <= renda * 5:
            print("O valor requisitado é compatível com a renda informada.")

            parcela = int(input("Insira a quantidade de meses em que gostaria de parcelar o valor do empréstimo: "))

            if parcela > 0 and parcela < 4:
                print("A taxa de juros é de 2.2% ao mês")
                juros = (emprestimo * parcela * 2.2) / 100
                print("Total de Juros: ", juros)

                total_pag = emprestimo + juros
                print("Total a ser pago: ", total_pag)
                valor_par = total_pag / parcela
                print(f"Valor das parcelas mensais: {valor_par:.2f}")

            elif parcela > 3 and parcela < 7:
                print("A taxa de juros é de 2.6% ao mês")
                juros = (emprestimo * parcela * 2.6) / 100
                print("Total de Juros: ", juros)

                total_pag = emprestimo + juros
                print("Total a ser pago: ", total_pag)
                valor_par = total_pag / parcela
                print(f"Valor das parcelas mensais: {valor_par:.2f}")

            elif parcela > 6 and parcela < 13:  # e o prazo (período max de 12 meses)
                print("A taxa de juros é de 3% ao mês")
                juros = (emprestimo * parcela * 3) / 100
                print("Total de Juros: ", juros)

                total_pag = emprestimo + juros
                print("Total a ser pago: ", total_pag)
                valor_par = total_pag / parcela
                print(f"Valor das parcelas mensais: {valor_par:.2f}") # Apresentação dos Resultados: A aplicação exibirá os resultados do cálculo, incluindo o valor das prestações mensais e o custo total do empréstimo.#

            else:
                print("Valor não correspondente.")
        else:
            print("O valor requisitado não foi aprovado.")
    else:
        print("Infelizmente não podemos prosseguir com a renda informada.")
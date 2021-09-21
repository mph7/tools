import statistics


def main():
    print("### Calcular dados estatisticos ###\n")
    tipo_dados = 0
    while 1:
        tipo_dados = input(
            "Voce quer fazer calculos de: \n1 - dados não agrupados\n2 - dados agrupados\n: "
        )
        if tipo_dados in ("1", "2"):
            break
        print("Insira um valor válido.")
    print("=" * 40)
    if tipo_dados == "1":
        nao_agrupados_hub()
    else:
        agrupados_hub()


# NAO AGRUPADOS
def nao_agrupados_hub():
    dados = []

    opcao = input("Usar dados prontos? 1 - Sim 2 - Nao\n:  ")
    precisao = int(input("Digite a precisão em casas após a virgula: "))
    if opcao == "1":
        dados = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    else:
        receber_dados_nao_agrupados(dados)
    media = round(statistics.mean(dados), precisao)
    moda = round(statistics.mode(dados), precisao)
    mediana = round(statistics.median(dados), precisao)
    quantil = quartil_nao_agrupados(dados, precisao)

    print("=" * 40, "\n")

    print("Média: {}".format(media))
    print("Moda: {}".format(moda))
    print("Mediana: {}\n".format(mediana))

    print_percentil(quantil, precisao)

    desvio = round(desvio_nao_agrupados(dados, media), precisao)

    print("Desvio padrão: %g" % desvio)
    print("Coeficiente de variação: %g%%" % round(((desvio / media) * 100), precisao))
    print(
        "Faixa normal entre %g e %g"
        % (round((media - desvio), precisao), round((media + desvio), precisao))
    )


def receber_dados_nao_agrupados(dados):
    quant = int(input("Quantos dados voce irá digitar? "))
    print("Digite os dados:")
    for i in range(quant):
        dados.append(float(input("Digite o {}° numero: ".format(i + 1))))
    print()


def quartil_nao_agrupados(dados, precisao):
    lista = list(statistics.quantiles(dados, n=20))
    for i, el in enumerate(lista):
        lista[i] = round(el, precisao)
    return lista


def print_percentil(quantil, precisao):
    for i in range(0, 10):
        print(
            "| {:<25}".format(
                "Percentil %d:  " % ((i + 1) * 5) + str(round(quantil[i], precisao))
            )
            + " | ",
            end="",
        )

        if i < 9:
            print(
                "{:<25}".format(
                    "Percentil %d:  " % ((i + 11) * 5)
                    + "{}".format(str(round(quantil[i + 10], precisao)))
                    + " |"
                )
            )
        else:
            print("\n")


def desvio_nao_agrupados(dados, media):
    soma = 0
    for i in dados:
        soma += (i - media) ** 2
    return (soma / len(dados)) ** 0.5


# AGRUPADOS
def agrupados_hub():
    dados = []
    precisao = int(input("Digite quantas casas apos a virgula:  "))
    dados = recebe_dados_agrupados(dados)
    dados = aplicar_precisao(dados, precisao)
    soma_fi, soma_xifi = print_grouped_data(dados)
    media = round(media_agrupados(soma_fi, soma_xifi), precisao)
    moda = round(moda_agrupados(dados), precisao)
    mediana = round(mediana_agrupados(dados, soma_fi), precisao)
    desvio_padrao = desvio_padrao_agrupados(dados, media)

    print("Media: {}".format(media))
    print("Moda: {}".format(moda))
    print("Mediana: {}".format(mediana))
    print(f"Desvio padrao: {desvio_padrao}")
    print("Coeficiente de variaçao: {}".format(desvio_padrao / media) * 100)
    print(f"Faixa normal entre {media-desvio_padrao} e {media + desvio_padrao}")


def recebe_dados_agrupados(dados):
    fa = xi = xifi = 0
    dados = []
    opcao = int(input("Deseja usar dados prontos?\n1 - Sim\n2 - Nao\n:  "))
    if opcao == 1:
        dados = [[1, 2, 75], [2, 3, 78], [3, 4, 128], [4, 5, 82], [5, 6, 12]]
    else:
        quant = int(input("Quantas linhas de dados serao inseridos?  "))
        print(
            "Digite os dados na sequencia: Limite_inferior limite_superior \
frequencia, separados por espaço:"
        )
        for i in range(quant):
            dados.append(list(map(float, input("{}° Dado:  ".format(i + 1)).split())))

    for i, el in enumerate(dados):
        fa += el[2]
        xi = (el[0] + el[1]) / 2
        xifi = xi * el[2]
        dados[i].append(fa)
        dados[i].append((el[0] + el[1]) / 2)
        dados[i].append(xifi)
    return dados


def print_grouped_data(dados):

    soma_fi = soma_xifi = 0
    for i in range(len(dados)):
        soma_fi += dados[i][2]
        soma_xifi += dados[i][5]

    print("=" * 84)
    print(
        "|"
        + "{:^30}".format("Linf----Lsup")
        + " | {:^10}".format("fi")
        + " | {:^10}".format("fa")
        + " | {:^10}".format("xi")
        + " | {:^10}".format("xi.fi")
        + "|"
    )
    print("-" * 84)
    for _, el in enumerate(dados):
        print(
            "|"
            + "{:^30}".format("{}".format(el[0]) + " ---- {}".format(el[1]))
            + " | {:^10}".format(el[2])
            + " | {:^10}".format(el[3])
            + " | {:^10}".format(el[4])
            + " | {:^10}".format(el[5])
            + "|"
        )
    print("-" * 84)
    print(
        "|"
        + "{:^30}".format("Total (n)")
        + " | {:^10}".format(soma_fi)
        + " | {:^10}".format(soma_fi)
        + " | {:^10}".format("-")
        + " | {:^10}".format(soma_xifi)
        + "|"
    )
    print("=" * 84)
    return soma_fi, soma_xifi


def media_agrupados(soma_fi, soma_xifi):
    return soma_xifi / soma_fi


def moda_agrupados(dados):
    maior = d1 = d2 = 0
    index = 0
    for i, el in enumerate(dados):
        if el[2] > maior:
            maior = el[2]
            index = i

    if index > 0:
        d1 = dados[index][2] - dados[index - 1][2]
    d2 = dados[index][2] - dados[index + 1][2]

    return dados[index][0] + ((d1) / (d1 + d2)) * (dados[index][1] - dados[index][0])


def mediana_agrupados(dados, soma_fi):
    vc = soma_fi / 2
    index = faa = 0
    for i, el in enumerate(dados):
        if el[3] > vc:
            index = i
            break
    if index != 0:
        faa = dados[index - 1][3]

    return dados[index][0] + ((vc - faa) / dados[index][2]) * (
        dados[index][1] - dados[index][0]
    )


def desvio_padrao_agrupados(dados, media):
    somatoria = 0
    for i, el in enumerate(dados):
        somatoria += (el[4] ** 2) * el[2]
    soma = somatoria / len(dados)
    soma = soma - (media ** 2)
    return soma ** 0.5


def aplicar_precisao(dados, precisao):
    for i in range(len(dados)):
        for j in range(len(dados[i])):
            dados[i][j] = round(dados[i][j], precisao)
    return dados


if __name__ == "__main__":
    main()

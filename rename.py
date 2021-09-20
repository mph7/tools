import os
import re
import sys

from unidecode import unidecode


def main():
    print("###### RENOMEADOR DE ARQUIVOS ######")
    while 1:
        print("#" * 40)
        opcaohub = input("\
1 - Normalizer\n\
2 - Semi-Automatic renamer\n\
3 - Rename in Order\n\
4 - Info\n\
5 - Sair\n:  ")
        if opcaohub == "1":
            normalizador()
        if opcaohub == "2":
            semi_automatic()
            break
        if opcaohub == "3":
            em_ordem()
            break
        if opcaohub == "4":
            explicacoes(1)
            continue
        if opcaohub == "5":
            print("Exitting....")
            sys.exit()
        print("Please select a valid option")


def normalizador():
    dados = []
    cont = 0
    path = os.getcwd() + "/"
    delimiters = [" ", ",", ":", ";", "_", "-", "\n", "."]
    opcao = 0
    while 1:
        print("#" * 40)
        opcao = input("Convert all the files name to:\n1 - camelCase\n2\
 - UpperCamelCase\n3 - snake_case\n4 - Spaces\n5 - Voltar ao Menu Anterior\n\
6 - Exit\n:  ")
        if opcao in ("1", "2", "3"):
            break
        if opcao == "4":
            explicacoes(2)
            continue
        if opcao == "5":
            main()
        if opcao == "6":
            print("Exiting...")
            sys.exit()
        print("Please select a valid option.\n")

    for nome in os.listdir(path):
        regex_pattern = "|".join(map(re.escape, delimiters))
        dados = list(re.split(regex_pattern, unidecode(str(nome))))
        extensao = "." + dados[-1]
        dados.pop()
        dados = list(map(lambda x: re.sub("([A-Z])", r" \g<0>", x), dados))
        dados = list(re.split("(\\d)+", str(" ".join(dados))))
        dados = list(re.split(regex_pattern, str(" ".join(dados))))
        dados = [i.lower() for i in dados if i not in delimiters + [""]]
        nome_normalizado = dados

        if opcao == "1":
            to_camel_case(path, nome_normalizado, extensao, nome)
        elif opcao == "2":
            to_upper_camel_case(path, nome_normalizado, extensao, nome)
        elif opcao == "3":
            to_snake_case(path, nome_normalizado, extensao, nome)
        elif opcao == "4":
            to_spaces(path, nome_normalizado, extensao, nome)
        cont += 1
    print("{} files was renamed in total.".format(cont))


def to_camel_case(path, nome_normalizado, extensao, nome):
    first = nome_normalizado[0]
    novo_nome = list(map(lambda x: x.capitalize(), nome_normalizado))
    novo_nome[0] = first
    novo_nome = "".join(novo_nome)
    os.rename(path + nome, path + novo_nome + extensao)
    print("arquivo " + nome + " alterado para " + novo_nome + extensao)


def to_upper_camel_case(path, nome_normalizado, extensao, nome):
    novo_nome = list(map(lambda x: x.capitalize(), nome_normalizado))
    novo_nome = "".join(novo_nome)
    os.rename(path + nome, path + novo_nome + extensao)
    print("arquivo " + nome + " alterado para " + novo_nome + extensao)


def to_snake_case(path, nome_normalizado, extensao, nome):
    novo_nome = "_".join(nome_normalizado)
    os.rename(path + nome, path + novo_nome + extensao)
    print("arquivo " + nome + " alterado para " + novo_nome + extensao)


def to_spaces(path, nome_normalizado, extensao, nome):
    novo_nome = " ".join(nome_normalizado)
    os.rename(path + nome, path + novo_nome + extensao)
    print("arquivo " + nome + " alterado para " + novo_nome + extensao)


def em_ordem():
    cont = 0
    path = os.getcwd() + "/"
    while 1:
        print("#" * 40)
        opcao = input('Tem certeza que deseja renomear todos \
os arquivos no diretório "{}" ?\n(Esta é uma ação irreversível!!) \n\
Y - Yes\n\
N - No\n\
i - Informações\n\
X - Voltar ao menu anterior\n: '.format(path))
        if opcao in ("N", "n"):
            sys.exit()
        if opcao in ("i", "I"):
            explicacoes(3)
            continue
        if opcao in ("X", "x"):
            main()
        if opcao in ("Y", "y"):
            break
        print("Please select a valid option")
        continue

    directory = os.listdir(path)
    directory.sort()

    for nome in directory:
        dados = nome.split(".")
        extensao = "." + dados[-1]
        dados.pop()
        novo_padrao = input(
            "\n\nType the new default name to \
rename all files with a number index: "
        )
        cont += 1
        novo_nome = novo_padrao + str(cont)
        os.rename(path + nome, path + novo_nome + extensao)
        print("arquivo " + nome + " alterado para " + novo_nome + extensao)
    print("Voce renomeou {} arquivos.".format(cont))


def semi_automatic():
    cont_y = cont_n = 0
    path = os.getcwd()

    for nome in os.listdir(path):
        dados = nome.split(".")
        extensao = "." + dados[-1]
        dados.pop()
        nome_sem = "_".join(dados)
        explicacoes(4)
        novo_nome = input("Nome Atual: {}\nNovo Nome: ".format(nome_sem + extensao))
        print("#" * 40)
        if novo_nome == "":
            novo_nome = nome_sem
            cont_n += 1
        else:
            os.rename(path + nome, path + novo_nome + extensao)
            print("arquivo " + nome + " alterado para " + novo_nome + extensao)
            cont_y += 1
    print("Voce renomeou %d arquivos e %d arquivos nao foram renomeados." %
          (cont_y, cont_n))


def explicacoes(bloco):
    if bloco == 1:  # Hub Block
        print("Welcome to rename HUB, now on explains of each functionality:\n\
First, you will execute this script while in the folder you want to rename\
\nYour Actual folder: {} \n\
Second, be atent if the folder have ONLY FILES\n\n\
1 - Normalizer: It will receive all the files and give four options to \
rename it in a normalized format, camelCase, UpperCamelCase, snake_case, \
Spaces, you select one and your files in directory will be Normalized.\n\n\
2 - Semi Automatic Renamer: this is going to make rename files by hand easier,\
 you receive filename, and put new filename, direct in all files of directory.\
\n3 - In Order Renamer: This option will rename your files in a padronized\
 format like:\n FileName1.py, FileName2.py .... FileNameNumber.py\n, \
you choose the FileName, and the script will rename it if ordened numbers, \
and the extension will be the same as before.".format(os.getcwd()))
    if bloco == "2":  # Normalizer Block
        print("Choose one format to normalize all your files in directory, \
camelCase - it will Make Different words capitalized, except the first, with \
no spaces between then.\n\
UpperCamelCase - Same as camelCase, but the first word is capitalized.\n\
snake_case - All the words are lowercase and underscore separated.\n\
Spaces - All the words are lowercase and separated by spaces.")
        return
    if bloco == "3":  # In order Block
        print("Simply choose the new filename that you want to rename \
your files, the script will rename all the files with that filename + a \
number ordered in crescent order, the extension will be the same.")
        return
    if bloco == "4":  # Semi Authomatic Block
        print("This make possible and easier to rename files with a name that \
you choose, you will receive the actual name and write the new name (DON'T \
write the extension again, it will keep the same).")


if __name__ == "__main__":
    main()

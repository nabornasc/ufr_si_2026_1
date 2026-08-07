import os

cls = lambda: os.system("cls" if os.name == "nt" else "clear")
cls()

vtA = 0
vtB = 0
vtC = 0
vtN = 0
vtBranco = 0


def candidatos(candidato):

    global vtA, vtB, vtC, vtN, vtBranco

    if candidato == 1:
        vtA += 1
        return "Candidato AAA", vtA
    elif candidato == 2:
        vtB += 1
        return "Candidato BBB", vtB
    elif candidato == 3:
        vtC += 1
        return "Candidato CCC", vtC
    elif candidato == 4:
        vtN += 1
        return "Nulo", vtN
    else:
        vtBranco += 1
        return "Branco", vtBranco


flag = True

while flag:
    cls()
    print(
        "1- Candidato AAA\n2- Candidato BBB\n3- Candidato CCC\n4- Nulo\n5- Branco\n999- Sair"
    )
    eleicao = int(input("Digite a opção desejada: "))
    if eleicao == 999:
        flag = False
    else:
        print(candidatos(eleicao))
print(
    f"\nVotos do Candidato AAA: {vtA}\nVotos do Candidato BBB: {vtB}\nVotos do Candidato CCC: {vtC}\nVotos Nulos: {vtN}\nVotos em Branco: {vtBranco}"
)

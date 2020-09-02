#REGIÃO ONDE FOI REALIZADA A ENTREVISTA;IDADE: QUAL A SUA IDADE (EM ANOS COMPLETOS)?;ÁREA;SEXO;COR OU RAÇA;ÚLTIMA SÉRIE ESCOLAR QUE CONCLUIU COM APROVAÇÃO;ATÉ QUE SÉRIE O SEU PAI ESTUDOU;ATÉ QUE SÉRIE A SUA MÃE ESTUDOU;RENDA TOTAL DO CHEFE DA FAMÍLIA NO ÚLTIMO MÊS;RENDA TOTAL DE TODOS OS MORADORES (PARENTES E AGREGADOS) NO ÚLTIMO MÊS;NÚMERO DE MORADORES NO DOMICÍLIO (PARENTES E AGREGADOS);NO ÚLTIMO MÊS, ALGUMA PESSOA DESTE DOMICÍLIO RECEBEU RENDIMENTOS DO BOLSA FAMÍLI;RELIGIÃO;MULHERES QUE USAM ROUPAS QUE MOSTRAM O CORPO MERECEM SER ATACADAS;AS MULATAS SÃO MAIS FOGOSAS DO QUE AS MULHERES BRANCAS;DÁ PARA ENTENDER QUE UM HOMEM QUE CRESCEU EM UMA FAMÍLIA VIOLENTA AGRIDA SUA MUL;OS HOMENS DEVEM SER A CABEÇA DO LAR;CASOS DE VIOLÊNCIA DENTRO DE CASA DEVEM SER DISCUTIDOS SOMENTE ENTRE OS MEMBROS ;INCOMODA VER DOIS HOMENS, OU DUAS MULHERES, SE BEIJANDO NA BOCA EM PÚBLICO;SE AS MULHERES SOUBESSEM COMO SE COMPORTAR, HAVERIA MENOS ESTUPROS;HOMEM QUE BATE NA ESPOSA TEM QUE IR PARA A CADEIA;É VIOLÊNCIA FALAR MENTIRAS SOBRE UMA MULHER PARA OS OUTROS;TODA MULHER SONHA EM SE CASAR;O QUE ACONTECE COM O CASAL EM CASA NÃO INTERESSA AOS OUTROS;QUANDO HÁ VIOLÊNCIA, OS CASAIS DEVEM SE SEPARAR;CASAIS DE PESSOAS DO MESMO SEXO DEVEM TER OS MESMOS DIREITOS DOS OUTROS CASAIS;DÁ PRA ENTENDER QUE UM HOMEM RASGUE OU QUEBRE AS COISAS DA MULHER SE FICOU NERVO;UM HOMEM PODE XINGAR E GRITAR COM SUA PRÓPRIA MULHER;É DA NATUREZA DO HOMEM SER VIOLENTO;EM BRIGA DE MARIDO E MULHER, NÃO SE METE A COLHER;A ROUPA SUJA DEVE SER LAVADA EM CASA;UMA MULHER SÓ SE SENTE REALIZADA QUANDO TEM FILHOS/AS;A MULHER CASADA DEVE SATISFAZER O MARIDO NA CAMA, MESMO QUANDO NÃO TEM VONTADE;PIADA DE PRETO É SÓ BRINCADEIRA, NÃO É RACISMO;UM CASAL DE DOIS HOMENS VIVE UM AMOR TÃO BONITO QUANTO ENTRE UM HOMEM E UMA MULH;MULHER QUE É AGREDIDA E CONTINUA COM O PARCEIRO GOSTA DE APANHAR;CASAMENTO DE HOMEM COM HOMEM OU DE MULHER COM MULHER DEVE SER PROIBIDO;A MULHER QUE APANHA EM CASA DEVE FICAR QUIETA PARA NÃO PREJUDICAR OS FILHOS;A QUESTÃO DA VIOLÊNCIA CONTRA AS MULHERES RECEBE MAIS IMPORTÂNCIA DO QUE MERECE;TEM MULHER QUE É PRA CASAR, TEM MULHER QUE É PRA CAMA
#c) A base é composta por quantas linhas e colunas?
#d) Calcule a frequência de pessoas em cada região do Brasil.
#e) Qual é a região mais frequente (moda)?
#f) Qual é a idade da pessoa mais nova nessa amostra? E da mais velha?
#g) Calcule a média, a mediana e a moda para a variável idade. A partir disso, o que você pode dizer sobre a distribuição dessa variável (assimétrica positiva, assimétrica negativa ou simétrica)?
import math
import statistics

def getMaisNova(dados):
    idade = 500 #uma idade que nenhum ser humano consegue viver
    for i in range(1, len(dados)):#variável inicializada em 1 para ignorar o índice
        temp = int(dados[i])
        if(idade >= temp):
            idade = temp
    return idade

def getMaisVelho(dados):
    idade = 0  # a idade minima possível
    for i in range(1, len(dados)):  # variável inicializada em 1 para ignorar o índice
        temp = int(dados[i])
        if (idade <= temp):
            idade = temp
    return idade

def linhaColunaBase(conteudo):
    coluna = len(conteudo[0])
    linha = len(conteudo) - 1 #desconsiderando o indice da tabela
    return [linha, coluna]

def frequenciaDados(conteudo):
    resultado = []
    referencia = getDistinct(conteudo)
    for indice in referencia:
        count = 0
        for linha in conteudo:
            if linha in indice:
                count+=1
        resultado.append([indice, count])
    return resultado

def simetria(moda, media):
    x = media - moda
    if(x > 0):
        return "Assimétrica positiva"
    elif(x < 0):
        return "Assimétrica negativa"
    else:
        return "Simétrica"

def lerArquivo(nomeArquivo):
    arquivo = open(nomeArquivo, "r")
    temp = arquivo.readlines()
    arquivo.close()
    conteudo = []
    for linha in temp:
        conteudo.append(linha.split(";"))
    return conteudo

def adicionaFaixaEtaria(nomeArquivo):
    conteudo = lerArquivo(nomeArquivo)
    colunaIdade = buscaColuna(conteudo[0], "idade")
    resultado = []
    cIdade = int(colunaIdade[0])
    for i in range(len(conteudo)):
        linha = conteudo[i]
        if(i == 0):
            linha.insert(cIdade + 1,"Faixa etária:")
        else:
            idade = int(conteudo[i][colunaIdade[0]])

            if(idade <= 29):
                linha.insert(cIdade + 1,"Jovens")
            elif(30<= idade <= 59):
                linha.insert(cIdade + 1,"Adultos")
            else:
                linha.insert(cIdade + 1,"Idosos")
        resultado.append(linha)
    return resultado


#função que retorna os valores distintos de uma coluna
def getDistinct(conteudo):
    temp = []
    for linha in conteudo:
        if not str(linha) in temp:
            try:
                x = int(linha)
                temp.append(x)
            except:
                temp.append(linha)
    return temp

def getModa(dados):
    ref = getDistinct(dados)
    quantidade  = 0
    resultado = []
    #print("dados", dados)
    temp = frequenciaDados(dados)
    for linha in temp:
        if(linha[1] >= quantidade):
            quantidade = linha[1]
    for linha in temp:
        if(linha[1] == quantidade):
            resultado.append(linha)
    return resultado

def buscaColuna(indice, valor):
    coluna = []
    for i in range(len(indice)):
        if valor in indice[i]:
            coluna.append(i)
    return coluna

def getMedia(dados, consideraNulo):
    soma = 0
    divisor = len(dados) - 1
    #temp.pop(0)
    for i in range(1, len(dados), 1):
        if(dados[i]):
            soma += int(dados[i])
        else:#se o dado for nulo, diminui o divisor
            if(consideraNulo == False):
                divisor -= 1
    media = soma/divisor
    return media
    
def getMediana(dados):
    vetOrdenado = sorted(dados)
    vMeio = []
    qAmostras = len(vetOrdenado)
    meio = qAmostras // 2
    res = 0
    if(qAmostras % 2 == 0):#se o numero de amostras for par [1,2,3,4,5]
        vMeio.append([int(vetOrdenado[meio-1]), int(vetOrdenado[meio])])
        res = ((vMeio[0][0]) + (vMeio[0][1]))/2
    else:
        vMeio.append(int(vetOrdenado[meio]))
        res = vMeio[0]
    #print("res",res)
    return res

def getMatrizColuna(dados, coluna):
    #print("teste:", dados[0])
    temp = dados
    col = []
    #temp.pop(0) #tirando o índice
    for linha in temp:
        x = 0
        try:
            x = int(linha[coluna])
            col.append(x)
        except:
            col.append(linha[coluna])
    return col
def escreveArquivo(conteudo, nomeArquivo):
    arquivo = open(nomeArquivo, "w")
    for j in range(len(conteudo)):
        saida = ""
        for i in range(len(conteudo[j])):
            saida += conteudo[j][i]
            if(i < len(conteudo[j]) - 1):
                saida  += ";"
        arquivo.writelines(saida)
    arquivo.close()
    return True

def quartil(dados, tipo):
    if(tipo ==  1):
        print("TODO")
    elif(tipo == 2):
        print("TODO")
    elif(tipo ==  3):
        print("TODO")
    else:
        print("TODO")

def deltaV(dados):
    print("TODO")

def desvioPadrao(dados, consideraNulo):
    temp = dados
    media = getMedia(dados, consideraNulo)
    temp = []
    somatorio = 0
    divisor = len(dados)
    for i in range(1, len(dados), 1):
        if(dados[i]):
            x = float(dados[i]) - media
            x = x**2
            somatorio += x
        else:
            if(consideraNulo == False):
                divisor -= 1
    somatorio = somatorio/divisor
    somatorio = math.sqrt(somatorio)
    return somatorio

def main():
    nomeArquivo = "base_ipea.csv"
    conteudo = lerArquivo(nomeArquivo)
    print("Conteúdo: ",conteudo[0])
    # c) A base é composta por quantas linhas e colunas?
    linhaColuna = linhaColunaBase(conteudo)
    print("Linhas: ",linhaColuna[0], "Colunas: ", linhaColuna[1])
    # d) Calcule a frequência de pessoas em cada região do Brasil.
    colunaRegiao = getMatrizColuna(conteudo, 0)
    #referencia = getDistinct(colunaRegiao)
    #print("Referência:",referencia)
    #frequencia = frequenciaDados(conteudo, 0, referencia)
    #print("Frequência: ",frequencia)
    # e) Qual é a região mais frequente (moda)?
    maiorFrequencia = getModa(colunaRegiao)
    print("Região mais frequente: ",maiorFrequencia[0][0]+",", "Frequência:", maiorFrequencia[0][1])
    # f) Qual é a idade da pessoa mais nova nessa amostra? E da mais velha?
    valor = "idade"
    #print("conteudo",conteudo[0])
    res = buscaColuna(conteudo[0], valor)
    reg = buscaColuna(conteudo[0], "região")
    #print("coluna(s) correspondente(s) à busca:", "região", reg)

    colunaIdade = getMatrizColuna(conteudo, res[0])
    #print("coluna(s) correspondente(s) à busca:", valor, res)
    maisNova = getMaisNova(colunaIdade)
    print("Idade da pessoa mais nova:", maisNova)
    maisVelha = getMaisVelho(colunaIdade)
    print("Idade da pessoa mais velha:", maisVelha)
    mediaIdade = getMedia(colunaIdade, 0)
    ci = getMatrizColuna(conteudo, res[0])
    ci.pop(0)
    print(ci)
    print("Media de idade: ", mediaIdade, statistics.mean(ci))
    modaIdade = getModa(colunaIdade)
    print("Moda: ", modaIdade[0][0]+",", "Frequência:", modaIdade[0][1])
    medianaIdade = getMediana(colunaIdade)
    svec = sorted(colunaIdade)
    print("Mediana:", medianaIdade)
    x = int(modaIdade[0][0])
    print(simetria(x, mediaIdade))
    conteudo = adicionaFaixaEtaria(nomeArquivo)
    arqSaida = "tabela_modificada.csv"
    #if(escreveArquivo(conteudo, arqSaida)):
        #print("A tabela foi modificada e salva como:", arqSaida)
    renda = buscaColuna(conteudo[0], "renda total de todos os moradores")
    colunaRenda = getMatrizColuna(conteudo, renda[0])
    desvio = desvioPadrao(colunaRenda, False)
    print(desvio)
main()
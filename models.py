from dynamodb_mapper.model import DynamoDBModel

class Analise(DynamoDBModel):
    __table__ = u"numerologia-ws-analises"
    __hash_key__ = u"nome"
    __schema__ = {
            u"nome": unicode,
            u"valor": int,
            u"resultado": unicode,
     }

class Numerologia:
    @staticmethod
    def analisar(nome):
	if not nome:
            raise Exception('Nome invalido!')
        dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':9,'K':10,'L':20,'M':30,'N':40,'O':50,'P':60,'Q':70,'R':80,'S':90,'T':100,'U':200,'V':200,'W':200,'X':300,'Y':300,'Z':400}
        letras = list(filter(lambda c: c.isalpha(), nome) )
        soma = 0
        for letra in letras:
            if not letra:
                continue
            elif letra.isspace() and not letra.isLetter():
                continue
            else:
                soma = soma + dic[letra.upper()]
        resultadoSoma = 0
        if soma <=  22:
            resultadoSoma = soma
        else:
            somaString = str(soma)
            somaFinal = 0
            letras = list(somaString)
            for letra in letras:
                somaFinal = somaFinal + float(letra)
            resultadoSoma = somaFinal
        excelente = {11,22,14,17,19,9,7,25}
        bom = {8,4,3,20,5,23}
        pessimo = {16,18,10,15,13,12,21}
        ruim = {6}
        if resultadoSoma in excelente:
            resultadoAnalise = 'EXCELENTE'
        elif resultadoSoma in bom:
            resultadoAnalise = 'BOM'
        elif resultadoSoma in pessimo:
            resultadoAnalise = 'PESSIMO'
        elif resultadoSoma in ruim:
            resultadoAnalise = 'RUIM'
        else:
            resultadoAnalise = 'NAO INTERPRETADO'
        analise = Analise()
        analise.nome = nome
        analise.valor = resultadoSoma
        analise.resultado = resultadoAnalise
        return analise

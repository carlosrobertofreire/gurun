# coding=UTF-8

from dynamodb_mapper.model import DynamoDBModel, utc_tz
from datetime import datetime
import pytz
from unicodedata import normalize

local_tz = pytz.timezone('America/Sao_Paulo')

def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    print local_tz.normalize(local_dt)
    return local_tz.normalize(local_dt)

def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII','ignore')

class Analise(DynamoDBModel):
    __table__ = u"numerologia-ws-analises"
    __hash_key__ = u"nome"
    __range_key__ = u"data"
    __schema__ = {
            u"nome": unicode,
            u"data": datetime,
            u"valor": float,
            u"resultado": unicode,
     }

class Numerologia:
    @staticmethod
    def analisar(nome):
	if not nome:
            raise Exception('Nome inválido!')
        nome = nome.upper()
        nomeSemAcentos = remover_acentos(nome)
        dic = {'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':9,'K':10,'L':20,'M':30,'N':40,'O':50,'P':60,'Q':70,'R':80,'S':90,'T':100,'U':200,'V':200,'W':200,'X':300,'Y':300,'Z':400}
        letras = list(filter(lambda c: c.isalpha(), nomeSemAcentos) )
        soma = 0
        for letra in letras:
            if not letra:
                continue
            elif letra.isspace() and not letra.isLetter():
                continue
            else:
                soma = soma + dic[letra]
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
        bom = {2,8,4,3,20,5,23,22}
        pessimo = {1,16,18,10,15,13,12,21}
        ruim = {6,24}
        if resultadoSoma in excelente:
            resultadoAnalise = 'EXCELENTE'
        elif resultadoSoma in bom:
            resultadoAnalise = 'BOM'
        elif resultadoSoma in pessimo:
            resultadoAnalise = 'PÉSSIMO'
        elif resultadoSoma in ruim:
            resultadoAnalise = 'RUIM'
        else:
            resultadoAnalise = 'NÃO INTERPRETADO'
        analise = Analise()
        analise.nome = nome
        analise.data = utc_to_local(datetime.now(utc_tz))
        analise.valor = resultadoSoma + 0.0
        analise.resultado = resultadoAnalise
        return analise

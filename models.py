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
    return normalize('NFKD', txt).encode('ASCII', 'ignore')


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


DICTIONARY = {
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 9,
    'K': 10,
    'L': 20,
    'M': 30,
    'N': 40,
    'O': 50,
    'P': 60,
    'Q': 70,
    'R': 80,
    'S': 90,
    'T': 100,
    'U': 200,
    'V': 200,
    'W': 200,
    'X': 300,
    'Y': 300,
    'Z': 400
}

INTERPRETACAO_EXCELENTE = {11, 22, 14, 17, 19, 9, 7, 25}
INTERPRETACAO_BOM = {2, 8, 4, 3, 20, 5, 23, 22}
INTERPRETACAO_PESSIMO = {1, 16, 18, 10, 15, 13, 12, 21}
INTERPRETACAO_RUIM = {6, 24}


class Numerologia:

    @staticmethod
    def calcular(nome):
        letras = list(filter(lambda c: c.isalpha(), nome))
        soma = 0
        for letra in letras:
            if not letra:
                continue
            elif letra.isspace() and not letra.isLetter():
                continue
            else:
                soma = soma + DICTIONARY[letra]
        resultadosoma = 0
        if soma <= 22:
            resultadosoma = soma
        else:
            somastring = str(soma)
            somafinal = 0
            letras = list(somastring)
            for letra in letras:
                somafinal = somafinal + float(letra)
            resultadosoma = somafinal
        return resultadosoma

    @staticmethod
    def analisar(nome):
        if not nome:
            raise Exception('Nome inválido!')
        nome = nome.upper()
        nome_sem_acentos = remover_acentos(nome)
        resultadosoma = Numerologia.calcular(nome_sem_acentos)
        if resultadosoma in INTERPRETACAO_EXCELENTE:
            interpretacao = 'EXCELENTE'
        elif resultadosoma in INTERPRETACAO_BOM:
            interpretacao = 'BOM'
        elif resultadosoma in INTERPRETACAO_PESSIMO:
            interpretacao = 'PÉSSIMO'
        elif resultadosoma in INTERPRETACAO_RUIM:
            interpretacao = 'RUIM'
        else:
            interpretacao = 'NÃO INTERPRETADO'
        analise = Analise()
        analise.nome = nome
        analise.data = utc_to_local(datetime.now(utc_tz))
        analise.valor = resultadosoma + 0.0
        analise.resultado = interpretacao
        return analise

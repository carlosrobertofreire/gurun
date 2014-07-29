# coding=UTF-8
from dynamodb_mapper.model import DynamoDBModel
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

# coding=UTF-8
from dynamodb_mapper.model import DynamoDBModel
from datetime import datetime


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

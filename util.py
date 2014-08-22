# coding=UTF-8
import pytz
import re
from unicodedata import normalize

local_tz = pytz.timezone('America/Sao_Paulo')


def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    print local_tz.normalize(local_dt)
    return local_tz.normalize(local_dt)


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore')


def remover_caracteres_especiais(txt):
    return re.sub('[^A-Za-zÀ-ú]+', ' ', txt)

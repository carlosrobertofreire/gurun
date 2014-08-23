# coding=UTF-8
import pytz
import string
from unicodedata import normalize

local_tz = pytz.timezone('America/Sao_Paulo')


def utc_to_local(utc_dt):
    local_dt = utc_dt.replace(tzinfo=pytz.utc).astimezone(local_tz)
    print local_tz.normalize(local_dt)
    return local_tz.normalize(local_dt)


def remover_acentos(txt):
    return normalize('NFKD', txt).encode('ASCII', 'ignore')


def remover_acentos_e_caracteres_especiais(txt):
    return ''.join(
        x for x in remover_acentos(txt)  \
            if (x in string.ascii_letters) or (x in string.whitespace)
    )

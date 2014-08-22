# coding=UTF-8
from flask.ext.restful import Resource, reqparse, fields, marshal_with
from util import remover_caracteres_especiais
from numerologia import analisar


analise_fields = {
    'nome': fields.String,
    'resultado': fields.String
}

class AnaliseAPI(Resource):

    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'nome',
            type=unicode,
            required=True,
            help='Nenhum nome informado.'
        )
        super(AnaliseAPI, self).__init__()

    @marshal_with(analise_fields)
    def post(self, **kwargs):
        args = self.reqparse.parse_args()
        nome = remover_caracteres_especiais(args['nome'])
        analisedb = analisar(nome)
        analisedb.resultado = analisedb.resultado.decode('utf-8')
        analisedb.save()
        return analisedb, 201

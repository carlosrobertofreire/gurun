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
        resultado = 0
        if soma <=  22:
            resultado = soma
        else:
            somaString = str(soma)
            somaFinal = 0
            letras = list(somaString)
            for letra in letras:
                somaFinal = somaFinal + float(letra)
            resultado = somaFinal
        excelente = {11,22,14,17,19,9,7,25}
        bom = {8,4,3,20,5,23}
        pessimo = {16,18,10,15,13,12,21}
        ruim = {6}
        if resultado in excelente:
            analise = 'EXCELENTE'
        elif resultado in bom:
            analise = 'BOM'
        elif resultado in pessimo:
            analise = 'PESSIMO'
        elif resultado in ruim:
            analise = 'RUIM'
        else:
            analise = 'NAO INTERPRETADO'
        return analise

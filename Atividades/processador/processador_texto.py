class ProcessadorTexto:

    def __init__(self, modo_processo:str):
        self.modo_processo = modo_processo
        self.__contador_linha = 0

    def processar(self, linha:str):
        if self.modo_processo == 'upper':
            return linha.upper()
        elif self.modo_processo == 'lower':
            return linha.lower()
        elif self.modo_processo == 'strip':
            while '  ' in linha:
                linha = linha.replace('  ', ' ')
            return f'{linha}\n'
        elif self.modo_processo == 'list':
            linha = f'{self.__contador_linha} | {linha}'
            self.__contador_linha += 1
            return linha
        return linha

from processador_texto import ProcessadorTexto

caminho = './processador/'

def main():

    modo = input('Digite os modos de processamento do texto (upper | lower | strip | list): ')
    entrada = input('Digite o nome do arquivo de entrada: ')
    saida = input('Digite o nome do arquivo de saída: ')

    try:
        processador = ProcessadorTexto(modo)

        with open(caminho + entrada, encoding='utf-8') as arq_entrada, \
             open(caminho + saida, mode='w', encoding='utf-8') as arq_saida:
            for linha in arq_entrada:
                linha_processada = processador.processar(linha)
                arq_saida.write(linha_processada)

        print('Programa encerrado com sucesso.')

    except FileNotFoundError:
        print('Erro: Arquivo de entrada não encontrado. Verifique o nome e tente novamente.')
    except Exception as e:
        print(f'Ocorreu um erro: {e}')

if __name__ == '__main__':
    main()

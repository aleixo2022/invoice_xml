import os
import time
from datetime import datetime
from glob import glob

import lxml
from bs4 import BeautifulSoup

''''
instalar dependencias cx_freeze
pip install cx-Freeze
devlopment:cxfreeze ./invoiceXml.py
production:python ./setup.py build
'''

inicio = time.time()

# substituir arquivo
alter = '''
<detPag>
<tPag>99</tPag>
</detPag>
'''
archive = sorted(glob(r'C:/xml_vendas/*.xml'))
totalFile = 0
# listando e contando arquivos xml
for i in archive:
    totalFile += 1

# apagando dados da pasta para alocar novos dados
# filelist = glob(r'C:/xml_vendas/*.xml')
# for f in filelist:
#     os.remove(f)


# função prinicipal para processar dados e alterar xml
def updateNF():
    # sub função que processa xml a xml
    def process_nf(nf, filename):

        with open(nf, 'r') as f:  # lendo arquivos
            file = f.read()
        # alterando valores no XML
        soup = BeautifulSoup(file, 'xml')
        # fazendo backup dos arquivos XML intactos
        with open('C:/xml_backup_alterados/venda_'+filename, 'w') as f:
            f.write(soup.prettify(formatter=None))
        cnpj = soup.emit.find_all('CNPJ')
        busc = soup.emit.find_all('CNPJ', string='36770176000170')
        if busc:
            for i in cnpj:
                i.string = '36770176000270'
        else:
            for i in cnpj:
                i.string = '17407833000274'

        # ean = soup.find_all('cEAN') informar todos os EAN
        tPagf = soup.find_all('tPag')
        if tPagf:
            # print("existe")
            soup.pag.tPag.string = '99'
        else:
            npag = soup.find_all('pag')
            for i in npag:
                i.string = "<detPag><tPag>99</tPag></detPag>"

        # print(soup.pag.prettify(formatter=None))
        # verificando cada SKU existente
        skuExist = soup.find_all('cProd')
        for sku in skuExist:
            ean = sku.find_next("cEAN")
            ean.string = sku.string

        # local de processamento principal do arquivo
        dcnpj = soup.dest.find_all('CNPJ')
        # fazendo backup dos alterados
        with open('C:/xml_backup_alterados/backup_'+filename, 'w') as f:
            f.write(soup.prettify(formatter=None))

        # salva o valor alterado no arquivo
        '''
        Se destinatario possui CNPJ então salva em processados caso contrario salva na pasta millennium.
        '''
        if dcnpj:
            with open('C:/xml_processados/'+filename, 'w') as f:
                f.write(soup.prettify(formatter=None))
        else:
            with open('D:/SYS/XML'+filename, 'w') as f:
                f.write(soup.prettify(formatter=None))
    '''
		buscar todos os arquivos a serem alterados
		'''
    file_list = sorted(glob(r'C:/xml_vendas/*.xml'))

    # listando arquivos xml
    for i in file_list:
        nf = i
        filename = os.path.basename(nf)
        process_nf(nf, filename)


updateNF()
# apagando dados da pasta vendas
filelist = glob(r'C:/xml_vendas/*.xml')
for f in filelist:
    os.remove(f)
fim = time.time()
with open('C:/xml_processados/log.txt', 'w') as f:
    f.write(
        f"Log de execução:\nTotal de Arquivos Processados:{totalFile}\n * O tempo de Execução foi de {fim - inicio}s.\n Data processamento: {datetime.now()}")

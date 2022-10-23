import os
import time
import lxml
from glob import glob
from bs4 import BeautifulSoup
from datetime import datetime

''''
instalar dependencias cx_freeze
pip install cx-Freeze


devlopment:cxfreeze ./invoiceXml.py
production:python ./setup.py build
'''

inicio = time.time()

#apagando dados da pasta para alocar novos dados
filelist = glob(r'C:/Users/alex/Downloads/Emitidas_Mercado_Livre/exe/data/*.xml')
for f in filelist:
    os.remove(f)

#função prinicipal para processar dados e alterar xml
def updateNF():	
	# sub função que processa xml a xml
		def process_nf(nf, filename):
		
					with open(nf, 'r') as f:
						file = f.read()
					# alterando valores no XML 
					soup = BeautifulSoup(file, 'xml') # BeautifulSoup
					cnpj = soup.find_all('CNPJ')
					for i in cnpj:
							i.string = '36770176000270'
					ean = soup.find_all('cEAN')
					for i in ean:
							i.string = soup.cProd.string
					tp = soup.find_all('tPag')
					for i in tp:
							i.string = '99'
					# salva o valor alterado no arquivo
					with open('C:/Users/alex/Downloads/Emitidas_Mercado_Livre/exe/data/'+filename, 'w') as f:
								f.write(soup.prettify())
		'''
		buscar todos os arquivos a serem alterados
		'''
		file_list = sorted(glob(r'C:/Users/alex/Downloads/Emitidas_Mercado_Livre/NF-e de venda/XML/Autorizadas/*.xml'))

		# listando arquivos xml
		for i in file_list:
			nf = i
			filename = os.path.basename(nf)
			process_nf(nf,filename)
            

updateNF()
fim = time.time()
with open('C:/Users/alex/Downloads/Emitidas_Mercado_Livre/exe/data/log.text', 'w') as f:
	f.write(f"Log de execução:\n * O tempo de Execução foi de {fim - inicio}.s\n Data processamento: {datetime.now()}")


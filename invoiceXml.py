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
totalFile=0
		# listando arquivos xml
for i in archive:
	totalFile+=1

 

alter_soup = BeautifulSoup(alter, 'xml') # BeautifulSoup
#apagando dados da pasta para alocar novos dados
filelist = glob(r'C:/xml_processados/*.xml')
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
					cnpj = soup.emit.find_all('CNPJ')
					for i in cnpj:
							i.string = '36770176000270'
					ean = soup.find_all('cEAN')
					for i in ean:
							i.string = soup.cProd.string

					if len(soup.pag.text) == 1:
						soup.pag.append(alter_soup)
					elif len(soup.pag.text)>= 2:
						soup.pag.string = ""
						soup.pag.append(alter_soup)
						
					# salva o valor alterado no arquivo
					with open('C:/xml_processados/'+filename, 'w') as f:
								f.write(soup.prettify())
		'''
		buscar todos os arquivos a serem alterados
		'''
		file_list = sorted(glob(r'C:/xml_vendas/*.xml'))

		# listando arquivos xml
		for i in file_list:
			nf = i
			filename = os.path.basename(nf)
			process_nf(nf,filename)
            

updateNF()
fim = time.time()
with open('C:/xml_processados/log.text', 'w') as f:
	f.write(f"Log de execução:\nTotal de Arquivos Processados:{totalFile}\n * O tempo de Execução foi de {fim - inicio}s.\n Data processamento: {datetime.now()}")
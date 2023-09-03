import re

def extract_numeros_nfe(root):
    numeros_nfe = []
    infNFe_elements = root.findall('.//{http://www.portalfiscal.inf.br/cte}infNFe')
    for infNFe_element in infNFe_elements:
        chave_element = infNFe_element.find('.//{http://www.portalfiscal.inf.br/cte}chave')
        if chave_element is not None:
            chave = chave_element.text[25:34].lstrip('0')
            numero_nfe = re.search(r'(\d+)', chave).group()  # Extrai os números da NFe usando expressões regulares
            numeros_nfe.append(numero_nfe)
    return numeros_nfe
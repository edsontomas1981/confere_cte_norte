import os
from extract_num_nf import extract_numeros_nfe
from extract_data_emissao_cte import extract_data_cte
from extract_destinatario import extract_destinatario
from extract_remetente import extract_remetente
from extract_informacoes_carga import extract_informacoes_carga
from extract_terceiro_tomador import extract_terceiro_tomador
from extract_valor_mercadoria import extract_valor_mercadoria
import pandas as pd
import xml.etree.ElementTree as ET
from verifica_inconsistencias_cte import verifica_cte


def gera_dict(pasta):
        # Especificar o caminho da pasta contendo os arquivos XML
    dados_cte={}
    # Iterar sobre todos os arquivos na pasta
    for arquivo in os.listdir(pasta):
        # Verificar se o arquivo tem extensão XML
        if arquivo.endswith('.xml'):
            # Obter o caminho completo do arquivo
            caminho_arquivo = os.path.join(pasta, arquivo)

            try:
                # Fazer o parsing do arquivo XML
                tree = ET.parse(caminho_arquivo)
                root = tree.getroot()
                namespace = {'cte': 'http://www.portalfiscal.inf.br/cte'}

                destinatario=extract_destinatario(root,namespace)
                remetente=extract_remetente(root,namespace)
                infCarga = extract_informacoes_carga(root, namespace)
                ncte = root.find('.//{http://www.portalfiscal.inf.br/cte}nCT').text
                total_prest = root.find('.//{http://www.portalfiscal.inf.br/cte}vTPrest').text
                tomador = root.find('.//{http://www.portalfiscal.inf.br/cte}toma').text
                numeros_nfe = extract_numeros_nfe(root)
                valor_nfs = extract_valor_mercadoria(root,namespace)
                data_emissao = extract_data_cte(root,namespace)

                if tomador == '4':
                    terceiro_tomador = extract_terceiro_tomador(root,namespace)

                if tomador == '0':
                    dados_cte[ncte]={'num_cte':ncte,'rem':remetente,'peso':infCarga['peso_faturado'],
                                    'm3':infCarga['m3'],'volumes':infCarga['volumes'],
                                    'frete':total_prest,'nf':numeros_nfe,'dest':destinatario,'notas':numeros_nfe,
                                    'valor':valor_nfs,'tomador':remetente,'data_emissao':data_emissao}
                elif tomador == '4':
                    dados_cte[ncte]={'num_cte':ncte,'rem':remetente,'peso':infCarga['peso_faturado'],
                                    'm3':infCarga['m3'],'volumes':infCarga['volumes'],'frete':total_prest,
                                    'nf':numeros_nfe,'dest':destinatario,'notas':numeros_nfe,
                                    'valor':valor_nfs,'tomador':terceiro_tomador,'data_emissao':data_emissao}
                else:
                    dados_cte[ncte]={'num_cte':ncte,'rem':remetente,'peso':infCarga['peso_faturado'],
                                    'm3':infCarga['m3'],'volumes':infCarga['volumes'],'frete':total_prest,
                                    'nf':numeros_nfe,'dest':destinatario,'notas':numeros_nfe,
                                    'valor':valor_nfs,'tomador':destinatario,'data_emissao':data_emissao}
            except Exception as e:
                print(f"Erro ao processar o arquivo {arquivo}: {str(e)}")

    df=pd.DataFrame(dados_cte)
    
    dados_totais = []
    for coluna in df.columns:
        num_cte = df[coluna]['num_cte']
        remetente = df[coluna]['rem']['Nome']
        cnpj_remetente = df[coluna]['rem']['CNPJ']
        destinatario = df[coluna]['dest']['Nome']
        cidade_destino = df[coluna]['dest']['Municipio']
        cnpj_destinatario = df[coluna]['dest']['CNPJ']
        tomador = df[coluna]['tomador']['Nome']
        cnpj_tomador = df[coluna]['tomador']['CNPJ'] 
        vlr_nfs = float(df[coluna]['valor'])
        volumes = float(df[coluna]['volumes'])
        m3 = float(df[coluna]['m3'])
        peso = float(df[coluna]['peso'])
        data_emissao_cte = df[coluna]['data_emissao']

    
        frete = float(df[coluna]['frete'])
        dados_totais.append({'num_cte':num_cte,'cnpj_tomador': cnpj_tomador,'tomador': tomador,
                            'cnpj_rem': cnpj_remetente,'remetente': remetente,
                            'cnpj_dest': cnpj_destinatario,'destinatario': destinatario,
                            'frete': frete,'vlr_nfs':vlr_nfs,'volumes':volumes,'peso':peso,'m3':m3,
                            'cidade_destino':cidade_destino})

    return dados_totais,dados_cte


# # # Exemplo de uso
# # pasta_ctes = "xml_ctes"
# # ctes,ctes_1 = gera_dict(pasta_ctes)

# verifica_cte(ctes)
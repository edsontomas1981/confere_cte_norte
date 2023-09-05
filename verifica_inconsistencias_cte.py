from cidades_atendidas import get_cidades_atendidas 

def verifica_cte(lista_ctes,dados):
    cte_erros=[]
    for cte in lista_ctes:
        if remetente_igual_destinatario(cte):
            cte_erros.append((f'{cte["num_cte"]}',(f'Mesmo remetente e destinatário.'),cte['cnpj_dest']))

        if verificar_cidade(cte['cidade_destino'], dados['filial']):
            cte_erros.append((f'{cte["num_cte"]}',(f'Não está vinculado à filial de carregamento correspondente.'),cte['cidade_destino']))

        if verificar_coleta_madeirao(cte):
            cte_erros.append(((f'{cte["num_cte"]}',(f'Provavelmente possui um valor de coleta no frete. Valor do frete: {cte["frete"]}'),cte["frete"])))

        if verificar_mo_galvao(cte):
            cte_erros.append(((cte["num_cte"],(f'Verificar m3 cliete M O Galvão.'),cte["m3"])))

        if verificar_peso_volumes(cte,dados['peso_maximo']):
            cte_erros.append((cte["num_cte"],(f'''Peso por volume kg, possivelmente desacordo com o peso real.'''),round(float(cte["peso"])/float(cte["volumes"]),2)))

        if verificar_frete_abaixo(cte,dados['valor_minimo']):            
            cte_erros.append((cte["num_cte"],(f'Frete por kg abaixo do normal'),round(float(cte["frete"])/float(cte["peso"]),2)))

        if verificar_frete_acima(cte,dados['valor_maximo']):            
            cte_erros.append((cte["num_cte"],(f'Frete por kg acima do normal'),round(float(cte["frete"])/float(cte["peso"]),2)))            
    
    return cte_erros


def remetente_igual_destinatario(cte):
    if cte['cnpj_dest'] == cte['cnpj_rem']:
        return True
    else:
        return False

def verificar_cidade(cidade, filial_esperada):
    dic_cidades = get_cidades_atendidas()
    if cidade.upper() in dic_cidades:
        filial_real = dic_cidades[cidade].upper()
        if filial_real.upper() == filial_esperada.upper():
            return False
        else:
            return  True
    else:
        return True
    
def verificar_coleta_madeirao(cte):
    if 'MADEIRAO'.upper() in cte['destinatario'].upper():
        if float(cte['frete']) > float(cte['peso']) and cte['frete']>100:
            return True
    else:
        return False
    
def verificar_mo_galvao(cte):
    if 'GALVAO ATACADISTA'.upper() in cte['destinatario'].upper():
        if not cte['m3']:
            return True
    else:
        return False

def verificar_peso_volumes(cte,peso_maximo):
    peso = float(cte['peso'])
    volumes = float(cte['volumes'])
    peso_por_volumes = peso/volumes
    if peso_por_volumes>peso_maximo:
        return True
    else:
        return False
    
def verificar_frete_abaixo(cte,valor_minimo):
    peso = float(cte['peso'])
    frete = float(cte['frete'])
    vlr_kg = frete/peso
    
    if vlr_kg < valor_minimo :
        return True
    else:
        return False
    
def verificar_frete_acima(cte,valor_maximo):
    peso = float(cte['peso'])
    frete = float(cte['frete'])
    vlr_kg = frete/peso
    
    if vlr_kg > valor_maximo and frete > 180 :
        return True
    else:
        return False



    
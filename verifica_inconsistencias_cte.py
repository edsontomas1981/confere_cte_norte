from cidades_atendidas import get_cidades_atendidas 

def verifica_cte(lista_ctes):
    cte_erros=[]
    for cte in lista_ctes:
        if remetente_igual_destinatario(cte):
            cte_erros.append(f'O CTe de número {cte["num_cte"]} apresenta o mesmo remetente e destinatário.')
        if verificar_cidade(cte['cidade_destino'], 'Teresina-PI'):
            cte_erros.append(f'O CTe de número {cte["num_cte"]} não está vinculado à filial de carregamento correspondente.')
        if verificar_coleta_madeirao(cte):
            cte_erros.append(f'O CTe de número {cte["num_cte"]} provavelmente possui um valor de coleta no frete. Valor do frete: {cte["frete"]}')
        if verificar_peso_volumes(cte):
            cte_erros.append(f'O CTe de número {cte["num_cte"]} tem um peso total de {cte["peso"]} kg. O peso dos volumes é de {float(cte["peso"])/float(cte["volumes"])} kg. O peso dos volumes é alto e pode não estar de acordo com o peso real. Favor verificar o peso dos volumes.')
        if verificar_frete_abaixo(cte):            
            cte_erros.append(f'O CTe de número {cte["num_cte"]} tem o frete por kg abaixo do normal,o valor por kg é R$ {round(float(cte["frete"])/float(cte["peso"]),2)}')
        if verificar_frete_acima(cte):            
            cte_erros.append(f'O CTe de número {cte["num_cte"]} tem o frete por kg acima do normal,o valor por kg é R$ {round(float(cte["frete"])/float(cte["peso"]),2)}')            
            
    print(len(cte_erros))

    for erro in cte_erros:
        print(erro)
    


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
        if float(cte['frete']) > float(cte['peso']):
            return True
    else:
        return False

def verificar_peso_volumes(cte):
    peso = float(cte['peso'])
    volumes = float(cte['volumes'])
    peso_por_volumes = peso/volumes
    if peso_por_volumes>75.00:
        return True
    else:
        return False
    
def verificar_frete_abaixo(cte):
    peso = float(cte['peso'])
    frete = float(cte['frete'])
    vlr_kg = frete/peso
    
    if vlr_kg < 0.8 :
        return True
    else:
        return False
    
def verificar_frete_acima(cte):
    peso = float(cte['peso'])
    frete = float(cte['frete'])
    vlr_kg = frete/peso
    
    if vlr_kg > 1.7 :
        return True
    else:
        return False



    
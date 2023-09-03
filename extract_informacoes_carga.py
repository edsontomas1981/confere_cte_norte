def extract_informacoes_carga(root, namespace):
    vols = 0
    peso_faturado = 0
    m3 = 0
    informacoes_carga = {}
    infCarga = root.find('.//cte:infCarga', namespace)
    if infCarga is not None:
        for infQ in infCarga.findall('.//cte:infQ', namespace):
            tpMed = infQ.find('cte:tpMed', namespace)
            qCarga = infQ.find('cte:qCarga', namespace)
            if tpMed is not None and tpMed.text:
                if qCarga is not None and qCarga.text:
                    if tpMed.text == 'Volumes':
                        vols += float(qCarga.text)
                    elif tpMed.text == 'Peso Faturado':
                        peso_faturado += float(qCarga.text)
                    elif tpMed.text == 'Metro Cubico':
                        m3 += float(qCarga.text)
            else:
                print("Elemento tpMed não encontrado.")
    else:
        print("Elemento infCarga não encontrado.")
    
    informacoes_carga['volumes'] = vols
    informacoes_carga['peso_faturado'] = peso_faturado
    informacoes_carga['m3'] = m3

    return informacoes_carga

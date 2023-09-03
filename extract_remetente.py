def extract_remetente(root, namespace):
    remetente = {}
    rem = root.find('.//cte:rem', namespace)
    if rem is not None:
        CNPJ = rem.find('.//cte:CNPJ', namespace)
        xNome = rem.find('.//cte:xNome', namespace)
        enderReme = rem.find('.//cte:enderReme', namespace)
        xLgr = enderReme.find('.//cte:xLgr', namespace)
        nro = enderReme.find('.//cte:nro', namespace)
        xBairro = enderReme.find('.//cte:xBairro', namespace)
        cMun = enderReme.find('.//cte:cMun', namespace)
        xMun = enderReme.find('.//cte:xMun', namespace)
        CEP = enderReme.find('.//cte:CEP', namespace)
        UF = enderReme.find('.//cte:UF', namespace)
        cPais = enderReme.find('.//cte:cPais', namespace)
        xPais = enderReme.find('.//cte:xPais', namespace)
        
        if CNPJ is not None and CNPJ.text:
            remetente['CNPJ'] = CNPJ.text
        if xNome is not None and xNome.text:
            remetente['Nome'] = xNome.text
        if xLgr is not None and xLgr.text:
            remetente['Endereco'] = xLgr.text
        if nro is not None and nro.text:
            remetente['Numero'] = nro.text
        if xBairro is not None and xBairro.text:
            remetente['Bairro'] = xBairro.text
        if cMun is not None and cMun.text:
            remetente['CodigoMunicipio'] = cMun.text
        if xMun is not None and xMun.text:
            remetente['Municipio'] = xMun.text
        if CEP is not None and CEP.text:
            remetente['CEP'] = CEP.text
        if UF is not None and UF.text:
            remetente['UF'] = UF.text
        if cPais is not None and cPais.text:
            remetente['CodigoPais'] = cPais.text
        if xPais is not None and xPais.text:
            remetente['Pais'] = xPais.text
    return remetente

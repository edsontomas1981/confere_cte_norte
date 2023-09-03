def extract_destinatario(root, namespace):
    destinatario = {}
    dest = root.find('.//cte:dest', namespace)
    if dest is not None:
        CNPJ = dest.find('.//cte:CNPJ', namespace)
        CPF = dest.find('.//cte:CPF', namespace)
        xNome = dest.find('.//cte:xNome', namespace)
        enderDest = dest.find('.//cte:enderDest', namespace)
        xLgr = enderDest.find('.//cte:xLgr', namespace)
        nro = enderDest.find('.//cte:nro', namespace)
        xBairro = enderDest.find('.//cte:xBairro', namespace)
        cMun = enderDest.find('.//cte:cMun', namespace)
        xMun = enderDest.find('.//cte:xMun', namespace)
        CEP = enderDest.find('.//cte:CEP', namespace)
        UF = enderDest.find('.//cte:UF', namespace)
        cPais = enderDest.find('.//cte:cPais', namespace)
        xPais = enderDest.find('.//cte:xPais', namespace)

        if CNPJ is not None:
            destinatario['CNPJ'] = CNPJ.text or ''

        if CPF is not None and CPF.text:
            destinatario['CNPJ'] = CPF.text

        if xNome is not None and xNome.text:
            destinatario['Nome'] = xNome.text
        if xLgr is not None and xLgr.text:
            destinatario['Endereco'] = xLgr.text
        if nro is not None and nro.text:
            destinatario['Numero'] = nro.text
        if xBairro is not None and xBairro.text:
            destinatario['Bairro'] = xBairro.text
        if cMun is not None and cMun.text:
            destinatario['CodigoMunicipio'] = cMun.text
        if xMun is not None and xMun.text:
            destinatario['Municipio'] = xMun.text
        if CEP is not None and CEP.text:
            destinatario['CEP'] = CEP.text
        if UF is not None and UF.text:
            destinatario['UF'] = UF.text
        if cPais is not None and cPais.text:
            destinatario['CodigoPais'] = cPais.text
        if xPais is not None and xPais.text:
            destinatario['Pais'] = xPais.text
    return destinatario

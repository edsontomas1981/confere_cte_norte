def extract_terceiro_tomador(root, namespace):
    tomador_3 = {}
    toma = root.find('.//cte:toma4', namespace)
    if toma is not None:
        CNPJ = toma.find('.//cte:CNPJ', namespace)
        xNome = toma.find('.//cte:xNome', namespace)
        enderToma = toma.find('.//cte:enderToma', namespace)
        xLgr = enderToma.find('.//cte:xLgr', namespace)
        nro = enderToma.find('.//cte:nro', namespace)
        xBairro = enderToma.find('.//cte:xBairro', namespace)
        cMun = enderToma.find('.//cte:cMun', namespace)
        xMun = enderToma.find('.//cte:xMun', namespace)
        CEP = enderToma.find('.//cte:CEP', namespace)
        UF = enderToma.find('.//cte:UF', namespace)
        cPais = enderToma.find('.//cte:cPais', namespace)
        xPais = enderToma.find('.//cte:xPais', namespace)

        if CNPJ is not None and CNPJ.text:
            tomador_3['CNPJ'] = CNPJ.text
        if xNome is not None and xNome.text:
            tomador_3['Nome'] = xNome.text
        if xLgr is not None and xLgr.text:
            tomador_3['Endereco'] = xLgr.text
        if nro is not None and nro.text:
            tomador_3['Numero'] = nro.text
        if xBairro is not None and xBairro.text:
            tomador_3['Bairro'] = xBairro.text
        if cMun is not None and cMun.text:
            tomador_3['CodigoMunicipio'] = cMun.text
        if xMun is not None and xMun.text:
            tomador_3['Municipio'] = xMun.text
        if CEP is not None and CEP.text:
            tomador_3['CEP'] = CEP.text
        if UF is not None and UF.text:
            tomador_3['UF'] = UF.text
        if cPais is not None and cPais.text:
            tomador_3['CodigoPais'] = cPais.text
        if xPais is not None and xPais.text:
            tomador_3['Pais'] = xPais.text
    return tomador_3
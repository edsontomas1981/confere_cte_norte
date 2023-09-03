def extract_valor_mercadoria(root, namespace):
    valor_mercadoria = 0.0
    det_elements = root.findall('.//cte:infCarga', namespace)
    for det_element in det_elements:
        vProd_element = det_element.find('.//cte:vCarga', namespace)
        if vProd_element is not None and vProd_element.text:
            valor_mercadoria += float(vProd_element.text)
    return valor_mercadoria

from datetime import datetime
def extract_data_cte(root, namespace):
    data = root.find('.//cte:dhEmi', namespace)
    data_formatada=datetime.strptime(data.text, "%Y-%m-%dT%H:%M:%S%z")
    return data_formatada

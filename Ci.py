from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import webbrowser


def imprimir_documento():

    # Texto com quebras de linha
    texto_com_quebras = """
    <br />
    <br />
    <br />
    """
    logo_image = Image("logonorte.jpg", width=75, height=12)
    logo_image.hAlign = 'LEFT'
    # Dados do documento
    empresa_nome = "SERAFIM TRANSPORTE DE CARGAS LTDA"
    empresa_endereco = "Rua : Nova Veneza,172 Cumbica – Guarulhos-SP"
    empresa_telefones = "Tel(11)2481-9121/2481-9697/2412-4886/2412-3927"
    comunicacao_interna = "COMUNICAÇÃO INTERNA Nº 1138"
    origem_destino =  "SPO - THE"
    data = "02/09/2023"
    destinatario = "Srº Serafim"
    manifesto_numero = "4691 – THE"
    valor_a_ser_pago = "R$ 28.000,00"
    responsavel_pagamento = "Jasciano de Oliveira Rodrigues"
    conhecimentos_frete = "CIF e FOB"
    caixas_destinatario = "Srº Ewaldo Alves da Silva"
    transportadora = "Nortecargas – SP"

    # Configurar o PDF
    pdf_filename = "documento.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    story = []

    # Estilos de texto
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    normal_style.alignment = 0  # 0 = left, 1 = center, 2 = right

    h1 = styles['Heading1']
    h1.alignment = 1  # 0 = left, 1 = center, 2 = right
    h2 = styles['Heading2']
    h2.alignment = 1  # 0 = left, 1 = center, 2 = right
    h3 = styles['Heading3']     
    h3.alignment = 1  # 0 = left, 1 = center, 2 = right
    h5 = styles['Heading5']         
    h5.alignment = 1  # 0 = left, 1 = center, 2 = right
    h6 = styles['Heading6']         
    h6.alignment = 1  # 0 = left, 1 = center, 2 = right


    # Inserir a imagem no documento
    story.append(logo_image)

    # Criar um objeto Paragraph com o texto
    story.append(Paragraph(texto_com_quebras, normal_style))

    # # Adicionar texto ao documento
    # story.append(Paragraph('Comunicação Interna', h1))
    story.append(Paragraph(empresa_nome, h1))
    story.append(Paragraph(empresa_endereco, h5))
    story.append(Paragraph(empresa_telefones, h5))
    story.append(Paragraph("", normal_style))  # Linha em branco
    # Criar um objeto Paragraph com o texto
    story.append(Paragraph(texto_com_quebras, normal_style))

    story.append(Paragraph(comunicacao_interna, h3))
    story.append(Paragraph(f"Data : {data} Percurso : {origem_destino}", h5))

    # Criar um objeto Paragraph com o texto     
    story.append(Paragraph(texto_com_quebras, normal_style))

    texto = f"{destinatario},<br /><br />" \
            f"Estamos enviando o manifesto de transporte de cargas nº {manifesto_numero}. Este manifesto inclui conhecimentos de frete {conhecimentos_frete}.<br /><br />" \
            f"De acordo com este manifesto, solicitamos o pagamento de R$ {valor_a_ser_pago} ao motorista {responsavel_pagamento}, referente à Ordem de Pagamento (OP).<br /><br />" \
            f"Para mais informações, entre em contato conosco na transportadora {transportadora}.<br /><br />"


    observacao =f"Também informamos que estamos despachando 12 caixas que estão aos cuidados do. {caixas_destinatario}.<br /><br />" \

    story.append(Paragraph(texto, normal_style))
    story.append(Paragraph(observacao, normal_style))

    # Criar um objeto Paragraph com o texto     
    story.append(Paragraph(texto_com_quebras, normal_style))

    # Criar um objeto Paragraph com o texto     
    story.append(Paragraph(texto_com_quebras, normal_style))


    story.append(Paragraph(transportadora, normal_style))

    # Gerar o PDF
    doc.build(story)

if __name__ == "__main__":
    imprimir_documento()

    # Após gerar o PDF, abrir automaticamente para impressão
    pdf_filename = "documento.pdf"
    try:
        webbrowser.open(pdf_filename)
    except Exception as e:
        print(f"Erro ao abrir o PDF: {e}")

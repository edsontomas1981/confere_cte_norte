from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import webbrowser



def imprimir_relatorio(ctes,fretes,clientes):

    empresa_nome = "SERAFIM TRANSPORTE DE CARGAS LTDA"
    empresa_endereco = "Rua : Nova Veneza,172 Cumbica – Guarulhos-SP"
    empresa_telefones = "Tel(11)2481-9121/2481-9697/2412-4886/2412-3927"
    assinatura = "Nortecargas – SP"

    # Texto com quebras de linha
    texto_com_quebras = """
    <br />
    <br />
    <br />
    """

    # Configurar o PDF
    pdf_filename = "documento.pdf"
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    story = []
    logo_image = Image("logonorte.jpg", width=75, height=12)
    logo_image.hAlign = 'LEFT'


    # Estilos de texto
    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]
    normal_style.alignment = 0  # 0 = left, 1 = center, 2 = right
    normal_style.fontSize = 12  # Tamanho da fonte (por exemplo, 12)

    # Defina o espaçamento entre as linhas (leading)
    normal_style.leading = 20  # Altere esse valor para ajustar o espaçamento desejado

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
    
    story.append(Paragraph('Diversos', h5))

    for cte in ctes:
        story.append(Paragraph(f'Cte : {cte[0]} Descrição : {cte[1]} Valor : {cte[2]}', normal_style))
        # story.append(Paragraph(linha, normal_style))

    story.append(Paragraph('Fretes', h5))

    for frete in fretes:
        story.append(Paragraph(f'Cte : {frete[0]} Descrição : {frete[1]} Valor : {frete[2]}', normal_style))
        # story.append(Paragraph(linha, normal_style))
    story.append(Paragraph('Clientes', h5))

    for cliente in clientes:
        story.append(Paragraph(f'Cte : {cliente[0]} Descrição : {cliente[1]} Valor : {cliente[2]}', normal_style))
        # story.append(Paragraph(linha, normal_style))

    # Gerar o PDF
    doc.build(story)




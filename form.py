from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton

KV = '''
BoxLayout:
    orientation: 'vertical'

    MDBoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: dp(56)  # Altura da barra de título

        MDRaisedButton:
            text: 'Formulário de Impressão'

    ScrollView:
        GridLayout:
            cols: 2
            padding: dp(16)
            spacing: dp(16)

            MDLabel:
                text: 'Destinatário:'
            MDTextField:
                id: destinatario

            MDLabel:
                text: 'Número do Manifesto:'
            MDTextField:
                id: manifesto_numero

            MDLabel:
                text: 'Valor a ser Pago:'
            MDTextField:
                id: valor_a_ser_pago

            MDLabel:
                text: 'Responsável pelo Pagamento:'
            MDTextField:
                id: responsavel_pagamento

            MDLabel:
                text: 'Conhecimentos de Frete:'
            MDTextField:
                id: conhecimentos_frete

            MDLabel:
                text: 'Cuidados do Destinatário:'
            MDTextField:
                id: caixas_destinatario

            MDRaisedButton:
                text: 'Imprimir'
                on_release: app.imprimir_formulario()


'''


class FormularioApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def imprimir_formulario(self):
        destinatario = self.root.ids.destinatario.text
        manifesto_numero = self.root.ids.manifesto_numero.text
        valor_a_ser_pago = self.root.ids.valor_a_ser_pago.text
        responsavel_pagamento = self.root.ids.responsavel_pagamento.text
        conhecimentos_frete = self.root.ids.conhecimentos_frete.text
        caixas_destinatario = self.root.ids.caixas_destinatario.text

        # Agora você pode usar esses valores para criar a impressão do documento

        # Exemplo de impressão dos dados
        print(f"Destinatário: {destinatario}")
        print(f"Número do Manifesto: {manifesto_numero}")
        print(f"Valor a ser Pago: {valor_a_ser_pago}")
        print(f"Responsável pelo Pagamento: {responsavel_pagamento}")
        print(f"Conhecimentos de Frete: {conhecimentos_frete}")
        print(f"Cuidados do Destinatário: {caixas_destinatario}")


if __name__ == '__main__':
    FormularioApp().run()

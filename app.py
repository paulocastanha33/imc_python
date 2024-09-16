import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap

class IMCApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(IMCApp, self).__init__()
        # Carrega a interface do Qt Designer
        uic.loadUi('imc.ui', self)  
        # Configura a imagem da seta que indicará o resultado do imc na listagem
        self.seta_pixmap = QPixmap('seta.png')  
        self.seta.setPixmap(self.seta_pixmap)
        
        # Conectar o botão "Calcular" com a função de cálculo
        self.btn_calcular.clicked.connect(self.calcular_imc)
         # Conectar o botão "Limpar" com a função limpar
        self.pushButton_limpar.clicked.connect(self.limpar)
        
        # Define a ordem de tabulação
        self.setTabOrder(self.input_peso, self.input_altura)
        self.setTabOrder(self.input_altura, self.btn_calcular)
        self.setTabOrder(self.btn_calcular, self.pushButton_limpar)    

    def calcular_imc(self):
        try:
            # Coleta os valores de peso e altura
            peso = float(self.input_peso.text())
            altura = float(self.input_altura.text())
            
            # Calcula o IMC
            imc = peso / (altura ** 2)
            
            # Exibe o resultado
            self.label_resultado.setText(f"IMC: {imc:.2f}")
            
            # Define a faixa do IMC e ajusta a seta para posição do label referente
            if imc < 17:
                faixa = "Muito Abaixo do Peso ( imc < 17 )"
                self.seta.move(536, 117)  
            elif 17 <= imc < 18.5:
                faixa = "Abaixo do Peso ( 17 <= imc < 18.5 )"
                self.seta.move(536, 150)  
            elif 18.5 <= imc < 25:
                faixa = "Normal (18.5 <= imc < 25)"
                self.seta.move(536, 184)  
            elif 25 <= imc < 30:
                faixa = "Acima do Peso (25 <= imc < 30)"
                self.seta.move(536, 220) 
            elif 30 <= imc < 35:
                faixa = "Obesidade I (30 <= imc < 35)"
                self.seta.move(536, 256)  
            elif 35 <= imc < 40:
                faixa = "Obesidade II (severa)(35 <= imc < 40)"
                self.seta.move(536, 291) 
            else:
                faixa = "Obesidade III (mórbida)(imc > 40)"
                self.seta.move(536, 324) 
            
            # Atualiza o texto do rótulo
            self.label_faixa.setText(faixa)
        except ValueError:
            self.label_resultado.setText("Valores inválidos")
            self.label_faixa.setText("")

    def limpar(self):
        """Limpa os campos de entrada e reseta os labels, a posição da seta e coloca o foco no campo
        peso."""
        self.input_peso.clear()
        self.input_altura.clear()
        self.label_resultado.clear()
        self.label_faixa.clear()
        self.seta.move(536, 79)  
        self.input_peso.setFocus() 

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = IMCApp()
    window.show()
    sys.exit(app.exec_())

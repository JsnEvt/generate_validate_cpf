from typing import Mapping
import sys
from validador_cpf import valida_cpf
from gerador_cpf import gerador_cpf
from PyQt5.QtWidgets import QApplication, QMainWindow

import design


class GeraValidaCPF(QMainWindow, design.Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)

        self.btn_gerar.clicked.connect(self.gera_cpf)
        self.btn_valida.clicked.connect(self.valida_cpf)

    def gera_cpf(self):
        self.Retorno.setText(
            str(gerador_cpf())
        )

    def valida_cpf(self):  # aqui e uma funcao chamada na propria classe.
        cpf = self.inputValidaCPF.text()
        self.Retorno.setText(
            # aqui, o valida cpf usa o codigo fonte para realizar a validacao
            str(valida_cpf(cpf))
        )


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    gera_cpf = GeraValidaCPF()
    gera_cpf.show()
    qt.exec_()

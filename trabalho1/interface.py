from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QSplitter, QFrame, QLineEdit, QComboBox, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np
from metodos import cenarios, f, newtonRaphson, secante, posicaoFalsa

metodos = {
    "Newton-Raphson": newtonRaphson,
    "Secante": secante,
    "Posição Falsa": posicaoFalsa
}

class MainWindow(QWidget):
    '''Janela principal'''
    def __init__(self):
        super().__init__()
        # Controles
        self.label_cenario = QLabel('Cenário:')
        self.combo_cenario = QComboBox()
        self.combo_cenario.addItems(list(cenarios.keys()))
        self.combo_cenario.currentTextChanged.connect(self.carrega_cenario)
        self.label_metodo = QLabel('Método:')
        self.combo_metodo = QComboBox()
        self.combo_metodo.addItems(list(metodos.keys()))
        self.label_a = QLabel('a (m/s²):')
        self.edit_a = QLineEdit()
        self.label_tr = QLabel('tr (s):')
        self.edit_tr = QLineEdit()
        self.label_cm = QLabel('cm (1/m):')
        self.edit_cm = QLineEdit()
        self.label_D = QLabel('D (m):')
        self.edit_D = QLineEdit()
        self.label_ini = QLabel('Início do intervalo:')
        self.edit_ini = QLineEdit('0')
        self.label_fim = QLabel('Fim do intervalo:')
        self.edit_fim = QLineEdit('40')
        self.label_tol = QLabel('Tolerância:')
        self.edit_tol = QLineEdit('1e-6')
        self.label_n = QLabel('Máx. de iterações:')
        self.edit_n = QLineEdit('50')
        self.button_gerar = QPushButton('Calcular e gerar gráfico')
        self.button_gerar.clicked.connect(self.gera_grafico)
        self.espaco = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        # Layout e frame da esquerda
        layout_controles = QVBoxLayout()
        layout_controles.addWidget(self.label_cenario)
        layout_controles.addWidget(self.combo_cenario)
        layout_controles.addWidget(self.label_metodo)
        layout_controles.addWidget(self.combo_metodo)
        layout_controles.addWidget(self.label_a)
        layout_controles.addWidget(self.edit_a)
        layout_controles.addWidget(self.label_tr)
        layout_controles.addWidget(self.edit_tr)
        layout_controles.addWidget(self.label_cm)
        layout_controles.addWidget(self.edit_cm)
        layout_controles.addWidget(self.label_D)
        layout_controles.addWidget(self.edit_D)
        layout_controles.addWidget(self.label_ini)
        layout_controles.addWidget(self.edit_ini)
        layout_controles.addWidget(self.label_fim)
        layout_controles.addWidget(self.edit_fim)
        layout_controles.addWidget(self.label_tol)
        layout_controles.addWidget(self.edit_tol)
        layout_controles.addWidget(self.label_n)
        layout_controles.addWidget(self.edit_n)
        layout_controles.addWidget(self.button_gerar)
        layout_controles.addItem(self.espaco)
        frame_controles = QFrame()
        frame_controles.setLayout(layout_controles)
        # Gráfico
        self.figura = Figure(figsize=(5, 4), dpi=100)
        self.canvas = FigureCanvasQTAgg(self.figura)
        # Splitter
        splitter = QSplitter(Qt.Horizontal)
        splitter.addWidget(frame_controles)
        splitter.addWidget(self.canvas)
        splitter.setSizes([250, 600])
        # Layout da janela
        layout_principal = QVBoxLayout(self)
        layout_principal.addWidget(splitter)
        self.setWindowTitle('Velocidade segura')
        self.carrega_cenario(self.combo_cenario.currentText())

    def carrega_cenario(self, nome):
        '''Preenche os campos com o cenário escolhido'''
        self.edit_a.setText(str(cenarios[nome]["a"]))
        self.edit_tr.setText(str(cenarios[nome]["tr"]))
        self.edit_cm.setText(str(cenarios[nome]["cm"]))
        self.edit_D.setText(str(cenarios[nome]["D"]))

    def gera_grafico(self):
        '''Calcula a raiz e gera o gráfico'''
        # Limpa o gráfico anterior e cria um novo
        self.figura.clear()
        ax = self.figura.add_subplot(111)
        # Pega os dados
        a = float(self.edit_a.text())
        tr = float(self.edit_tr.text())
        cm = float(self.edit_cm.text())
        D = float(self.edit_D.text())
        inicio = float(self.edit_ini.text())
        fim = float(self.edit_fim.text())
        tol = float(self.edit_tol.text())
        n = int(self.edit_n.text())
        metodo = metodos[self.combo_metodo.currentText()]
        # Calcula a raiz (a tabela de iterações é impressa no terminal)
        raiz = metodo(inicio, fim, tol, n, a, tr, cm, D)
        lista_pontos = np.linspace(inicio, fim, 400)
        ax.grid()
        ax.plot(lista_pontos, f(lista_pontos, a, tr, cm, D), label='f(v)', color='purple')
        ax.axhline(0, color='black', linewidth=1)
        ax.plot(raiz, 0, 'ro', label=f'raiz: v = {raiz:.2f} m/s ({raiz * 3.6:.1f} km/h)')
        ax.set_title(f'Velocidade segura: {raiz * 3.6:.1f} km/h')
        ax.legend()
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
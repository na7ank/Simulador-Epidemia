'''
    Exemplo de implementação do modelo S.I.R
    (S) --> (I) --> (R)

    Por: NATAN
'''

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QTime, Qt
from pyqtgraph import PlotWidget,  BarGraphItem 
import pyqtgraph as pg
import pyqtgraph.exporters

import numpy as np

from scipy.integrate import odeint # Este módulo nos ajudara a resolver as integrai


class Ui_SIRepidemias(object):
    def setupUi(self, SIRepidemias):
        SIRepidemias.setObjectName("SIRepidemias")
        SIRepidemias.resize(960, 593)
        SIRepidemias.setMinimumSize(QtCore.QSize(960, 593))
        SIRepidemias.setMaximumSize(QtCore.QSize(960, 593))
        self.centralwidget = QtWidgets.QWidget(SIRepidemias)
        self.centralwidget.setMinimumSize(QtCore.QSize(960, 593))
        self.centralwidget.setMaximumSize(QtCore.QSize(960, 593))
        self.centralwidget.setStyleSheet("background-color: rgb(203, 203, 203);")
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 10, 941, 551))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_left = QtWidgets.QFrame(self.frame)
        self.frame_left.setGeometry(QtCore.QRect(0, 0, 281, 571))
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.variaveis = QtWidgets.QFrame(self.frame_left)
        self.variaveis.setGeometry(QtCore.QRect(0, 10, 271, 481))
        self.variaveis.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.variaveis.setFrameShadow(QtWidgets.QFrame.Raised)
        self.variaveis.setObjectName("variaveis")
        self.frame_4 = QtWidgets.QFrame(self.variaveis)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 261, 71))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setMinimumSize(QtCore.QSize(0, 20))
        self.label.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label.setStyleSheet("font: 14pt \"Chandas\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.SPopula = QtWidgets.QSpinBox(self.frame_4)
        self.SPopula.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SPopula.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"font: 15pt \"Chandas\";\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"color: rgb(238, 238, 236);\n"
"")
        self.SPopula.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SPopula.setMaximum(1000000)
        self.SPopula.setProperty("value", 1000)
        self.SPopula.setObjectName("SPopula")
        self.verticalLayout.addWidget(self.SPopula)
        self.frame_5 = QtWidgets.QFrame(self.variaveis)
        self.frame_5.setGeometry(QtCore.QRect(0, 70, 261, 71))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setMinimumSize(QtCore.QSize(0, 20))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_2.setStyleSheet("font: 15pt \"Chandas\";")
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.SProbContato = QtWidgets.QDoubleSpinBox(self.frame_5)
        self.SProbContato.setMinimumSize(QtCore.QSize(100, 0))
        self.SProbContato.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SProbContato.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"font: 15pt \"Chandas\";\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"color: rgb(238, 238, 236);\n"
"")
        self.SProbContato.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SProbContato.setDecimals(2)
        self.SProbContato.setMaximum(1.0)
        self.SProbContato.setSingleStep(0.01)
        self.SProbContato.setProperty("value", 0.3)
        self.SProbContato.setObjectName("SProbContato")
        self.verticalLayout_2.addWidget(self.SProbContato)
        self.frame_7 = QtWidgets.QFrame(self.variaveis)
        self.frame_7.setGeometry(QtCore.QRect(0, 210, 261, 71))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame_7)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_4.setStyleSheet("font: 15pt \"Chandas\";")
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.SMaxSaude = QtWidgets.QSpinBox(self.frame_7)
        self.SMaxSaude.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SMaxSaude.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"font: 15pt \"Chandas\";\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"color: rgb(238, 238, 236);\n"
"")
        self.SMaxSaude.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SMaxSaude.setMinimum(0)
        self.SMaxSaude.setMaximum(1000000)
        self.SMaxSaude.setProperty("value", 300)
        self.SMaxSaude.setObjectName("SMaxSaude")
        self.verticalLayout_4.addWidget(self.SMaxSaude)
        self.frame_8 = QtWidgets.QFrame(self.variaveis)
        self.frame_8.setGeometry(QtCore.QRect(0, 140, 261, 71))
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.frame_8)
        self.label_6.setMinimumSize(QtCore.QSize(0, 20))
        self.label_6.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_6.setStyleSheet("font: 15pt \"Chandas\";")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.SProbRec = QtWidgets.QDoubleSpinBox(self.frame_8)
        self.SProbRec.setMinimumSize(QtCore.QSize(100, 0))
        self.SProbRec.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SProbRec.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"font: 15pt \"Chandas\";\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"color: rgb(238, 238, 236);\n"
"")
        self.SProbRec.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SProbRec.setDecimals(2)
        self.SProbRec.setMaximum(1.0)
        self.SProbRec.setSingleStep(0.01)
        self.SProbRec.setProperty("value", 0.1)
        self.SProbRec.setObjectName("SProbRec")
        self.verticalLayout_5.addWidget(self.SProbRec)
        self.frame_9 = QtWidgets.QFrame(self.variaveis)
        self.frame_9.setGeometry(QtCore.QRect(0, 280, 261, 71))
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.frame_9)
        self.label_7.setMinimumSize(QtCore.QSize(0, 20))
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_7.setStyleSheet("font: 15pt \"Chandas\";")
        self.label_7.setObjectName("label_7")
        self.verticalLayout_6.addWidget(self.label_7)
        self.SDias = QtWidgets.QSpinBox(self.frame_9)
        self.SDias.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SDias.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"font: 15pt \"Chandas\";\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"color: rgb(238, 238, 236);\n"
"")
        self.SDias.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SDias.setMinimum(0)
        self.SDias.setMaximum(1000000)
        self.SDias.setProperty("value", 400)
        self.SDias.setObjectName("SDias")
        self.verticalLayout_6.addWidget(self.SDias)
        self.frame_10 = QtWidgets.QFrame(self.variaveis)
        self.frame_10.setGeometry(QtCore.QRect(0, 350, 261, 71))
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.frame_10)
        self.label_8.setMinimumSize(QtCore.QSize(0, 20))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setStyleSheet("font: 15pt \"Chandas\";")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_7.addWidget(self.label_8)
        self.SInfectados = QtWidgets.QSpinBox(self.frame_10)
        self.SInfectados.setMaximumSize(QtCore.QSize(200, 16777215))
        self.SInfectados.setStyleSheet("background-color: rgb(46, 52, 54);\n"
"font: 15pt \"Chandas\";\n"
"border: 1px solid  rgb(0, 0, 0);\n"
"color: rgb(238, 238, 236);\n"
"")
        self.SInfectados.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.SInfectados.setMinimum(1)
        self.SInfectados.setMaximum(1000000)
        self.SInfectados.setProperty("value", 1)
        self.SInfectados.setObjectName("SInfectados")
        self.verticalLayout_7.addWidget(self.SInfectados)
        self.label_3 = QtWidgets.QLabel(self.variaveis)
        self.label_3.setGeometry(QtCore.QRect(0, 420, 261, 41))
        self.label_3.setStyleSheet("font: 20pt \"Chandas\";\n"
"color: rgb(182, 182, 182);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.botoes = QtWidgets.QFrame(self.frame_left)
        self.botoes.setGeometry(QtCore.QRect(0, 479, 271, 71))
        self.botoes.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.botoes.setFrameShadow(QtWidgets.QFrame.Raised)
        self.botoes.setObjectName("botoes")
        self.BSimular = QtWidgets.QPushButton(self.botoes)
        self.BSimular.setGeometry(QtCore.QRect(0, 10, 111, 51))
        self.BSimular.setStyleSheet("QPushButton{\n"
"font: 15pt \"Chandas\";\n"
"color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-radius: 60px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 87, 83);\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(136, 138, 133);\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.BSimular.setObjectName("BSimular")
        self.BSalvar = QtWidgets.QPushButton(self.botoes)
        self.BSalvar.setGeometry(QtCore.QRect(160, 10, 111, 51))
        self.BSalvar.setStyleSheet("QPushButton{\n"
"font: 15pt \"Chandas\";\n"
"color: rgb(186, 189, 182);\n"
"background-color: rgb(46, 52, 54);\n"
"border-radius: 60px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 87, 83);\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"\n"
"QPushBotton{\n"
"background-color: rgb(136, 138, 133);\n"
"color: rgb(238, 238, 236);\n"
"}\n"
"")
        self.BSalvar.setObjectName("BSalvar")
        self.frame_right = QtWidgets.QFrame(self.frame)
        self.frame_right.setGeometry(QtCore.QRect(280, 0, 661, 571))
        self.frame_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_right.setObjectName("frame_right")
        self.graphicsView = PlotWidget(self.frame_right)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 641, 531))
        self.graphicsView.setObjectName("graphicsView")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 570, 941, 16))
        self.label_5.setObjectName("label_5")
        SIRepidemias.setCentralWidget(self.centralwidget)

        self.retranslateUi(SIRepidemias)
        QtCore.QMetaObject.connectSlotsByName(SIRepidemias)

    # --------------------------------------------------------------
        self.BSimular.clicked.connect(lambda:self.draw_grafico())
        self.BSalvar.clicked.connect(lambda:self.directory())
    def draw_grafico(self):
        self.graphicsView.clear()
        self.graphicsView.show()
        viewBox = self.graphicsView.getViewBox()
        viewBox.setMouseEnabled(x = False, y = False)
        self.graphicsView.setMenuEnabled(enableViewBoxMenu = False)
        self.graphicsView.hideButtons()
        self.graphicsView.setBackground((46, 52, 54))
        self.graphicsView.showGrid(x = True, y = True, alpha = 0.1)
        self.graphicsView.setTitle("SIR - Simulação")
        self.graphicsView.addLegend()
        #self.graphicsView.setYRange(0, 60, padding = 0)
        self.graphicsView.setLabel('left', 'Número de Pessoas', units='')
        self.graphicsView.setLabel('right')
        self.graphicsView.setLabel('bottom', 'Dias', units='')
        ''' Variáveis '''
        N  = self.SPopula.value()    # Total population, N.
        D  = self.SDias.value()      # Dias totais
        MS = self.SMaxSaude.value()  # Máximo de Pessoas que o sistema de saúde comporta
        I0 = self.SInfectados.value()# Número de infectados inicialmente
        R0 = 0                       # Número de recuperados inicialmente
        S0 = N - I0 - R0# Número de indivíduos suscetíveis
        y0 = S0, I0, R0# Condições iniciais

        beta = self.SProbContato.value()# Taxa de contato
        gamma = self.SProbRec.value()# Taxa de Recuperação

        x = np.array(range(0, D)) # Array com os dias 0 a D (Eixo X)

        ''' Equações Diferencias do Modelo SIR'''
        def dif_SIR(y, t, N, beta, gamma):
            '''
                Equações diferenciais (EDO) do SIR
            '''
            S, I, R = y
            dS_sobre_dt = -beta * (I/N) * S                 # dS(t)/dt
            dI_sobre_dt =  beta * (I/N) * S  - (gamma * I)  # dI(t)/dt
            dR_sobre_dt =  gamma * I                        # dR(t)/dt
        
            return dS_sobre_dt, dI_sobre_dt, dR_sobre_dt
        
        '''Resolve as diferenciais para cada valor de t '''
        integral = odeint(dif_SIR, y0, x, args=(N, beta, gamma))
        S, I, R = integral.T # S(t) , I(t), R(t)

        M = np.array(D*[MS])# Máximo de Pessoas que o sistema de saúde pode comportar
        
        ''' Plots Linhas '''
        pen = pg.mkPen(color = (0, 213, 255), width = 2)
        self.graphicsView.plot(x, S, pen=pen, name='Suscetível (S)')
        pen = pg.mkPen(color = 'g', width = 2)
        self.graphicsView.plot(x, R, pen=pen, name='Recuperado (R)')
        pen = pg.mkPen(color = 'w', width = 2, style=QtCore.Qt.DashLine)
        self.graphicsView.plot(x, M, pen=pen, name='Máx. Sist. Saúde')
        pen = pg.mkPen(color = 'r', width = 2)
        self.graphicsView.plot(x, I, pen=pen, name='Infectado (I)')
        
    def directory(self):
        dialog = QtGui.QFileDialog()
        teste = dialog.getSaveFileName(None, 'Save PNG File','SIR-Simulação',"(*.png)")
        exporter = pg.exporters.ImageExporter(self.graphicsView.plotItem)
        exporter.export(teste[0])
    # --------------------------------------------------------------

    def retranslateUi(self, SIRepidemias):
        _translate = QtCore.QCoreApplication.translate
        SIRepidemias.setWindowTitle(_translate("SIRepidemias", "MainWindow"))
        self.label.setText(_translate("SIRepidemias", "População (N)"))
        self.label_2.setText(_translate("SIRepidemias", "Prob. Contato"))
        self.label_4.setText(_translate("SIRepidemias", "Máx. Sist. de Saúde"))
        self.label_6.setText(_translate("SIRepidemias", "Prob. Recuperação"))
        self.label_7.setText(_translate("SIRepidemias", "Dias de Epidemia"))
        self.label_8.setText(_translate("SIRepidemias", "Infectados Iniciais"))
        self.label_3.setText(_translate("SIRepidemias", "( S ) --> ( I ) --> ( R )"))
        self.BSimular.setText(_translate("SIRepidemias", "Simular"))
        self.BSalvar.setText(_translate("SIRepidemias", "Salvar"))
        self.label_5.setText(_translate("SIRepidemias", "SIR -  simulador criado por  Natan B.B.  para aprender melhor sobre pandemias                                                                                                                                                                       Versão 0.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SIRepidemias = QtWidgets.QMainWindow()
    ui = Ui_SIRepidemias()
    ui.setupUi(SIRepidemias)
    SIRepidemias.show()
    sys.exit(app.exec_())

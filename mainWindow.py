from cgitb import text
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import Slot
from ui_mainWindow import Ui_MainWindow
#incluir clases partuclas 
from Actividad05_ClasesyObjetos.particulas import Particulas
from Actividad05_ClasesyObjetos.particula import Particula
class MainWindow(QMainWindow):
    def __init__(self): 
        super(MainWindow, self).__init__() #Contructor de QMainWindow
        #Guardar particulas
        self.particulas = Particulas()
        
        self.ui = Ui_MainWindow()
        #mandar los datos de self.ui a la ventana
        self.ui.setupUi(self)
        # Eventos en botones
        self.ui.pbAgregarInicio.clicked.connect(self.click_agregarInicio)
        self.ui.pbAgregaFinal.clicked.connect(self.click_agregarFinal)
        self.ui.pbMostrar.clicked.connect(self.click_mostrar)
        
    @Slot()
    def click_mostrar(self):
        self.ui.salida.clear()
        self.particulas.mostrar()
        self.ui.salida.insertPlainText(str(self.particulas))
        
    @Slot() #Guardar los datos obenidos
    def click_agregarInicio(self):
        id = self.ui.leId.text()
        origenx = self.ui.leOrigenx.text()
        origeny = self.ui.leOrigenY.text()
        destinox = self.ui.leDestinoX.text()
        destinoy = self.ui.leDestinoY.text()
        velocidad = self.ui.leVelocidad.text()
        red = self.ui.sbRed.value()
        green = self.ui.sbGreen.value()
        blue = self.ui.sbBlue.value()
        #Crear particla
        particula = Particula(int(id),int(origenx),int(origeny),int(destinox),int(destinoy),int(velocidad),red,green,blue)
        self.particulas.agregar_inicio(particula)
        
    @Slot() #Guardar los datos obenidos
    def click_agregarFinal(self):
        id = self.ui.leId.text()
        origenx = self.ui.leOrigenx.text()
        origeny = self.ui.leOrigenY.text()
        destinox = self.ui.leDestinoX.text()
        destinoy = self.ui.leDestinoY.text()
        velocidad = self.ui.leVelocidad.text()
        red = self.ui.sbRed.value()
        green = self.ui.sbGreen.value()
        blue = self.ui.sbBlue.value()
        #Crear particla
        particulafinal = Particula(int(id),int(origenx),int(origeny),int(destinox),int(destinoy),int(velocidad),red,green,blue)
        self.particulas.agregar_final(particulafinal)
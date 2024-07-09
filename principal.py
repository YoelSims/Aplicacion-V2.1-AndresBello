import os
import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow
from src.ui_interfaz import *
########################################################################
# Importacion de Modulos Personalizados Widgets
#from Custom_Widgets import *
#from Custom_Widgets.QAppSettings import QAppSettings
########################################################################

#Importacion de Funciones
from Funciones.funcionesgeneral import *
from BaseDatos.basededatos import init_db

settings = QSettings()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        #QMainWindow.__init__(self)
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class-
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)
        ########################################################################
        # Aplicando Estilos JSON
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
        }) 
        ###########################
        #Mostrar Ventana
        self.show()
        #Aplicar Cambios
        QAppSettings.updateAppSettings(self)
        # Iniciar Base de Datos y Generar Tablas
        init_db()
        #Llamando las Funciones
        self.app_functions = AppFunctions(self.ui)

    def sassCompilationProgress(self, n):
        self.ui.progressBar.setValue(n)
        
        #Mostrar tablas inicialmente
        self.app_functions.display_users()
        
        
        
# Ejecutar Aplicacion
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

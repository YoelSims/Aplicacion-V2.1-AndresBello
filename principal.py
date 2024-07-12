import os
import sys
#from PyQt5.QtWidgets import QApplication, QMainWindow
#Importando Interfaz
from src.ui_interfaz import *
#Importacion de Modulos Personalizados Widgets
from Custom_Widgets import *
#from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomQToolTip import QCustomQToolTipFilter
########################################################################
from functools import partial
import csv

#Importacion de Funciones
from Funciones.funcionesgeneral import *
#Importacion Iniciar Base de Datos
from BaseDatos.basededatos import init_db

#Custom_Widgets --convert-ui ui --qt-library PySide6

settings = QSettings()

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        #QMainWindow.__init__(self)
        self.ui = Ui_ventanaPrincipal()
        self.ui.setupUi(self)
        #####################################
        # Aplicando Estilos JSON
        loadJsonStyle(self, self.ui, jsonFiles = {
            "json-styles/style.json"
        }) 
        ###########################
        self.create_percentage_bar_chart()

        #Mostrar Ventana
        self.show()
        #Aplicar Cambios
        QAppSettings.updateAppSettings(self)

        ######sizegrip########
        # Iniciar Base de Datos y Generar Tablas
        init_db()
        #Llamando las Funciones
        self.app_functions = AppFunctions(self.ui)
    #Progreso Instalando Tema
    def sassCompilationProgress(self, n):
        self.ui.temaProgreso.setValue(n)
        
        #Mostrar tablas inicialmente
        self.app_functions.display_users()

    def create_percentage_bar_chart(self):
        #########
        firstname = {}
        lastname = {}

        ####### Obtener csv filas contador
        rowCount = 0

        ###Leer los datos del csv
        with open('csv/Estudiantes.csv', encoding='utf-8') as csvfile:
            csvReader = csv.reader(csvfile, delimiter=';')
            #print(csvReader)
            ##Iterar a trabes de las filas del csv
            for row in csvReader:
                print(row)
                #Ignorar el primer campo del csv fila
                if rowCount > 0:
                    #Agregar datos al json
                    if not row[2] in firstname:
                        firstname[row[2]] = []
                        firstname[row[2]].append({"name": row[0], "lastname": row[4]})
                    else:
                        firstname[row[2]].append({"name": row[0], "lastname": row[4]})
                #Incrementar el contador
                rowCount += 1
        
        
# Ejecutar Aplicacion
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ###########################
    #TipOverlay Personalizados
    eventoTips = QCustomQToolTipFilter(tailPosition="auto", duration=700, icon="Qss/icons/ff0000/feather/search.png")
    app.installEventFilter(eventoTips)
    ##########################
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())



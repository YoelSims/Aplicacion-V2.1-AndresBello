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
        # Mostrar Ventana
        self.show()
        #Aplicar Cambios
        QAppSettings.updateAppSettings(self)
        #settings = QSettings()
        #Cambiar Tema
        #settings.setValue("THEME", "Default-Theme")

        #QAppSettings.updateAppSettings(self)
        
        # Iniciar Base de Datos y Generar Tablas
        init_db()
        #Llamando las Funciones
        self.app_functions = AppFunctions(self.ui)
        # Inicializar el tema de la aplicación
        #self.app_functions.initializeAppTheme()
        # Conectar el cambio de tema a la función
        #self.ui.temaLista.currentIndexChanged.connect(self.app_functions.changeAppTheme)

        #Botones Funciones Principales
        self.ui.actualizarBoton.clicked.connect(self.app_functions.add_user)
        self.ui.eliminarBoton.clicked.connect(self.app_functions.delete_user)
        self.ui.editarBoton.clicked.connect(self.app_functions.update_user)
        #Boton Busqueda Evento
        self.ui.busquedaBoton.clicked.connect(self.app_functions.showSearchResults)
        
        #Mostrar tablas inicialmente
        self.app_functions.display_users()
        
        ##############
        #Actualizar Tema
        ##############
        ## Expandir Menu Central Botones
        self.ui.ajustesBoton.clicked.connect(lambda: self.ui.menuCentroContenedor.expandMenu())
        self.ui.acercaDeBoton.clicked.connect(lambda: self.ui.menuCentroContenedor.expandMenu())
        self.ui.ayudaBoton.clicked.connect(lambda: self.ui.menuCentroContenedor.expandMenu())
        ##############
        ## Expandir Menu Derecho Botones
        self.ui.masBoton.clicked.connect(lambda: self.ui.menuContenedorDerecho.expandMenu())
        self.ui.perfilBoton.clicked.connect(lambda: self.ui.menuContenedorDerecho.expandMenu())
        self.ui.botonMenuEliminar.clicked.connect(lambda: self.ui.menuContenedorDerecho.expandMenu())
        #################
        ### Cerrar Menu Central Botones
        self.ui.cerrarMenuCentro.clicked.connect(lambda: self.ui.menuCentroContenedor.collapseMenu())
        #################
        ### Cerrar Menu Derecho
        self.ui.cerrarMenuDerecho.clicked.connect(lambda: self.ui.menuContenedorDerecho.collapseMenu())
        #################
        ### Cerrar Notificacion
        self.ui.cerrarNotificacion.clicked.connect(lambda: self.ui.emergenteNotificacionContenedor.collapseMenu())
        
# Ejecutar Aplicacion
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

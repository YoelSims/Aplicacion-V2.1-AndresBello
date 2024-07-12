import time
#Import Modelos, tablas
from Modelos.modelo import Usuarios
#Importar Base de Datos
from BaseDatos.basededatos import SessionLocal
from sqlalchemy import *
#Import Custom_Widgets - Widgets personalizados
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader, QCustomArcLoader, QCustomPerlinLoader, QCustomSpinner
#Import PySide6
from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import QSettings, QSize
from PySide6.QtGui import QColor, QFont, QFontDatabase
from PySide6.QtWidgets import QTableWidgetItem
#from PySide6.QtCore import QSettings, QTimer
#from PySide6.QtWidgets import QGraphicsDropShadowEffect
#from PySide6.QtWidgets import QApplication, QMainWindow, QWidget

class AppFunctions:
    def __init__(self, ui):
        self.ui = ui
        #Aplicar Fuentes
        self.cargarFuente()
        #Aplicar Tema
        self.initializeAppTheme()
        #Aplicar Estilo, otro metodo
        #self.applyStyles()
        self.conexionBotones()
    
    def conexionBotones(self):
        #Botones Funciones Principales
        self.ui.actualizarBoton.clicked.connect(self.add_user)
        self.ui.eliminarBoton.clicked.connect(self.delete_user)
        self.ui.editarBoton.clicked.connect(self.update_user)
        #Boton Busqueda Evento
        self.ui.busquedaBoton.clicked.connect(self.showSearchResults)
        #Expandir Menu Central Botones
        self.ui.ajustesBoton.clicked.connect(lambda: self.ui.menuCentroContenedor.expandMenu())
        self.ui.acercaDeBoton.clicked.connect(lambda: self.ui.menuCentroContenedor.expandMenu())
        self.ui.ayudaBoton.clicked.connect(lambda: self.ui.menuCentroContenedor.expandMenu())
        #Expandir Menu Derecho Botones
        self.ui.masBoton.clicked.connect(lambda: self.ui.menuContenedorDerecho.expandMenu())
        self.ui.perfilBoton.clicked.connect(lambda: self.ui.menuContenedorDerecho.expandMenu())
        self.ui.botonMenuEliminar.clicked.connect(lambda: self.ui.menuContenedorDerecho.expandMenu())
        #Cerrar Menu Central Botones
        self.ui.cerrarMenuCentro.clicked.connect(lambda: self.ui.menuCentroContenedor.collapseMenu())
        #Cerrar Menu Derecho
        self.ui.cerrarMenuDerecho.clicked.connect(lambda: self.ui.menuContenedorDerecho.collapseMenu())
        #Cerrar Notificacion
        self.ui.cerrarNotificacion.clicked.connect(lambda: self.ui.emergenteNotificacionContenedor.collapseMenu())
    
    #Crear cuadro de resultados busqueda
    def createSearchTipOverlay(self):
        self.searchTooltip = QCustomTipOverlay(
            title = "Buscando...",
            description = "Buscando...",
            icon="Qss/icons/ff0000/feather/search.png",
            image="Qss/icons/ff0000/feather/activity.png",
            isClosable=True,
            target=self.ui.busquedaTexto,
            parent=self.ui.centralContenedor,
            aniType="pull-up",
            deleteOnClose=True,
            duration=-1, #-1 Para evitar el autocierre
            tailPosition="top-center",
            closeIcon="Qss/icons/ff0000/material_design/clear.png",
            toolFlag = True
        )

        #Loader 3 Tipos
        """gelatinaLoader = QCustomPerlinLoader(
            parent=self.searchTooltip,
            size=QSize(600, 600),
            message="Cargando...",
            color=QColor("white"),
            fontFamily="Ebrima",
            fontSize=30,
            rayon=200,
            duration=60 * 1000,
            noiseOctaves=0.8,
            noiseSeed=int(time.time()),
            backgroundColor=QColor("transparent"),
            circleColor1=QColor("#ff2e63"),
            circleColor2=QColor("#082e63"),
            circleColor3=QColor("#ff0000")
        )"""

        """figurasLoader = QCustom3CirclesLoader(
            parent=self.searchTooltip,
            color=QColor("#ff0000"),
            penWidth=20,
            animationDuration=400
        )"""

        espiralLoader = QCustomArcLoader(
            parent=self.searchTooltip,
            color=QColor("#ff0000"),
            penWidth=20
        )

        """circuloLoader = QCustomSpinner(
            lineWidth=2,
            lineColor=None,  # Use default color if None
            direction="Clockwise",  # or "Counterclockwise"
            animationType="Bounce"  # or "Smooth"
        )"""

        self.searchTooltip.addWidget(espiralLoader)


    def showSearchResults(self):
        buscarCampo = self.ui.busquedaTexto.text()
        #Validar que no este vacio
        if not buscarCampo:
            return
        try:
            self.searchTooltip.show()
        except:
            self.createSearchTipOverlay()
            self.searchTooltip.show()
        
        #Actualizar descripcion de Busqueda
        self.searchTooltip.setDescription("Mostando resultados para: "+buscarCampo)

    def initializeAppTheme(self):
        settings = QSettings()
        current_theme = settings.value("THEME")
        #print("El Tema actual es:", current_theme)
        #Agregar Temas de la Lista
        self.populateThemeList(current_theme)
        #Conectar los Cambios del tema en la aplicacion
        self.ui.temaLista.currentTextChanged.connect(self.changeAppTheme)
    
    def populateThemeList(self, current_theme):
        theme_count = -1
        for theme in self.ui.themes:
            self.ui.temaLista.addItem(theme.name, theme.name)
            #Ver el actual tema
            if theme.defaultTheme or theme.name == current_theme:
                self.ui.temaLista.setCurrentIndex(theme_count)
    
    def changeAppTheme(self):
        #Cambiar tema basado en la eleccion del usuario
        settings = QSettings()
        selected_theme = self.ui.temaLista.currentData()
        current_theme = settings.value("THEME")

        if current_theme != selected_theme:
            #Aplicar el Tema
            settings.setValue("THEME", selected_theme)
            QAppSettings.updateAppSettings(self.ui, reloadJson=True)

    #Fuentes Carga
    def cargarFuente(self):
        font_id = QFontDatabase.addApplicationFont("./fonts/ProductSans-Bold.ttf")
        # Si la fuente esta cargada
        if font_id == -1:
            print("Fallo al cargar las Fuente Product Sans")
            return
        # Aplicar Fuente
        font_family = QFontDatabase.applicationFontFamilies(font_id)
        if font_family:
            product_sans = QFont(font_family[0])
        else:
            product_sans = QFont("Sans Serif")
        # Aplicar a todos los widgets de la Ventana Principal
        self.establecerFuenteTodo(self.ui.centralContenedor, product_sans)
    
    def establecerFuenteTodo(self, widget, font):
        widget.setFont(font)
        for fuente in widget.findChildren(QWidget):
            fuente.setFont(font)


    def get_all_users(self):
        with SessionLocal() as session:
            return session.query(Usuarios).all()
        
    def add_user(self):
        with SessionLocal() as session:
            cedula = self.ui.cedula.text()
            nombre = self.ui.nombre.text()
            apellido = self.ui.apellido.text()
            telefono = self.ui.telefono.text()
            correo = self.ui.correo.text()

            nuevo_usuario = Usuarios(
                cedula=cedula,
                nombre=nombre,
                apellido=apellido,
                telefono=telefono,
                correo=correo
            )
            session.add(nuevo_usuario)
            session.commit()

        self.ui.cedula.setText("")
        self.ui.nombre.setText("")
        self.ui.apellido.setText("")
        self.ui.telefono.setText("")
        self.ui.correo.setText("")

        self.display_users()
    
    def delete_user(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            user_item = self.ui.tableWidget.item(selected_row, 0)
            if user_item:
                user_id = user_item.text()
                if user_id:
                    try:
                        with SessionLocal() as session:
                            user_to_delete = session.query(Usuarios).filter(Usuarios.id_usuario == user_id).first()
                            if user_to_delete:
                                session.delete(user_to_delete)
                                session.commit()
                                self.display_users()
                            else:
                                print(f"User with ID {user_id} not found.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                else:
                    print("Selected user ID is empty.")
            else:
                print("No user item found in the selected row.")
        else:
            print("No row selected.")

    def update_user(self):
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row >= 0:
            user_item = self.ui.tableWidget.item(selected_row, 0)
            if user_item:
                user_id = user_item.text()
                if user_id:
                    cedula = self.ui.cedulaEliminar.text()
                    nombre = self.ui.nombreActualizar.text()
                    apellido = self.ui.apellidoActualizar.text()
                    telefono = self.ui.telefonoActualizar.text()
                    correo = self.ui.correoActualizar.text()

                    try:
                        with SessionLocal() as session:
                            user_to_update = session.query(Usuarios).filter(Usuarios.id_usuario == user_id).first()
                            if user_to_update:
                                user_to_update.cedula = cedula
                                user_to_update.nombre = nombre
                                user_to_update.apellido = apellido
                                user_to_update.telefono = telefono
                                user_to_update.correo = correo
                                session.commit()
                                self.display_users()
                                print(f"User with ID {user_id} has been updated.")
                            else:
                                print(f"User with ID {user_id} not found.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
                else:
                    print("Selected user ID is empty.")
            else:
                print("No user item found in the selected row.")
        else:
            print("No row selected.")
            
    def display_users(self):
        users = self.get_all_users()
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(6)
        for row_number, user in enumerate(users):
            self.ui.tableWidget.insertRow(row_number)
            self.ui.tableWidget.setItem(row_number, 0, QTableWidgetItem(str(user.id_usuario)))
            self.ui.tableWidget.setItem(row_number, 1, QTableWidgetItem(user.cedula))
            self.ui.tableWidget.setItem(row_number, 2, QTableWidgetItem(user.nombre))
            self.ui.tableWidget.setItem(row_number, 3, QTableWidgetItem(user.apellido  + " " + user.nombre))
            self.ui.tableWidget.setItem(row_number, 4, QTableWidgetItem(user.telefono))
            self.ui.tableWidget.setItem(row_number, 5, QTableWidgetItem(user.correo))
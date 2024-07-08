from PySide6.QtWidgets import QTableWidgetItem
from Modelos.modelo import Usuarios
from BaseDatos.basededatos import SessionLocal
from sqlalchemy import *
#########################################
from Custom_Widgets import *
from Custom_Widgets.QAppSettings import QAppSettings
from Custom_Widgets.QCustomTipOverlay import QCustomTipOverlay
#from Custom_Widgets.QCustomLoadingIndicators import QCustom3CirclesLoader

from PySide6.QtGui import QFont, QFontDatabase
from PySide6.QtCore import QSettings
#from PySide6.QtCore import QSettings, QTimer
#from PySide6.QtGui import QColor, QFont, QFontDatabase
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
        self.ui.busquedaBoton.clicked.connect(self.showSearchResults)
    
    #Crear cuadro de resultados busqueda
    def createSearchTipOverlay(self):
        self.searchTooltip = QCustomTipOverlay(
            title = "Buscando Resultados.",
            description = "Buscando...",
            icon=self.ui.PATH_RESOURCES+"feather/search.png",
            isClosable=True,
            target=self.ui.busquedaTexto,
            parent=self.ui,
            deleteOnClose=True,
            duration=-1, #-1 Para evitar el autocierre
            tailPosition="top-center",
            closeIcon=self.ui.PATH_RESOURCES+"material_design/close.png",
            toolFlag = True
        )
    
    def showSearchResults(self):
        try:
            self.searchTooltip.show()
        except:
            self.createSearchTipOverlay()
            self.searchTooltip()

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
            self.ui.tableWidget.setItem(row_number, 3, QTableWidgetItem(user.apellido))
            self.ui.tableWidget.setItem(row_number, 4, QTableWidgetItem(user.telefono))
            self.ui.tableWidget.setItem(row_number, 5, QTableWidgetItem(user.correo))
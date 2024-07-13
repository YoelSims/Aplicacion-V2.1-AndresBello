# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_interfaz.ui'
##
## Created by: Qt User Interface Compiler version 6.7.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QProgressBar, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

from Custom_Widgets.QCustomQStackedWidget import QCustomQStackedWidget
from Custom_Widgets.QCustomSlideMenu import QCustomSlideMenu
class Ui_ventanaPrincipal(object):
    def setupUi(self, ventanaPrincipal):
        if not ventanaPrincipal.objectName():
            ventanaPrincipal.setObjectName(u"ventanaPrincipal")
        ventanaPrincipal.resize(1322, 783)
        ventanaPrincipal.setMinimumSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u":/feather/icons/feather/grid.png", QSize(), QIcon.Normal, QIcon.Off)
        ventanaPrincipal.setWindowIcon(icon)
        ventanaPrincipal.setStyleSheet(u"")
        self.centralContenedor = QWidget(ventanaPrincipal)
        self.centralContenedor.setObjectName(u"centralContenedor")
        self.horizontalLayout = QHBoxLayout(self.centralContenedor)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menuContenedorIzquierdo = QCustomSlideMenu(self.centralContenedor)
        self.menuContenedorIzquierdo.setObjectName(u"menuContenedorIzquierdo")
        self.menuContenedorIzquierdo.setMaximumSize(QSize(42, 16777215))
        self.verticalLayout = QVBoxLayout(self.menuContenedorIzquierdo)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.subMenuContenedorIzquierdo = QWidget(self.menuContenedorIzquierdo)
        self.subMenuContenedorIzquierdo.setObjectName(u"subMenuContenedorIzquierdo")
        self.verticalLayout_2 = QVBoxLayout(self.subMenuContenedorIzquierdo)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.subMenuContenedorIzquierdo)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(1, 6, 0, 0)
        self.menuBoton = QPushButton(self.frame)
        self.menuBoton.setObjectName(u"menuBoton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.menuBoton.sizePolicy().hasHeightForWidth())
        self.menuBoton.setSizePolicy(sizePolicy)
        self.menuBoton.setMinimumSize(QSize(0, 0))
        self.menuBoton.setContextMenuPolicy(Qt.NoContextMenu)
        self.menuBoton.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/font_awesome_solid/icons/font_awesome/solid/align-justify.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBoton.setIcon(icon1)
        self.menuBoton.setIconSize(QSize(30, 30))

        self.verticalLayout_3.addWidget(self.menuBoton)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.subMenuContenedorIzquierdo)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 10, 0, 10)
        self.inicioBoton = QPushButton(self.frame_2)
        self.inicioBoton.setObjectName(u"inicioBoton")
        sizePolicy.setHeightForWidth(self.inicioBoton.sizePolicy().hasHeightForWidth())
        self.inicioBoton.setSizePolicy(sizePolicy)
        self.inicioBoton.setLayoutDirection(Qt.LeftToRight)
        self.inicioBoton.setAutoFillBackground(False)
        self.inicioBoton.setStyleSheet(u"background-color: #e0dcd5;")
        icon2 = QIcon()
        icon2.addFile(u":/feather/icons/feather/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.inicioBoton.setIcon(icon2)
        self.inicioBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.inicioBoton)

        self.estudianteBoton = QPushButton(self.frame_2)
        self.estudianteBoton.setObjectName(u"estudianteBoton")
        self.estudianteBoton.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/font_awesome_solid/icons/font_awesome/solid/user-large.png", QSize(), QIcon.Normal, QIcon.Off)
        self.estudianteBoton.setIcon(icon3)
        self.estudianteBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.estudianteBoton)

        self.materiaBoton = QPushButton(self.frame_2)
        self.materiaBoton.setObjectName(u"materiaBoton")
        icon4 = QIcon()
        icon4.addFile(u":/feather/icons/feather/layers.png", QSize(), QIcon.Normal, QIcon.Off)
        self.materiaBoton.setIcon(icon4)
        self.materiaBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.materiaBoton)

        self.profesorBoton = QPushButton(self.frame_2)
        self.profesorBoton.setObjectName(u"profesorBoton")
        icon5 = QIcon()
        icon5.addFile(u":/font_awesome_solid/icons/font_awesome/solid/user-group.png", QSize(), QIcon.Normal, QIcon.Off)
        self.profesorBoton.setIcon(icon5)
        self.profesorBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.profesorBoton)

        self.notaBoton = QPushButton(self.frame_2)
        self.notaBoton.setObjectName(u"notaBoton")
        icon6 = QIcon()
        icon6.addFile(u":/feather/icons/feather/clipboard.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notaBoton.setIcon(icon6)
        self.notaBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.notaBoton)

        self.documentoBoton = QPushButton(self.frame_2)
        self.documentoBoton.setObjectName(u"documentoBoton")
        icon7 = QIcon()
        icon7.addFile(u":/font_awesome_solid/icons/font_awesome/solid/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.documentoBoton.setIcon(icon7)
        self.documentoBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_4.addWidget(self.documentoBoton)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.subMenuContenedorIzquierdo)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 10, 0, 10)
        self.gradosBoton = QPushButton(self.frame_3)
        self.gradosBoton.setObjectName(u"gradosBoton")
        icon8 = QIcon()
        icon8.addFile(u":/font_awesome_solid/icons/font_awesome/solid/graduation-cap.png", QSize(), QIcon.Normal, QIcon.Off)
        self.gradosBoton.setIcon(icon8)
        self.gradosBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.gradosBoton)

        self.ajustesBoton = QPushButton(self.frame_3)
        self.ajustesBoton.setObjectName(u"ajustesBoton")
        icon9 = QIcon()
        icon9.addFile(u":/feather/icons/feather/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ajustesBoton.setIcon(icon9)
        self.ajustesBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.ajustesBoton)

        self.acercaDeBoton = QPushButton(self.frame_3)
        self.acercaDeBoton.setObjectName(u"acercaDeBoton")
        icon10 = QIcon()
        icon10.addFile(u":/feather/icons/feather/alert-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.acercaDeBoton.setIcon(icon10)
        self.acercaDeBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.acercaDeBoton)

        self.ayudaBoton = QPushButton(self.frame_3)
        self.ayudaBoton.setObjectName(u"ayudaBoton")
        icon11 = QIcon()
        icon11.addFile(u":/material_design/icons/material_design/help_outline.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ayudaBoton.setIcon(icon11)
        self.ayudaBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_5.addWidget(self.ayudaBoton)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.subMenuContenedorIzquierdo)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 10, 0, 10)
        self.cerrarSesionBoton = QPushButton(self.frame_4)
        self.cerrarSesionBoton.setObjectName(u"cerrarSesionBoton")
        icon12 = QIcon()
        icon12.addFile(u":/font_awesome_solid/icons/font_awesome/solid/lock.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cerrarSesionBoton.setIcon(icon12)
        self.cerrarSesionBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_6.addWidget(self.cerrarSesionBoton)

        self.frame_21 = QFrame(self.frame_4)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMinimumSize(QSize(10, 10))
        self.frame_21.setMaximumSize(QSize(10, 10))
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.frame_21, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.subMenuContenedorIzquierdo)


        self.horizontalLayout.addWidget(self.menuContenedorIzquierdo)

        self.menuCentroContenedor = QCustomSlideMenu(self.centralContenedor)
        self.menuCentroContenedor.setObjectName(u"menuCentroContenedor")
        self.verticalLayout_7 = QVBoxLayout(self.menuCentroContenedor)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.menuSubCentroContenedor = QWidget(self.menuCentroContenedor)
        self.menuSubCentroContenedor.setObjectName(u"menuSubCentroContenedor")
        self.menuSubCentroContenedor.setMinimumSize(QSize(250, 0))
        self.verticalLayout_8 = QVBoxLayout(self.menuSubCentroContenedor)
        self.verticalLayout_8.setSpacing(3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(5, 0, 0, 0)
        self.frame_5 = QFrame(self.menuSubCentroContenedor)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.cerrarMenuCentro = QPushButton(self.frame_5)
        self.cerrarMenuCentro.setObjectName(u"cerrarMenuCentro")
        icon13 = QIcon()
        icon13.addFile(u":/font_awesome_regular/icons/font_awesome/regular/circle-xmark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cerrarMenuCentro.setIcon(icon13)
        self.cerrarMenuCentro.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.cerrarMenuCentro, 0, Qt.AlignRight)


        self.verticalLayout_8.addWidget(self.frame_5)

        self.centroPaginas = QCustomQStackedWidget(self.menuSubCentroContenedor)
        self.centroPaginas.setObjectName(u"centroPaginas")
        self.ajustePagina = QWidget()
        self.ajustePagina.setObjectName(u"ajustePagina")
        self.verticalLayout_9 = QVBoxLayout(self.ajustePagina)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_4 = QWidget(self.ajustePagina)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_17 = QVBoxLayout(self.widget_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.widget_4)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_17.addWidget(self.label_10, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.frame_14 = QFrame(self.widget_4)
        self.frame_14.setObjectName(u"frame_14")
        font = QFont()
        font.setFamilies([u"MS UI Gothic"])
        self.frame_14.setFont(font)
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_26 = QLabel(self.frame_14)
        self.label_26.setObjectName(u"label_26")

        self.horizontalLayout_12.addWidget(self.label_26)

        self.temaLista = QComboBox(self.frame_14)
        self.temaLista.setObjectName(u"temaLista")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.temaLista.sizePolicy().hasHeightForWidth())
        self.temaLista.setSizePolicy(sizePolicy2)

        self.horizontalLayout_12.addWidget(self.temaLista)


        self.verticalLayout_17.addWidget(self.frame_14)


        self.verticalLayout_9.addWidget(self.widget_4, 0, Qt.AlignVCenter)

        self.centroPaginas.addWidget(self.ajustePagina)
        self.acercaDePagina = QWidget()
        self.acercaDePagina.setObjectName(u"acercaDePagina")
        self.verticalLayout_10 = QVBoxLayout(self.acercaDePagina)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_3 = QLabel(self.acercaDePagina)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(13)
        self.label_3.setFont(font1)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_3)

        self.centroPaginas.addWidget(self.acercaDePagina)
        self.ayudaPagina = QWidget()
        self.ayudaPagina.setObjectName(u"ayudaPagina")
        self.verticalLayout_11 = QVBoxLayout(self.ayudaPagina)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_4 = QLabel(self.ayudaPagina)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_4)

        self.centroPaginas.addWidget(self.ayudaPagina)

        self.verticalLayout_8.addWidget(self.centroPaginas)


        self.verticalLayout_7.addWidget(self.menuSubCentroContenedor)


        self.horizontalLayout.addWidget(self.menuCentroContenedor)

        self.principalCuerpoContenedor = QWidget(self.centralContenedor)
        self.principalCuerpoContenedor.setObjectName(u"principalCuerpoContenedor")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.principalCuerpoContenedor.sizePolicy().hasHeightForWidth())
        self.principalCuerpoContenedor.setSizePolicy(sizePolicy3)
        self.principalCuerpoContenedor.setStyleSheet(u"")
        self.verticalLayout_12 = QVBoxLayout(self.principalCuerpoContenedor)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.cabeceraContenedor = QWidget(self.principalCuerpoContenedor)
        self.cabeceraContenedor.setObjectName(u"cabeceraContenedor")
        self.horizontalLayout_4 = QHBoxLayout(self.cabeceraContenedor)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(20, 0, 5, 0)
        self.frame_6 = QFrame(self.cabeceraContenedor)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(10, 5, 5, 5)
        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(50, 50))
        self.label_5.setPixmap(QPixmap(u":/Imagen/Imagenes/Logo/2.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_6.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_6)

        self.notificacionBoton = QPushButton(self.frame_6)
        self.notificacionBoton.setObjectName(u"notificacionBoton")
        icon14 = QIcon()
        icon14.addFile(u":/font_awesome_regular/icons/font_awesome/regular/bell.png", QSize(), QIcon.Normal, QIcon.Off)
        self.notificacionBoton.setIcon(icon14)
        self.notificacionBoton.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.notificacionBoton)

        self.masBoton = QPushButton(self.frame_6)
        self.masBoton.setObjectName(u"masBoton")
        icon15 = QIcon()
        icon15.addFile(u":/feather/icons/feather/more-horizontal.png", QSize(), QIcon.Normal, QIcon.Off)
        self.masBoton.setIcon(icon15)
        self.masBoton.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.masBoton)

        self.perfilBoton = QPushButton(self.frame_6)
        self.perfilBoton.setObjectName(u"perfilBoton")
        icon16 = QIcon()
        icon16.addFile(u":/font_awesome_regular/icons/font_awesome/regular/circle-user.png", QSize(), QIcon.Normal, QIcon.Off)
        self.perfilBoton.setIcon(icon16)
        self.perfilBoton.setIconSize(QSize(24, 24))

        self.horizontalLayout_6.addWidget(self.perfilBoton)


        self.horizontalLayout_4.addWidget(self.frame_6)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.frame_15 = QFrame(self.cabeceraContenedor)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy4)
        self.frame_15.setMaximumSize(QSize(200, 16777215))
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.busquedaBoton = QPushButton(self.frame_15)
        self.busquedaBoton.setObjectName(u"busquedaBoton")
        icon17 = QIcon()
        icon17.addFile(u":/feather/icons/feather/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.busquedaBoton.setIcon(icon17)
        self.busquedaBoton.setIconSize(QSize(24, 24))

        self.horizontalLayout_13.addWidget(self.busquedaBoton)

        self.busquedaTexto = QLineEdit(self.frame_15)
        self.busquedaTexto.setObjectName(u"busquedaTexto")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.busquedaTexto.sizePolicy().hasHeightForWidth())
        self.busquedaTexto.setSizePolicy(sizePolicy5)
        self.busquedaTexto.setMinimumSize(QSize(0, 0))

        self.horizontalLayout_13.addWidget(self.busquedaTexto)


        self.horizontalLayout_4.addWidget(self.frame_15, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.frame_7 = QFrame(self.cabeceraContenedor)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 10, 0)
        self.botonMenuEliminar = QPushButton(self.frame_7)
        self.botonMenuEliminar.setObjectName(u"botonMenuEliminar")
        icon18 = QIcon()
        icon18.addFile(u":/font_awesome_regular/icons/font_awesome/regular/trash-can.png", QSize(), QIcon.Normal, QIcon.Off)
        self.botonMenuEliminar.setIcon(icon18)
        self.botonMenuEliminar.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.botonMenuEliminar)


        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.frame_8 = QFrame(self.cabeceraContenedor)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(25, 0, 0, 20)
        self.minimizarBoton = QPushButton(self.frame_8)
        self.minimizarBoton.setObjectName(u"minimizarBoton")
        icon19 = QIcon()
        icon19.addFile(u":/font_awesome_solid/icons/font_awesome/solid/minus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizarBoton.setIcon(icon19)
        self.minimizarBoton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.minimizarBoton)

        self.restaurarBoton = QPushButton(self.frame_8)
        self.restaurarBoton.setObjectName(u"restaurarBoton")
        icon20 = QIcon()
        icon20.addFile(u":/font_awesome_regular/icons/font_awesome/regular/square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restaurarBoton.setIcon(icon20)
        self.restaurarBoton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.restaurarBoton)

        self.cerrarBoton = QPushButton(self.frame_8)
        self.cerrarBoton.setObjectName(u"cerrarBoton")
        icon21 = QIcon()
        icon21.addFile(u":/font_awesome_solid/icons/font_awesome/solid/xmark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cerrarBoton.setIcon(icon21)
        self.cerrarBoton.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.cerrarBoton)


        self.horizontalLayout_4.addWidget(self.frame_8, 0, Qt.AlignRight|Qt.AlignTop)


        self.verticalLayout_12.addWidget(self.cabeceraContenedor)

        self.principalCuerpoContenido = QWidget(self.principalCuerpoContenedor)
        self.principalCuerpoContenido.setObjectName(u"principalCuerpoContenido")
        sizePolicy1.setHeightForWidth(self.principalCuerpoContenido.sizePolicy().hasHeightForWidth())
        self.principalCuerpoContenido.setSizePolicy(sizePolicy1)
        self.principalCuerpoContenido.setMinimumSize(QSize(839, 520))
        self.horizontalLayout_7 = QHBoxLayout(self.principalCuerpoContenido)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.principalContenidosContenedor = QWidget(self.principalCuerpoContenido)
        self.principalContenidosContenedor.setObjectName(u"principalContenidosContenedor")
        sizePolicy4.setHeightForWidth(self.principalContenidosContenedor.sizePolicy().hasHeightForWidth())
        self.principalContenidosContenedor.setSizePolicy(sizePolicy4)
        self.principalContenidosContenedor.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_28 = QVBoxLayout(self.principalContenidosContenedor)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.principalPaginas = QCustomQStackedWidget(self.principalContenidosContenedor)
        self.principalPaginas.setObjectName(u"principalPaginas")
        sizePolicy4.setHeightForWidth(self.principalPaginas.sizePolicy().hasHeightForWidth())
        self.principalPaginas.setSizePolicy(sizePolicy4)
        self.principalPaginas.setAutoFillBackground(False)
        self.inicioPagina = QWidget()
        self.inicioPagina.setObjectName(u"inicioPagina")
        self.horizontalLayout_15 = QHBoxLayout(self.inicioPagina)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.inicioPagina)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_21 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.frame_18 = QFrame(self.widget_7)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 5, 0, 5)
        self.label_53 = QLabel(self.frame_18)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setMaximumSize(QSize(40, 40))
        self.label_53.setPixmap(QPixmap(u":/material_design/icons/material_design/home.png"))
        self.label_53.setScaledContents(True)
        self.label_53.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_53)

        self.label_34 = QLabel(self.frame_18)
        self.label_34.setObjectName(u"label_34")
        sizePolicy4.setHeightForWidth(self.label_34.sizePolicy().hasHeightForWidth())
        self.label_34.setSizePolicy(sizePolicy4)
        self.label_34.setFont(font1)
        self.label_34.setLayoutDirection(Qt.LeftToRight)
        self.label_34.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_26.addWidget(self.label_34)


        self.horizontalLayout_21.addWidget(self.frame_18, 0, Qt.AlignHCenter)


        self.verticalLayout_18.addWidget(self.widget_7)

        self.cartasContenedor = QWidget(self.widget_6)
        self.cartasContenedor.setObjectName(u"cartasContenedor")
        self.horizontalLayout_17 = QHBoxLayout(self.cartasContenedor)
        self.horizontalLayout_17.setSpacing(20)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(10, 10, 10, 10)
        self.carta1 = QFrame(self.cartasContenedor)
        self.carta1.setObjectName(u"carta1")
        self.carta1.setMinimumSize(QSize(160, 0))
        self.carta1.setFrameShape(QFrame.StyledPanel)
        self.carta1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.carta1)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(10, -1, -1, -1)
        self.frame_19 = QFrame(self.carta1)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_19)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_35 = QLabel(self.frame_19)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font2)

        self.horizontalLayout_19.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_19)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setMaximumSize(QSize(40, 40))
        self.label_36.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/user-graduate.png"))
        self.label_36.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.label_36)


        self.verticalLayout_29.addWidget(self.frame_19)

        self.label_37 = QLabel(self.carta1)
        self.label_37.setObjectName(u"label_37")
        font3 = QFont()
        font3.setPointSize(10)
        self.label_37.setFont(font3)

        self.verticalLayout_29.addWidget(self.label_37, 0, Qt.AlignTop)


        self.horizontalLayout_17.addWidget(self.carta1)

        self.carta2 = QFrame(self.cartasContenedor)
        self.carta2.setObjectName(u"carta2")
        self.carta2.setMinimumSize(QSize(160, 0))
        self.carta2.setFrameShape(QFrame.StyledPanel)
        self.carta2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.carta2)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.frame_22 = QFrame(self.carta2)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_44 = QLabel(self.frame_22)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font2)

        self.horizontalLayout_22.addWidget(self.label_44)

        self.label_45 = QLabel(self.frame_22)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setMaximumSize(QSize(40, 40))
        self.label_45.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/user-tie.png"))
        self.label_45.setScaledContents(True)

        self.horizontalLayout_22.addWidget(self.label_45)


        self.verticalLayout_33.addWidget(self.frame_22)

        self.label_46 = QLabel(self.carta2)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font3)

        self.verticalLayout_33.addWidget(self.label_46, 0, Qt.AlignTop)


        self.horizontalLayout_17.addWidget(self.carta2)

        self.carta3 = QFrame(self.cartasContenedor)
        self.carta3.setObjectName(u"carta3")
        self.carta3.setMinimumSize(QSize(160, 0))
        self.carta3.setFrameShape(QFrame.StyledPanel)
        self.carta3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.carta3)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.frame_23 = QFrame(self.carta3)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_47 = QLabel(self.frame_23)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font2)

        self.horizontalLayout_23.addWidget(self.label_47)

        self.label_48 = QLabel(self.frame_23)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setMaximumSize(QSize(40, 40))
        self.label_48.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/layer-group.png"))
        self.label_48.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.label_48)


        self.verticalLayout_36.addWidget(self.frame_23)

        self.label_49 = QLabel(self.carta3)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font3)

        self.verticalLayout_36.addWidget(self.label_49, 0, Qt.AlignTop)


        self.horizontalLayout_17.addWidget(self.carta3)

        self.carta4 = QFrame(self.cartasContenedor)
        self.carta4.setObjectName(u"carta4")
        self.carta4.setMinimumSize(QSize(160, 0))
        self.carta4.setFrameShape(QFrame.StyledPanel)
        self.carta4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.carta4)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.frame_24 = QFrame(self.carta4)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_50 = QLabel(self.frame_24)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font2)

        self.horizontalLayout_24.addWidget(self.label_50)

        self.label_51 = QLabel(self.frame_24)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setMaximumSize(QSize(40, 40))
        self.label_51.setPixmap(QPixmap(u":/font_awesome_solid/icons/font_awesome/solid/cubes.png"))
        self.label_51.setScaledContents(True)

        self.horizontalLayout_24.addWidget(self.label_51)


        self.verticalLayout_37.addWidget(self.frame_24)

        self.label_52 = QLabel(self.carta4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font3)

        self.verticalLayout_37.addWidget(self.label_52, 0, Qt.AlignTop)


        self.horizontalLayout_17.addWidget(self.carta4)


        self.verticalLayout_18.addWidget(self.cartasContenedor)

        self.listadoVer = QWidget(self.widget_6)
        self.listadoVer.setObjectName(u"listadoVer")
        sizePolicy1.setHeightForWidth(self.listadoVer.sizePolicy().hasHeightForWidth())
        self.listadoVer.setSizePolicy(sizePolicy1)
        self.horizontalLayout_25 = QHBoxLayout(self.listadoVer)
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.widget_8 = QWidget(self.listadoVer)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_34 = QVBoxLayout(self.widget_8)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.frame_25 = QFrame(self.widget_8)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_25)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_54 = QLabel(self.frame_25)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font2)

        self.horizontalLayout_27.addWidget(self.label_54, 0, Qt.AlignLeft)

        self.masVer = QPushButton(self.frame_25)
        self.masVer.setObjectName(u"masVer")
        self.masVer.setMinimumSize(QSize(75, 0))
        icon22 = QIcon()
        icon22.addFile(u":/font_awesome_solid/icons/font_awesome/solid/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.masVer.setIcon(icon22)
        self.masVer.setIconSize(QSize(24, 24))

        self.horizontalLayout_27.addWidget(self.masVer, 0, Qt.AlignRight)


        self.verticalLayout_34.addWidget(self.frame_25, 0, Qt.AlignTop)

        self.frame_26 = QFrame(self.widget_8)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_26)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.label_56 = QLabel(self.frame_26)
        self.label_56.setObjectName(u"label_56")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.label_56.setFont(font4)

        self.gridLayout_6.addWidget(self.label_56, 0, 1, 1, 1)

        self.label_57 = QLabel(self.frame_26)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font4)

        self.gridLayout_6.addWidget(self.label_57, 0, 2, 1, 1)

        self.label_55 = QLabel(self.frame_26)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font4)

        self.gridLayout_6.addWidget(self.label_55, 0, 0, 1, 1)

        self.label_58 = QLabel(self.frame_26)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font3)

        self.gridLayout_6.addWidget(self.label_58, 1, 0, 1, 1)

        self.label_60 = QLabel(self.frame_26)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setFont(font3)

        self.gridLayout_6.addWidget(self.label_60, 1, 2, 1, 1)

        self.label_59 = QLabel(self.frame_26)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font3)

        self.gridLayout_6.addWidget(self.label_59, 1, 1, 1, 1)

        self.label_62 = QLabel(self.frame_26)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font3)

        self.gridLayout_6.addWidget(self.label_62, 2, 1, 1, 1)

        self.label_65 = QLabel(self.frame_26)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font3)

        self.gridLayout_6.addWidget(self.label_65, 3, 1, 1, 1)

        self.label_64 = QLabel(self.frame_26)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font3)

        self.gridLayout_6.addWidget(self.label_64, 3, 0, 1, 1)

        self.label_66 = QLabel(self.frame_26)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font3)

        self.gridLayout_6.addWidget(self.label_66, 3, 2, 1, 1)

        self.label_63 = QLabel(self.frame_26)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font3)

        self.gridLayout_6.addWidget(self.label_63, 2, 2, 1, 1)

        self.label_61 = QLabel(self.frame_26)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setFont(font3)

        self.gridLayout_6.addWidget(self.label_61, 2, 0, 1, 1)

        self.label_67 = QLabel(self.frame_26)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font3)

        self.gridLayout_6.addWidget(self.label_67, 4, 0, 1, 1)

        self.label_68 = QLabel(self.frame_26)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font3)

        self.gridLayout_6.addWidget(self.label_68, 4, 1, 1, 1)

        self.label_69 = QLabel(self.frame_26)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font3)

        self.gridLayout_6.addWidget(self.label_69, 4, 2, 1, 1)


        self.verticalLayout_34.addWidget(self.frame_26)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_34.addItem(self.verticalSpacer_2)


        self.horizontalLayout_25.addWidget(self.widget_8)

        self.widget_9 = QWidget(self.listadoVer)
        self.widget_9.setObjectName(u"widget_9")
        self.verticalLayout_30 = QVBoxLayout(self.widget_9)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_27 = QFrame(self.widget_9)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFont(font1)
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame_27)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_70 = QLabel(self.frame_27)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font2)

        self.horizontalLayout_28.addWidget(self.label_70, 0, Qt.AlignLeft)

        self.verMas2 = QPushButton(self.frame_27)
        self.verMas2.setObjectName(u"verMas2")
        icon23 = QIcon()
        icon23.addFile(u":/feather/icons/feather/arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.verMas2.setIcon(icon23)
        self.verMas2.setIconSize(QSize(24, 24))

        self.horizontalLayout_28.addWidget(self.verMas2, 0, Qt.AlignRight)


        self.verticalLayout_30.addWidget(self.frame_27, 0, Qt.AlignTop)

        self.frame_28 = QFrame(self.widget_9)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_75 = QLabel(self.frame_28)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setMinimumSize(QSize(50, 50))
        self.label_75.setMaximumSize(QSize(50, 50))
        self.label_75.setPixmap(QPixmap(u":/Imagen/Imagenes/Logo/2.png"))
        self.label_75.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_75)

        self.label_76 = QLabel(self.frame_28)
        self.label_76.setObjectName(u"label_76")

        self.horizontalLayout_29.addWidget(self.label_76)

        self.label_77 = QLabel(self.frame_28)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setMinimumSize(QSize(35, 35))
        self.label_77.setMaximumSize(QSize(35, 35))
        self.label_77.setPixmap(QPixmap(u":/feather/icons/feather/facebook.png"))
        self.label_77.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_77)

        self.label_78 = QLabel(self.frame_28)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setMinimumSize(QSize(35, 35))
        self.label_78.setMaximumSize(QSize(35, 35))
        self.label_78.setPixmap(QPixmap(u":/font_awesome_brands/icons/font_awesome/brands/whatsapp.png"))
        self.label_78.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_78)

        self.label_79 = QLabel(self.frame_28)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setMinimumSize(QSize(35, 35))
        self.label_79.setMaximumSize(QSize(35, 35))
        self.label_79.setPixmap(QPixmap(u":/feather/icons/feather/phone.png"))
        self.label_79.setScaledContents(True)

        self.horizontalLayout_29.addWidget(self.label_79)


        self.verticalLayout_30.addWidget(self.frame_28)

        self.frame_30 = QFrame(self.widget_9)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_30)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_85 = QLabel(self.frame_30)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setMinimumSize(QSize(50, 50))
        self.label_85.setMaximumSize(QSize(50, 50))
        self.label_85.setPixmap(QPixmap(u":/Imagen/Imagenes/Logo/2.png"))
        self.label_85.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_85)

        self.label_86 = QLabel(self.frame_30)
        self.label_86.setObjectName(u"label_86")

        self.horizontalLayout_31.addWidget(self.label_86)

        self.label_87 = QLabel(self.frame_30)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setMinimumSize(QSize(35, 35))
        self.label_87.setMaximumSize(QSize(35, 35))
        self.label_87.setPixmap(QPixmap(u":/feather/icons/feather/facebook.png"))
        self.label_87.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_87)

        self.label_88 = QLabel(self.frame_30)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setMinimumSize(QSize(35, 35))
        self.label_88.setMaximumSize(QSize(35, 35))
        self.label_88.setPixmap(QPixmap(u":/font_awesome_brands/icons/font_awesome/brands/whatsapp.png"))
        self.label_88.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_88)

        self.label_89 = QLabel(self.frame_30)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setMinimumSize(QSize(35, 35))
        self.label_89.setMaximumSize(QSize(35, 35))
        self.label_89.setPixmap(QPixmap(u":/feather/icons/feather/phone.png"))
        self.label_89.setScaledContents(True)

        self.horizontalLayout_31.addWidget(self.label_89)


        self.verticalLayout_30.addWidget(self.frame_30)

        self.frame_29 = QFrame(self.widget_9)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_80 = QLabel(self.frame_29)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setMinimumSize(QSize(50, 50))
        self.label_80.setMaximumSize(QSize(50, 50))
        self.label_80.setPixmap(QPixmap(u":/Imagen/Imagenes/Logo/2.png"))
        self.label_80.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_80)

        self.label_81 = QLabel(self.frame_29)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_30.addWidget(self.label_81)

        self.label_82 = QLabel(self.frame_29)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setMinimumSize(QSize(35, 35))
        self.label_82.setMaximumSize(QSize(35, 35))
        self.label_82.setPixmap(QPixmap(u":/feather/icons/feather/facebook.png"))
        self.label_82.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_82)

        self.label_83 = QLabel(self.frame_29)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setMinimumSize(QSize(35, 35))
        self.label_83.setMaximumSize(QSize(35, 35))
        self.label_83.setPixmap(QPixmap(u":/font_awesome_brands/icons/font_awesome/brands/whatsapp.png"))
        self.label_83.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_83)

        self.label_84 = QLabel(self.frame_29)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setMinimumSize(QSize(35, 35))
        self.label_84.setMaximumSize(QSize(35, 35))
        self.label_84.setPixmap(QPixmap(u":/feather/icons/feather/phone.png"))
        self.label_84.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.label_84)


        self.verticalLayout_30.addWidget(self.frame_29)

        self.frame_20 = QFrame(self.widget_9)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_38 = QLabel(self.frame_20)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setMinimumSize(QSize(50, 50))
        self.label_38.setMaximumSize(QSize(50, 50))
        self.label_38.setPixmap(QPixmap(u":/Imagen/Imagenes/Logo/2.png"))
        self.label_38.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_20)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_20.addWidget(self.label_39)

        self.label_40 = QLabel(self.frame_20)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setMinimumSize(QSize(35, 35))
        self.label_40.setMaximumSize(QSize(35, 35))
        self.label_40.setPixmap(QPixmap(u":/feather/icons/feather/facebook.png"))
        self.label_40.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_40)

        self.label_42 = QLabel(self.frame_20)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setMinimumSize(QSize(35, 35))
        self.label_42.setMaximumSize(QSize(35, 35))
        self.label_42.setPixmap(QPixmap(u":/font_awesome_brands/icons/font_awesome/brands/whatsapp.png"))
        self.label_42.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_42)

        self.label_41 = QLabel(self.frame_20)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setMinimumSize(QSize(35, 35))
        self.label_41.setMaximumSize(QSize(35, 35))
        self.label_41.setPixmap(QPixmap(u":/feather/icons/feather/phone.png"))
        self.label_41.setScaledContents(True)

        self.horizontalLayout_20.addWidget(self.label_41)


        self.verticalLayout_30.addWidget(self.frame_20)


        self.horizontalLayout_25.addWidget(self.widget_9)


        self.verticalLayout_18.addWidget(self.listadoVer)


        self.horizontalLayout_15.addWidget(self.widget_6)

        self.principalPaginas.addWidget(self.inicioPagina)
        self.estudiantesPagina = QWidget()
        self.estudiantesPagina.setObjectName(u"estudiantesPagina")
        self.horizontalLayout_14 = QHBoxLayout(self.estudiantesPagina)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.widget_2 = QWidget(self.estudiantesPagina)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_19 = QVBoxLayout(self.widget_2)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_11)

        self.tableWidget = QTableWidget(self.widget_2)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy6)
        font5 = QFont()
        font5.setPointSize(9)
        self.tableWidget.setFont(font5)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setShowGrid(True)

        self.verticalLayout_19.addWidget(self.tableWidget)


        self.horizontalLayout_14.addWidget(self.widget_2)

        self.principalPaginas.addWidget(self.estudiantesPagina)
        self.materiasPagina = QWidget()
        self.materiasPagina.setObjectName(u"materiasPagina")
        self.verticalLayout_20 = QVBoxLayout(self.materiasPagina)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_12 = QLabel(self.materiasPagina)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_12)

        self.principalPaginas.addWidget(self.materiasPagina)
        self.profesoresPagina = QWidget()
        self.profesoresPagina.setObjectName(u"profesoresPagina")
        self.verticalLayout_21 = QVBoxLayout(self.profesoresPagina)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_13 = QLabel(self.profesoresPagina)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_13)

        self.principalPaginas.addWidget(self.profesoresPagina)
        self.notasPagina = QWidget()
        self.notasPagina.setObjectName(u"notasPagina")
        self.verticalLayout_22 = QVBoxLayout(self.notasPagina)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_14 = QLabel(self.notasPagina)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_14)

        self.principalPaginas.addWidget(self.notasPagina)
        self.documentosPagina = QWidget()
        self.documentosPagina.setObjectName(u"documentosPagina")
        self.verticalLayout_23 = QVBoxLayout(self.documentosPagina)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.widget_5 = QWidget(self.documentosPagina)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_14 = QVBoxLayout(self.widget_5)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_15 = QLabel(self.widget_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_15)

        self.tableWidget_3 = QTableWidget(self.widget_5)
        if (self.tableWidget_3.columnCount() < 7):
            self.tableWidget_3.setColumnCount(7)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        if (self.tableWidget_3.rowCount() < 7):
            self.tableWidget_3.setRowCount(7)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setVerticalHeaderItem(6, __qtablewidgetitem19)
        self.tableWidget_3.setObjectName(u"tableWidget_3")

        self.verticalLayout_14.addWidget(self.tableWidget_3)


        self.verticalLayout_23.addWidget(self.widget_5)

        self.principalPaginas.addWidget(self.documentosPagina)
        self.gradosPagina = QWidget()
        self.gradosPagina.setObjectName(u"gradosPagina")
        sizePolicy4.setHeightForWidth(self.gradosPagina.sizePolicy().hasHeightForWidth())
        self.gradosPagina.setSizePolicy(sizePolicy4)
        self.verticalLayout_26 = QVBoxLayout(self.gradosPagina)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_19 = QLabel(self.gradosPagina)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font1)

        self.verticalLayout_26.addWidget(self.label_19, 0, Qt.AlignHCenter)

        self.frame_17 = QFrame(self.gradosPagina)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.tableWidget_2 = QTableWidget(self.frame_17)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        if (self.tableWidget_2.rowCount() < 11):
            self.tableWidget_2.setRowCount(11)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, __qtablewidgetitem35)
        self.tableWidget_2.setObjectName(u"tableWidget_2")

        self.horizontalLayout_18.addWidget(self.tableWidget_2)


        self.verticalLayout_26.addWidget(self.frame_17)

        self.principalPaginas.addWidget(self.gradosPagina)

        self.verticalLayout_28.addWidget(self.principalPaginas)


        self.horizontalLayout_7.addWidget(self.principalContenidosContenedor)

        self.menuContenedorDerecho = QCustomSlideMenu(self.principalCuerpoContenido)
        self.menuContenedorDerecho.setObjectName(u"menuContenedorDerecho")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.menuContenedorDerecho.sizePolicy().hasHeightForWidth())
        self.menuContenedorDerecho.setSizePolicy(sizePolicy7)
        self.menuContenedorDerecho.setMinimumSize(QSize(200, 0))
        self.verticalLayout_13 = QVBoxLayout(self.menuContenedorDerecho)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.subMenuDerecho = QWidget(self.menuContenedorDerecho)
        self.subMenuDerecho.setObjectName(u"subMenuDerecho")
        self.subMenuDerecho.setMinimumSize(QSize(0, 0))
        self.verticalLayout_31 = QVBoxLayout(self.subMenuDerecho)
        self.verticalLayout_31.setSpacing(3)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.subMenuDerecho)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setPointSize(11)
        font6.setBold(True)
        font6.setItalic(False)
        self.label_7.setFont(font6)

        self.horizontalLayout_8.addWidget(self.label_7)

        self.cerrarMenuDerecho = QPushButton(self.frame_9)
        self.cerrarMenuDerecho.setObjectName(u"cerrarMenuDerecho")
        self.cerrarMenuDerecho.setLayoutDirection(Qt.LeftToRight)
        self.cerrarMenuDerecho.setIcon(icon13)
        self.cerrarMenuDerecho.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.cerrarMenuDerecho, 0, Qt.AlignRight)


        self.verticalLayout_31.addWidget(self.frame_9)

        self.derechoPaginas = QCustomQStackedWidget(self.subMenuDerecho)
        self.derechoPaginas.setObjectName(u"derechoPaginas")
        self.perfilPagina = QWidget()
        self.perfilPagina.setObjectName(u"perfilPagina")
        self.verticalLayout_15 = QVBoxLayout(self.perfilPagina)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.perfilPagina)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(224, 308))
        self.verticalLayout_27 = QVBoxLayout(self.widget)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.label_25 = QLabel(self.widget)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setMinimumSize(QSize(50, 50))
        self.label_25.setMaximumSize(QSize(50, 50))
        self.label_25.setPixmap(QPixmap(u":/feather/Icons/Black/edit.svg"))
        self.label_25.setScaledContents(True)

        self.verticalLayout_27.addWidget(self.label_25)

        self.frame_11 = QFrame(self.widget)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setLayoutDirection(Qt.LeftToRight)
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.gridLayout_5 = QGridLayout(self.frame_11)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.correo = QLineEdit(self.frame_11)
        self.correo.setObjectName(u"correo")
        self.correo.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.correo, 9, 0, 1, 1)

        self.label_33 = QLabel(self.frame_11)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setMaximumSize(QSize(200, 20))
        font7 = QFont()
        font7.setPointSize(11)
        font7.setBold(True)
        self.label_33.setFont(font7)

        self.gridLayout_5.addWidget(self.label_33, 0, 0, 1, 1)

        self.apellido = QLineEdit(self.frame_11)
        self.apellido.setObjectName(u"apellido")
        self.apellido.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.apellido, 5, 0, 1, 1)

        self.label_23 = QLabel(self.frame_11)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setMaximumSize(QSize(200, 20))
        self.label_23.setFont(font7)

        self.gridLayout_5.addWidget(self.label_23, 6, 0, 1, 1)

        self.nombre = QLineEdit(self.frame_11)
        self.nombre.setObjectName(u"nombre")
        self.nombre.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.nombre, 3, 0, 1, 1)

        self.cedula = QLineEdit(self.frame_11)
        self.cedula.setObjectName(u"cedula")
        self.cedula.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.cedula, 1, 0, 1, 1)

        self.telefono = QLineEdit(self.frame_11)
        self.telefono.setObjectName(u"telefono")
        self.telefono.setMinimumSize(QSize(200, 0))

        self.gridLayout_5.addWidget(self.telefono, 7, 0, 1, 1)

        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setMaximumSize(QSize(100, 20))
        self.label_20.setFont(font7)
        self.label_20.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_5.addWidget(self.label_20, 2, 0, 1, 1)

        self.label_21 = QLabel(self.frame_11)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setMaximumSize(QSize(100, 20))
        self.label_21.setFont(font7)
        self.label_21.setLayoutDirection(Qt.LeftToRight)

        self.gridLayout_5.addWidget(self.label_21, 4, 0, 1, 1)

        self.label_32 = QLabel(self.frame_11)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setMaximumSize(QSize(150, 20))
        self.label_32.setFont(font7)
        self.label_32.setStyleSheet(u"")

        self.gridLayout_5.addWidget(self.label_32, 8, 0, 1, 1)


        self.verticalLayout_27.addWidget(self.frame_11)


        self.verticalLayout_15.addWidget(self.widget)

        self.actualizarBoton = QPushButton(self.perfilPagina)
        self.actualizarBoton.setObjectName(u"actualizarBoton")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.actualizarBoton.sizePolicy().hasHeightForWidth())
        self.actualizarBoton.setSizePolicy(sizePolicy8)
        self.actualizarBoton.setMinimumSize(QSize(140, 40))
        self.actualizarBoton.setMaximumSize(QSize(140, 40))
        self.actualizarBoton.setFont(font7)
        self.actualizarBoton.setLayoutDirection(Qt.LeftToRight)
        icon24 = QIcon()
        icon24.addFile(u":/feather/icons/feather/check-circle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actualizarBoton.setIcon(icon24)
        self.actualizarBoton.setIconSize(QSize(32, 32))

        self.verticalLayout_15.addWidget(self.actualizarBoton, 0, Qt.AlignHCenter)

        self.label_8 = QLabel(self.perfilPagina)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_15.addWidget(self.label_8, 0, Qt.AlignHCenter|Qt.AlignBottom)

        self.derechoPaginas.addWidget(self.perfilPagina)
        self.masPagina = QWidget()
        self.masPagina.setObjectName(u"masPagina")
        self.verticalLayout_16 = QVBoxLayout(self.masPagina)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.masPagina)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)

        self.verticalLayout_16.addWidget(self.label_9)

        self.derechoPaginas.addWidget(self.masPagina)
        self.eliminarPagina = QWidget()
        self.eliminarPagina.setObjectName(u"eliminarPagina")
        self.gridLayout = QGridLayout(self.eliminarPagina)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_22 = QLabel(self.eliminarPagina)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout.addWidget(self.label_22, 7, 0, 1, 1)

        self.label_24 = QLabel(self.eliminarPagina)
        self.label_24.setObjectName(u"label_24")
        sizePolicy9 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy9.setHorizontalStretch(50)
        sizePolicy9.setVerticalStretch(50)
        sizePolicy9.setHeightForWidth(self.label_24.sizePolicy().hasHeightForWidth())
        self.label_24.setSizePolicy(sizePolicy9)
        self.label_24.setMinimumSize(QSize(50, 50))
        self.label_24.setPixmap(QPixmap(u":/feather/icons/feather/trash-2.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setWordWrap(False)

        self.gridLayout.addWidget(self.label_24, 0, 0, 1, 1, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.eliminarPagina)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMinimumSize(QSize(227, 224))
        self.widget_3.setMaximumSize(QSize(227, 16777215))
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_13 = QFrame(self.widget_3)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.gridLayout_2 = QGridLayout(self.frame_13)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(0)
        self.gridLayout_2.setVerticalSpacing(3)
        self.gridLayout_2.setContentsMargins(9, 0, 0, 2)
        self.label_28 = QLabel(self.frame_13)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font7)

        self.gridLayout_2.addWidget(self.label_28, 2, 0, 1, 1)

        self.nombreActualizar = QLineEdit(self.frame_13)
        self.nombreActualizar.setObjectName(u"nombreActualizar")

        self.gridLayout_2.addWidget(self.nombreActualizar, 3, 0, 1, 1)

        self.cedulaEliminar = QLineEdit(self.frame_13)
        self.cedulaEliminar.setObjectName(u"cedulaEliminar")
        self.cedulaEliminar.setMinimumSize(QSize(0, 0))
        self.cedulaEliminar.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.cedulaEliminar, 1, 0, 1, 1)

        self.label_29 = QLabel(self.frame_13)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font7)

        self.gridLayout_2.addWidget(self.label_29, 4, 0, 1, 1)

        self.label_27 = QLabel(self.frame_13)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font7)

        self.gridLayout_2.addWidget(self.label_27, 0, 0, 1, 1)

        self.correoActualizar = QLineEdit(self.frame_13)
        self.correoActualizar.setObjectName(u"correoActualizar")

        self.gridLayout_2.addWidget(self.correoActualizar, 9, 0, 1, 1)

        self.telefonoActualizar = QLineEdit(self.frame_13)
        self.telefonoActualizar.setObjectName(u"telefonoActualizar")

        self.gridLayout_2.addWidget(self.telefonoActualizar, 7, 0, 1, 1)

        self.apellidoActualizar = QLineEdit(self.frame_13)
        self.apellidoActualizar.setObjectName(u"apellidoActualizar")

        self.gridLayout_2.addWidget(self.apellidoActualizar, 5, 0, 1, 1)

        self.label_30 = QLabel(self.frame_13)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font7)

        self.gridLayout_2.addWidget(self.label_30, 6, 0, 1, 1)

        self.label_31 = QLabel(self.frame_13)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font7)

        self.gridLayout_2.addWidget(self.label_31, 8, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_13, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget_3, 1, 0, 1, 1)

        self.eliminarBoton = QPushButton(self.eliminarPagina)
        self.eliminarBoton.setObjectName(u"eliminarBoton")
        self.eliminarBoton.setMinimumSize(QSize(0, 10))
        self.eliminarBoton.setFont(font7)
        icon25 = QIcon()
        icon25.addFile(u":/feather/icons/feather/alert-triangle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.eliminarBoton.setIcon(icon25)
        self.eliminarBoton.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.eliminarBoton, 6, 0, 1, 1, Qt.AlignHCenter)

        self.editarBoton = QPushButton(self.eliminarPagina)
        self.editarBoton.setObjectName(u"editarBoton")
        self.editarBoton.setMinimumSize(QSize(0, 10))
        self.editarBoton.setFont(font7)
        icon26 = QIcon()
        icon26.addFile(u":/feather/icons/feather/refresh-cw.png", QSize(), QIcon.Normal, QIcon.Off)
        self.editarBoton.setIcon(icon26)
        self.editarBoton.setIconSize(QSize(40, 40))

        self.gridLayout.addWidget(self.editarBoton, 2, 0, 1, 1, Qt.AlignHCenter)

        self.derechoPaginas.addWidget(self.eliminarPagina)

        self.verticalLayout_31.addWidget(self.derechoPaginas)


        self.verticalLayout_13.addWidget(self.subMenuDerecho)


        self.horizontalLayout_7.addWidget(self.menuContenedorDerecho)

        self.menuContenedorDerecho.raise_()
        self.principalContenidosContenedor.raise_()

        self.verticalLayout_12.addWidget(self.principalCuerpoContenido)

        self.emergenteNotificacionContenedor = QCustomSlideMenu(self.principalCuerpoContenedor)
        self.emergenteNotificacionContenedor.setObjectName(u"emergenteNotificacionContenedor")
        self.verticalLayout_24 = QVBoxLayout(self.emergenteNotificacionContenedor)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.emergenteNotificacionSubContenedor = QWidget(self.emergenteNotificacionContenedor)
        self.emergenteNotificacionSubContenedor.setObjectName(u"emergenteNotificacionSubContenedor")
        self.verticalLayout_25 = QVBoxLayout(self.emergenteNotificacionSubContenedor)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_17 = QLabel(self.emergenteNotificacionSubContenedor)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font7)

        self.verticalLayout_25.addWidget(self.label_17, 0, Qt.AlignHCenter)

        self.frame_10 = QFrame(self.emergenteNotificacionSubContenedor)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setLayoutDirection(Qt.LeftToRight)
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, -1, 0)
        self.label_16 = QLabel(self.frame_10)
        self.label_16.setObjectName(u"label_16")
        sizePolicy3.setHeightForWidth(self.label_16.sizePolicy().hasHeightForWidth())
        self.label_16.setSizePolicy(sizePolicy3)
        self.label_16.setFont(font7)
        self.label_16.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_16)

        self.cerrarNotificacion = QPushButton(self.frame_10)
        self.cerrarNotificacion.setObjectName(u"cerrarNotificacion")
        self.cerrarNotificacion.setLayoutDirection(Qt.LeftToRight)
        self.cerrarNotificacion.setIcon(icon13)
        self.cerrarNotificacion.setIconSize(QSize(24, 24))

        self.horizontalLayout_9.addWidget(self.cerrarNotificacion, 0, Qt.AlignRight)


        self.verticalLayout_25.addWidget(self.frame_10)


        self.verticalLayout_24.addWidget(self.emergenteNotificacionSubContenedor)


        self.verticalLayout_12.addWidget(self.emergenteNotificacionContenedor)

        self.pieContenedor = QWidget(self.principalCuerpoContenedor)
        self.pieContenedor.setObjectName(u"pieContenedor")
        self.horizontalLayout_10 = QHBoxLayout(self.pieContenedor)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(20, 0, 0, 0)
        self.frame_16 = QFrame(self.pieContenedor)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_16)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_2 = QLabel(self.frame_16)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_16.addWidget(self.label_2)

        self.temaProgreso = QProgressBar(self.frame_16)
        self.temaProgreso.setObjectName(u"temaProgreso")
        self.temaProgreso.setMaximumSize(QSize(16777215, 10))
        self.temaProgreso.setValue(24)
        self.temaProgreso.setTextVisible(False)

        self.horizontalLayout_16.addWidget(self.temaProgreso)


        self.horizontalLayout_10.addWidget(self.frame_16, 0, Qt.AlignLeft)

        self.frame_12 = QFrame(self.pieContenedor)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.NoFrame)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_18 = QLabel(self.frame_12)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font7)

        self.horizontalLayout_11.addWidget(self.label_18)


        self.horizontalLayout_10.addWidget(self.frame_12, 0, Qt.AlignRight)

        self.dimensionBarra = QFrame(self.pieContenedor)
        self.dimensionBarra.setObjectName(u"dimensionBarra")
        self.dimensionBarra.setMinimumSize(QSize(10, 10))
        self.dimensionBarra.setMaximumSize(QSize(10, 10))
        self.dimensionBarra.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_10.addWidget(self.dimensionBarra, 0, Qt.AlignBottom)


        self.verticalLayout_12.addWidget(self.pieContenedor)


        self.horizontalLayout.addWidget(self.principalCuerpoContenedor)

        ventanaPrincipal.setCentralWidget(self.centralContenedor)

        self.retranslateUi(ventanaPrincipal)

        self.centroPaginas.setCurrentIndex(0)
        self.principalPaginas.setCurrentIndex(0)
        self.derechoPaginas.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(ventanaPrincipal)
    # setupUi

    def retranslateUi(self, ventanaPrincipal):
        ventanaPrincipal.setWindowTitle(QCoreApplication.translate("ventanaPrincipal", u"Sistema Gestion Estudiantil Andres Bello", None))
#if QT_CONFIG(tooltip)
        self.menuBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBoton.setText("")
#if QT_CONFIG(tooltip)
        self.inicioBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Inicio", None))
#endif // QT_CONFIG(tooltip)
        self.inicioBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"INICIO", None))
#if QT_CONFIG(tooltip)
        self.estudianteBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Estudiantes", None))
#endif // QT_CONFIG(tooltip)
        self.estudianteBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ESTUDIANTES", None))
#if QT_CONFIG(tooltip)
        self.materiaBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Materias", None))
#endif // QT_CONFIG(tooltip)
        self.materiaBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"MATERIAS", None))
#if QT_CONFIG(tooltip)
        self.profesorBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Profesores", None))
#endif // QT_CONFIG(tooltip)
        self.profesorBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"PROFESORES", None))
#if QT_CONFIG(tooltip)
        self.notaBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Notas", None))
#endif // QT_CONFIG(tooltip)
        self.notaBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"NOTAS", None))
#if QT_CONFIG(tooltip)
        self.documentoBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Documentos", None))
#endif // QT_CONFIG(tooltip)
        self.documentoBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"DOCUMENTOS", None))
#if QT_CONFIG(tooltip)
        self.gradosBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Grados", None))
#endif // QT_CONFIG(tooltip)
        self.gradosBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"GRADOS", None))
#if QT_CONFIG(tooltip)
        self.ajustesBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Ajustes", None))
#endif // QT_CONFIG(tooltip)
        self.ajustesBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"AJUSTES", None))
#if QT_CONFIG(tooltip)
        self.acercaDeBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Acerca de", None))
#endif // QT_CONFIG(tooltip)
        self.acercaDeBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ACERCA DE", None))
#if QT_CONFIG(tooltip)
        self.ayudaBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Ayuda", None))
#endif // QT_CONFIG(tooltip)
        self.ayudaBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"AYUDA", None))
#if QT_CONFIG(tooltip)
        self.cerrarSesionBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Sesion", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarSesionBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"CERRAR SESION", None))
        self.label.setText(QCoreApplication.translate("ventanaPrincipal", u"Mas cositas", None))
#if QT_CONFIG(tooltip)
        self.cerrarMenuCentro.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Menu", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarMenuCentro.setText("")
        self.label_10.setText(QCoreApplication.translate("ventanaPrincipal", u"Eleccion de Tema", None))
        self.label_26.setText(QCoreApplication.translate("ventanaPrincipal", u"Tema:", None))
        self.label_3.setText(QCoreApplication.translate("ventanaPrincipal", u"ACERCA DE", None))
        self.label_4.setText(QCoreApplication.translate("ventanaPrincipal", u"AYUDA", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("ventanaPrincipal", u"COMPLEJO EDUCATIVO ANDRES BELLO", None))
#if QT_CONFIG(tooltip)
        self.notificacionBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Notificacion", None))
#endif // QT_CONFIG(tooltip)
        self.notificacionBoton.setText("")
#if QT_CONFIG(tooltip)
        self.masBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Mas", None))
#endif // QT_CONFIG(tooltip)
        self.masBoton.setText("")
#if QT_CONFIG(tooltip)
        self.perfilBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Perfil", None))
#endif // QT_CONFIG(tooltip)
        self.perfilBoton.setText("")
#if QT_CONFIG(tooltip)
        self.busquedaBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Buscar", None))
#endif // QT_CONFIG(tooltip)
        self.busquedaBoton.setText("")
        self.busquedaTexto.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Busqueda...", None))
#if QT_CONFIG(tooltip)
        self.botonMenuEliminar.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Borrar", None))
#endif // QT_CONFIG(tooltip)
        self.botonMenuEliminar.setText("")
#if QT_CONFIG(tooltip)
        self.minimizarBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Minimizar Ventana", None))
#endif // QT_CONFIG(tooltip)
        self.minimizarBoton.setText("")
#if QT_CONFIG(tooltip)
        self.restaurarBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Restaurar Ventana", None))
#endif // QT_CONFIG(tooltip)
        self.restaurarBoton.setText("")
#if QT_CONFIG(tooltip)
        self.cerrarBoton.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Ventana", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarBoton.setText("")
        self.label_53.setText("")
        self.label_34.setText(QCoreApplication.translate("ventanaPrincipal", u"INICIO", None))
        self.label_35.setText(QCoreApplication.translate("ventanaPrincipal", u"2304000", None))
        self.label_36.setText("")
        self.label_37.setText(QCoreApplication.translate("ventanaPrincipal", u"Matriculados", None))
        self.label_44.setText(QCoreApplication.translate("ventanaPrincipal", u"+340", None))
        self.label_45.setText("")
        self.label_46.setText(QCoreApplication.translate("ventanaPrincipal", u"Docentes", None))
        self.label_47.setText(QCoreApplication.translate("ventanaPrincipal", u"450", None))
        self.label_48.setText("")
        self.label_49.setText(QCoreApplication.translate("ventanaPrincipal", u"Materias", None))
        self.label_50.setText(QCoreApplication.translate("ventanaPrincipal", u"2304000", None))
        self.label_51.setText("")
        self.label_52.setText(QCoreApplication.translate("ventanaPrincipal", u"Secciones", None))
        self.label_54.setText(QCoreApplication.translate("ventanaPrincipal", u"Ultimos Estudiantes", None))
        self.masVer.setText(QCoreApplication.translate("ventanaPrincipal", u"Ver mas", None))
        self.label_56.setText(QCoreApplication.translate("ventanaPrincipal", u"Grado", None))
        self.label_57.setText(QCoreApplication.translate("ventanaPrincipal", u"Sexo", None))
        self.label_55.setText(QCoreApplication.translate("ventanaPrincipal", u"Nacionalidad", None))
        self.label_58.setText(QCoreApplication.translate("ventanaPrincipal", u"V", None))
        self.label_60.setText(QCoreApplication.translate("ventanaPrincipal", u"F", None))
        self.label_59.setText(QCoreApplication.translate("ventanaPrincipal", u"\"A\"", None))
        self.label_62.setText(QCoreApplication.translate("ventanaPrincipal", u"\"C\"", None))
        self.label_65.setText(QCoreApplication.translate("ventanaPrincipal", u"\"A\"", None))
        self.label_64.setText(QCoreApplication.translate("ventanaPrincipal", u"V", None))
        self.label_66.setText(QCoreApplication.translate("ventanaPrincipal", u"F", None))
        self.label_63.setText(QCoreApplication.translate("ventanaPrincipal", u"M", None))
        self.label_61.setText(QCoreApplication.translate("ventanaPrincipal", u"E", None))
        self.label_67.setText(QCoreApplication.translate("ventanaPrincipal", u"V", None))
        self.label_68.setText(QCoreApplication.translate("ventanaPrincipal", u"\"B\"", None))
        self.label_69.setText(QCoreApplication.translate("ventanaPrincipal", u"F", None))
        self.label_70.setText(QCoreApplication.translate("ventanaPrincipal", u"Ultimas Materias", None))
        self.verMas2.setText(QCoreApplication.translate("ventanaPrincipal", u"Ver Mas", None))
        self.label_75.setText("")
        self.label_76.setText(QCoreApplication.translate("ventanaPrincipal", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Universidad</span></p><p>UBV</p></body></html>", None))
        self.label_77.setText("")
        self.label_78.setText("")
        self.label_79.setText("")
        self.label_85.setText("")
        self.label_86.setText(QCoreApplication.translate("ventanaPrincipal", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Universidad</span></p><p>UBV</p></body></html>", None))
        self.label_87.setText("")
        self.label_88.setText("")
        self.label_89.setText("")
        self.label_80.setText("")
        self.label_81.setText(QCoreApplication.translate("ventanaPrincipal", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Universidad</span></p><p>UBV</p></body></html>", None))
        self.label_82.setText("")
        self.label_83.setText("")
        self.label_84.setText("")
        self.label_38.setText("")
        self.label_39.setText(QCoreApplication.translate("ventanaPrincipal", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Universidad</span></p><p>UBV</p></body></html>", None))
        self.label_40.setText("")
        self.label_42.setText("")
        self.label_41.setText("")
        self.label_11.setText(QCoreApplication.translate("ventanaPrincipal", u"ESTUDIANTES", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ventanaPrincipal", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ventanaPrincipal", u"Cedula", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ventanaPrincipal", u"Nombre", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ventanaPrincipal", u"Apellido", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("ventanaPrincipal", u"Telefono", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("ventanaPrincipal", u"Correo", None));
        self.label_12.setText(QCoreApplication.translate("ventanaPrincipal", u"MATERIAS", None))
        self.label_13.setText(QCoreApplication.translate("ventanaPrincipal", u"PROFESORES", None))
        self.label_14.setText(QCoreApplication.translate("ventanaPrincipal", u"NOTAS", None))
        self.label_15.setText(QCoreApplication.translate("ventanaPrincipal", u"DOCUMENTOS", None))
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem7 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem8 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem9 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem10 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem11 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem12 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem13 = self.tableWidget_3.verticalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem14 = self.tableWidget_3.verticalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem15 = self.tableWidget_3.verticalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem16 = self.tableWidget_3.verticalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem17 = self.tableWidget_3.verticalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget_3.verticalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget_3.verticalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        self.label_19.setText(QCoreApplication.translate("ventanaPrincipal", u"GRADOS", None))
        ___qtablewidgetitem20 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem21 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem22 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem23 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem24 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("ventanaPrincipal", u"New Column", None));
        ___qtablewidgetitem25 = self.tableWidget_2.verticalHeaderItem(0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem26 = self.tableWidget_2.verticalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem27 = self.tableWidget_2.verticalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem28 = self.tableWidget_2.verticalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem29 = self.tableWidget_2.verticalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem30 = self.tableWidget_2.verticalHeaderItem(5)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem31 = self.tableWidget_2.verticalHeaderItem(6)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem32 = self.tableWidget_2.verticalHeaderItem(7)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem33 = self.tableWidget_2.verticalHeaderItem(8)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem34 = self.tableWidget_2.verticalHeaderItem(9)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        ___qtablewidgetitem35 = self.tableWidget_2.verticalHeaderItem(10)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("ventanaPrincipal", u"New Row", None));
        self.label_7.setText(QCoreApplication.translate("ventanaPrincipal", u"Informacion Detallada", None))
#if QT_CONFIG(tooltip)
        self.cerrarMenuDerecho.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Menu", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarMenuDerecho.setText("")
        self.label_25.setText("")
        self.correo.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Correo Electronico", None))
        self.label_33.setText(QCoreApplication.translate("ventanaPrincipal", u"Cedula de Identidad", None))
        self.apellido.setText("")
        self.apellido.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Apellido", None))
        self.label_23.setText(QCoreApplication.translate("ventanaPrincipal", u"Telefono", None))
        self.nombre.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Nombre", None))
        self.cedula.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Nro. de Cedula", None))
        self.telefono.setText("")
        self.telefono.setPlaceholderText(QCoreApplication.translate("ventanaPrincipal", u"Telefono", None))
        self.label_20.setText(QCoreApplication.translate("ventanaPrincipal", u"Nombre", None))
        self.label_21.setText(QCoreApplication.translate("ventanaPrincipal", u"Apellido", None))
        self.label_32.setText(QCoreApplication.translate("ventanaPrincipal", u"Correo Electronico", None))
        self.actualizarBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ACTUALIZAR", None))
        self.label_8.setText(QCoreApplication.translate("ventanaPrincipal", u"PERFIL", None))
        self.label_9.setText(QCoreApplication.translate("ventanaPrincipal", u"MAS...", None))
        self.label_22.setText(QCoreApplication.translate("ventanaPrincipal", u"CUIDADO", None))
        self.label_24.setText("")
        self.label_28.setText(QCoreApplication.translate("ventanaPrincipal", u"Nombre", None))
        self.label_29.setText(QCoreApplication.translate("ventanaPrincipal", u"Apellido", None))
        self.label_27.setText(QCoreApplication.translate("ventanaPrincipal", u"Cedula", None))
        self.label_30.setText(QCoreApplication.translate("ventanaPrincipal", u"Telefono", None))
        self.label_31.setText(QCoreApplication.translate("ventanaPrincipal", u"Correo", None))
        self.eliminarBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ELIMINAR", None))
        self.editarBoton.setText(QCoreApplication.translate("ventanaPrincipal", u"ACTUALIZAR", None))
        self.label_17.setText(QCoreApplication.translate("ventanaPrincipal", u"Notificacion", None))
        self.label_16.setText(QCoreApplication.translate("ventanaPrincipal", u"Notificacion Mensaje Acivo para Los Efectos Especiales", None))
#if QT_CONFIG(tooltip)
        self.cerrarNotificacion.setToolTip(QCoreApplication.translate("ventanaPrincipal", u"Cerrar Notificacion", None))
#endif // QT_CONFIG(tooltip)
        self.cerrarNotificacion.setText("")
        self.label_2.setText(QCoreApplication.translate("ventanaPrincipal", u"Tema Progreso", None))
        self.label_18.setText(QCoreApplication.translate("ventanaPrincipal", u"Creado por: Yoel Rivero UBV", None))
    # retranslateUi


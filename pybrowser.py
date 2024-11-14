#PySide Browser, by Lee

from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon
from PySide2.QtWebEngineWidgets import *
from PySide2.QtCore import QUrl, QSize

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide Browser - Indev")
        self.setWindowIcon(QIcon("icons/globe.png"))

        self.tabs = QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tabs.setTabsClosable(True)

        self.tabs.currentChanged.connect(self.web_url)
        self.tabs.tabCloseRequested.connect(self.close_tab)

        self.url = "https://google.com"

        toolbar = QToolBar("Actions")
        toolbar.setIconSize(QSize(16,16))
        toolbar.setMovable(False)
        
        back_button = QPushButton()
        back_button.clicked.connect(self.web_back)
        back_button.setIcon(QIcon("icons/back.png"))
        back_button.setToolTip("Go back")

        forward_button = QPushButton()
        forward_button.clicked.connect(self.web_forward)
        forward_button.setIcon(QIcon("icons/forward.png"))
        forward_button.setToolTip("Go forward")

        home_button = QPushButton()
        home_button.clicked.connect(self.web_home)
        home_button.setIcon(QIcon("icons/home.png"))
        home_button.setToolTip("Go home")

        self.searchbox = QLineEdit()
        self.searchbox.returnPressed.connect(self.web_search)

        refresh_button = QPushButton()
        refresh_button.clicked.connect(self.web_refresh)
        refresh_button.setIcon(QIcon("icons/refresh.png"))
        refresh_button.setToolTip("Refresh page")

        clear_button = QPushButton()
        clear_button.clicked.connect(self.web_clear)
        clear_button.setIcon(QIcon("icons/clear.png"))
        clear_button.setToolTip("Clear")

        new_tab_button = QPushButton()
        new_tab_button.clicked.connect(self.new_tab)
        new_tab_button.setIcon(QIcon("icons/new.png"))
        new_tab_button.setToolTip("New tab")

        toolbar.addWidget(back_button)
        toolbar.addWidget(forward_button)
        toolbar.addWidget(refresh_button)
        toolbar.addWidget(home_button)
        toolbar.addSeparator()
        toolbar.addWidget(self.searchbox)
        toolbar.addWidget(clear_button)
        toolbar.addSeparator()
        toolbar.addWidget(new_tab_button)

        self.addToolBar(toolbar)

        self.setCentralWidget(self.tabs)

    def new_tab(self):
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(self.url))
        self.browser.urlChanged.connect(self.web_url)
        self.browser.urlChanged.connect(self.web_title)
        self.tabs.addTab(self.browser,"google.com")
        self.tabs.setCurrentIndex(self.tabs.count()-1)

    def web_back(self):
        self.tabs.currentWidget().back()

    def web_forward(self):
        self.tabs.currentWidget().forward()

    def web_refresh(self):
        self.tabs.currentWidget().reload()

    def web_home(self):
        self.browser.setUrl(QUrl(self.url))

    def web_search(self):
        textbox = self.searchbox.text()
        widget = self.tabs.currentWidget()
        if textbox.find(".") == -1:
            widget.setUrl(QUrl("https://www.google.com/search?q="+self.searchbox.text()))
        elif textbox[:8] != "https://":
            widget.setUrl(QUrl("https://"+textbox))
        else:
            self.tabs.currentWidget().setUrl(QUrl(self.searchbox.text()))

    def web_url(self):
        self.searchbox.setText(self.tabs.currentWidget().url().toString())

    def web_clear(self):
        self.searchbox.clear()

    def close_tab(self,i):
        if self.tabs.count() < 2:
            self.new_tab()
        self.tabs.removeTab(i)

    def web_title(self):
        new_url = self.tabs.currentWidget().url().toString()
        new_url = new_url[12:] if new_url[8:11] == "www" else new_url[8:]
        self.tabs.setTabText(self.tabs.currentIndex(),new_url[:new_url.find("/")])

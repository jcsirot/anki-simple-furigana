from aqt.qt import *
from aqt import mw

class SettingsGui(QWidget):
    def __init__(self, mw):
        super(SettingsGui, self).__init__()
        self.mw = mw
        self.readingsForNumbers = QCheckBox('Add readings for numbers')
        self.readingsForNumbers.setFixedHeight(30)
        self.readingsForNumbers.setToolTip('Enable/disable readings for numbers.')
        self.cancelButton = QPushButton('Cancel')
        self.applyButton = QPushButton('Apply')
        self.cancelButton.clicked.connect(self.close)
        self.applyButton.clicked.connect(self.saveConfig)
        self.layout = QVBoxLayout()
        # self.settingsTab = QWidget(self)
        self.loadConfig()
        self.setWindowTitle('Simple Furigana settings')
        self.setupLayout()
        self.resize(300, 100)

    def setupLayout(self):

        readingNumberLayout = QHBoxLayout()
        readingNumberLayout.addWidget(self.readingsForNumbers)
        #readingNumberLayout.addWidget(QLabel('Add furiganas for numbers'))
        readingNumberLayout.addStretch(1)
        self.layout.addLayout(readingNumberLayout)
        
        self.layout.addStretch(1)
        
        buttonsLayout = QHBoxLayout()
        buttonsLayout.addStretch(1)
        buttonsLayout.addWidget(self.cancelButton)
        buttonsLayout.addWidget(self.applyButton)
        self.layout.addLayout(buttonsLayout)

        self.setLayout(self.layout)

    def getConfig(self):
        return self.mw.addonManager.getConfig(__name__)

    def loadConfig(self):
        config = self.getConfig()
        self.readingsForNumbers.setChecked(config['readingsForNumbers'])

    def saveConfig(self):
        nc = self.getConfig()
        nc['readingsForNumbers'] = self.readingsForNumbers.isChecked()
        self.mw.addonManager.writeConfig(__name__, nc)
        self.hide()
        self.mw.refreshConfig()

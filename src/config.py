from aqt.qt import *
from aqt import mw
from .const import FURIGANA_PATTERNS

class SettingsGui(QWidget):
    def __init__(self, mw):
        super(SettingsGui, self).__init__()
        self.mw = mw
        self.readingsForNumbers = QCheckBox('Add readings for numbers')
        self.readingsForNumbers.setFixedHeight(30)
        self.readingsForNumbers.setToolTip('Enable/disable readings for numbers.')
        self.readingsPatternLabel = QLabel('Readings pattern:')
        self.readingsPattern = QComboBox()
        self.readingsPattern.addItems(FURIGANA_PATTERNS)
        self.readingsPattern.setToolTip('Pattern applied when adding readings.')
        self.cancelButton = QPushButton('Cancel')
        self.applyButton = QPushButton('Apply')
        self.cancelButton.clicked.connect(self.close)
        self.applyButton.clicked.connect(self.saveConfig)
        self.layout = QVBoxLayout()
        self.loadConfig()
        self.setWindowTitle('Simple Furigana settings')
        self.setupLayout()
        self.resize(330, 100)

    def setupLayout(self):

        readingNumberLayout = QHBoxLayout()
        readingNumberLayout.addWidget(self.readingsForNumbers)
        readingNumberLayout.addStretch(1)
        self.layout.addLayout(readingNumberLayout)
        
        patternLayout = QHBoxLayout()
        patternLayout.addWidget(self.readingsPatternLabel)
        patternLayout.addWidget(self.readingsPattern)
        patternLayout.addStretch(1)
        self.layout.addLayout(patternLayout)

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
        self.readingsPattern.setCurrentText(config['readingsPattern'])

    def saveConfig(self):
        nc = self.getConfig()
        nc['readingsForNumbers'] = self.readingsForNumbers.isChecked()
        nc['readingsPattern'] = self.readingsPattern.currentText()
        self.mw.addonManager.writeConfig(__name__, nc)
        self.hide()
        self.mw.refreshConfig()

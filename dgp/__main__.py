# -*- coding: utf-8 -*-
import sys
import time
import traceback

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QSplashScreen

from dgp.gui.main import MainWindow

app = None


def excepthook(type_, value, traceback_):
    """This allows IDE to properly display unhandled exceptions which are
    otherwise silently ignored as the application is terminated.
    Override default excepthook with
    >>> sys.excepthook = excepthook

    See: http://pyqt.sourceforge.net/Docs/PyQt5/incompatibilities.html
    """
    traceback.print_exception(type_, value, traceback_)
    QtCore.qFatal('')


def main():
    _align = Qt.AlignBottom | Qt.AlignHCenter
    global app
    sys.excepthook = excepthook
    app = QApplication(sys.argv)
    splash = QSplashScreen(QPixmap(":/icons/dgp_large"))
    splash.showMessage("Loading Dynamic Gravity Processor", _align)
    splash.show()
    time.sleep(.5)
    window = MainWindow()
    splash.finish(window)
    window.sigStatusMessage.connect(lambda msg: splash.showMessage(msg, _align))
    window.load()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()

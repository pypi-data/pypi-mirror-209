
# Automaticly generated code.
# Changes here can get overwritten!

import os


class PequenaApi:
    def __init__(self, window):
        self._window = window

    def getWindowInfo(self):
        return {"x": self._window.x, "y": self._window.y, "width": self._window.width, "height": self._window.height}

    def minimizeWindow(self):
        return self._window.minimize()

    def unminimizeWindow(self):
        return self._window.restore()

    def hideWindow(self):
        return self._window.hide()

    def unhideWindow(self):
        return self._window.show()

    def toggleFullscreen(self):
        return self._window.toggle_fullscreen()

    def moveWindow(self, _x, _y):
        return self._window.move(_x, _y)

    def resizeWindow(self, _width, _height):
        return self._window.resize(_width, _height)

    def setWindowName(self, _name):
        return self._window.set_title(_name)


class NodeApi:
    class fs:
        def readFile(self, _path):
            with open(_path, 'r') as file:
                return file.read()

        def writeFile(self, _path, _content):
            with open(_path, 'w') as file:
                file.write(_content)

        def mkdir(self, _path):
            os.mkdir(_path)

        def readdir(self, _path):
            return os.listdir(_path)

        def pathExists(self, _path):
            return os.path.exists(_path)

        def isfile(self, _path):
            return os.path.isfile(_path)

        def isdir(self, _path):
            return os.path.isdir(_path)

    class path:
        def join(self, *paths):
            return os.path.join(*paths)

        def basename(self, _path):
            return os.path.basename(_path)

        def dirname(self, _path):
            return os.path.dirname(_path)

        def resolve(self, *paths):
            return os.path.abspath(os.path.join(*paths))

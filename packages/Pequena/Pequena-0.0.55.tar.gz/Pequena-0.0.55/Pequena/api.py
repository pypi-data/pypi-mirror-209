
# Automaticly generated code.
# Changes here can get overwritten!

import webview
import os


class PequenaApi:
    def getWindowInfo():
        return {"x": webview.windows[0].x, "y": webview.windows[0].y, "width": webview.windows[0].width, "height": webview.windows[0].height}

    def getScreenInfo():
        return {"width": webview.screens[0].width, "height": webview.screens[0].height}

    def minimizeWindow():
        return webview.windows[0].minimize()

    def unminimizeWindow():
        return webview.windows[0].restore()

    def hideWindow():
        return webview.windows[0].hide()

    def unhideWindow():
        return webview.windows[0].show()

    def toggleFullscreen():
        return webview.windows[0].toggle_fullscreen()

    def moveWindow(_x, _y):
        return webview.windows[0].move(_x, _y)

    def resizeWindow(_width, _height):
        return webview.windows[0].resize(_width, _height)

    def setWindowName(_name):
        return webview.windows[0].set_title(_name)


class NodeApi:
    class fs:
        def readFile(_path):
            with open(_path, 'r') as file:
                return file.read()

        def writeFile(_path, _content):
            with open(_path, 'w') as file:
                file.write(_content)

        def mkdir(_path):
            os.mkdir(_path)

        def readdir(_path):
            return os.listdir(_path)

        def pathExists(_path):
            return os.path.exists(_path)

        def isfile(_path):
            return os.path.isfile(_path)

        def isdir(_path):
            return os.path.isdir(_path)

    class path:
        def join(*paths):
            return os.path.join(*paths)

        def basename(_path):
            return os.path.basename(_path)

        def dirname(_path):
            return os.path.dirname(_path)

        def resolve(*paths):
            return os.path.abspath(os.path.join(*paths))

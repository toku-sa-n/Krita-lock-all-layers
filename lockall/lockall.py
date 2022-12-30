from krita import Krita, Extension


def lock_leaves(node):
    children = node.childNodes()

    if children:
        node.setLocked(False)

        for child in children:
            lock_leaves(child)
    else:
        node.setLocked(True)


class LockAllExtension(Extension):
    def __init__(self, parent):
        super().__init__(parent)

    def setup(self):
        pass

    def createActions(self, window):
        action = window.createAction("lockall", "Lock all layers")
        action.triggered.connect(self.lock_all)

    def lock_all(self):
        d = Krita.instance().activeDocument()
        if d:
            lock_leaves(d.rootNode())


Krita.instance().addExtension(LockAllExtension(Krita.instance()))

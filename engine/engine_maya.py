from engine.engine_base import BaseEngine


class MayaEngine(BaseEngine):
    implements = ['open', 'save', 'reference']
    valid_extensions = ['ma', 'mb']

    def __init__(self):
        super(MayaEngine, self).__init__()

    def open(self, path):
        import pymel.core as pm
        try:
            pm.openFile(path, f=True)
        except RuntimeError as e:
            print("Failed to open file: {}".format(e))

    def save(self, path):
        import pymel.core as pm
        pm.saveFile()

    def reference(self, path):
        import pymel.core as pm
        pm.createReference(path)


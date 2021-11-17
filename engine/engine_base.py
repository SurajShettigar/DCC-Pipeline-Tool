class BaseEngine(object):
    implements = ['open', 'save']
    valid_extensions = ['ma', 'mb']

    def __init__(self):
        pass

    def open(self, path):
        print("Opening file with path: {}".format(path))

    def save(self, path):
        print("Saving current file: {}".format(path))

    @staticmethod
    def get_engine():
        from engine.engine_maya import MayaEngine
        from engine.engine_houdini import HoudiniEngine
        import sys
        exe = sys.executable
        if str(exe).lower().__contains__('maya') > 0:
            return MayaEngine()
        elif str(exe).lower().__contains__('houdini') > 0:
            return HoudiniEngine()
        else:
            return BaseEngine()

if __name__ == '__main__':
    print(BaseEngine.get_engine())

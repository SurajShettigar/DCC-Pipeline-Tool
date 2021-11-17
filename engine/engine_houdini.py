import six

from engine.engine_base import BaseEngine


class HoudiniEngine(BaseEngine):
    implements = ['open', 'save', 'merge']
    valid_extensions = ['hip', 'hiplc', 'hipnc']

    def __init__(self):
        super(HoudiniEngine, self).__init__()

    def open(self, path):
        from hou import hipFile as hp
        hp.load(path, suppress_save_prompt=True)

    def save(self, path):
        from hou import hipFile as hp
        hp.save()

    def merge(self, path):
        from hou import hipFile as hp
        hp.merge(path)

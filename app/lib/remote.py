from app.lib import conf
from app import __metadata__ as meta
import os
import json
import logging

log = logging.getLogger(__name__)

class Remote(object):
    """
    Remotes List Module
    """
    def __init__(self):
        self.remotes = []
        try:
            self.remotes_file = conf.Config().get(meta.APP_NAME, '{}.remote.conf'.format(meta.APP_NAME.lower()))
            self.remotes = self.load()
        except Exception('Unable to load remotes list.') as e:
            log.debug(e)

    def load(self):
        try:
            with open(self.remotes_file, 'r') as f:
                # make sure the file is not empty
                if os.stat(self.remotes_file).st_size != 0:
                    log.info('Reading remotes file.')
                    data = f.read()
                    return json.loads(data)
        except (FileNotFoundError, IOError) as e:
            log.info('Unable to open remotes file: ' + self.remotes_file)
            log.debug(e)
        return []

    def get(self, i):
        if i is None or len(self.remotes) <= i:
            return None
        else:
            return self.remotes[i]

    def get_list(self):
        return self.remotes

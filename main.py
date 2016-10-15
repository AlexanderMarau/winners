
from tornado import ioloop, web

from modules.Home import Home
from modules.Auth import Auth

import settings
import os

application = web.Application([
    (r'/static/(.*)', web.StaticFileHandler, dict(path=settings.settings['static_path'])),
    (r'/', Home),
    (r'/login', Auth)
], **settings.settings)

if __name__ == "__main__":
    application.listen(8888)
    ioloop.IOLoop.instance().start()
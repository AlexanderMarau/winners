
from tornado import ioloop,web

from modules.Index import Index
from modules.ClientsHandler import ClientsHandler

import settings

application = web.Application([
    (r'/', Index),
    (r'/index', Index),
    (r'/api/v1/clients',ClientsHandler)
], **settings.settings)

if __name__ == "__main__":
    application.listen(8888)
    ioloop.IOLoop.instance().start()
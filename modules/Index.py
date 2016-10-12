import tornado.ioloop
import tornado.web
 
class Index(tornado.web.RequestHandler):
    def get(self):
    	tornado.web.Application([
	        (r"/", self.write("Hello, world TEST")),
	    ])
        
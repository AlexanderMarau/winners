import tornado.ioloop
import tornado.web
 
class Auth(tornado.web.RequestHandler):
    
    def get(self):
    	tornado.web.Application([
	        (r"/", self.render("login.html")),
	    ])
        
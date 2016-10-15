import tornado.ioloop
import tornado.web
 
class Home(tornado.web.RequestHandler):
    
    def get(self):
    	tornado.web.Application([
	        (r"/", self.render("home.html")),
	    ])
        
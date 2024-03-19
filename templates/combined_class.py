class MainHandler(SessionBaseHandler):

     def __init__(self, *args, **kwargs):
         global logger
         super(MainHandler, self).__init__(*args, **kwargs)

     @tornado.web.asynchronous
     @tornado.gen.coroutine
     def post(self,func_name):
         request = self.request.body
         func = getattr(self, func_name)
         response = yield tornado.gen.Task(func,request)           
         self.write(response)                
         self.finish()     

     def Foo(self, query, callback):
         callback({"queryFoo":query})        

     def Bar(self, query, callback):
         callback({"queryBar":query})     


class TornadoApplication(tornado.web.Application):

     def __init__(self):
         handlers = [
             (r"/dev/(.*)", acquiring.MainHandler),
         ]
         settings.update(session=session_settings)
         tornado.web.Application.__init__(self, handlers)


http_server = tornado.httpserver.HTTPServer(TornadoApplication())
http_server.listen(Config.get('WebServer','Port'))
tornado.ioloop.IOLoop.instance().start()  
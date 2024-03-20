class MainHandlerFoo(SessionBaseHandler):

     def __init__(self, *args, **kwargs):
         global logger
         super(MainHandler, self).__init__(*args, **kwargs)    

     @tornado.web.asynchronous
     @tornado.gen.coroutine
     def post(self,func_name):
         request = self.request.body
         response = yield tornado.gen.Task(self._Foo,request)           
         self.write(response)                
         self.finish()     

     def _Foo(self, query, callback):
        callback({"queryFoo":query})                

class MainHandlerBar(SessionBaseHandler):

     def __init__(self, *args, **kwargs):
         global logger
         super(MainHandler, self).__init__(*args, **kwargs)

     @tornado.web.asynchronous
     @tornado.gen.coroutine
     def post(self,func_name):
         request = self.request.body
         response = yield tornado.gen.Task(self._Bar,request)           
         self.write(response)                
         self.finish()     

     def _Bar(self, query, callback):
         callback({"queryBar":query})                

class TornadoApplication(tornado.web.Application):

     def __init__(self):
         handlers = [
             (r"/dev/Foo", acquiring.MainHandlerFoo),
             (r"/dev/Bar", acquiring.MainHandlerBar),
         ]
         settings.update(session=session_settings)
         tornado.web.Application.__init__(self, handlers)


http_server = tornado.httpserver.HTTPServer(TornadoApplication())
http_server.listen(Config.get('WebServer','Port'))
tornado.ioloop.IOLoop.instance().start()  
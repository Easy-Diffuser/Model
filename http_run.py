import _socket
import os
import http.server
import socketserver
import uuid
import run
import json

global model

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    
        
    def do_POST(self):
        content_len = int(self.headers.get('Content-Length'))
        post_body = self.rfile.read(content_len)
        
        image = post_body.decode('utf-8')
        
        model.run(image)
        
        reply = {
            'pos' : model.model.pos.split(),
            'neg' : model.model.neg.split()
        }
        
        reply_body = json.dumps(reply)

        self.send_response(201, 'Created')
        self.end_headers()
        self.wfile.write(reply_body.encode('utf-8'))

    def do_GET(self):
        self.send_response(404, 'Not Found')
        self.end_headers()
        self.wfile.write(b'')

if __name__ == '__main__':
    model=run.export_tag()
    
    print("Server Run")
    PORT = 5998
    
    server = http.server.HTTPServer(('', PORT), HTTPRequestHandler)
    
    server.serve_forever()
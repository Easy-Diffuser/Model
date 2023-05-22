import _socket
import os
import http.server
import socketserver
import uuid
import run
import json

global model

class HTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    
        
    def do_PUT(self):
        filename = os.path.basename(self.path)
        
        name, ext = os.path.splitext(filename)

        unique_filename = str(uuid.uuid4()) + ext

        file_length = int(self.headers['Content-Length'])
        read = 0
        with open(unique_filename, 'wb+') as output_file:
            while read < file_length:
                new_read = self.rfile.read(min(66556, file_length - read))
                read += len(new_read)
                output_file.write(new_read)

        # model run 추가 - 파일 이름 : unique_filename
        print(unique_filename)
        model.run(unique_filename)
        
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
    PORT = 5998
    model=run.export_tag()
    server = http.server.HTTPServer(('', PORT), HTTPRequestHandler)
    
    server.serve_forever()
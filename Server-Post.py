from http.server import BaseHTTPRequestHandler, HTTPServer
import cgi
import os

# Configura el directorio donde se guardarán los archivos subidos
UPLOAD_DIR = 'uploads'
if not os.path.exists(UPLOAD_DIR):
    os.makedirs(UPLOAD_DIR)

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'''
                <!doctype html>
                <html>
                <head>
                    <title>Subir Archivo</title>
                </head>
                <body>
                    <h1>Subir un archivo</h1>
                    <form action="/upload" method="post" enctype="multipart/form-data">
                        <input type="file" name="file">
                        <input type="submit" value="Subir">
                    </form>
                </body>
                </html>
            ''')
        else:
            self.send_error(404, "Página no encontrada")

    def do_POST(self):
        if self.path == '/upload':
            # Obtén el tipo de contenido del formulario
            content_type, _ = cgi.parse_header(self.headers['Content-Type'])
            if content_type == 'multipart/form-data':
                form = cgi.FieldStorage(fp=self.rfile, headers=self.headers,
                                        environ={'REQUEST_METHOD': 'POST',
                                                 'CONTENT_TYPE': self.headers['Content-Type']})
                # Obtén el archivo subido
                file_item = form['file']
                if file_item.filename:
                    # Guarda el archivo
                    file_path = os.path.join(UPLOAD_DIR, os.path.basename(file_item.filename))
                    with open(file_path, 'wb') as output_file:
                        output_file.write(file_item.file.read())
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(b'<html><body><h1>Archivo subido exitosamente!</h1></body></html>')
                else:
                    self.send_error(400, "No se ha subido ningún archivo")
            else:
                self.send_error(400, "Tipo de contenido no soportado")

# Configura y arranca el servidor
def run(server_class=HTTPServer, handler_class=RequestHandler, port=8888):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("="*70)
    print(" "*15 + "🚀 Servidor de Subida de Archivos 🚀")
    print("="*70)
    print("Este script inicia un servidor HTTP simple que permite subir archivos.")
    print(f'Servidor corriendo en http://localhost:{port}/')
    print("="*70)
    httpd.serve_forever()

if __name__ == "__main__":
    run()

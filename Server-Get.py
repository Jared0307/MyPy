from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import urllib.parse

class CustomHTTPRequestHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        """Sobrescribe el método para mostrar IP, código de estado y archivo solicitado."""
        client_ip = self.client_address[0]
        status_code = getattr(self, 'status_code', 200)  # Usar 200 por defecto
        requested_file = urllib.parse.unquote(self.path)  # Decodifica la URL

        # Imprime el log en el formato deseado
        print(f'{client_ip} - {status_code} - {requested_file}')

    def send_response(self, code):
        """Sobrescribe el método para capturar el código de estado antes de enviarlo."""
        self.status_code = code
        super().send_response(code)

def run(server_class=HTTPServer, handler_class=CustomHTTPRequestHandler, port=8080):
    # Cambia el directorio de trabajo si deseas servir archivos desde un directorio específico
    os.chdir('.')  # Esto sirve archivos desde el directorio actual, puedes cambiar el path aquí si lo deseas

    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("="*70)
    print(" "*20 + "🚀 Servidor HTTP en Ejecucion 🚀")
    print("="*70)
    print(f'Servidor corriendo en http://localhost:{port}/')
    print("="*70)
    httpd.serve_forever()

if __name__ == "__main__":
    run()

import http.server
import socketserver
import uuid

AUTH_TOKEN = str(uuid.uuid4())  # Zapisz to, bo musi być zsynchronizowane z frontendem

print("[INFO] Twój token logowania:")
print(AUTH_TOKEN)

# Lokalny serwer HTTP nasłuchujący na żądania POST
class AuthHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode("utf-8")
        if post_data.strip() == AUTH_TOKEN:
            print("[SUKCES] Zalogowano ✔")
        else:
            print("[BŁĄD] Nieprawidłowy token:", post_data)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

PORT = 8000
with socketserver.TCPServer(("", PORT), AuthHandler) as httpd:
    print(f"[INFO] Nasłuchiwanie na http://localhost:{PORT}")
    httpd.serve_forever()

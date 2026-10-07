import os
from functools import partial
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("PORT", "8080"))
Handler = partial(SimpleHTTPRequestHandler, directory=BASE_DIR)
server = ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
print(f"SkiFlow est lancé sur http://localhost:{PORT}")
server.serve_forever()

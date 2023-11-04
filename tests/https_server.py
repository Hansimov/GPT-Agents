"""
* Python HTTP(S) Server — Example · AnvilEight Blog
  * https://anvileight.com/blog/posts/simple-python-http-server/

* simple-https-server.py
  * https://gist.github.com/DannyHinshaw/a3ac5991d66a2fe6d97a569c6cdac534

Run this command in Git bash (because it is built-in with proper openssl):
  openssl req -new -x509 -keyout key.pem -out server.pem -days 365 -nodes

This following command takes too long. Do not recommend:
  openssl req -x509 -newkey rsa:2048 -keyout key.pem -out cert.pem -days 365

"""

import http.server
import ssl

server_address = ("0.0.0.0", 12346)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
ctx.load_cert_chain(certfile="server.pem", keyfile="key.pem")
httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
httpd.serve_forever()

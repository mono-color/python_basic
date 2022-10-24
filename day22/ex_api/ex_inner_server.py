# python 내장 서버
import http.server
import socketserver
#python 현재 위치한 디렉터리를 웹 루트로 두고 실행
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", 8080), Handler)
print('serving at port:', 8080)
httpd.serve_forever()
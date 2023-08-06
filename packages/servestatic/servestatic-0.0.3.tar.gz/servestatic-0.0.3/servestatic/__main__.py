from servestatic.server import Server

def run_server():
    server = Server()
    server.start_listener()

if __name__ == '__main__':
    run_server()
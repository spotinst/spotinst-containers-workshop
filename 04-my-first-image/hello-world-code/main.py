import os

import responder

api = responder.API()
name: str = os.getenv('MY_NAME')

@api.route("/")
def hello_world(req, resp):
    if name is None:
        resp.text = 'hello world!'
    else:
        resp.text = 'hello {}'.format(name)


def start_the_server():
        api.run()

def main():
    start_the_server()

if __name__ == "__main__":
    main()
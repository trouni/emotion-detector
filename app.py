import responder

api = responder.API()

@api.route("/")
def index(req, resp):
    resp.media = {'hello': 'world'}

if __name__ == '__main__':
    api.run()
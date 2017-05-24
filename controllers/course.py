
def index():
    print "got a request for a book", request.args

def serve():

    basecourse = request.args[0]
    chapter = request.args[1]
    rest = "/".join(request.args[2:])
    if ".css" in request.args[-1]:
        response.headers['Content-Type'] = 'text/css'
        with open("applications/runestone/views/course/thinkcspy/{}/{}".format(chapter, rest)) as f:
            return f.read()
    elif ".js" in request.args[-1]:
        response.headers['Content-Type'] = 'application/javascript'
        with open("applications/runestone/views/course/thinkcspy/{}/{}".format(chapter, rest)) as f:
            return f.read()

    response.view = 'course/thinkcspy/{}/{}'.format(chapter, rest)
    print "got a request for a book", request.args
    return dict(basecourse='thinkcspy')

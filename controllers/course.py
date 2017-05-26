
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
    return dict(basecourse=basecourse, course='', app='runestone')



# <script type="text/javascript">
#   eBookConfig = {};
#   eBookConfig.host = 'http://127.0.0.1:8000' ? 'http://127.0.0.1:8000' : 'http://127.0.0.1:8000';
#   eBookConfig.app = eBookConfig.host+'/runestone';
#   eBookConfig.ajaxURL = eBookConfig.app+'/ajax/';
#   eBookConfig.course = 'thinkcspy';
#   eBookConfig.logLevel = 10;
#   eBookConfig.loginRequired = false;
#   eBookConfig.build_info = "3.7.2";
#   eBookConfig.isLoggedIn = false;
#   eBookConfig.useRunestoneServices = true;
#   eBookConfig.python3 = true;
#   eBookConfig.basecourse = 'thinkcspy';
#   eBookConfig.runestone_version = '2.7.13';
# </script>

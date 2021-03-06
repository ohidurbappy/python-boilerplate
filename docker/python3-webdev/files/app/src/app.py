from wsgiref.simple_server import make_server


data = """<!DOCTYPE html>

<html>
<head>
    <title>Dockerized Web Application</title>

    <!-- This stylesheet is statically served by Nginx -->
    <link rel="stylesheet" href="/static/style.css">
</head>

<body>
    <h1>Congratulations!</h1>
    <p>Your docker container is working! Of course you must still configure it
    for your application. The best way to do it is to create a Dockerfile that
    is based on this image:

<code><pre>
# Dockerfile
FROM pythonboilerplate/django:base

# Tell docker the python path of your application
ENV GUNICORN_WSGI_APPLICATION=my_application.wsgi

# Assuming that your project files are under src/:
ADD . /app

</pre></code>
    </p>
    <p>Enjoy :)</p>

</body>
</html>
"""


def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/html; charset=utf-8')]
    start_response(status, headers)

    # That is actually an static content :-\
    return [x.encode('utf8') for x in data.splitlines(keepends=True)]

from cgi import parse_qs
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])

    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]

    if '' in [a,b]:
        a, b = [0, 0]
    else:
        a, b = [int(a), int(b)]
    
    response_body = html.format(valA = a, valB = b, valAdd = a+b, valMul=a*b)

    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])

    return [response_body]
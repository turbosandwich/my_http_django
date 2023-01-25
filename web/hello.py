def app(environ, start_response):
	#MIME-type - text/plain, it contains all GET params for each string
	start_response('200 OK', [('Content-Type', 'text/plain')])
	return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')), encoding="utf8")]

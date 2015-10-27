def add_cors_headers_response_callback(event):
	def cors_headers(request, response):
		response.headers.update({
		'Access-Control-Allow-Origin': 'http://localhost:8080',
		'Access-Control-Allow-Methods': 'POST, GET, DELETE, PUT, OPTIONS',
		'Access-Control-Allow-Headers': 'Origin, X-Requested-With, Content-Type, accept, authorization',
		'Content-Type': 'application/json; charset=UTF-8'})
	event.request.add_response_callback(cors_headers)

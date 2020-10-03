from views import frontend

def setup_routes(app):
#	app.add_route('GET','/',frontend.index)
	app.router.add_get('/',frontend.index)
	app.router.add_get('/kek',frontend.kek)
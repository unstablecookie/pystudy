from sqlalchemy import select
from aiohttp import web
from aiohttp_jinja2 import template
from sqlalchemy.sql import text
from aiohttpapp1 import kek1

@template('index.html')
async def index(request):
	site_name = request.app['config'].get('site_name')
	return {'site_name': site_name}
#	return web.Response(text='ok')

async def kek(request):
	async with request.app['db'].acquire() as conn:
		query = select([kek1])
#		query = text("Select * from kek;")
		result = await conn.fetch(query)
	return web.Response(body = str(result))
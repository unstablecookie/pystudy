from aiohttp import web
from routes import setup_routes
import argparse
from configs import load_config
import aiohttp_jinja2
import jinja2
import asyncpgsa


parser = argparse.ArgumentParser(description='App1')
parser.add_argument("-c", "--config",type=argparse.FileType('r'))
args = parser.parse_args()
config=load_config(args.config)


app = web.Application()
app['config'] = config
#setup templates
aiohttp_jinja2.setup(app,
loader = jinja2.PackageLoader('aiohttpapp1','templates') #create empty aiohttpapp1.py file for this shit
)
setup_routes(app)


async def on_start(app):
	confif = app['config']
	app['db'] = await asyncpgsa.create_pool(dsn=config['database_uri'],
		user='app1user',
		password='P@ssw0rd')


async def on_shutdown(app):
	await app['db'].close()




app.on_startup.append(on_start)
app.on_cleanup.append(on_shutdown)

if __name__ == '__main__':
	web.run_app(app , host='127.0.0.1',port=8080)
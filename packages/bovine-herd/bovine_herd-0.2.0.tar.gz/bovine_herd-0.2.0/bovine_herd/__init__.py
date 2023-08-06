import logging
import os

from bovine_pubsub import configure_bovine_pub_sub
from bovine_store.blueprint import bovine_store_blueprint
from bovine_store.config import configure_bovine_store
from quart import Quart, render_template, send_from_directory
from quart_redis import RedisHandler
from tortoise.contrib.quart import register_tortoise

from .config import TORTOISE_ORM, configure_bovine_herd
from .server import default_configuration
from .server.endpoints import endpoints

# from .version import __version__

logfile = os.environ.get("BOVINE_LOGFILE", "bovine.log")

log_format = "[%(asctime)s] %(levelname)-8s %(name)-12s %(message)s"
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    filename=(logfile),
)
domain = os.environ.get("DOMAIN", "my_domain")

app = Quart(__name__, template_folder="templates", static_folder="static")
app.config.update(
    {
        "REDIS_URI": "redis://localhost",
        "DOMAIN": domain,
    }
)


RedisHandler(app)


@app.before_serving
async def startup():
    await configure_bovine_herd(app)
    await configure_bovine_store(app)
    await configure_bovine_pub_sub(app)


@app.after_serving
async def shutdown():
    await app.config["session"].close()


app.register_blueprint(default_configuration)
app.register_blueprint(endpoints, url_prefix="/endpoints")
app.register_blueprint(bovine_store_blueprint, url_prefix="/objects")


@app.get("/")
async def index():
    return await render_template("index.html")


@app.get("/static/<path:path>")
async def static_file(path):
    return await send_from_directory("static", path)


register_tortoise(
    app,
    db_url=TORTOISE_ORM["connections"]["default"],
    modules={"models": TORTOISE_ORM["apps"]["models"]["models"]},
    generate_schemas=True,
)


def run():
    app.run()

import asyncio

from quart_redis import RedisHandler, get_redis


async def configure_bovine_pub_sub(app):
    app.config["REDIS_URI"] = "redis://localhost"

    RedisHandler(app)
    app.config["bovine_pub_sub"] = BovinePubSub()


class BovinePubSub:
    def __init__(self):
        self.health_pings = {}

    async def send(self, endpoint_path, data):
        redis = get_redis()
        await redis.publish(endpoint_path, data)

    async def event_stream(self, endpoint_path):
        self.health_pings[endpoint_path] = asyncio.create_task(
            self.health_ping(endpoint_path)
        )
        redis = get_redis()
        async with redis.pubsub() as pubsub:
            await pubsub.subscribe(endpoint_path)
            async for message in pubsub.listen():
                if message["type"] == "message":
                    msg = message["data"]
                    yield msg
                    yield "\n".encode("utf-8")

    async def health_ping(self, endpoint_path):
        while True:
            await asyncio.sleep(30)
            await self.send(endpoint_path, (":" + " " * 2048 + "\n").encode("utf-8"))

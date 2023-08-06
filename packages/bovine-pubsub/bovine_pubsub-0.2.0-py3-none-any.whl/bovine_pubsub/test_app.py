from examples.basic_app import app

from . import configure_bovine_pub_sub


# This test demonstrates the issue in
#     https://github.com/enchant97/quart-redis/issues/4
#
async def test_event_source():
    await configure_bovine_pub_sub(app)
    async with app.test_client() as client:
        response = await client.get("/")

        assert response

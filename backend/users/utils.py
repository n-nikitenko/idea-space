from config.utils.redis import redis_client


def add_to_blacklist(token):
    try:
        redis_client.set(token, "blacklisted", ex=3600)
        print(f"Token {token} added to blacklist")  # todo: add logs
    except ConnectionError:
        print("Failed to connect to Redis while adding token to blacklist")  # todo: add logs

from __future__ import annotations

from urllib.parse import quote
import aiohttp
import aioredis
import databases

from config import config

redisurl = "redis://:{password}@{host}/{db}".format(
      password=config.redis_pass,
      host=config.redis_host,
      db=config.redis_db
    )

redis: aioredis.Redis = aioredis.from_url(redisurl)

url = databases.DatabaseURL(
    "mysql+asyncmy://{username}:{password}@{host}:3306/{db}".format(
        username=config.sql_user,
        password=quote(config.sql_pass),
        host=config.sql_host,
        db=config.sql_db,
    ),
)
database: databases.Database = databases.Database(url)

http: aiohttp.ClientSession

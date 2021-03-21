from abc import ABC

import asyncpg

import settings as cfg


class ConfigurableDB(ABC):
    pool: asyncpg.pool.Pool

    @classmethod
    def configurate(cls, pool: asyncpg.pool.Pool):
        cls.pool = pool


class TopWords(ConfigurableDB):
    CREATE_TABLE = (
        "CREATE TABLE IF NOT EXISTS top_words "
        "( "
        "id SERIAL PRIMARY KEY, "
        "text VARCHAR(256),"
        "result_of INTEGER "
        "); "
    )
    CREATE_ROW = (
        "INSERT INTO top_words (text,result_of) "
        "VALUES ($1,$2)"
    )
    CLEAR_TABLE = (
        'TRUNCATE TABLE top_words RESTART IDENTITY;'
    )

    @classmethod
    async def create_table(cls):
        await cls.pool.execute(cls.CREATE_TABLE)

    @classmethod
    async def create(cls, text: str, result_of: int):
        await cls.pool.execute(cls.CREATE_ROW, text, result_of)

    @classmethod
    async def clear_table(cls):
        await cls.pool.execute(cls.CLEAR_TABLE)


async def preapare_db(*args, **kwargs):
    pool = await asyncpg.create_pool(user=cfg.APP_DB_USER, password=cfg.APP_DB_PASS,
                                     database=cfg.APP_DB_NAME, host=cfg.APP_DB_HOST)

    TopWords.configurate(pool)
    await TopWords.create_table()

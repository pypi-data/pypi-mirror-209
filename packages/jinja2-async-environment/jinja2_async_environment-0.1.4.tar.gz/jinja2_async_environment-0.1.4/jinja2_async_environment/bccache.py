import typing as t

from .environment import AsyncEnvironment
from jinja2 import BytecodeCache
from jinja2.bccache import Bucket
from redis.asyncio import Redis as AsyncRedis


class AsyncRedisBytecodeCache(AsyncRedis, BytecodeCache):
    def __init__(self, prefix: t.Optional[str] = None, **configs) -> None:
        super().__init__(**configs)
        self.prefix = prefix

    def get_bucket_name(self, key):
        return ":".join([self.prefix, key]) if self.prefix else key

    async def load_bytecode(self, key_bucket):
        code = await self.get(self.get_bucket_name(key_bucket.key))
        if code is not None:
            return key_bucket.bytecode_from_string(code)

    async def dump_bytecode(self, key_bucket) -> None:
        await self.set(
            self.get_bucket_name(key_bucket.key), key_bucket.bytecode_to_string()
        )

    async def get_bucket(
        self,
        environment: "AsyncEnvironment",
        name: str,
        filename: t.Optional[str],
        source: str,
    ) -> Bucket:
        key = self.get_cache_key(name, filename)
        checksum = self.get_source_checksum(source)
        bucket = Bucket(environment, key, checksum)
        await self.load_bytecode(bucket)
        return bucket

    async def set_bucket(self, bucket: Bucket) -> None:
        await self.dump_bytecode(bucket)

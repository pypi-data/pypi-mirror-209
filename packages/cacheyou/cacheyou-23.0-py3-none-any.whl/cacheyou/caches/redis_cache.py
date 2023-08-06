# SPDX-FileCopyrightText: 2015 Eric Larson, 2023 Frost Ming
#
# SPDX-License-Identifier: Apache-2.0


from datetime import datetime, timezone

from cacheyou.cache import BaseCache


class RedisCache(BaseCache):
    def __init__(self, conn):
        self.conn = conn

    def get(self, key):
        return self.conn.get(key)

    def set(self, key, value, expires=None):
        if not expires:
            self.conn.set(key, value)
        elif isinstance(expires, datetime):
            now_utc = datetime.now(timezone.utc)
            if expires.tzinfo is None:
                now_utc = now_utc.replace(tzinfo=None)
            expires = expires - now_utc
            self.conn.setex(key, int(expires.total_seconds()), value)
        else:
            self.conn.setex(key, expires, value)

    def delete(self, key):
        self.conn.delete(key)

    def clear(self):
        """Helper for clearing all the keys in a database. Use with
        caution!"""
        for key in self.conn.keys():
            self.conn.delete(key)

    def close(self):
        """Redis uses connection pooling, no need to close the connection."""
        pass

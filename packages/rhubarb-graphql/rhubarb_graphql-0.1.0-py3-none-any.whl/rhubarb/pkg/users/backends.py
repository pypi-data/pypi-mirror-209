import asyncio
import datetime
import random
import uuid

from psycopg import AsyncConnection
from rhubarb.config import config
from rhubarb.pkg.audit.models import log_event
from rhubarb.pkg.redis.rate_limit import rate_limit
from starlette.authentication import (
    AuthenticationBackend,
    AuthenticationError,
    AuthCredentials, UnauthenticatedUser,
)
from starlette.requests import HTTPConnection

from rhubarb import save, RhubarbException
from rhubarb.pkg.postgres.connection import connection
from rhubarb.pkg.users.models import get_user, U
from rhubarb.core import Unset


class SessionAuthBackend(AuthenticationBackend):
    async def authenticate(self, conn):
        if user_id := conn.session.get("user_id"):
            async with connection() as conn:
                if user := await get_user(conn, user_id):
                    return AuthCredentials(["authenticated"]), user
                raise AuthenticationError(f"User not found")


async def login(conn: AsyncConnection, user: U, request: HTTPConnection) -> U:
    if not isinstance(user.id, Unset) and user.id:
        request.session["user_id"] = user.id
    else:
        raise RhubarbException(f"Cannot login {user} because it doesn't have an id")
    await log_event(request=request, event_name="login")
    user.last_login = datetime.datetime.utcnow()
    return await save(conn, user).execute()


async def try_login_with_pw(conn: AsyncConnection, username: uuid.UUID, candidate_pw: str, request: HTTPConnection) -> U | None:
    # Sleep a random amount of time to avoid enumeration attacks.
    conf = config()
    await asyncio.sleep(random.randrange(25, 75) / 100.0)
    with rate_limit(key=f"login-{request.client.host}", max_times=conf.users.auth_rate_limit_max_attempts, ttl_seconds=conf.users.auth_rate_limit_timeout_seconds):
        if u := await get_user(conn, username=username):
            if u.password:
                if u.password.check(candidate_pw):
                    return await login(conn, u, request)
        return None


async def logout(request: HTTPConnection):
    if request.user.is_authenticated:
        del request.session["user_id"]
        if "impersonator_id" in request.session:
            del request.session["impersonator_id"]
        request.scope["auth"] = AuthCredentials()
        request.scope["user"] = UnauthenticatedUser()
        await log_event(request=request, event_name="logout")

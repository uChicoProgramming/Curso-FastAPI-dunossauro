from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from fastapi_zero.settings import Settings

settings = Settings()

# --- CORREÇÃO MAIS ROBUSTA PARA O FLY.IO ---
# Verifica se a URL já tem o driver asyncpg. Se não tiver, forçamos a troca.
# Tratamos tanto 'postgres://' quanto 'postgresql://'
if "postgresql+asyncpg" not in settings.DATABASE_URL:
    settings.DATABASE_URL = settings.DATABASE_URL.replace(
        "postgres://", "postgresql+asyncpg://"
    )
    settings.DATABASE_URL = settings.DATABASE_URL.replace(
        "postgresql://", "postgresql+asyncpg://"
    )
# -------------------------------------------

engine = create_async_engine(settings.DATABASE_URL)


async def get_session():  # pragma: no cover
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

from fastapi_zero.settings import Settings

settings = Settings()

if settings.DATABASE_URL.startswith('postgres://'):
    settings.DATABASE_URL = settings.DATABASE_URL.replace(
        'postgres://', 'postgresql+asyncpg://', 1
    )

engine = create_async_engine(settings.DATABASE_URL)


async def get_session():  # pragma: no cover
    async with AsyncSession(engine, expire_on_commit=False) as session:
        yield session

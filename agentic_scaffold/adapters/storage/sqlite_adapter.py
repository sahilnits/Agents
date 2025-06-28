import aiosqlite, asyncio

class SQLiteAdapter:
    DB_PATH = "agentic.db"

    async def save_event(self, event: str, payload: dict):
        async with aiosqlite.connect(self.DB_PATH) as db:
            await db.execute(
                "CREATE TABLE IF NOT EXISTS events (evt TEXT, payload TEXT)"
            )
            await db.execute(
                "INSERT INTO events(evt, payload) VALUES(?, ?)",
                (event, str(payload)),
            )
            await db.commit()
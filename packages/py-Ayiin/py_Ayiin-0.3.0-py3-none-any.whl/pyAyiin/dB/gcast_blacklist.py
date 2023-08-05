
from ._core import mongodb

gcastdb = mongodb.gcast


async def get_blgcast() -> list:
    bl_gcast = await gcastdb.find_one({"gcast": "gcast"})
    if not bl_gcast:
        return []
    return bl_gcast["bl_gcast"]


async def add_gcast(chat_id: int) -> bool:
    bl_gcast = await get_blgcast()
    bl_gcast.append(chat_id)
    await gcastdb.update_one(
        {"gcast": "gcast"}, {"$set": {"bl_gcast": bl_gcast}}, upsert=True
    )
    return True


async def remove_gcast(chat_id: int) -> bool:
    bl_gcast = await get_blgcast()
    bl_gcast.remove(chat_id)
    await gcastdb.update_one(
        {"gcast": "gcast"}, {"$set": {"bl_gcast": bl_gcast}}, upsert=True
    )
    return True


async def check_gcast(gcast_id):
    already_gcast = await gcastdb.find_one({"gcast": "gcast"})
    if already_gcast:
        gcast_list = [int(gcast_id) for gcast_id in already_gcast.get("gcast_id")]
        if int(gcast_id) in gcast_list:
            return True
        else:
            return False
    else:
        return False

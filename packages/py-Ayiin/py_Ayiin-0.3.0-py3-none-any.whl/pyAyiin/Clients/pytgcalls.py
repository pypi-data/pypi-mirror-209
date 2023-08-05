# py - Ayiin
# Copyright (C) 2022-2023 @AyiinXd
#
# This file is a part of < https://github.com/AyiinXd/pyAyiin >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/AyiinXd/pyAyiin/blob/main/LICENSE/>.
#
# FROM py-Ayiin <https://github.com/AyiinXd/pyAyiin>
# t.me/AyiinChat & t.me/AyiinSupport


# ========================×========================
#            Jangan Hapus Credit Ngentod
# ========================×========================


from fipper.raw.functions.channels import GetFullChannel
from fipper.raw.functions.messages import GetFullChat
from fipper.raw.functions.phone import CreateGroupCall, EditGroupCallTitle
from fipper.raw.types import InputPeerChannel, InputPeerChat

from ..methods.queue import Queues

from .client import *


try:
    from pytgcalls import StreamType
    from pytgcalls.types import Update
    from pytgcalls.types.input_stream import AudioVideoPiped
    from pytgcalls.types.stream import StreamAudioEnded
except ImportError:
    StreamType = None
    Update = None
    AudioVideoPiped = None
    StreamAudioEnded = None


class GroupCalls(Queues):
    def __init__(self):
        self.chat_id = []
        self.clients = {}
        self.active_calls = []
        self.msgid_cache = {}
        self.play_on = {}
    
    async def TitleVc(self, client, m, title: str):
        peer = await client.resolve_peer(m.chat.id)
        if isinstance(peer, InputPeerChannel):
            chat = await client.send(GetFullChannel(channel=peer))
        if isinstance(peer, InputPeerChat):
            chat = await client.send(GetFullChat(chat_id=peer.chat_id))
        return await client.send(
            EditGroupCallTitle(
                call=chat.full_chat.call,
                title=title,
            )
        )

    async def StartVc(self, client, m, title=None):
        peer = await client.resolve_peer(m.chat.id)
        await client.send(
            CreateGroupCall(
                peer=InputPeerChannel(
                    channel_id=peer.channel_id,
                    access_hash=peer.access_hash,
                ),
                random_id=client.rnd_id() // 9000000000,
            )
        )
        titt = title if title else "🎧 Ayiin Music 🎧"
        await self.TitleVc(client, m, title=titt)

    async def pause_stream(self, chat_id: int):
        await assistant.pause_stream(chat_id)

    async def resume_stream(self, chat_id: int):
        await assistant.resume_stream(chat_id)

    async def mute_stream(self, chat_id: int):
        await assistant.mute_stream(chat_id)

    async def unmute_stream(self, chat_id: int):
        await assistant.unmute_stream(chat_id)

    async def stop_stream(self, chat_id: int):
        try:
            self.clear_queue(chat_id)
            await assistant.leave_group_call(chat_id)
        except BaseException:
            pass


    async def stream_call(self, chat_id, link):
        await assistant.join_group_call(
            chat_id,
            AudioVideoPiped(link),
            stream_type=StreamType().pulse_stream,
        )


    async def decorators(self):
        @assistant.on_kicked()
        async def on_kicked(_, chat_id: int):
            if chat_id in self.queue:
                self.clear_queue(chat_id)
        
        @assistant.on_closed_voice_chat()
        async def closed_voice_chat(_, chat_id: int):
            if chat_id in self.queue:
                self.clear_queue(chat_id)
        
        @assistant.on_left()
        async def stream_services_handler(_, chat_id: int):
            self.clear_queue(chat_id)

        @assistant.on_stream_end()
        async def stream_end_handler1(client, update: Update):
            if not isinstance(update, StreamAudioEnded):
                return
            await self.skip_song(client, update.chat_id)

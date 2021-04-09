import asyncio
import json
import time
from .custom_encoder import CustomEncoder
from ..default.renderer.paidmessage import LiveChatPaidMessageRenderer
from ..default.renderer.paidsticker import LiveChatPaidStickerRenderer
from ..default.renderer.legacypaid import LiveChatLegacyPaidMessageRenderer
from ..default.processor import Chat
from ..default.processor import Chatdata
from ..default.processor import DefaultProcessor
from .. chat_processor import ChatProcessor
from ... import config

logger = config.logger(__name__)


class SuperChatLogProcessor(DefaultProcessor):
    def __init__(self):
        self.first = True
        self.abs_diff = 0
        self.renderers = {
            "liveChatPaidMessageRenderer": LiveChatPaidMessageRenderer(),
            "liveChatPaidStickerRenderer": LiveChatPaidStickerRenderer(),
            "liveChatLegacyPaidMessageRenderer": LiveChatLegacyPaidMessageRenderer(),
        }
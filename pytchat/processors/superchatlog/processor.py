import asyncio
import json
import time
from .custom_encoder import CustomEncoder
from ..default.renderer.paidmessage import LiveChatPaidMessageRenderer
from ..default.renderer.paidsticker import LiveChatPaidStickerRenderer
from ..default.renderer.legacypaid import LiveChatLegacyPaidMessageRenderer
from ..default.renderer.donation import LiveChatDonationAnnouncementRenderer
from ..default.renderer.placeholder import LiveChatPlaceholderItemRenderer
from ..default.renderer.membership import LiveChatMembershipItemRenderer
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
            "liveChatMembershipItemRenderer": LiveChatMembershipItemRenderer(),
            "liveChatPlaceholderItemRenderer": LiveChatPlaceholderItemRenderer()
        }
        
    def _parse(self, item):
        try:
            key = list(item.keys())[0]
            renderer = self.renderers.get(key)
            if renderer is None:
                return None
            renderer.setitem(item.get(key), Chat())
            renderer.settype()
            renderer.get_snippet()
            renderer.get_authordetails()
            rendered_chatobj = renderer.get_chatobj()
            renderer.clear()
        except (KeyError, TypeError) as e:
            logger.error(f"{str(type(e))}-{str(e)} item:{str(item)}")
            return None
        
        return rendered_chatobj


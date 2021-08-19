from .base import BaseRenderer


class LiveChatPlaceholderItemRenderer(BaseRenderer):
    def settype(self):
        self.chat.type = "placeholder"
    
    def get_authordetails(self):
        self.chat.author.badgeUrl = ""
        (self.chat.author.isVerified,
         self.chat.author.isChatOwner,
         self.chat.author.isChatSponsor,
         self.chat.author.isChatModerator) = (
            self.get_badges(self.item)
        )
        self.chat.author.channelId = None
        self.chat.author.channelUrl = None
        self.chat.author.name = None
        self.chat.author.imageUrl = None

    def get_message(self, item):
        message = None
        message_ex = []
        return message, message_ex

    def get_badges(self, renderer):
        self.chat.author.type = ''
        isVerified = False
        isChatOwner = False
        isChatSponsor = False
        isChatModerator = False
        return isVerified, isChatOwner, isChatSponsor, isChatModerator
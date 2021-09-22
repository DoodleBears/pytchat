from .base import BaseRenderer


class LiveChatMembershipItemRenderer(BaseRenderer):
    def settype(self):
        if "message" in self.item.keys():
            self.chat.type = "sponsorMessage"
        else:
            self.chat.type = "newSponsor"

    def get_authordetails(self):
        super().get_authordetails()
        self.chat.author.isChatSponsor = True

    def get_message(self, item):
        message = ''
        message_ex = []
        if "message" in item.keys():
            message, message_ex = super().get_message(item)
        else:
            try:
                message = ''.join([mes.get("text", "")
                               for mes in item["headerSubtext"]["runs"]])
                message_ex = [message]
            except KeyError:
                return "Welcome New Member!", ["Welcome New Member!"]
        return message, message_ex
    
    def get_snippet(self):
        super().get_snippet()
        self.chat.member_level = "None"
        member_stage_msgs = self.item.get("headerSubtext", {}).get("simpleText", None)
        if "message" in self.item.keys() and "headerPrimaryText" in self.item.keys():
            runs = self.item.get("headerPrimaryText", {}).get("runs", [])
            if len(runs) == 3:
                self.chat.amountString = runs[1]["text"]
                self.chat.amountValue = float(self.chat.amountString)
                time = runs[2]["text"].strip()
                self.chat.currency = "MEMB"
                if time in ["months","month"]:
                    self.chat.currency = "MON"
                if time in ["days","day"]:
                    self.chat.currency = "DAYS"
            if member_stage_msgs:
                self.chat.member_level = member_stage_msgs
        else:
            member_stage_msgs = self.item.get("headerSubtext", {}).get("runs", [])
            if len(member_stage_msgs) > 1:
                self.chat.member_level = member_stage_msgs[1].get("text")
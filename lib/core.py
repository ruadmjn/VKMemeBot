import random
import time
import vk
from config import config
from lib.groups import groups


class vkMemes():
    picList = []
    textList = []
    wasException = False

    @classmethod
    def GetMeme(self, category="amoral", excaptionFlag=False):
        if not self.wasException:
            self.wasException = excaptionFlag
        group = groups.groups[category][random.randint(0, len(groups.groups[category])-1)]
        session = vk.Session(config.vk_secret)
        vkapi = vk.API(session=session)
        try:
            if group["type"] == "photo":
                if len(self.picList) < 450:
                    for memePage in range(0, 5):
                        offset = memePage * 100
                        posts = vkapi.wall.get(owner_id=group["owner_id"], domain=group["domain"], filter="owner",
                                               version="5.64", count=100, offset=offset)
                        for post in posts:
                            if type(post) == type({}) and "attachment" in post:
                                if post["attachment"]["type"] == "photo" and post["likes"]["count"] > int(group["likes"]):
                                    if post["attachment"]["photo"]["src_big"] not in self.picList:
                                        self.picList.append(post["attachment"]["photo"]["src_big"])
                    return {"photo": self.picList[random.randint(0, len(self.picList)-1)]}
                return {"photo": self.picList[random.randint(0, len(self.picList) - 1)]}

            if group["type"] == "text":
                if len(self.textList) < 450:
                    for memePage in range(0, 5):
                        offset = memePage * 100
                        posts = vkapi.wall.get(owner_id=group["owner_id"], domain=group["domain"], filter="owner",
                                               version="5.64", count=100, offset=offset)
                        for post in posts:
                            if type(post) == type({}) and not "attachment" in post:
                                self.textList.append(post["text"])
                    return {"text": self.textList[random.randint(0, len(self.textList) - 1)]}
                return {"text": self.textList[random.randint(0, len(self.textList) - 1)]}
        except Exception as ex:
            self.wasException = True
            if group["type"] == "photo":
                if len(self.picList) == 0:
                    time.sleep(6)
                    self.GetMeme(category, True)
                else:
                    return {"photo": self.picList[random.randint(0, len(self.picList)-1)]}
            if group["type"] == "text":
                if len(self.textList) == 0:
                    time.sleep(6)
                    self.GetMeme(category, True)
                else:
                    return {"text": self.textList[random.randint(0, len(self.textList) - 1)]}
        finally:
            if self.wasException == False:
                if len(self.picList) >= 450:
                    self.picList = []
                if len(self.textList) >= 450:
                    self.textList = []
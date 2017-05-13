import random
import vk
from config import config
class vkMemes:
    picList = []

    @classmethod
    def GetMeme(self):
        session = vk.Session(config.vk_secret)
        vkapi = vk.API(session=session)
        for memePage in range(0, 2):
            offset = memePage * 100
            posts = vkapi.wall.get(owner_id="-45745333", domain="vk.com/4ch", filter="owner", version="5.64", count=100, offset=offset)
            for post in posts:
                if type(post) == type({}):
                    if post["attachment"]["type"] == "photo" and post["likes"]["count"] > 4000:
                        self.picList.append(post["attachment"]["photo"]["src_big"])
        return self.picList[random.randint(0, len(self.picList)-1)]
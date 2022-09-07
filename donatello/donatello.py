import requests


class Donatello:
    def __init__(self, token: str, apiUrls = None):
        self.token = {"X-Token": token}
        if apiUrls is None:
            self.apiUrls = {
                "me": "https://donatello.to/api/v1/me",
                "donates": "https://donatello.to/api/v1/donates",
                "clients": "https://donatello.to/api/v1/clients",
            }

    def me(self):
        target = requests.get(url=self.apiUrls["me"], headers=self.token)

        return target.json()

    def donates(self):
        target = requests.get(url=self.apiUrls["donates"], headers=self.token)

        return target.json()

    def clients(self):
        target = requests.get(url=self.apiUrls["clients"], headers=self.token).json()

        return target["clients"]

    # Quick access

    def get_total_donates(self):
        target = self.donates()

        return target["total"]

    def get_full_info(self):

        targets = [self.me(), self.donates(), self.clients()]

        inf = []

        for i in targets:
            inf.append(i)

        return inf

    def get_nickname(self):
        target = self.me()

        return target["nickname"]

    def get_donates(self):
        target = self.me()

        return target["donates"]

    def created_at(self):
        target = self.me()

        return target["createdAt"]

    def get_status(self):
        target = self.me()

        return {"IsActive": target["isActive"], "isPublic": target["isPublic"]}

    def get_page(self):
        target = self.me()

        return target["page"]



donate = Donatello(token="d509463259fd9c5b04f3e9ab0e727777")
print(donate.created_at())

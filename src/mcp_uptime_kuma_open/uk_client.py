from uptime_kuma_api import UptimeKumaApi


class KumaService:
    def __init__(
            self,
            url,
            username,
            password
    ):
        self.password=password,
        self.username=username,
        self.url=url,
        self._api = None

    def __enter__(self):
        self._api=UptimeKumaApi(self.url)
        self._api.login(self.username,self.password)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self._api:
            self._api.disconnect()



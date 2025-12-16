from uptime_kuma_api import UptimeKumaApi


class KumaService:
    def __init__(
            self,
            url,
            username,
            password
    ):
        self._password=password
        self._username=username
        self._url=url
        self.api = None

    def __enter__(self):
        try:
            self.api=UptimeKumaApi(url=self._url)
            self.api.login(
                username=self._username,
                password=self._password
            )
            return self.api

        except Exception as e:
            if self.api:
                self.api.disconnect()
            raise e

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.api:
            self.api.disconnect()
        return False



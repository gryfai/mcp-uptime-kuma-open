from os import getenv
from dotenv import load_dotenv
import services
from uk_client import KumaService

load_dotenv()

UPTIME_KUMA_URL=getenv("UPTIME_KUMA_URL", "http://localhost:3001")
UPTIME_KUMA_USERNAME=getenv("UPTIME_KUMA_USERNAME", None)
UPTIME_KUMA_PASSWORD=getenv("UPTIME_KUMA_PASSWORD", None)

serv = KumaService(UPTIME_KUMA_URL,UPTIME_KUMA_USERNAME,UPTIME_KUMA_PASSWORD)


def test():
    mon = services.get_monitors(serv)
    print(mon,"\n")


test()
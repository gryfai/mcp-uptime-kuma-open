from os import getenv
from dotenv import load_dotenv

load_dotenv()

UPTIME_KUMA_URL=getenv("UPTIME_KUMA_URL")
UPTIME_KUMA_USERNAME=getenv("UPTIME_KUMA_USERNAME")
UPTIME_KUMA_PASSWORD=getenv("UPTIME_KUMA_PASSWORD")


from fastapi import FastAPI
from agora_token_builder import RtcTokenBuilder
import time

app = FastAPI()

APP_ID = "72eeb2348bb3481da8fb082981baa6e4"
APP_CERTIFICATE = "YOUR_PRIMARY_CERTIFICATE"

@app.get("/")
def read_root():
    return {"status": "Agora Server is running"}

@app.get("/rtcToken")
def get_rtc_token(channelName: str, uid: int = 0, role: int = 1):
    expiration_time_in_seconds = 3600 * 24
    current_timestamp = int(time.time())
    privilege_expired_ts = current_timestamp + expiration_time_in_seconds

    token = RtcTokenBuilder.buildTokenWithUid(
        APP_ID, APP_CERTIFICATE, channelName, uid, role, privilege_expired_ts
    )
    return {"token": token}

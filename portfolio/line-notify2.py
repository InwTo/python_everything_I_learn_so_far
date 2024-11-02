#bd0NZz7QDS9euhy1KyHj98qUxNtMPG8piyHAr1TNtlO
#อย่าพึ่งฟุ่งซ่าน เอางี้1)ที่จำได้คือไม่ว่าอะไรมันจะมีbodyกับheaderคือเอาไว้ใส่ของต่างๆที่เราต้องการจะโชว์ headerคือตั้งค่าapiป่าววะ งงๆแต่เหมือนตั้งว่ามันจะส่งข้อมูลอะไรยังไงอะ
#2)แล้วพอเรา ตั้งค่าไรพวกนั้นเสร็จที่เหลือก็resp = post.api(body = body header = header tokenด้วย) นั้นคือconceptคร่าวๆที่เข้่าใจ
#3)แล้วdocumentทำไมอ่านแล้วมันงงๆวะ
import requests
api = "https://notify-api.line.me/api/notify"
token = "bd0NZz7QDS9euhy1KyHj98qUxNtMPG8piyHAr1TNtlO"
body  = {
    "message":"hello test testsdsdsd"
}



header= {
    "Authorization" : f"Bearer {token}",
    "Content-Type": "application/x-www-form-urlencoded"
}
resp = requests.post(api, headers=header,  data =body )
resp_json = resp.json()
print(resp_json)
#49a6896e-8a9f-41b5-b3a5-ca8199d934ea
#โอเคโจทย์คือให้เรารายงานสภาพอาการศฯผ่านไลน์ ก็ต้องไปลองอ่านdocดู
#http://api.airvisual.com/v2/city?city=Los Angeles&state=California&country=USA&key={{YOUR_API_KEY}}
#คือเราจะรับข้อมูลมาว่าอยู่ทึ่ไหน stateไหน city=Los Angeles&state=California&country=USA&key={{YOUR_API_KEY}} อ่าห่ะตรงนี้เราทำเป็นf string
#เราก็ดึงข้อมูลมาให้เป็นdicให้ได้ก่อน แล้วก็เอาข้อมูลเก็บไว้ในตัวแปร แล้วก็ใส่เหมือนline notifyเลย เขียนให้สวยๆ แล้วก็น่าจะประมาณนั้น
import requests
token_line = "bd0NZz7QDS9euhy1KyHj98qUxNtMPG8piyHAr1TNtlO"
api_line = "https://notify-api.line.me/api/notify"
token_air = "49a6896e-8a9f-41b5-b3a5-ca8199d934ea"
"""city = input("city:")
state = input("state:")
country = input("country:")"""
#air = requests.get(f"http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={token_air}")
air = requests.get(f"http://api.airvisual.com/v2/city?city=Surat Thani&state=Surat Thani&country=Thailand&key={token_air}")
air_dict = air.json()
pollution = (air_dict["data"]["current"]["pollution"])
weather = (air_dict["data"]["current"]["weather"])
print(pollution)
Time_stamp = pollution["ts"]
Aqi_us = pollution["aqius"]
Main_polution = pollution["mainus"]
Temperator = weather["tp"]
humidity  = weather["hu"]
wind_speed = weather ["ws"]
wind_direction = weather["wd"]

"""" },
    "current": {
      "pollution": {
        "ts": "2024-10-23T06:00:00.000Z",
        "aqius": 56,
        "mainus": "p2",
        "aqicn": 17,
        "maincn": "p2"
      },
      "": {
        "ts": "2024-10-23T06:00:00.000Z",
        "tp": 31,
        "pr": 1009,
        "hu": 63,
        "ws": 2.5,
        "wd": 86,
        "ic": "10d"
      }
    }
  }"""""
body = {
    "message":f"forecast information of Surat thani \n Time_stamp: {Time_stamp} \n Aqi us: {Aqi_us} \n Main polution: {Main_polution} \n Temperator: {Temperator}Celsius \n Humidity: {humidity}% \n Wind speed: {wind_speed}m/s \n Wind direction: {wind_direction}'"

}
header = {
    "Authorization": f"Bearer {token_line}"
}
resp  = requests.post(api_line , data = body , headers=header  )
line_resp = resp.json()
print(line_resp)
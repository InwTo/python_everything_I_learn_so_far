#Api คือลิงค์ข้อมูลที่มีองกรณ์ต่างๆสร้างมาให้มาฟรีๆในรูปjson
import requests#ก็ก่อนจะใช้APIก็ต้องเรียกใช้requestsก่อน requestsเป็นคำสั่งใช้import API เราลยต้องimportก่อน

resp = requests.get("https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all")#จากข้างบนคราวนี้เราใช้คำสั่งrequestsมาimport api เข้าตัวแปรให้ใช้ได้เป็นแบบนี้resp = requests.get("https://covid19.ddc.moph.go.th/api/Cases/today-cases-all")
print(resp.json())#แต่ถ้าเราเรียกใช้แค่print(resp)เราจะได้<Response [200]> อาวไมไม่เหมือนjsonแบบที่คุ้นเคยก็เราจะไม่เรียกใช้แบบjson เป็นแบบนี้print(resp.json())
data = resp.json()
print(data[0]["new_case"])
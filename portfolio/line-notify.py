#bd0NZz7QDS9euhy1KyHj98qUxNtMPG8piyHAr1TNtlO
import requests
token = "bd0NZz7QDS9euhy1KyHj98qUxNtMPG8piyHAr1TNtlO"
url = "https://notify-api.line.me/api/notify"

img_f = open("image\IMG_7645.JPG", "rb")
file = {
    "imageFile": img_f
}
body = {
    "message": "Hello Beam",
    "imageThumbnail":"https://www.istudiobyspvi.com/cdn/shop/files/iPhone_15_Pink_PDP_Image_Position-1__GBEN_e9c47876-bbad-489a-9260-e6c9864ed940.jpg?v=1718115290",
    "imageFullsize":"https://www.istudiobyspvi.com/cdn/shop/files/iPhone_15_Pink_PDP_Image_Position-1__GBEN_e9c47876-bbad-489a-9260-e6c9864ed940.jpg?v=1718115290",
    "stickerPackageId":"1070",
    "stickerId":"17841"
}

# config of requests 
headers = {
    #"Content-Type": "application/x-www-form-urlencoded",
    "Authorization": f"Bearer {token}"
}

resp = requests.post(url, data=body, headers=headers, files=file)
data = resp.json()
print(data)
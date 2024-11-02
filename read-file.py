file = open("resource/name.txt", "r") # mode => r: read, w: write, a: append #มันหน้าที่เปิดไฟล์นั้นๆแล้วก็ประเภทว่าเปิดเพื่ออ่าน/เขียน/เพิ่ม จากนั้นก็รับค่าเป็นตัวแปรไฟล์นั้นได้(เหมือนlink)ก็คือ file = open("resource/name.txt", "r")นั้นแหละ
#print(file.read()) # read all content
print(file)
for line in file:
    print(len(line))
    print(line)
file.close()


import easyocr
reader = easyocr.Reader(['ko'], gpu = True, recog_network='custom')
reader = easyocr.Reader(['ko','en'], gpu = True)
result = reader.readtext('./src/gray.jpg', detail = 0)
for i in result:
    print(i)

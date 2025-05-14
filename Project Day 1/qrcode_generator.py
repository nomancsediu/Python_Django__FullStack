import qrcode

def generate_qr_code(filepath):

    with open(filepath, "r") as file:
        lines = file.readlines()

    text = lines[0].strip()
    filename = lines[1].strip()

    #convert text or url to qrcode
    image_qrcode = qrcode.make(text)

    #save the qrcode image
    image_qrcode.save(filename)

generate_qr_code("input.txt")     

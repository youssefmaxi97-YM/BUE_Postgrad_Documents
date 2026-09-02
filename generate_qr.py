import qrcode

url = "https://graduation-landing-page-olive.vercel.app/"
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction for printing
    box_size=20,
    border=4,
)
qr.add_data(url)
qr.make(fit=True)

# BUE Dark Blue color for the QR Code
img = qr.make_image(fill_color="#003366", back_color="white") 
img.save("QR_Code_Production.png")
print("QR Code generated as QR_Code_Production.png")

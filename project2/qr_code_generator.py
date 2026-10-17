import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=5,
)
qr.add_data("https://www.linkedin.com/in/your-username/")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("linkedin_qr.png")
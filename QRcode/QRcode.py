import qrcode

portfolio_url = 'https://github.com/Sgilb-Portfolio'

# Create a QR code instance
qr = qrcode.QRCode(
    version=1,  # Controls the size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each box (pixel size)
    border=4  # Thickness of the border (in boxes)
)

# Adds the GitHub URL to the QR code
qr.add_data(portfolio_url)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill='black', back_color='white')

# Save the image to a file
img.save('github-portfolio-qr.png')

print('QR code generated and saved as github-portfolio-qr.png')

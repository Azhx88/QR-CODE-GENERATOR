import qrcode
from PIL import Image
def generate_qr_code(data, file_name, fill_color="black", back_color="white"):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    # Create an image from the QR code instance
    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    # Save the image
    img.save(file_name)
    return img
def main():
    # Input data from the user
    data = input("Enter the data to be encoded in the QR code: ")
    file_name = input("Enter the filename to save the QR code (e.g., 'qrcode.png'): ")
    fill_color = input("Enter the fill color for the QR code (default is 'black'): ") or "black"
    back_color = input("Enter the background color for the QR code (default is 'white'): ") or "white"
    # Generate QR code
    img = generate_qr_code(data, file_name, fill_color, back_color)
    img.show()
if __name__ == "__main__":
    main()
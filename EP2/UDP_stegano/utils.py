from stegano import lsb
import io
from PIL import Image

def steganogram_image(IN_IMG: str, msg: str) -> Image:
    """
    Puts a stegnogram in an image

    Args:
        IN_IMG (str): Path to initial image without secret
        msg (str): Desired secret message

    Returns:
        Image: Image with secret
    """
    # Hides the secret with stegano lib
    secret = lsb.hide(IN_IMG, msg)    
    return secret

def reveal_stagnogram(secret_image:Image) -> str:
    """
    Reveals an image stegnogram

    Args:
        secret_image (Image): Image with secret 

    Returns:
        str: Secret revealed
    """
    # Reveals the secret with stegano lib
    secret = lsb.reveal(secret_image)    
    return secret

def convert_to_byte_arr(image: Image, format: str) -> bytes:
    """Convert image to byte arrat

    Args:
        image (Image): Image to be transformed
        format (str): Image format

    Returns:
        bytes: Bytes array of image
    """
    b = io.BytesIO()
    image.save(b, format=format)
    return b.getvalue()

def send_byte_array(msg, s, SEG_SIZE, HOST, PORT):
    byte_arr = bytes(msg,"UTF-8")
    byte_arr = [byte_arr[i:i + SEG_SIZE] for i in range(0, len(byte_arr), SEG_SIZE)]
    for i in range(len(byte_arr)):
        s.sendto(byte_arr[i], (HOST,PORT))
        print("Segment sended", i)

def send_byte_array_img(img, s, SEG_SIZE, HOST, PORT):
    img =  [img[i:i + SEG_SIZE] for i in range(0, len(img), SEG_SIZE)]
    for i in range(len(img)):
        s.sendto(bytes(img[i]), (HOST,PORT))
        print(len(img))

def receive_byte_array(s, TOTAL_SIZE, SEG_SIZE):
    byte_arr = []
    data, addr = s.recvfrom(SEG_SIZE)
    byte_arr.append(data)
    print("Segment received from", addr, data)
    return byte_arr, addr

def receive_byte_array_img(s, TOTAL_SIZE, SEG_SIZE):
    byte_arr = []
    for i in range(680):
        data, addr = s.recvfrom(SEG_SIZE)
        byte_arr.append(data)
        print("Segment received from", addr)
    return byte_arr, addr
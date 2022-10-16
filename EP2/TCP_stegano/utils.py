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

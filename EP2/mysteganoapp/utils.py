from stegano import lsb
import io
import matplotlib.pyplot as plt
from PIL import Image

# 1.1
def steganogram_image(IN_IMG: str, OUT_IMG: str, msg: str, plot: bool) -> Image:
    """
    Puts a stegnogram in an image and reveals its secret

    Args:
        IN_IMG (str): Path to initial image without secret
        OUT_IMG (str): Path to save image with secret
        msg (str): Desired secret message
        plot (bool): True if user wants to plot the image with the revealed secret

    Returns:
        Image: Image with secret
    """
    # Hides the secret with stegano lib
    secret = lsb.hide(IN_IMG, msg)
    # Saves img with secret
    secret.save(OUT_IMG)

    if plot:
        image = plt.imread(OUT_IMG)
        clear_message = lsb.reveal(OUT_IMG)

        plt.imshow(image)
        plt.title("Revealed message:"+ clear_message)
        plt.show()
    
    return secret



def convert_to_byte_arr(image, format):
    b = io.BytesIO()
    image.save(b, format=format)
    return b.getvalue()

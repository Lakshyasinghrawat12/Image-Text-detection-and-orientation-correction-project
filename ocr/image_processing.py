from PIL import Image, ImageOps, ImageEnhance
import logging

def process_image(image_path, contract_factor):
    try:
        image= Image.open(image_path)

        #grayscaling image
        gray_image= ImageOps.grayscale(image)

        #enhancing the image
        enhancer= ImageEnhance.Contrast(gray_image)
        Image_enhanced= enhancer.enhance(contract_factor)


        #resize the image to make the test more readble
        Image_enhanced= Image_enhanced.resize((Image_enhanced.width*2, Image_enhanced.height*2), Image.LANCZOS)
        return Image_enhanced
    except Exception as e:
        logging.error(f'Error in processiong image {e}')
        raise
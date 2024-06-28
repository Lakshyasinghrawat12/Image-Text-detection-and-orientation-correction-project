import logging
import yaml
from ocr.image_processing import process_image
from ocr.tesseract_ocr import extract_rotation, detect_orientation, setup_tesseract


#Loading config file
with open('config/config.yaml', 'r') as f:
    config= yaml.safe_load(f)


#setup logging
logging.basicConfig(filename=config['log_file'], level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def main():
    try:
        logging.info("Starting OCR process")

        #setup tesseract command
        setup_tesseract(config['tesseract_cmd'])

        #process the image
        Image_enhanced= process_image(config['input_image_path'], config['contrast_factor'])
        Image_enhanced.save(config['output_image_path'])

        #Detect orientation
        osd= detect_orientation(Image_enhanced, config['dpi'])
        logging.info(f'OSD output: {osd}')


        #Extract rotation angle
        rotate_angle= extract_rotation(osd)
        logging.info(f'Rotate angle: {rotate_angle} degree')

        #Rotate the image if nessesary
        if rotate_angle!=0:
            rotated_image= Image_enhanced.rotate(-rotate_angle, expand=True)
            rotated_image.save(config['rotated_image_path'])
            logging.info("Rotated image saved")

        else:
            logging.info("NO rotation is needed")

        logging.info("OCR process completed successfully")
    except Exception as e:
        logging.error(f"Error in OCR process: {e}")

if __name__ == "__main__":
    main()
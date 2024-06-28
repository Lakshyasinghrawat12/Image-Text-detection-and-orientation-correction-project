import pytesseract
import logging


def setup_tesseract(tesseract_cmd):
    pytesseract.pytesseract.tesseract_cmd= tesseract_cmd

def detect_orientation(Image_enhanced, dpi):
    try:
        osd= pytesseract.image_to_osd(Image_enhanced, config=f'--dpi {dpi}')
        return osd
    except pytesseract.pytesseract.TesseractError as e:
        logging.error(f'TesseractError: {e}')
        raise
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        raise

def extract_rotation(osd_output):
    for line in osd_output.split('\n'):
        if 'Rotate' in line:
            return int(line.split(':')[-1].strip())
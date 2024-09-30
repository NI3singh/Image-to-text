import numpy as np
import easyocr
from transformers import AutoModel, AutoTokenizer
from PIL import Image
import warnings
from transformers import logging
import re

#To Surpaas warnings
warnings.filterwarnings("ignore", message="The attention mask and the pad token id were not set.")
warnings.filterwarnings("ignore", message="Setting `pad_token_id` to `eos_token_id`")
warnings.filterwarnings("ignore", message="The `seen_tokens` attribute is deprecated")

logging.set_verbosity_error()


tokenizer = AutoTokenizer.from_pretrained('srimanth-d/GOT_CPU', trust_remote_code=True)
model = AutoModel.from_pretrained('srimanth-d/GOT_CPU', trust_remote_code=True, low_cpu_mem_usage=True, use_safetensors=True, pad_token_id=tokenizer.eos_token_id)
model = model.eval()


easyocr_reader = easyocr.Reader(['hi'], gpu=False)  

# Function to perform OCR based on selected language
def perform_ocr(image, language):
    if language == "Hindi":
        image_np = np.array(image)  
        result = easyocr_reader.readtext(image_np, detail=0)
        return ' '.join(result)
    elif language == "English":
        image_path = 'temp_image.png'
        image.save(image_path)
        result = model.chat(tokenizer, image_path, ocr_type='ocr')
        return result
    else:
        return "Invalid language selection. Please choose Hindi or English."

def process_keyword(image, language, keyword):
    extracted_text = perform_ocr(image, language)  
    if keyword:
        keyword_regex = re.escape(keyword)
        highlighted_text = re.sub(
            f'({keyword_regex})', r'<mark style="background-color: yellow">\1</mark>', extracted_text, flags=re.IGNORECASE
        )
        
        if highlighted_text != extracted_text:
            return highlighted_text
        else:
            return f"No keyword '{keyword}' found in the text."
    else:
        return extracted_text

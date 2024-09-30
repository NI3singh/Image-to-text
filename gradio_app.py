import gradio as gr
from ocr_project import perform_ocr, process_keyword

def process_image(image, language, keyword):
    return process_keyword(image, language, keyword)

with gr.Blocks() as interface:
    gr.Markdown("## OCR Image Upload with Keyword Search")
    gr.Markdown("Upload an image, select the language, extract text, and search for keywords within the text.")

    language_dropdown = gr.Dropdown(choices=["Hindi", "English"], label="Select Language", value="English")

    image_input = gr.Image(type="pil", label="Upload Image")

    keyword_input = gr.Textbox(label="Enter keyword to search", placeholder="Type a keyword here")

    output_box = gr.HTML(label="Extracted Text", elem_id="output")

    submit_button = gr.Button("Submit")
    clear_button = gr.Button("Clear")

    submit_button.click(fn=process_image, inputs=[image_input, language_dropdown, keyword_input], outputs=output_box)

    clear_button.click(fn=lambda: None, inputs=[], outputs=[output_box])

if __name__ == "__main__":
    interface.launch(share=True)

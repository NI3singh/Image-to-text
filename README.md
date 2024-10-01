<h3><a href="">Image to text Using GOT OCR2.0 and easyocr</a></h3>

## Install
0. This project has been optimized to run on CPU, ensuring accessibility for environments without GPU support.
1. Create Environment
   ```bash
   conda create --name ocr_project python=3.10
   conda activate ocr_project
```
2. Clone this repository and navigate to the GOT folder
```bash
git clone https://github.com/NI3singh/Image-to-text.git
```
3. Install Package
```Shell
conda create -n got_ocr python=3.10 -y
conda activate got_ocr
pip install -r requirements.txt .
```
4. Run command
```Shell
cd environment folder
python gradio_app.py
now CTRL+Click on the http://127.0.0.1:7860
```
5. Using Application
```Shell
Select the language of the input Image either HINDI or ENGLISH.
Upload the Image.
Enter the Keyword.
Then Submit.
```
6. Deployment Process
```Shell
Prepare the application
Create Huggingface Account
Navigate to the Spaces page
Create a New Space
Select Gradio as the SDK
Upload Application Files
Specify Ports (if needed)
Build and Launch
Get the Public URL



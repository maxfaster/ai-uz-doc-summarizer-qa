
import gradio as gr
import pdfplumber
import easyocr
from PIL import Image
from docx import Document
from transformers import pipeline
from deep_translator import GoogleTranslator
import numpy as np

# OCR: O‘zbek va ingliz tillari uchun
ocr_reader = easyocr.Reader(['uz', 'en'], gpu=False)

# Tarjima funksiyalari
def uz_to_en(text):
    return GoogleTranslator(source='uz', target='en').translate(text)

def en_to_uz(text):
    return GoogleTranslator(source='en', target='uz').translate(text)

# Hugging Face summarizer va Q&A model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

# Fayldan olingan matnni saqlovchi global o‘zgaruvchi
stored_text = ""

def extract_text_from_file(file):
    global stored_text
    ext = file.name.split(".")[-1].lower()
    text = ""

    if ext == "pdf":
        with pdfplumber.open(file.name) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
                else:
                    img = page.to_image(resolution=300).original
                    pil_image = Image.frombytes("RGB", img.size, img.tobytes())
                    ocr_result = ocr_reader.readtext(np.array(pil_image), detail=0)
                    text += "\n".join(ocr_result)

    elif ext == "docx":
        doc = Document(file.name)
        text = "\n".join([p.text for p in doc.paragraphs])

    elif ext == "txt":
        text = file.read().decode("utf-8")

    else:
        text = "Noto‘g‘ri format. Faqat .pdf, .docx, .txt."

    stored_text = text
    return text

def summarize_file(file):
    text = extract_text_from_file(file)
    if not text.strip():
        return "Matn topilmadi."

    eng_text = uz_to_en(text[:1024])
    summary_en = summarizer(eng_text, max_length=130, min_length=30, do_sample=False)
    summary_uz = en_to_uz(summary_en[0]['summary_text'])
    return summary_uz

def answer_question(question):
    global stored_text
    if not stored_text.strip():
        return "Avval fayl yuklang."

    eng_context = uz_to_en(stored_text[:1024])
    eng_question = uz_to_en(question)
    result = qa_pipeline(question=eng_question, context=eng_context)
    answer_uz = en_to_uz(result['answer'])
    return answer_uz

# Gradio interfeys
with gr.Blocks() as demo:
    gr.Markdown("# 📄 AI Summarizer + Q&A with OCR (O'zbekcha + Deep Translator)")

    with gr.Row():
        file_input = gr.File(label="PDF, DOCX yoki TXT yuklang")
        summary_output = gr.Textbox(label="Qisqacha mazmun", lines=6)
    summarize_btn = gr.Button("🔍 Qisqacha mazmun chiqarish")
    summarize_btn.click(fn=summarize_file, inputs=file_input, outputs=summary_output)

    gr.Markdown("## ❓ Savol-javob (Fayl matni asosida)")
    question_input = gr.Textbox(label="Savolingiz")
    answer_output = gr.Textbox(label="Javob", lines=3)
    ask_btn = gr.Button("Javob berish")
    ask_btn.click(fn=answer_question, inputs=question_input, outputs=answer_output)

demo.launch()

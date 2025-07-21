
---

**1. GitHub repository nomi:**

```
ai-uz-doc-summarizer-qa
```

---

**2. Folder/fayl tuzilmasi:**

```
ai-uz-doc-summarizer-qa/
??? app.py                ? Gradio ilova kodi
??? requirements.txt      ? Kutubxonalar
??? README.md             ? GitHub tavsifi (quyida tayyor)
??? .gitignore            ? __pycache__, env, DS_Store, va boshqalar
```

---

**3. README.md — tayyor nusxa**

````markdown
AI Document Summarizer + Q&A (O‘zbekcha + OCR + Deep Translator)

Bu Gradio asosidagi web-ilova PDF, DOCX yoki TXT hujjatlarni yuklab:
- Matnni avtomatik ajratadi (hatto rasmli PDF bo‘lsa ham OCR orqali),
- Qisqacha mazmun chiqaradi (summarization),
- Matn asosida savollarga javob beradi (Q&A),
- Hammasini o‘zbek tilida bajaradi — tarjima funksiyasi orqali!

---

 Demo (Hugging Face Spaces)
 [Ishchi demo linkini bu yerga joylashtiring]

---

Texnologiyalar

| Texnologiya        | Maqsadi                          |
|--------------------|----------------------------------|
| Gradio             | Foydalanuvchi interfeysi         |
| EasyOCR            | Rasmli matndan matn ajratish     |
| pdfplumber         | PDF matn ajratish (text-based)   |
| python-docx        | DOCX fayl matni o‘qish           |
| deep-translator    | O‘zbek ? Ingliz tarjima          |
| HuggingFace Transformers | Summarizer + Q&A modellar |
| Torch              | LLM modellarni ishga tushirish   |

---

 Foydalanish

1. Reponi klonlang:

```bash
git clone https://github.com/yourusername/ai-uz-doc-summarizer-qa.git
cd ai-uz-doc-summarizer-qa
````

2. Virtual environment yarating (ixtiyoriy, lekin tavsiya qilinadi):

```bash
python -m venv venv
source venv/bin/activate  # yoki Windows: venv\\Scripts\\activate
```

3. Kutubxonalarni o‘rnating:

```bash
pip install -r requirements.txt
```

4. Ilovani ishga tushiring:

```bash
python app.py
```

---

 Ilova ko‘rinishi

* Fayl yuklash
* “Qisqacha mazmun chiqarish”
* “Savol-javob” bo‘limi

---

To‘liq imkoniyatlar

* ? PDF / DOCX / TXT qo‘llab-quvvatlash
* ? OCR (PDF rasmli bo‘lsa ham)
* ? O‘zbek tilida savol-javob va mazmun chiqarish
* ? Deep Translator orqali tarjima
* ? Hugging Face summarizer va Q\&A modellar

---

Litsenziya

MIT

---

Muallif

 Loyihani yaratdi: \[dradiomaxfaster (GitHub profilingiz)]
* Yordamchi: ChatGPT (OpenAI)

````

---

4. `.gitignore` (ixtiyoriy, lekin tavsiya qilinadi)

```gitignore
__pycache__/
*.pyc
*.pyo
*.pyd
.env
.venv
*.DS_Store
*.pdf
*.docx
*.txt
````

---

Tayyor bo‘ldi. Endi nima qilasiz:

1. GitHub’da yangi repo yarating: `ai-uz-doc-summarizer-qa`
2. Quyidagilarni joylashtiring:

   * `app.py`
   * `requirements.txt`
   * `README.md`
   * `.gitignore`
3. Keyin repo bilan `Hugging Face Space`ni ulang — avtomatik build qiladi.

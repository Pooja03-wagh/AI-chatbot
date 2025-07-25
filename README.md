# 🩺 Healthcare Assistant Chatbot

A simple AI-powered healthcare chatbot built using Hugging Face Transformers and Streamlit. It provides basic healthcare-related guidance and can generate general responses using a pretrained language model.

---

## 🚀 Features

- 💬 **Keyword Detection**: Recognizes keywords like "symptom", "appointment", and "medication" to offer specific suggestions.
- 🤖 **Text Generation**: Uses GPT-2 (via Hugging Face Transformers) to generate responses when no keywords are matched.
- 🖥️ **Web Interface**: User-friendly chatbot UI built with Streamlit.
- 📚 **Tokenization Support**: Downloads and uses NLTK's Punkt tokenizer.

---

## 🛠️ Technologies Used

- Python 3.10+
- [Transformers (Hugging Face)](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io/)
- [NLTK](https://www.nltk.org/)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Healthcare_Chatbot.git
cd Healthcare_Chatbot

### 2. Create and Activate a Virtual Environment
bash
Copy code
# Windows
python -m venv myenv
myenv\Scripts\activate

# macOS/Linux
python3 -m venv myenv
source myenv/bin/activate
3. Install the Dependencies
bash
Copy code
pip install -r requirements.txt
▶️ How to Run the Chatbot
bash
Copy code
streamlit run app.py
The chatbot will open in your browser at:
http://localhost:8501

📁 Project Structure
bash
Copy code
Healthcare_Chatbot/
│
├── app.py               # Streamlit app logic
├── requirements.txt     # List of required Python packages
├── .gitignore           # Prevents myenv/ and others from being pushed
└── README.md            # Project documentation

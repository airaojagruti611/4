import streamlit as st
from PIL import Image
import pyttsx3
import PyPDF2
from gtts import gTTS

play = pyttsx3.init()

def main():
    st.title("BookReader")
    image = Image.open('Audiobook.jpg')
    st.image(image, caption='Audiobook')
    data = st.file_uploader("Upload PDF File", type=['pdf'])
    if data is not None:
        pdf_reader = PyPDF2.PdfFileReader(data)
        pages = pdf_reader.numPages
        st.success("File uploaded successfully....")
        if st.button("Play PDF"):
            for num in range(0, pages):
                page = pdf_reader.getPage(num)
                text = page.extractText()

            tts = gTTS(text=text, lang='en')
            tts.save("speech.mp3")


if __name__=='__main__':
    main()

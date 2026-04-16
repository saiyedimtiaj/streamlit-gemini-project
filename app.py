import streamlit as st
from api_calling import note_generate,audio_transcription,quiz_generator
from PIL import Image


st.title("Note summary and Quiz Generator")
st.markdown("Upload upto 3 files to generate a summary and quiz questions based on the content.")
st.divider()

with st.sidebar:
    st.header("Controls")
    images = st.file_uploader(
        "Upload the photo of your notes",
        type=["jpg", "jpeg", "png", ],
        accept_multiple_files=True,
    )

    pil_images = []
    for img in images:
        pil_images.append(Image.open(img))

    if images:
        if len(images) > 3:
            st.error("Upload at maximum 3 files.")
        else:
            st.subheader("Uploaded images")
            col = st.columns(len(images))
            for i ,img in enumerate(images):
                with col[i]:
                    st.image(img)

    # difficulty
    selectedOption = st.selectbox(
        "Select the difficulty of your quiz",
        ("Easy","Medium","Hard"),
        index=None
    )


    pressed = st.button("Click the button to initiate AI",type="primary")

if pressed:
    if not images:
        st.error("You  must upload 1 image")
    if not selectedOption:
        st.error("You must select a difficulty")

    if images and selectedOption:
        # Note
        with st.container(border=True):
            st.subheader("📝 Your note")
            with st.spinner("Ai is writing notes for you : "):
                generatedNotes = note_generate(pil_images)
                st.markdown(generatedNotes)

        #Audio
        with st.container(border=True):
            st.subheader("♫ Your audio transcript")
            st.text("Note will be shown here")
            with st.spinner("Ai is generating your audio"):
                generatedNotes = generatedNotes.replace("#","")
                generatedNotes = generatedNotes.replace("*","")
                generatedNotes = generatedNotes.replace("-","")
                generatedNotes = generatedNotes.replace("`","")
                generatedNotes = generatedNotes.replace("'","")
                generatedAudio = audio_transcription(generatedNotes)
                st.audio(generatedAudio)

        #Quiz
        with st.container(border=True):
            st.subheader(f"📖 Your ({selectedOption}) difficulty")
            st.text("Note willbe shown here")

            with st.spinner("Ai is generating quize for you..."):
                quizes = quiz_generator(pil_images,selectedOption)
                st.markdown(quizes)


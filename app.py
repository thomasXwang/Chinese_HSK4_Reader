import streamlit as st
import requests



DATA_SOURCE_URL = "https://raw.githubusercontent.com/Thomas2512/Chinese_HSK4_Coursera/master/"
  

# Function which checks if URL points to an existing file
def exists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok


# Main Function for the Streamlit Web app
def main():

    st.header("Chinese HSK4 Learning Material")
    st.write("")

    week = st.slider(
        "Select Week",
        min_value=1,
        max_value=10,
        value=1
    )

    lesson = st.slider(
        "Select Lesson",
        min_value=1,
        max_value=5,
        value=1
    )

    WEEK_LESSON_URL = DATA_SOURCE_URL + f"Week{week}/Week{week}_Lesson{lesson}_"
    # st.write(WEEK_LESSON_URL)

    st.subheader("Vocabulary")

    VOCABULARY = 2

    for i in range(1, VOCABULARY+1):

        VOCAB_URL = WEEK_LESSON_URL + f"Voc{i}.png"
        # st.write(VOCAB_URL)
        # st.write(exists(VOCAB_URL))
        if exists(VOCAB_URL):
            st.write(f"{i})")
            st.image(VOCAB_URL,
                use_column_width=True
            )

    st.subheader("Reading")

    READING = 3

    for i in range(1, READING+1):

        READING_URL = WEEK_LESSON_URL + f"Reading{i}.png"
        # st.write(READING_URL)
        # st.write(exists(READING_URL))
        if exists(READING_URL):

            st.write(f"{i})")
            st.image(READING_URL,
                use_column_width=True
            )


    st.subheader("Listening")

    LISTENING = 2

    for i in range(1, LISTENING+1):

        LISTENING_AUDIO_URL = WEEK_LESSON_URL + f"Listening{i}.mp3"
        # st.write(LISTENING_AUDIO_URL)
        # st.write(exists(LISTENING_AUDIO_URL))
        if exists(LISTENING_AUDIO_URL):
            st.write(f"{i})")
            st.audio(LISTENING_AUDIO_URL)

        LISTENING_TEXT_URL = WEEK_LESSON_URL + f"Listening{i}.png"
        # st.write(LISTENING_TEXT_URL)
        # st.write(exists(LISTENING_TEXT_URL))
        if exists(LISTENING_TEXT_URL):
            st.image(LISTENING_TEXT_URL,
                use_column_width=True
            )

        st.write("")


    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")

    st.info("""\
        Source code: [GitHub](https://github.com/Thomas2512/Chinese_HSK4_Coursera) | [Thomas Wang](https://github.com/Thomas2512/)
    """)
    st.info("""\
        Course Material: [Coursera - Peking University](https://www.coursera.org/learn/hsk-4)
    """)

main()
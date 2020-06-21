import streamlit as st


DATA_SOURCE_URL = "https://raw.githubusercontent.com/Thomas2512/Chinese_HSK4_Coursera/master/"
  

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

    WEEK_LESSON_URL = DATA_SOURCE_URL + f"Week{week}_Lesson{lesson}_"
    # st.write(WEEK_LESSON_URL)

    st.subheader("Vocabulary")

    # vocabulary = st.slider(
    #     "Select Number of Vocabulary Images",
    #     min_value=1,
    #     max_value=2,
    #     value=1
    # )

    vocabulary = 2

    for i in range(1, vocabulary+1):
        VOCAB_URL = WEEK_LESSON_URL + f"Voc{i}.png"
        st.image(VOCAB_URL,
            use_column_width=True
        )

    st.subheader("Reading")

    # reading = st.slider(
    #     "Select Number of Reading Images",
    #     min_value=1,
    #     max_value=2,
    #     value=1
    # )

    reading = 3

    for i in range(1, reading+1):
        READING_URL = WEEK_LESSON_URL + f"Reading{i}.png"
        st.image(READING_URL,
            use_column_width=True
        )


    st.subheader("Listening")

    listening = 2

    for i in range(1, listening+1):

        LISTENING_URL = WEEK_LESSON_URL + f"Listening{i}.mp3"
        st.write(LISTENING_URL)
        st.audio(LISTENING_URL)


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
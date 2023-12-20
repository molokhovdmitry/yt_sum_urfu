from youtube_transcript_api import YouTubeTranscriptApi
from transformers import pipeline
import streamlit as st


@st.cache_resource
def load_summarizer():
    """
    Loads the summarization model pipeline.
    """

    raise NotImplementedError

@st.cache_resource
def load_translator():
    """
    Loads the translation model pipeline.
    """

    raise NotImplementedError

def get_transcript(video_id):
    """
    Loads the transcription of YouTube video.

    Args:
        video_id (string): YouTube video ID. Example: 'GecpgqEn4qQ'.

    Returns:
        string: Transcription of the video.
    """

    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_text = ' '.join([dictionary['text'] for dictionary in transcript])
    return transcript_text


@st.cache
def load_summarizer(text, model):
    summarizer = pipeline("summarization", model="Falconsai/text_summarization")
    return summarizer(text)
   

    summarized = model(text, max_length=130, min_length=30, do_sample=False)
    return summarized[0]['summary_text']


def translate_to_russian(text, model):
    """
    Translates text to russian with a model.

    Args:
        text (string): Input text.
        model (transformers.pipelines): Model pipeline.

    Returns:
        string: Russian translation of the text.
    """

    raise NotImplementedError

def summarize(video_id, summarizer, translator, translate=False):
    """
    Main function to summarize YouTube video by ID.

    Args:
        video_id (string): YouTube video ID. Example: 'GecpgqEn4qQ'.
        summarizer (transformers.pipelines): Summarization model pipeline.
        translator (transformers.pipelines): Translation model pipeline.
        translate (bool): Translate to russian or not.

    Returns:
        string: Summarized transcription of the video.
    """
    
    transcript = get_transcript(video_id)
    summarized = summarize_text(transcript, summarizer)
    if translate:
        summarized = translate_to_russian(summarized, translator)
    return summarized

# Load models
summarizer = load_summarizer()
translator = load_translator()

st.title('YouTube Суммаризатор')

# Video ID input and translation checkbox.
video_id = st.text_input('Введите ID YouTube видео, например "GecpgqEn4qQ"')
translate = st.checkbox('Перевести с английского')

result = st.button('Суммаризировать')

if result:
    try:
        summarized = summarize(video_id, summarizer, translator, translate=translate)
        st.write(summarized)
    except:
        st.write('Попробуйте другое видео')

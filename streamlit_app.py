import streamlit as st

from transformers import (
    AutoModelForSeq2SeqLM,
    AutoTokenizer,
    DataCollatorForSeq2Seq, 
    Seq2SeqTrainer,
    Seq2SeqTrainingArguments,
    pipeline
)

st.write("<h3 align='center'>Inshort News Summarization using Bidirectional and Auto-Regressive Transformers (BART)</h3>", unsafe_allow_html=True)

st.write("""
A web app which uses a fine-tuned BART model to generate concise and accurate summaries of news articles.
""")

st.image("images/repo-cover.jpg")

st.write("""
## About
<p align="justify">
    This project involves fine-tuning the BART (Bidirectional and Auto-Regressive Transformers) model for the task of generating abstractive summaries of news articles. The model is trained on the Inshorts news dataset, which consists of news articles from various categories such as sports, technology, entertainment, and more. You can try out the model by entering a news article in the input box below and clicking the 'Summarize' button. The model will generate a summary of the input article, which you can compare with the original article to see how well it captures the key points.
</p> 
""", unsafe_allow_html=True)         

def compare_summaries(input_text):
    # Load the original BART model and tokenizer
    bart_ckpt = "facebook/bart-base"
    bart_tokenizer = AutoTokenizer.from_pretrained(bart_ckpt)
    bart_model = AutoModelForSeq2SeqLM.from_pretrained(bart_ckpt).to("cuda" if torch.cuda.is_available() else "cpu")
    
    # Set up the original BART summarizer pipeline
    bart_summarizer = pipeline("summarization", model=bart_model, tokenizer=bart_tokenizer)
    
    # Load fine-tuned BART model from Hugging Face Hub
    finetuned_hub_model_id = "xgboost-lover/bart-base-finetuned-inshort-news"
    finetuned_summarizer = pipeline("summarization", model=finetuned_hub_model_id)
    
    # Generate summaries
    original_summary = bart_summarizer(input_text, max_length=50, min_length=25, do_sample=False)
    finetuned_summary = finetuned_summarizer(input_text, max_length=50, min_length=25, do_sample=False)
    
    return original_summary, finetuned_summary

input_text = st.text_area("Enter a news article to summarize:")

if st.button("Summarize"):
    if input_text:
        original_summary, finetuned_summary = compare_summaries(input_text)
        st.write("#### === Original BART Summary ===")
        st.write(original_summary[0]['summary_text'])
        st.write("#### === Fine-tuned BART Summary ===")
        st.write(finetuned_summary[0]['summary_text'])
    else:
        st.warning("Please enter a news article to summarize.")

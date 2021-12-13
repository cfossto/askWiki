from transformers import pipeline

class Summary:

    def summarize_wiki(self,text):
        summarizer = pipeline("summarization")
        print(summarizer(text[:120]))
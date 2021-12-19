from transformers import pipeline

class Summary:

    def summarize_wiki(self,text):
        summarizer = pipeline("summarization")
        print("Here is a short summary")
        print(summarizer(text[:120]))
from transformers import pipeline

class Comprehension:

    def ask_wiki(self,user_question,context):
        QA = pipeline("question-answering")
        uq = user_question.encode()

        result = QA(uq,context)
        print(result)

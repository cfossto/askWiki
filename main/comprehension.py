from transformers import pipeline

class Comprehension:

    def ask_wiki(self,user_question,context):
        QA = pipeline("question-answering")

        result = QA(user_question,context)
        print(result)




# Comprehension().ask_wiki("What did he write?","Arthur Schopenhauer died 22 February 1788 – 21 February 1787 . He was the son of a German philosopher and father of the philosopher . He wrote a book about the philosopher's work on the philosophy of the Enlightenment . He also wrote about the philosophy and philosophy of his work")
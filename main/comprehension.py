from transformers import pipeline


class Comprehension:

    def ask_wiki(self,user_question,context):
        QA = pipeline("question-answering")

        qa_input = { 'question':f'{user_question}',
                     'context':f'{context}'
                     }

        result = QA(qa_input)
        return result

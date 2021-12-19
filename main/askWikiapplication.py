from data_extr import WikiArticles
from summary import Summary
from comprehension import Comprehension


class Application:


    def run_app(self):

        state = True

        wiki = WikiArticles()
        summary = Summary()
        comprehension = Comprehension()

        while state:

            topic = input("Enter singular topic or person: ")
            print("Thank you. Processing...")

            topic_from_wiki = wiki.get_article(topic)
            summary_of_wiki = summary.summarize_wiki(topic_from_wiki)

            question = input("What do you want to know about the subject? ")

            answer = comprehension.ask_wiki(question,topic_from_wiki)
            true_score = int(answer["score"]*100)
            true_answer = answer["answer"]

            print("This is what I understand about the subject: \n")
            print(f"I am {true_score}% confident that the anwser is: {true_answer}")

            choice = input("\n Want to know more? Then write y for yes and n for no: ")

            if choice == "n":
                state = False
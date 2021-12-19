from bs4 import BeautifulSoup
import requests

class WikiArticles:

    '''
    This module extracts the most relevant data from
    Wikipedia-articles and presents it in a coherent list
    that is later passed on to the summarization-tool.

    This module uses:
        Beautiful Soup
    '''

    def get_article(self,subject_title):
        '''Takes in a title for a Wiki-pages and downloads it. Serves a list of the whole article.'''

        try:
            url = requests.get(f"https://en.wikipedia.org/wiki/{subject_title}")
            doc = BeautifulSoup(url.text,'html.parser')
            article_text = doc("p") # B-soup returns a p-tags as an array of p-tags
            formatted_article = [] # We need a new list to hold strings without p-tags

            # First For-loop is for extracting p-tags
            for p in article_text:
                formatted_article.append(p.get_text())

            # Formatted article to string
            article_as_string = "".join(formatted_article)
            #print(article_as_string)

            return article_as_string

        except:
            print("Can't find article, try again")


# g = WikiArticles().get_article("Arthur_Schopenhauer")
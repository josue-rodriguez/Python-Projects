import requests
import time
import webbrowser

while True:

    try:
        r = requests.get(r"https://en.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit=10&format=json")

        data = r.json()
        count = 0

        article_title = data['query']['random'][count]['title']

        text = 'Would you like to read about {}?\nY/N?\n'.format(article_title)
        answer = input(text)

        if answer[0].lower() == 'y':
            url_id = data['query']['random'][count]['id']
            url = 'http://en.wikipedia.org/wiki?curid={}'.format(url_id)

            webbrowser.open(url, new=2, autoraise=True)

        elif answer[0].lower() == 'n':
            while answer[0].lower() == 'n':
                count += 1
                article_title = data['query']['random'][count]['title']
                text = 'Would you like to read about {}?\nY/N?\n'.format(article_title)
                answer = input(text)

            url_id = data['query']['random'][count]['id']
            url = 'http://en.wikipedia.org/wiki?curid={}'.format(url_id)

            webbrowser.open(url, new=2, autoraise=True)

        else:
            print('The answer you entered is not valid. Please try again\n')
            answer = input(text)

            continue

        break

    except UnicodeEncodeError:
        """ BUILD AN EXCEPTION HANDLER"""
        continue

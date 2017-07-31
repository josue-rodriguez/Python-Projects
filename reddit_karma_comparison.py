
import requests
import time


class redditor(object):
    score = 0

    def __init__(self, name):
        self.name = name

    def getRecent(self):
        r = requests.get(r"https://www.reddit.com/user/{}/submitted/.json".format(self.name))
        data = r.json()

        title = data['data']['children'][0]['data']['title']
        self.score = int(data['data']['children'][0]['data']['ups'])

        print('Title: {}\n\nUpvotes: {}'.format(title, self.score))

one = input('Please enter a Reddit username: ')
two = input('\nPlease enter another Reddit username: ')

userone = redditor(one)
usertwo = redditor(two)

while True:
    try:
        userone.getRecent()
        time.sleep(3)
        break
    except KeyError:
        continue

while True:
    try:
        usertwo.getRecent()
        time.sleep(3)
        break
    except KeyError:
        continue


if userone.score > usertwo.score:
    print("\n{} got more upvotes".format(userone.name))
elif usertwo.score > userone.score:
    print("\n{} got more upvotes".format(usertwo.name))
else:
    print("\n{} and {} got the same amount of upvotes".format(userone.name, usertwo.name))

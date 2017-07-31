
import requests
import time


class redditor(object):
    score = 0

    def __init__(self, name):
        self.name = name

    def doIwork(self):
        print(self.name)

    def getRecent(self):
        print(r"https://www.reddit.com/user/{}/submitted/.json".format(self.name))
        time.sleep(3)
        r = requests.get(r"https://www.reddit.com/user/{}/submitted/.json".format(self.name))
        data = r.json()

        print(data.keys())

        title = data['data']['children'][0]['data']['title']
        self.score = data['data']['children'][0]['data']['ups']

        print('Title: {}\n\nUpvotes: {}'.format(title, self.score))

one = input('Please enter a Reddit username: ')
two = input('\nPlease enter another Reddit username: ')


while True:
    try:
        userone = redditor(one)
        userone.getRecent()
        break
    except KeyError:
        continue

while True:
    try:
        usertwo = redditor(two)
        usertwo.getRecent()
        break
    except KeyError:
        continue


if userone.score > usertwo.score:
    print("\n{} got more upvotes".format(userone.name))
elif usertwo.score > userone.score:
    print("\n{} got more upvotes".format(usertwo.name))
else:
    print("\n{} and {} got the same amount of upvotes".format(userone.name, usertwo.name))

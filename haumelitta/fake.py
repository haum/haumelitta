import logging


def get_logger():
    return logging.getLogger(__name__)


def txt2bool(t):
    resp = t == "y"
    print(resp)
    return resp


class FakeTeapot:
    """Fausse machine permettant de tester l'algorithme avec un terminal."""

    def __init__(self):
        self.START_TWEET_PAUSE = 1

    def stopHeating(self):
        pass

    def startHeating(self):
        pass

    def checkStartTweet(self):
        return txt2bool(input("Envoyer un tweet de départ ? (y/n) "))

    def checkStopTweet(self):
        return txt2bool(input("Envoyer un tweet de fin ? (y/n) "))

    def tweetStarting(self):
        pass

    def tweetProcessing(self):
        pass

    def tweetFail(self):
        pass

    def tweetDone(self):
        pass

    def waterIsPresent(self):
        return txt2bool(input("Eau présente ? (y/n) "))

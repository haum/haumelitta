import logging
import time

import coloredlogs

from fake import FakeTeapot
from logger import TeapotLogger

WATER_PRESENT_TIMEOUT = 120


def get_logger():
    return logging.getLogger(__name__)


# Machine à états

def fsm_off(m):
    """État de repos, attend un tweet pour démarer la FSM."""
    m.stopHeating()

    startTweet = False

    # Poll tweet de départ
    while not startTweet:
        startTweet = m.checkStartTweet()
        time.sleep(m.START_TWEET_PAUSE)

    # Lancement
    fsm_starting(m)


def fsm_starting(m):
    """État de départ, allume et attend l'arrivée de l'eau."""
    m.startHeating()
    m.tweetStarting()

    waited = 0

    while not m.waterIsPresent() and waited < WATER_PRESENT_TIMEOUT:
        time.sleep(1)
        waited += 1

    if waited > WATER_PRESENT_TIMEOUT:
        # L'eau chaude n'est pas arrivé en haut -> pas d'eau
        fsm_fail(m)
    else:
        # L'eau chaude est arrivé en haut
        fsm_processing(m)


def fsm_processing(m):
    """État intermédiaire, l'eau coule, attente fin du passage de l'eau."""
    m.tweetProcessing()
    stopTweet = False

    # Poll
    while m.waterIsPresent() and not stopTweet:
        stopTweet = m.checkStopTweet()
        time.sleep(60)

    # Fin
    fsm_done(m)


def fsm_done(m):
    """État de fin, le café a bien coulé, on notifie et éteind."""

    m.tweetDone()

    time.sleep(1)


def fsm_fail(m):
    """État d'erreur, on notifie et éteind."""

    m.tweetFail()

    time.sleep(1)

# Fin de la description des états, pour lancer la machine il faut lancer l'état
# initial en boucle


def run_fsm(m):
    get_logger().info("Démarrage de la FSM...")
    while True:
        fsm_off(m)

# Début du main

if __name__ == "__main__":
    coloredlogs.install(level='INFO')

    m = FakeTeapot()
    run_fsm(TeapotLogger(m))

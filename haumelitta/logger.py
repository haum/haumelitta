import logging

startLog = {
    'stopHeating': {
        'start': 'Arrêt de la cafetière…',
        'stop': 'Cafetière arrêtée.'
    },
    'startHeating': {
        'start': 'Démarrage de la cafetière…',
        'stop': 'Cafetière démarrée.'
    },

    'checkStartTweet': {
        'start': 'Vérification du tweet de départ…',
        'stop': 'Vérification terminée.'
    },
    'checkStopTweet': {
        'start': 'Vérification du tweet d’arrêt…',
        'stop': 'Vérification terminée.'
    },

    'tweetStarting': {
        'start': 'Envoi du tweet notifiant le départ',
        'stop': 'Envoi terminé.'
    },
    'tweetProcessing': {
        'start': 'Envoi du tweet d’attente…',
        'stop': 'Envoi terminé.'
    },
    'tweetFail': {
        'start': 'Envoi du tweet d’erreur…',
        'stop': 'Envoi terminé.'
    },
    'tweetDone': {
        'start': 'Envoi du tweet d’accomplissement…',
        'stop': 'Envoi terminé.'
    },

    'waterIsPresent': {
        'start': 'Vérication de la présence d’eau dans le conduit…',
        'stop': 'Vérification terminée'
    }

}


def get_logger():
    return logging.getLogger(__name__)


class TeapotLogger:
    def __init__(self, teapot):
        self.teapot = teapot

    def __getattr__(self, name):

        # Si c'est un attribut
        if not callable(getattr(self.teapot, name)):
            return getattr(self.teapot, name)

        # Si c'est une méthode, on l'emballe pour afficher des messages
        def f(*args, **kwargs):
            # On lit les messages pour la méthode
            msgs = None
            if name in startLog:
                msgs = startLog[name]

            # Affichage du message d'entrée
            if msgs is not None and 'start' in msgs:
                get_logger().info(msgs['start'])

            # Vrai appel à la méthode
            ret = getattr(self.teapot, name)(*args, **kwargs)

            # Affichage du message de sortie
            if msgs is not None and 'stop' in msgs:
                get_logger().info(msgs['stop'])

            # Retour de la méthode
            return ret

        return f

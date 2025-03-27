from queue import Queue


class MatchcommsClient:
    incoming_broadcast = Queue()
    outgoing_broadcast = Queue()

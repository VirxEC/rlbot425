from queue import Queue


class MatchcommsClient:
    incoming_broadcast: Queue[str | None] = Queue()
    outgoing_broadcast: Queue[str | None] = Queue()

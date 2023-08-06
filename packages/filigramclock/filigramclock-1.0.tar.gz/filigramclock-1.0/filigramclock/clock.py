from datetime import datetime


class Clock:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        if self.start_time is not None:
            raise ClockError("La minuterie a été démarrée plusieurs fois.")
        self.start_time = datetime.now()

    def end(self):
        if self.start_time is None:
            raise ClockError("La minuterie n'a pas encore été démarrée.")
        if self.end_time is not None:
            raise ClockError("La minuterie a déjà été arrêtée.")
        self.end_time = datetime.now()

    def result(self):
        if self.start_time is None or self.end_time is None:
            raise ClockError("La minuterie n'a pas encore été démarrée et arrêtée.")
        elapsed_time = self.end_time - self.start_time
        return f"Temps écoulé : {elapsed_time}"

    def reset(self):
        self.start_time = None
        self.end_time = None

    def error(self, e: str):
        raise ClockError(e)


class ClockError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
from datetime import datetime

class Transaction:
    def __init__(self, note, amount):
        self.timestamps= datetime.now()
        self.note= note
        self.amount= amount

    def __str__(self):
        formated_time= self.timestamps.strftime("%y-%m-%d %H:%M");

        return f"[{formated_time}]-{self.note}:{self.amount}"
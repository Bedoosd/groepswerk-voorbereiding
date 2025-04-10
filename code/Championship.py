class Championship:
    def __init__(self, winner, runner_up, start_date, end_date, location):
        self.winner = winner
        self.runner_up = runner_up
        self.start_date = start_date
        self.end_date = end_date
        self.location = location

    def get_data(self):
        pass

    def get_winner(self):
        return self.winner

    def get_runner_up(self):
        return self.runner_up

    def get_start_date(self):
        return self.start_date

    def get_end_date(self):
        return self.end_date

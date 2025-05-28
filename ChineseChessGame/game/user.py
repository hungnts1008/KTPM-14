class User:
    def __init__(self, name, elo, wins=0, losses=0):
        """
        Initialize a User object.

        :param name: The username of the player.
        :param elo: The Elo rating of the player.
        :param wins: The number of games the player has won (default is 0).
        :param losses: The number of games the player has lost (default is 0).
        """
        self.name = name
        self.elo = elo
        self.wins = wins
        self.losses = losses

    def update_elo(self, change):
        """
        Update the Elo rating of the player.

        :param change: The amount to change the Elo rating by (positive or negative).
        """
        self.elo += change

    def record_win(self):
        """
        Record a win for the player.
        """
        self.wins += 1

    def record_loss(self):
        """
        Record a loss for the player.
        """
        self.losses += 1

    def get_win_rate(self):
        """
        Calculate and return the win rate of the player.

        :return: The win rate as a percentage, or None if no games have been played.
        """
        total_games = self.wins + self.losses
        if total_games == 0:
            return None
        return (self.wins / total_games) * 100

    def __str__(self):
        """
        Return a string representation of the User object.
        """
        win_rate = self.get_win_rate()
        win_rate_str = f"{win_rate:.2f}%" if win_rate is not None else "N/A"
        return f"User: {self.name}, Elo: {self.elo}, Wins: {self.wins}, Losses: {self.losses}, Win Rate: {win_rate_str}"
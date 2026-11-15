# pylint: disable=missing-docstring
from auction import Auction
from utils import Cli
from itertools import count


class EnglishAuction(Auction):

    def __init__(self, cli=None):
        super().__init__(cli)
        self.auction_name="English"

    def auction_loop(self, opening_bid, bidders):
        # Collect bids
        standing_bid = opening_bid
        winner = None
        while True:
            accepted = self.bidding_round(bidders, standing_bid, live=True)
            if not accepted:
                break
            standing_bid,winner=accepted[-1]
        return winner, standing_bid
        

if __name__ == "__main__":
    EnglishAuction().play()






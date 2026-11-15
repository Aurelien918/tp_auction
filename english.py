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
        bid_bool=True
        while bid_bool:
            bid_bool=False
            for bidder in bidders:
                bid = self.cli.prompt(f"Standing bid is {standing_bid}. {bidder} bids:")
                if not bid:
                    continue
                bid = int(bid)
                if bid > standing_bid:
                    standing_bid = bid
                    winner = bidder
                    bid_bool=True
        return winner, standing_bid
        

if __name__ == "__main__":
    EnglishAuction().play()






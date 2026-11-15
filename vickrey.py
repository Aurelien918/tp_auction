from utils import Cli
from auction import Auction


class VickreyAuction(Auction):
    def __init__(self, cli=None):
        super().__init__(cli)
        self.auction_name="Vickrey"

    def auction_loop(self, opening_bid, bidders):
            bids = self.bidding_round(bidders, opening_bid)
            if not bids:
                 return None, opening_bid
            bids.sort(reverse=True)
            winner = bids[0][1]
            if len(bids)>1:
                price=bids[1][0]
            else:
                 price=opening_bid
            return winner, price

if __name__ == "__main__":
    VickreyAuction().play()

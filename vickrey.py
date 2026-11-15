from utils import Cli
from auction import Auction


class VickreyAuction(Auction):
    def __init__(self, cli=None):
        super().__init__(cli)
        self.auction_name="Vickrey"

    def auction_loop(self, opening_bid, bidders):
            bids=[]
            for bidder in bidders:
                 bid=self.cli.prompt(f"Opening bid is {opening_bid}. {bidder} bids:")
                 if not bid:
                      continue
                 bid=int(bid)
                 if bid>opening_bid:
                      bids.append((bid,bidder))
            if not bids:
                 return None, opening_bid
            bids.sort(reverse=True)
            winner=bids[0][1]
            if len(bids)==1:
                 price=opening_bid
            else:
                 price=bids[1][0]
            return winner, price

if __name__ == "__main__":
    VickreyAuction().play()

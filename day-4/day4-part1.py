text = open('cards.txt', 'r')
readLines = text.readlines()



class CheckWinner:
    
    def check_worth(self, list_of_cards: list[str])->int:
        total = 0
        for card in list_of_cards:
            winners, ours = self.check_card(card)
            winning_numbers = winners.intersection(ours)
            if '' in winning_numbers:
                winning_numbers.remove('')
            if ' ' in winning_numbers:
                winning_numbers.remove(' ')
            print(winning_numbers)

            if len(winning_numbers) > 0:
                total += pow(2,len(winning_numbers)-1)
        return total
    def check_card(self, card: str) -> list[set]:
        winners, ours = self.parse_card(card)
        winners = set(winners)
        ours = set(ours)
        
        return winners, ours
    def parse_card(self, card: str) -> list[int]:

        removed_colon = card.split(":")
        removed_bar = removed_colon[1].strip().split('|')
        winners = removed_bar[0].strip().split(" ")
        ours = removed_bar[1].strip().split(" ")
        return winners, ours

print(CheckWinner().check_worth(readLines))
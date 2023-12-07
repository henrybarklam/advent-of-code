text = open('cards.txt', 'r')
readLines = text.readlines()



class CheckWinner:

    def count_cards(self, list_of_cards: list[str]) -> int:
        map_of_number = {}
        count = 0
        for card_number in range(len(list_of_cards)):
            map_of_number[card_number] = 1

        for card in range(len(list_of_cards)):
            worth = self.check_worth(list_of_cards[card])
            for first_index in range(map_of_number[card]):
                count+=1
                for index in range(1,worth+1):
                    map_of_number[card + index] = map_of_number[card + index] + 1 

        return count
        


    
    def check_worth(self, card: str)->int:
        total = 0
        winners, ours = self.check_card(card)
        winning_numbers = winners.intersection(ours)
        if '' in winning_numbers:
            winning_numbers.remove('')
        if ' ' in winning_numbers:
            winning_numbers.remove(' ')

        if len(winning_numbers) > 0:
            total += len(winning_numbers)
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

print(CheckWinner().count_cards(readLines))
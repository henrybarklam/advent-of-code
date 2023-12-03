text = open('listp1.txt')
linesRead = text.readlines()

class Counter:

    def __init__(self):
        self.compare_dict = {'red':12, 'green': 13, 'blue':14}

    def isPossibleCounter(self, lines: list[str]) -> int:
        counter = 0
        game = 0
        for line in lines:
            game +=1
            if self.isPossible(line):
                counter+=game
        return counter
    

    def isPossible(self, line: str) -> bool:
        rounds = self.lineParser(line)
        gameValid = True
        for round in rounds:
            round_dict = self.roundParser(round)
            for key in round_dict:
                if self.compare_dict[key] < round_dict[key]:
                    gameValid = False
        return gameValid


    def lineParser(self, line: str) -> list[str]:
        colonSplit = line.split(':')
        semiColonSplit = colonSplit[1].split(";")
        return semiColonSplit
    
    def roundParser(self, round: str) -> dict:
        split_round = round.strip().split(",")
        color_number_dict = {}
        for pair in split_round:
            split_pair = pair.strip().split(" ")
            color_number_dict[split_pair[1]] = int(split_pair[0])
        return color_number_dict

print(Counter().isPossibleCounter(linesRead))

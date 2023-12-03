text = open('listp1.txt')
linesRead = text.readlines()

class Power:

    def minPossibleCounter(self, lines: list[str]) -> int:
        counter = 0
        for line in lines:
            counter+=self.howManyPossible(line)
        return counter
    

    def howManyPossible(self, line: str) -> int:
        rounds = self.lineParser(line)
        number = 1
        round_min_dict = {'red':0, 'green':0, 'blue':0}
        for round in rounds:
            round_dict = self.roundParser(round)
            for key in round_dict:
                if round_min_dict[key] < round_dict[key]:
                    round_min_dict[key] = round_dict[key]
        for key in round_min_dict:
            number *= round_min_dict[key]
        return number


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

print(Power().minPossibleCounter(linesRead))

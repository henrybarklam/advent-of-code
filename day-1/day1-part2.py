
toRead = open('listp2.txt', 'r')
linesRead = toRead.readlines()

class DecoderClass:

    def decode(self, lines: list[str]) -> int:
        count = 0
        for line in lines:
            count+= self.decoder(line=line)
        return count
    
    def decoder(self, line: str) -> int:

        list_of_numbers = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
        starter_letters = list("otfsen")
        ending_letters = list("eorxnt")
        found=False
        start, end, initial, final = 0, -1, 0, 0

        while start < len(line) and not found:
            if line[start].isnumeric():
                initial = int(line[start])
                found = True

            elif line[start] in starter_letters:
                checker = 3
                while not found and start+checker < len(line) and checker <= 5:
                    for number in list_of_numbers:
                        if number in line[start:start+checker]:
                            initial = list_of_numbers[number]
                            found= True
                    checker+=1
            start+=1
        found = False

        while abs(end) <= len(line) and not found:
            if(line[end].isnumeric()):
                final = int(line[end])
                found = True
            elif line[end] in ending_letters:
                checker = 2
                while not found and abs(end-checker) <= len(line) and checker <= 6:
                    for number in list_of_numbers:
                        if number in line[end-checker:]:
                            final = list_of_numbers[number]
                            found = True
                    checker+=1
            
            end-=1

        return initial*10+final
        
            
print(DecoderClass().decode(linesRead))

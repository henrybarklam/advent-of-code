
toRead = open('list.txt', 'r')
linesRead = toRead.readlines()

class DecoderClass:

    def decode(self, lines: list[str]) -> int:
        count = 0
        for line in lines:
            count+= self.decoder(line=line)
        return count

    def decoder(self, line: str) -> int:
        found=False
        start, end, initial, final = 0, -1, 0, 0

        while start < len(line) and not found:
            if line[start].isnumeric():
                initial = int(line[start])
                found = True
            else:
                start+=1
        found = False

        while abs(end) <= len(line) and not found:
            if(line[end].isnumeric()):
                final = int(line[end])
                found = True
            else:
                end-=1

        return initial*10+final
        
            
print(DecoderClass().decode(linesRead))



text = open('engine.txt','r')
readLines = text.readlines()

class EngineDecoder:

    def decode(self, lines: list[str]) -> int:
        
        grid = self.to_grid(lines)
        total_count = 0
        for row in range(len(grid)):
            for cell in range(len(grid[row])):
                if not grid[row][cell].isalnum() and not grid[row][cell] == '.':
                    is_part = False
                    is_part, grid, numbers_to_add = self.check_is_part(grid, cell, row)

                    if is_part:
                        total_count+= numbers_to_add[0] * numbers_to_add[1]
        return total_count

    def to_grid(self, lines: list[str]) -> list[list[str]]:
        grid = []
        for line in lines:
            row = list(line.rstrip())
            grid.append(row)
        return grid

    def get_entire_number_region(self, grid: list[list[str]], cell: int, row: int) -> list[int]:
        right_bound = len(grid[0])
        start = cell
        end = cell

        while start >= 0 and grid[row][start].isdigit():
            start-=1

        while end < right_bound and grid[row][end].isdigit():
            end += 1

        return [start+1, end]

    def check_is_part(self, grid: list[list[str]], x: int, y: int) -> bool:
        lower_bound, right_bound = len(grid), len(grid[0])
        is_part = False
        #Check this doesn't go out of bounds

        eight_directions = {
            "up": [x,y-1],
            "down": [x,y+1],
            "right": [x+1,y],
            "left": [x-1,y],
            "left_up": [x-1,y-1],
            "left_down": [x-1,y+1],
            "right_up": [x+1,y-1],
            "right_down": [x+1,y+1]
            }
        number_to_add = 0
        pair_of_numbers = []
        for direction in eight_directions:
            x_new, y_new = eight_directions[direction][0], eight_directions[direction][1]
            #Check not out of bounds
            if x_new >= 0 and x_new < right_bound and y_new >= 0 and y_new < lower_bound:
                if grid[y_new][x_new].isnumeric():
                    number_region = self.get_entire_number_region(grid=grid, cell=x_new, row=y_new,)
                    list_to_add = grid[y_new][number_region[0]:number_region[1]]
                    number_to_add = int(''.join(list_to_add))
                    pair_of_numbers.append(number_to_add)

                    for x in range(number_region[0],number_region[1]):
                        grid[y_new][x] = '.'


            #Somehow have to account for 3 parts? Might have to blank them out as going along

            if len(pair_of_numbers) == 2:
                is_part = True
        return is_part, grid, pair_of_numbers

print(EngineDecoder().decode(readLines))


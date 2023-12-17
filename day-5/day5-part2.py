text = open('seeds_map.txt','r')
readLines = text.readlines()


# Might be able to find ranges that can be searched through
class SeedLocator:

    def find_nearest(self, full_list: list[str]) -> int:
        seed_list = full_list[0].split(":")[1].strip().split(" ")
        parsed_list = self.parse_seed_map(full_list[2:])
        source_to_destination_list = []
        actual_seed_list = []

        map_of_ranges = {}

        for i in range(len(seed_list)):
            if i%2 == 0:
                map_of_ranges[seed_list[i]] = 0
            else:
                map_of_ranges[seed_list[i-1]] = int(seed_list[i])

                
        for seed in map_of_ranges:
            for range_index in range(map_of_ranges[seed]):
                actual_seed_list.append(int(seed)+range_index)


        for item in parsed_list.items():
            #Gets added as a tuple of key, value
            source_to_destination_list.append(item)
        list_of_locations = []

        for seed in actual_seed_list:
            current_check = int(seed)

            for specific_source_to_destination in source_to_destination_list:
                changed = False
                #Values in tuple
                for value in specific_source_to_destination[1]:
                        triplet = value.strip().split(" ")
                        destination = int(triplet[0])
                        source_start = int(triplet[1])
                        source_end = source_start + int(triplet[2])
                        if changed == False and current_check >= source_start and current_check <= source_end:
                            current_check = destination + (current_check - source_start)
                            changed = True
            list_of_locations.append(current_check)
        return min(list_of_locations)
    

    #Just hold ranges in here
    def source_to_destination_mapper(self, parsed_list_key: list) -> map:
        map_to_return = {}
        for list_key in parsed_list_key:
            destination, source, total = list_key.split(" ")

            new_key = source + "+" + str(int(source)+int(total))
            #Need to change this to just check a value is in a range
            for index in range(total):

                map_to_return[source+index] = destination+index
        return map_to_return

        
    def parse_seed_map(self, full_list: list[str]) -> map:
        map_of_titles = {
            "seed-to-soil map:": [],
            "soil-to-fertilizer map:": [], 
            "fertilizer-to-water map:": [], 
            "water-to-light map:": [],
            "light-to-temperature map:": [],
            "temperature-to-humidity map:": [],
            "humidity-to-location map:": []
        }

        current = "seed-to-soil map:"
        for line in full_list[2:]:
            line = line.strip()
            if line != "":
                if line in map_of_titles:
                    current = line
                else:
                    map_of_titles[current].append(line)
        return map_of_titles


print(SeedLocator().find_nearest(readLines))
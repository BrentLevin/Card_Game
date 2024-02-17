def import_deck():
    formatted_deck_list = {}
    num = ["0","1","2","3","4","5","6","7","8","9"]

    with open("MTG\\deck.txt") as f:
        lines = list(map(str.strip, f.readlines()))

    for line in lines:
        num_of_cards = 0
        i = 0
        while i < len(line) and line[i] in num:
            num_of_cards *= 10
            num_of_cards += int(line[i])
            i += 1
        
        if num_of_cards != 0:
            formatted_deck_list[line[i:]] = num_of_cards

        return formatted_deck_list




        
            
### maybe theres a way to read in other deck formats automatically figuring out which is which
### also how to read in multiple decks at once and indetify whose is whose
def minion_game(string):
    board = {'Stuart':0, 'Kevin': 0}
    Stuart_word, Kevin_word = {}, {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    string = string.lower()
    for index, char in enumerate(string):
        sliced = string[index:]
        start = 0
        if char in vowels:
            for x,c in enumerate(sliced):
                if sliced[start:len(sliced) - x] in Kevin_word:
                    Kevin_word[sliced[start:len(sliced) - x]] += 1
                else:
                    Kevin_word[sliced[start:len(sliced) - x]] = 1
        else:
            for x,c in enumerate(sliced):
                if sliced[start:len(sliced) - x] in Stuart_word:
                    Stuart_word[sliced[start:len(sliced) - x]] += 1
                else:
                    Stuart_word[sliced[start:len(sliced) - x]] = 1

    stuart_result = sum(Stuart_word.values())
    kevin_result = sum(Kevin_word.values())

    if (stuart_result > kevin_result):
        print("Stuart", stuart_result)
    elif (kevin_result > stuart_result):
        print("Kevin", kevin_result)
    else:
        print("Draw")

minion_game(input().lower())

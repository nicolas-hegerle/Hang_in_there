def draw_mistakes(tries = None):
    if tries == 10:
        print('\
             |========      \n\
             | /     |      \n\
             |/      O      \n\
             |      -|-     \n\
             |      / \     \n\
             |     -----    \n\
             |      | |     \n\
        ================    \n\
       WELCOME TO HANGMAN     \
        ')


    if tries == 9:
        print('\
        ================    \n\
          FIRST MISTAKE     \
        ')

    elif tries == 8:
        print('\
             |              \n\
             |              \n\
             |              \n\
             |              \n\
             |     -----    \n\
             |      | |     \n\
        ================    \n\
         SECOND MISTAKE     \
        ')

    elif tries == 7:
        print('\
             |========      \n\
             |              \n\
             |              \n\
             |              \n\
             |              \n\
             |     -----    \n\
             |      | |     \n\
        ================    \n\
          THIRD MISTAKE     \
        ')

    elif tries == 6:
        print('\
             |========      \n\
             | /            \n\
             |/             \n\
             |              \n\
             |              \n\
             |     -----    \n\
             |      | |     \n\
        ================    \n\
         FOURTH MISTAKE     \
        ')

    elif tries == 5:
        print('\
             |========      \n\
             | /     |      \n\
             |/             \n\
             |              \n\
             |              \n\
             |     -----    \n\
             |      | |     \n\
        ================    \n\
          FIFTH MISTAKE     \
        ')

    elif tries == 4:
        print('\
             |========      \n\
             | /     |      \n\
             |/      O      \n\
             |              \n\
             |              \n\
             |     -----    \n\
             |      | |     \n\
        ================    \n\
          SIXTH MISTAKE     \
        ')

    elif tries == 3:
        print('\
             |========      \n\
             | /     |      \n\
             |/      O      \n\
             |       |      \n\
             |              \n\
             |     -----    \n\
             |      | |     \n\
        ================    \n\
        SEVENTH MISTAKE     \
        ')

    elif tries == 2:
        print('\
             |========      \n\
             | /     |      \n\
             |/      O      \n\
             |       |      \n\
             |      / \     \n\
             |     -----    \n\
             |      | |     \n\
        ================    \n\
          EIGTH MISTAKE     \
        ')

    elif tries == 1:
        print('\
             |========      \n\
             | /     |      \n\
             |/      O      \n\
             |      -|-     \n\
             |      / \     \n\
             |     -----    \n\
             |      | |     \n\
        ================    \n\
          NINTH MISTAKE     \
        ')

    elif tries == 0:
        print("\
             |========      \n\
             | /     |      \n\
             |/      |      \n\
             |       @      \n\
             |      /|\     \n\
             |      / \     \n\
             |              \n\
        ================    \n\
         SORRY YOU LOST     \
        ")

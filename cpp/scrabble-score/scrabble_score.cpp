#include "scrabble_score.h"

#include<locale>
#include<map>

namespace scrabble_score {
    static std::map<char, unsigned> letter_values = {
        {'a', 1},
        {'e', 1},
        {'i', 1},
        {'o', 1},
        {'u', 1},
        {'l', 1},
        {'n', 1},
        {'r', 1},
        {'s', 1},
        {'t', 1},
        {'d', 2},
        {'g', 2},
        {'b', 3},
        {'c', 3},
        {'m', 3},
        {'p', 3},
        {'f', 4},
        {'h', 4},
        {'v', 4},
        {'w', 4},
        {'y', 4},
        {'k', 5},
        {'j', 8},
        {'x', 8},
        {'q', 10},
        {'z', 10}
    };

    unsigned score(std::string word) {
        unsigned the_score = 0;
        for(std::string::iterator letter=word.begin(); letter != word.end(); ++letter)
        {
            the_score += letter_values[std::tolower(*letter, std::locale())];
        }
        return the_score;
    }
}  // namespace scrabble_score

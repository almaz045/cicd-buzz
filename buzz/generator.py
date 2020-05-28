# -*- coding: utf-8 -*-
import random
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



buzz = ('Саламалейкум', 'Уалейкум')
adjectives = ('Крутой', 'Дикий')
adverbs = (' Ровно', 'Сильно')
verbs = ('Бьет', 'Идет', 'Дышит')


def sample(l, n = 1):
    result = random.sample(l, n)
    if n == 1:
        return result[0]
    return result

def generate_buzz():
    buzz_terms = sample(buzz, 2)
    phrase = ' '.join([sample(adjectives), buzz_terms[0], sample(adverbs),
        sample(verbs), buzz_terms[1]])
    return phrase.title()

if __name__ == "__main__":
    print (generate_buzz())

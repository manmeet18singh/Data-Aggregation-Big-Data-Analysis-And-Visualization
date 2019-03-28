from nytimesarticle import articleAPI
import jsonpickle

api = articleAPI('aruVhl4pt0AUEOnD9LR7V1s4p7wavw9H')

# collect articles with March Madness Keyword
mmArt = api.search(q = 'March Madness',
                    fq = 'The New York Times')

# collect articles with keywords Sport or Sports
# sportArt = api.search(q = ['Sport', 'Sports'], 
                        # fq = {'headline' : ['Sport', 'Sports'], 'body':['Sport', 'Sports']}, 
                        # begin_date = 20190101)

# Save collections as JSON file


print(mmArt['response']['docs'])
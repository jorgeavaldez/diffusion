# ![diffusion](assets/logo.png)
diffusion is the translation diff engine backend for BaoBao. It's split into two
main parts, the text extraction and parse tokenizer, and the translation diffing
engine. It uses the Readability API for web links, and the Parse library.

## pro strats
Right now, the feedme library has a class, Feedr, that can take in a web
article, will run it through the Readability API, and then will clean and return
the body text of the article.

### next Steps
- Run a tokenizer on the data
    - Determine parts of speech
    - Group into similar sentence constructs
- Run through translation engines
    - Bing Google Yahoo etc
    - Diff the results and find frequency of words to parts of speech in
      sentence structures
    - Determine "correctness" of a translation of a fragment, and mark as "most
      correct" and continue
    - Concurrency is key
 
## libraries
### feedme
feedme is the input feed library. This is what pulls web articles, and will be
extended to cleanse txt files and other forms of text for input.

### llama
llama is what runs the translations and tokenizes the text. It takes care of the
nlp of our input text and runs the translations on the text.

## links and misc.
- [stackoverflow thread](http://stackoverflow.com/questions/399200/calculating-the-semantic-distance-between-words)
  on sentence similarity

- [textbook](http://www.amazon.com/dp/0131873210/?tag=stackoverfl08-20) on nlp

- [wikipedia page](https://en.wikipedia.org/wiki/Levenshtein_distance) on
  levenshtein distance

- [beautiful soup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/#)
  documentation

- [the clips pattern library](http://www.clips.ua.ac.be/pattern)

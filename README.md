![diffusion](assets/logo.png)
# diffusion
Diffusion is the translation diff engine backend for BaoBao. It's split into two
main parts, the text extraction and parse tokenizer, and the translation diffing
engine. It uses the Readability API for web links, and the Parse library.

## pro strats
Current strategy is as follows:
- Dissect the [Krill package](https://github.com/p-e-w/krill.git) to find how
  they pull RSS and Twitter body data and links.
- Run the links through Readability if they haven't been stripped of external
  nastiness and cruft
    - Try to replicate a custom version of a content parser so as to remove the
      reliance on an external API for this.
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
 
## feedme
feedme is the feed library. This is what's gonna pull from an rss feed, a url, a
twitter link, a txt file etc., tokenize, and then feed to the translation
engine. This'll also include the diffing engine later on.

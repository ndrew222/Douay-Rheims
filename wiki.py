#!/usr/bin/env python3
from wikitrans.wiki2html import HtmlWikiMarkup
from wikitrans.wiki2text import TextWikiMarkup

markup = HtmlWikiMarkup(filename='334.wiki')
markup.html_base = ''
markup.parse()
#print(str(markup))
text = TextWikiMarkup(filename='334.wiki')
text.parse()
print(str(text))

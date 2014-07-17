baka-mecab
==========

Simple wrapper for mecab cli tool. No additional dependencies required (only
mecab itself).

## Example usage:

```Python

from bakamecab.cli import Parser as MeCab

parser = MeCab(u'任意のディレクトリ内で')

for word, info in parser.get_info().iteritems():
    print word
    for item in info:
        print item
    print '***'

for reading in parser.get_readings():
    print reading
```

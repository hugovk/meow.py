meow.py
=======

An entry for [NaNoGenMo 2014](https://github.com/dariusk/NaNoGenMo-2014/):

> Spend the month of November writing code that generates a novel of 50k+ words.

The rules say:

> The "novel" is defined however you want. It could be 50,000 repetitions of the word "meow". It could literally grab a random novel from Project Gutenberg. It doesn't matter, as long as it's 50k+ words.

Well, someone had better create 50,000 meows just to get it out of the way.

But this isn't just "meow" 50,000 times. meow.py replaces all words with a meow of the same length, keeping punctuation.

Usage
-----

    python meow.py infile.txt > outfile.txt

Output
------

Here's the above rule put through meow.py:

> Mew "meeow" me meeooow meoooow mew meow. Me meeow me me,mew meeeeeoooow me mew meow "meow". Me meoow meeeeeoow meow m meooow meoow meow Meeooow Meeeeeoow. Me meoow'm meooow, me meow me me'm mew+ meoow.

Here's the output of running meow.py on some Project Gutenberg (Purrject Mewtenberg):

| Original                                                                     |                        meow                        |  words |                     with translation                    |  words |
|------------------------------------------------------------------------------|:--------------------------------------------------:|:------:|:-------------------------------------------------------:|:------:|
| [Cats, by W. Gordon Stables](43429-0.txt?raw=true)                                   |  [txt](meow-43429-0.txt?raw=true) [pdf](meow-43429-0.pdf?raw=true) |  90,574 | [txt](meow-x2-43429-0.txt?raw=true) [pdf](meow-x2-43429-0.pdf?raw=true) | 181,149 |
| [Cats, by Charles H. Ross](43790-0.txt?raw=true)                                     |  [txt](meow-43790-0.txt?raw=true) [pdf](meow-43790-0.pdf?raw=true) |  59,725 | [txt](meow-x2-43790-0.txt?raw=true) [pdf](meow-x2-43790-0.pdf?raw=true) | 119,451 |
| [The Jungle Book by Kipling](jnglb10.txt?raw=true)                                   |  [txt](meow-jnglb10.txt?raw=true) [pdf](meow-jnglb10.pdf?raw=true) |  52,526 | [txt](meow-x2-jnglb10.txt?raw=true) [pdf](meow-x2-jnglb10.pdf?raw=true) | 105,052 |
| [An Enquiry Concerning the Principles of Morals by David Hume](nqpmr10.txt?raw=true) | [txt](meow-nqpmr10.txt?raw=true) [pdf]( meow-nqpmr10.pdf?raw=true) |  50,603 | [txt](meow-x2-nqpmr10.txt?raw=true) [pdf](meow-x2-nqpmr10.pdf?raw=true) | 101,206 |
| [Moby Dick; or The Whale, by Herman Melville](pg2701.txt?raw=true)                   |  [txt](meow-pg2701.txt?raw=true) [pdf]( meow-pg2701.pdf?raw=true)  | 215,136 |  [txt](meow-x2-pg2701.txt?raw=true) [pdf](meow-x2-pg2701.pdf?raw=true)  | 430,272 |

Extracts
--------

Here's part of Moby Dick:

```
"MEEOW.... Me. mew Mew. MEOW. Meow meooow me meoow meow meeooooow me
meeeoow; mew me Mew. MEOOW me meeeow me meeeeow." --MEEEEOW'M MEEEEEEOOW

"MEEOW.... Me me meow meeeeooooow meow mew Mew. mew Mew. MEOOOW; M.M.
MEOW-MEW, me meow, me meeoow." --MEEEOOOOOW'M MEEEEEEOOW

     MEOOW,               MEEOW.
     MEEOW,               MEOOW.
     MEEOW,               MEEOW-MEOOW.
     MEOOW,               MEEEOW.
     MEW,                 MEOOW.
     MEOW,                MEEEOOW.
     MEEOW,               MEEEEOOOW.
     MEOOW,               MEOOOOW.
     MEEOOOW,             MEOOOW.
     MEOOOOW,             MEEEOOW.
     MEEOW-MEOW-MEOW,     MEOOW.
     MEEOW-MEOW-MEOW,     MEEEEEOOOOW.

MEEEOOOW (Meeeeoow me m Mew-Mew-Meeeeeeow).
```

And here's part the Jungle Book with line-by-line translations:

```
He was a mongoose, rather like a little cat in his fur and his
Me mew m meeoooow, meeeow meow m meeeow mew me mew mew mew mew

tail, but quite like a weasel in his head and his habits.  His
meow, mew meoow meow m meeeow me mew meow mew mew meeoow.  Mew

eyes and the end of his restless nose were pink.  He could scratch
meow mew mew mew me mew meooooow meow meow meow.  Me meeow meeeoow

himself anywhere he pleased with any leg, front or back, that he
meeooow meeeeeow me meeooow meow mew mew, meeow me meow, meow me

chose to use.  He could fluff up his tail till it looked like a
meeow me mew.  Me meoow meeow me mew meow meow me meeeow meow m

bottle brush, and his war cry as he scuttled through the long
meeoow meeow, mew mew mew mew me me meeeeeow meeeoow mew meow

grass was: "Rikk-tikk-tikki-tikki-tchk!"
meoow mew: "Meow-meow-meeow-meoow-meow!"
```

Finally, here's [meow.py put through meow.py](meow.me).

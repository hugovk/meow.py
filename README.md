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


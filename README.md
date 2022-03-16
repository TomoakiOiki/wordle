# What is this?
Solver for [wordle](https://www.nytimes.com/games/wordle/index.html)

# How to use?
Start with,
`python3 solver.py`

Then input suggested word on wordle and input result like `-hb--`(`-`:⬛, `h`:🟩, `b`:🟨)

# example
```
------------------
Try: 1
unused_letters: []
blow_letters: []
hit_letters: []
Number of candidate: 12972
------------------
Selected word is muser
Input status:-hb--
------------------
Try: 2
unused_letters: ['m', 'e', 'r']
blow_letters: ['s']
hit_letters: [{'u': 1}]
Number of candidate: 4338
------------------
Selected word is gusts
Input status:
```

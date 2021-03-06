# Simple Wordle Clone on Python

A simple version of Wordle game, written entirely on Python. This is a clone of [The New York Times game](https://www.nytimes.com/games/wordle/index.html) (mobile version in dark mode), written for educational purposes.

![screenshot](https://user-images.githubusercontent.com/104437147/170983590-31fee18d-f2a1-424e-8a72-7f82c5f2ad7e.png)

## Gameplay description

If you are not familiar with Wordle, here are the short rules:

- You need to guess a 5-letter English word. You can use either your real keyboard, or a virtual one on the screen.

- The word is real, i.e. it can be found in dictionaries. You can see the full list in words.txt.

- You have six attempts to guess the word.

- After each attempt you can see which letters you did guess correctly:

"Green" letters are in the right place

"Yellow" letters are in the word, but in the wrong position

"Grey" letters are not in the word.

## Getting Started

### Dependencies

* Python
* [PyGame](https://github.com/pygame/)
* Stymie font (in repositary)
* [Colorama](https://pypi.org/project/colorama/) (for console version)

### Executing program

* Execute <b>launch.bat</b> 
or
* Build <b>wordle.py</b> in IDE
or
* Run in command line:
```
python wordle.py
```

## Console version

The repository also contains console version of Wordle:

![screen_console](https://user-images.githubusercontent.com/104437147/171115423-acc07e94-e0dc-47d1-a837-df5c972c5b1e.png)

You can play it by launching <b>console_wordle.py</b> in console:
```
python console_wordle.py
```


## Authors

<b>Vladislav Izhevskiy: </b>
[Github](https://github.com/ivlmag)
[LinkedIn](https://www.linkedin.com/in/izhevskiyvladislav)

## Version History

* 0.2 (31/05/2022)
    * Added console version
* 0.1 (30/05/2022)
    * Initial Release

## Acknowledgments

* [Orginal game](https://www.nytimes.com/games/wordle/index.html)
* [Josh Wardle](https://www.powerlanguage.co.uk/)

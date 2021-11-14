# Weekly Report 2

## Hours spent
5 hours in total. Breakdown below:

| Amount | Description                    |
| ------ | ------------------------------ |
| 2.5    | Configuring project and Python |
| 1.5    | Programming                    |
| 1      | Writing documentation          |

## What has been achieved this week?
A basic CLI app that understands the logic of the game 'rock paper scissors'

## What have I learned?
That Python is not that well suited for other uses than scripting /j. A large amount of time was spent on how OOP works in Python and trying to figure problems encountered.

## Problems encountered
Python in general. Various problems such as learning that you cannot inject dependencies in Python and still trying to figure out a good structure for the project; having problems with accessing packages from other packages changed my initial plan (see figure below), will look out for solving the problems next week.

```
└── src
    ├── logic
    │   └── ai.py
    ├── ui
    │   └── cli.py
    └── rock-paper-scissors.py
```

I wanted a class named `CLI` in `cli.py` inside `ui` package to have access to a class named `AI` in `ai.py`. My initial solution was to inject the `AI` class into `CLI`'s constructor, but apparently Python by itself doesn't have dependency injection. The next solution I had was to just call `AI` in `cli.py` but because of my package structure I encountered an ImportError. Will have to have a look into the structure next week.

## What's next?
Fleshing out the basic structure of the program. First look into the implementation of Markov chains.

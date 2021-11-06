# Specifications

## What does it do?
The software is a [rock paper scissors](https://en.wikipedia.org/wiki/Rock_paper_scissors) AI. It takes an inputs (rock, paper or scissors) from the user and calculates the probability of player giving a certain input from the previous inputs and outcomes of the games against said user. Options can be added to compare how the algorithm works if it considers different amount of games and even a comparison to another algorithms (if such algorithms for rock paper scissors exist).

## Algorithm
The algorithm used in the AI is [Markov chains](https://en.wikipedia.org/wiki/Markov_chain). There are two choices for the algorithm. Firstly I had never used it or even read about before unlike the most of the other algorithms presented in the [course documentation](https://tiralabra.github.io/2021_p2/en/topics/). Secondly the algorithm is best suited for our problem. It can adapt to players strategy unlike any other algorithm and can see patterns in opponents behaviour in this seemingly luck-based game.

## Time complexity and memory
The probability tables used by the algorithm are to be stored in either a hash table or two dimensional array (matrix). If stored in hash table the values can be updated and read in linear time O(1). If stored in a matrix, the said matrix would have 3 columns (one for each rock, paper and scissors) and n rows, where n=3^m (or 9^m, if also considering the outcomes of the previous games) and m is the amount of games the algorithm considers for deciding the probabilities of next input.

## Language
The language of choice is Python. The reason behind choosing Python is quite similar to the reasoning behind the choice of algorithm; it's a language I've previously used only for scripting and I want to learn how to do larger programs with it. It also has useful libraries like Pygame for creating the UI, so I don't have to spend too much time on 'useless stuff'. The issue with Python always is that it's not the most powerful language but the probability tables used in the program shouldn't be too large and using Python should not be a problem. I was also thinking about doing the project in JavaScript so it could be a webapp, but I didn't feel comfortable enough with my level of skill in the said language. I originally completed the course *Datastructures and algorithms* in Java so I should be able to peer review projects made in Java.

## Other stuff
I'm a student in Computer Science Bachelor program (Tietojenkäsittelytieteen kandidaatti (TKT)). The project was inspired by this [paper](https://arxiv.org/pdf/2003.06769.pdf). This and everything else related to the document will be written in English.

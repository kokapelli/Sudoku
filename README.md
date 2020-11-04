# Sudoku
Sudoku game made for fun by Hampus Falk. The game is minimalistic and is missing extra auxiliary functionalitites such as the capability to put several potential values in a square. A technique commonly used by more proficient Sudoku solvers. Once a sudoku has been solved, it will create a new one with the click of the mouse, and if a sudoku is proven to be too difficult, just press the shift button and it will solve it for you.

## How to Play
_Pre-req: Enter your "difficulty" in Game.py by setting the number of pre provided numbers you'll get. This is done by hardcoding the value <self.providedNumbers> to the amount of numbers you wish_
1. Enter a terminal or IDE of your choice capable of running Python
2. Enter  *py Game.py* or *Python Game.py* depending on preference and setup
3. Click a box to select it
    1. Hardcoded values are defined by a light grey background of its square
    2. Type using your keyboard the number you wish to enter in the box
4. If you wish to stop playing, simply hit your *Escape* key
5. If you wish to have the sudoku solved for you, simply hit the *Return* key
6. If you have finished the Sudoku, click the mouse to start a new automatically generated game.

## Issues
1. As mentioned above the game is highly minimalistic. Therefore the game can solely accept square values and determine whether you have provided a reasonable solution or not.
2. Auto generated games can create games with several correct solutions, therefore it lacks the beauty and quality of a sudoku with a unique answer.
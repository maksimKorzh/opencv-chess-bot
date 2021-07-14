# OpenCV Chess Bot
a proof of concept implementation of visual chessboard recognition<br>
and automated move making on the screen using Python, OpenCV and PyAutoGUI

# Demo video
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/1Tt_jFeYUWc/0.jpg)](https://youtu.be/1Tt_jFeYUWc)

# How it works
1. Makes a board screenshot
2. Detects chess pieces and stores it's coordinates
3. Generates FEN string based on piece coordinates
4. Passes FEN to the UCI engine
5. Converts best move to square coordinates on screen
6. Moves a mouse to coordinates associated with the source square then mimics a click,<br>
   moves a mouse to coordinates associated with the target square then mimics a click
7. Repeats until the game is over

# Disclaimer
Because of a cheating being a big issue nowadays<br> 
I didn't put any effort to adapt this project to be<br> 
easily used out of the box by end users, e.g. chess cheaters.<br>
This project is intended for programmers with a tinkering purposes in mind.<br>
Before asking any questions or opening issues make sure to follow<br>
the tutorials below - they are short and full of the timestamps<br>
so you can watch only those parts you're interested in 

# How to use it - YouTube tutorials
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/aUDkVUAHd0Q/0.jpg)](https://www.youtube.com/watch?v=aUDkVUAHd0Q&list=PLmN0neTso3Jzbh1P5Tr3o_wvAawFE2__e)

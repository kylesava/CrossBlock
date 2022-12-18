# CrossBlock

I'm going to preface by saying this is a VERY old project, in fact I view it as the first real coding project that I have made. This was all the way back at the start of 2015, when I was in grade 8. This was a time when I had never recieved any formal education on Python, and my knowledge of what I was doing was completely based on exparimentation and a plethora of google searches for things like "How do I make graphics in python", and "can I put an array inside of an array". This is very clearly refleced in my code, as without ever having made a project of this scale, and not learning some fundementals of programming - there are some extremely inefficient but clever workarounds I had to come up with for the problems I was facing. <br>
My favourite example of this comes with the first function that is defined, titled 'textfunc(r,x,i,o)'. On a first glance the nomenclature for variables is already horrendous, and it is completely unclear what these inputs refer to. If we look a little deeper though, we can see the purpose of this function, and when I had to use it. At the time, no one had ever taught me datatypes - I understood that I could use numbers, or I could have text with quotations, and that built-in functions may require these different types, but it never occured to me this was a problem that was 'already solved' so to speak. I've pasted the body of this function below so you can see for yourself if you're too lazy to go look at the Python file:

    if r == 0:
        a=""
    elif r == 1:
        a="1"
    elif r == 2:
        a="2"
    elif r == 3:
        a="3"
    elif r == 4:
        a="4"
    elif r == 5:
        a="5"
    elif r == 6:
        a="6"
    elif r == 7:
        a="7"
    elif r == 8:
        a="8"
    elif r == 9:
        a="9"
    text = font.render(a, True, x)
    screen.blit(text, [i,o])
<br>
This function was a glorified and less functional version of str(). It's funny to look back on these projects and see how my code as evolved in efficiency and readability over the years, and I think this program as a whole is a perfect portal into the mind of a young computer science obsessed teenager. <br>

<br>

As for the program itself, the game is actually still rather enjoyable and my roommate and I have become somewhat addicted to 'speed-running' the easy mode (my record is ~37 seconds). I titled the game Cross Block, and it was a complete ripoff of PiCross, a game that I remembered playing briefly as a much younger kid and decided to make my rendition. After more recent research, the game is more commonly known as a 'Nonogram', and there are many versions of it to be found. Mine forces the player to use a 9x9 pixel board, with the contents of each row and column indicated on the left side and top respectively. The goal is to figure out the correct 9x9 pixel image that satisfies the conditions given, very similar to Sudoku. <br>
There are three difficulties that I made, being easy, medium, and hard. I had the initial random generation of the board controlled by these difficulty levels, with the easier modes having more filled in squares on the board (which I still believe is a rather fair way of managing difficulty). The primary flaw of this program currently is my young mind's lack of realization that monitors can have different sizes, so the game is hard coded to a certain screen size and may not fit on some smaller monitors at all. I welcome you to give it a try though, and I've included some screenshots below of the game being played.
<br>

![image](https://user-images.githubusercontent.com/77376150/208271655-596f5ebc-3f61-4fdc-8aea-e65bffd95aa2.png)
![image](https://user-images.githubusercontent.com/77376150/208271669-8c2cc603-a155-40cb-9da0-e3c56b3e766a.png)
![image](https://user-images.githubusercontent.com/77376150/208271718-a549a350-604f-4248-b208-0d7767993ca4.png)
![image](https://user-images.githubusercontent.com/77376150/208271737-e6366466-054e-40ce-9e74-469dabdde7f8.png)


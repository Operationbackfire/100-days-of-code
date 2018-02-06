# 100 Days Of Code - Log

### Day 0: January 19, 2018

**Today's Progress:** Getting MEAN with... book tutorial.

**Thoughts:** Coudn't get 'heroku local web' to work. 

**Link to work:** [loc8r app](https://github.com/Operationbackfire/loc8r)

### Day 1: January 20, 2018

**Today's Progress:** Getting MEAN with... book tutorial.

**Thoughts:** heroku local still dosn't work. Made my first issue.

**Link to work:** [github 1. issue](https://github.com/Operationbackfire/loc8r/issues/1)

### Day 2: January 21, 2018

**Today's Progress:** Got heroku to work. Did some Jade. When I tried to push to heroku end the end it failed again.

**Thoughts:** I used an answer from Stackoverflow to get heroku to work, but en the end the answer failed me. I coudn't be repeated.

**Link to work:** Nothing.

### Day 3: January 22, 2018
**Today's Progress:** Referencing data in Jade templates: interpolation and buffered code. Mixin in Jade. Trying out MongoDB. Installed with brew. Don't know if it is alive yet. Intalled Mongoose package for NodeJS. Added some lines of code to models/db.js, and referenced it from app.js.

**Thoughts:** Will get MongoDB to work tomorrow.

**Link to work:** Not much. Heroku is still failing me. Something wrong the the Dezalgo package.

### Day 4: January 23, 2018

**Today's Progress:** MEANapp: mongodb is now working. There is a difference between 'mongod' and 'mongo'. Making the /data/db folder, changing permissions and adding to the $PATH. With some help from Stackoverflow and the mongodb installation homepage. New words: collection, document, schema and path.
Neso Academy and Digital Circuits: Watched youtube videos about latches,flip-flops and now counters. Not finished counters yet. 

**Thoughts:** Try to find the connection between Digital Circuit and the Gezel language.

**Link to work:** Nothing yet.

### Day 5: January 24, 2018

**Today's Progress:** Made a profile on mLab and mongodumped a collection from my MEANapp.

**Thoughts:** Every day a small step. Got Heroku to work by deleting all npm directories and package-lock.json. I also used npm update. I don't what worked, but it worked.

**Link to work:** Nothing yet.

### Day 6: January 25, 2018

**Today's Progress:** Arduinoday. Break from the MEANapp.

**Thoughts:** How to use the 16 pin DIP? Is it a shift Register/many flip-flops in a row. Maybe this one https://www.arduino.cc/en/Tutorial/ShiftOut.

**Link to work:** https://cryptic-spire-24600.herokuapp.com/

### Day 7: January 26, 2018

**Today's Progress:** Did some python. Got stuck in at recursive definition of a function, that had to count the depth of a treestructure tuple. Break from the MEANapp.

**Thoughts:** Shift Register SISO, PISO and PIPO, and SIPO at Neso Academy.

**Link to work:** The same as yesterday.

### Day 8: January 27, 2018

**Today's Progress:** New stuff in Python: dictionary {}, timeit library with the Timer function didn't, maybe because it was for Python 3. I did some recursion exercises, but got stuck in Pascals triangle.

**Thoughts:** When I haved solved some more recursion exercises I will go back to lib0 from the MIT AI course.

**Link to work:** Here are the link to the recursion exercises. https://www.python-course.eu/recursive_functions.php and https://www.python-course.eu/python3_recursive_functions.php

### Day 9: January 28, 2018

**Today's Progress:** I tried to understand the solution to calculating the n'th row of the Pascal Triangle nad also the solution to calculating the Fibonacci Sequence from the Pascal Triangle. I made an iterative solution to the Sieve of Eratosthenes, but still have to understand the solution to the recursive solution. 

**Thoughts:** Having the same thought as yesterday __When I haved solved some more recursion exercises I will go back to lib0 from the MIT AI course.__ I have to figure how a Fixed Point Combinator works and what Beta-reduction is. It has something to do with recursive functions.

**Link to work:** Here are the link to the recursion exercises. https://www.python-course.eu/recursive_functions.php and https://www.python-course.eu/python3_recursive_functions.php

### Day 10: January 29, 2018

**Today's Progress:** Finished lab0 of AT MIT.

**Thoughts:** Went back and nailed it.

**Link to work:** No links today.

### Day 11: January 30, 2018
**Today's Progress:** Tried to do lab1 of AT MIT. Wrote some family relation rules and used them to construct new rules about the family. Data: simpsons and black (from Harry Potter). I didn't write the backchaining function, but tried to understand a solution. It was important to use the functions match, populate and the member functions .antecedent and .consequent of the class IF. It was difficult to understand when to shift between the classes AND and OR and the list class.

**Thoughts:** I moved on to lab2. Need to implement DFS,BFS,Hill Climbing and Beam on a graph structure tomorrow. 

**Link to work:** No links today.

### Day 12: January 31, 2018
**Today's Progress:** I tried to implement DFS in lab2, but failed. I used recursion, but couldn't get it right. I looked at the code of someone having implemented DFS and BFS, and he didn't use recursion. In DFS the idea is to maintain a list with paths [('S','A'),('S','B')]. The idea is to delete the first path ('S','A') on the list and update it with its children [('S','A','B'),('S','A','D'),('S','B')]. Do the same with the front of the list. We get ('S','A','B','C') and ('S','A','B','G') that has to be added to the front after deleting ('S','A','B').
In BFS the updated paths should be placed in the back [('S','B'),('S','A','B'),('S','A','D')] and the front should be updated. Do the same again. [('S','A','B'),('S','A','D'),('S','B','A'),('S','B','C')].

**Thoughts:** Hill Climbing is DFS/BFS? with sorting of the heuristic distances to goal. Only 1 line added. BEAM is DFS/BFS? only looking at k children e.g. 2.

**Link to work:** Nothing.

### Day 13: February 1, 2018
**Today's Progress:** Forsøgte at implementere DFS igen. 

**Thoughts:** Didn't have much time today.

**Link to work:** Nothing.

### Day 14 and 15: February 2 an 3, 2018
**Today's Progress:** 14: I reimplemented DFS, BFS, Hill Climbing and BEAM in Python. It cut out at while loop of the first 3. I don't know if BEAM has to save all paths or just save beam_width # of shortest paths at each level.
I tried to implement branch and bound, but I didn't make it. I used the data structure (path, path_length) and 'min' with an anonymous function to find minimum.
I still need to look at A*.
I learned about 2 constraint satisfaction problems: line drawings (Huffmann, Guzman and Waltz) and graph coloring. Contraint propagation.
15: Games and minimax. I wrote a simple score function in lab3 modeled after the basic scoring function. My scoring function lost playing Connect Four. I now understand how the recursive minimax function works using -1 to change between min and max.

**Thoughts:** Next is to implement and understand alpha-beta pruning. I need to understand Deep Cut-off.

**Link to work:** Nothing.

### Day 16: February 4, 2018
**Today's Progress:** Used the Selenium library for Python to login and download userinfo to a file. Storing it in a database will be the next step. Also timing it could be fun - e.g setting it to download everyday at noon. I also did some regex.

**Pending Projects:**
1. MEANapp - continue work
2. alpha-beta pruning - watch video and implement
3. MySQL - forgot password
4. sklearn - library not working
5. python3 - not working
6. unittest - learn to test
7. Timing in Python.

**Links:** Great way to learn https://regexone.com/

### Day 17: February 5, 2018
**Today's Progress:** Tried to understand the code around the alpha-beta pruning function mainly the tree_searcher.py. I read through an implementation of the function and now I have an idea of how to start.
I did some more Selenium. I had some problems with instances of a class, that didn't want to return the values that I had put into them.

**Pending Projects:**
1. MEANapp - continue work
2. alpha-beta pruning - implement
3. MySQL - forgot password
4. sklearn - library not working
5. python3 - not working
6. unittest - learn to test
7. Timing in Python.

**Links:** No links.

### Day 18: February 6, 2018
**Today's Progress:** I read in data from a file line by line using regex to select name and age and tried to add it to a class. The idea was to do something simple so that i could try out the unittest library. I get it now. I watched some videos: Nearest Neighbors (The Robotic Arm Example looking up position, speed, acceleration in a table and then NN interpolation. Only few iterations are needed.). Identification Trees and Disorder (The Vampire 8 Sample Example - the idea is to select at path of tests in the test tree by calculating the testquality - here the disorder is used - to identify a vampire among the the 8 samples). Neural Net (The 2 neuron example is worth looking through again. Important concept: eliminating the threshold T by adding an extra neuron with weight T and input -1, threshold stairfunction -> sigmoid function and performancefunction as the -norm (the idea is to maximize the -norm = minimizing the norm = training the neural net)). Neural Nets are used in image recognition e.g. the toronto neural net. Deep Neural Net: well...
<img src="assets\banner.png">
<br>
<br>

# Python Mini Projects

An open source repo consisting of all the Python projects 

<br>
<br>

# Table of Contents
- [ How-to-Contribute ](#How-to-Contribute)
- [ Project-List](#Project-List)
  - [Projecy-1 (Unsolved)](#project-1)
  - [Projecy-2 (Unsolved)](#project-2)
  - [Projecy-3 (Unsolved)](#project-3)
  - [Projecy-4 ](#project-4)
  - [Projecy-5 (Unsolved)](#project-5)
  - [Projecy-6 (Unsolved)](#project-6)
  - [Projecy-7 (Unsolved)](#project-7)
  - [Projecy-8 (Unsolved)](#project-8)
  - [Projecy-9 (Unsolved)](#project-9)
  - [Projecy-10 (Unsolved)](#project-10)
  - [Projecy-11 (Unsolved)](#project-11)
  - [Projecy-12 (Unsolved)](#project-12)
  - [Projecy-13 (Unsolved)](#project-13)
  - [Projecy-14 (Unsolved)](#project-14)
  - [Projecy-15 (Unsolved)](#project-15)
  - [Projecy-16 (Unsolved)](#project-16)
  - [Projecy-17 (Unsolved)](#project-17)
  - [Projecy-18 (Unsolved)](#project-18)
  - [Projecy-19 (Unsolved)](#project-19)
  - [Projecy-20 (Unsolved)](#project-20)
  - [Projecy-21 (Unsolved)](#project-21)
  - [Projecy-22 (Unsolved)](#project-22)
  - [Projecy-23 (Unsolved)](#project-23)
  - [Projecy-24 (Unsolved)](#project-24)



<br>
<br>

## Thanks to all contributors!
<a href = "https://github.com/D3FaltXD/Python-MiniProjects-LPU2022/graphs/contributors">
   <img src = "https://contrib.rocks/image?repo=D3FaltXD/Python-MiniProjects-LPU2022"/>
</a>

<br>
<br>

# Project-List

Contribute to the projects which are tagged as `Need Solution`

## Project-1 
## `Need Solution`
Design a project where as an input student will give a static number (between 1 to 6) and then roll the dice which randomly generate some value between 1 to 6. The winning situation arrives when the given static/fixed number exactly same to the number came after rolling the dice.<br>
<br>
User can play the game as many numbers of times he wants until user wants to exit, and whenever winning situation occur some scores must be given to the user, and these scores goes on adding if user play this game multiple number of times.
Note: Dice contains face value’s (1 to 6)<br>
<br>
Hint: Make use of random.randint() function <br>
<br>
(Student is free to decide the input and output layout for this mini project)


## Project-2
## `Need Solution`
Create the Rock, Paper and Scissors game with Python, we need to take the user’s choice and then we need to compare it with the computer choice which is taken using the random module in Python from a list of choices, and if the user wins, then the score will increase by 1.
<br><br>
Example:<br>
User: Rock, Paper or Scissors?<br>
CPU: rock<br>
Tie<br>
User: Rock, Paper or Scissors?<br>
CPU: paper<br>
You win! Paper covers Rock<br>
User: Rock, Paper or Scissors?<br>
CPU: scissors<br>
You lose… Rock smashes Scissors<br>
Rock, Paper or Scissors?<br>
End the game<br>
Final Scores:<br>
CPU:1<br>
User:1<br>
<br><br>
Hint: Make use of random module to design the game
(Student is free to decide the input and output layout for this mini project)
<br>

<br><br>

## Project-3

## `Need Solution`

Email Slicer is just a simple tool that will take multiple email address as an input and slice it to produce the username and the domain associated with it. The email must be divided into two strings by using ‘@’ as the separator.<br><br>
So, user provides n number of email addresses and you have to design a logic to slice the username and the domain out of those email addresses. The domain part must print in capitals.
Note: Email addresses must be stored first in some container and then operate the required logic on it.<br><br>
Example:<br>
abc@gmail.com<br>
xyz@yahoo.com<br>
after slicing<br>
username :abc and domain: GMAIL.COM<br>
username: xyz and domain: YAHOO.COM<br>
(Student is free to decide the input and output layout for this mini project)
<br>
<br><br>

## Project 4

## ``Solved``

Create a program that takes the length of the password as input and generates a random password of the same length. The strength of the password depends equally on the 4 properties mentioned below. If the password generated randomly following the rules or constraints given below, then that password is treated as good in terms of strength and accepted otherwise ignore that password.<br><br>
The properties to be followed for a strong password are:
- At least 12 characters.<br>
- A mixture of both uppercase and lowercase letters.<br>
- A mixture of letters and numbers. <br>
- Inclusion of at least one special character, e.g., @ #?]
<br>

Note: do not use < or > in your password, as both can cause problems in Web browsers.
<br>
(Student is free to decide the input and output layout for this mini project)

[``Solution``]()

 <br><br>



## Project-5

## `Need Solution`

The task is to create a script that generates a random number between a fixed range, and  if the user guesses the number right in three chances, then user wins otherwise user lose.
This game user can play as many numbers of times and whenever user wins a score is to be given to the user.<br><br>
At the end the users score must be displayed on the screen.
Hint: Make use of random module to design the game<br><br>
Abstract steps:
- The user enters the lower and upper bounds of the range.
As a result, the compiler generates a random integer between the range and stores it in a variable for future use.
- A while loop will be created for repetitive guessing.
- When a user guesses a number that is greater than a randomly selected number, the user receives the message “have one more try”. Your guess was too high.
- If the user guesses a number smaller than a randomly selected number, the user gets an output of “have one more try “. Your guess was too small”
- In addition, if the user guesses within a minimum number of attempts, they get a “Congrat’s” message and also get the winning scores.
- If the user fails to guess the integer in the minimum number of guesses, he/she will receive a “Better Luck Next Time!
<br><br>

(Student is free to decide the input and output layout for this mini project)
<br>
<br>

## Project-6

## `Need Solution`

You need to write a python script that generates an acronym word from a given sentence.<br><br>
- Take multiple strings as input in the form of list.
- Add the first letter of each string to output.
- Iterate over the complete string and add every next letter to - space to output.
- Change the output to uppercase (required acronym).
- You have to generate acronyms for all given strings.

(Student is free to decide the input and output layout for this mini project)
Hint: You can use split and indexing to fetch the first word and then combine it.
<br><br>

## Project-7

## `Need Solution`

The task is to generate a random story every time user runs the program.<br><br>
Every time the user runs the program, we must produce a random tale. We'll first store the portions of the tales in distinct lists, and then use the Random module to choose random sections of the stories from those lists:<br><br>
To construct a random narrative, we first imported the random module, then built sections of the stories in separate lists, then randomly picked portions of the lists.<br><br>
Note: You store the portion of your tale/story in different lists, and during displaying the story when you pick the portions randomly your complete story must make some sense.
(Student is free to decide the input and output layout for this mini project)<br><br>
Hint: <br>
- Random module can be used to select random parts of the story stored in different lists.
- Sections of the story can be an adjective, a preposition, a proper noun, etc.
<br><br>

## Project-8

## `Need Solution`

Your task is to build a currency converter that will allow you to convert currencies from one unit to another, such as converting Indian rupee into pounds, euros, US dollar, Canadian dollar, Chinese yuan, Russia’s Rubal, etc. or vice versa.<br><br>
In this project build a TUI (Text based user interface), where you will enter the source currency to be converted and conversion rate. And after conversion display the amount in the target currency.<br><br>
(Student is free to decide the input and output layout for this mini project)

<br>
<br>

<div align="center"  class="icons-social" style="margin-left: 10px;">
 <a   target="_blank" href="https://discord.gg/AHAqK569Hq">
			<img src="images/join_us.png"></a>
   <br>
	<small>A Hackathon 2022 Repo </small>
</div>

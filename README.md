# Password Hashing Visualizer and Cracker
A web application built with Python and Flask demonstrating password hashing concepts through an offensive and defensive lense. Done as I was learning about these concepts. Actually learned during the process that chaining, 
especially with the technique I used, is actaully a vulnerability to my secuirty instead of a helper. I knew that Argon2 is not something that can be realistically attacked with dictionary cracking and is the standard in security practice
but wanted to see if there was a way
to add even more security anyway and ended up creating a vulnerability. Through my learning process in this project I learned about a chaining technique that actuallly can add more security and will be using it in the second version of
this project.


## What it Does and What I learned

### 1 - Chained Password Hashing Visualizer
Hashes a user input using 5 cryptographic hashing algorithms in a sequence that would be different in different instances. The output of one algorithm is the input of the next.
It displays the final Hash output, computation time in milliseconds, notes about the concepts.
The Hashing Chain goes in order from MD5, Sha1, Sha256, Bcryot, and Argon2 but in my learning process found that this is a pretty weak combination being that it goes from weakest to strongest and a hacker would 
only have to guess the first(weakest in this instance) algorithm. I aslo risk reducing information space.
Although Argon2 is more than enough, I thouught a smarter combination would be to start with Argon2 and mix up the combinations. I later find that even this is not good.

### 2 - Password Cracker 
A manual application of real world dictionary attacks on passowords using the rockyou.txt wordlist which contains 14 million password combinations.
The hashing Chain goes from weakest to strongest (md5, sha1, sha256, bcrypt, argon2), and my simple dictionary attacker is displayed to not be able to crack argon2 and notes that it would take years to compute, and crack md5 rather quickly. 
My program caps the amount of attempts for argon2 at 1000 for the sake of the project.
Around here is when I learned that adding cheaper algorithms after a strong one like argon2 or bcrypt can shrink the attack space or let an attacker bypass inner algorithms completely and is just as bad as adding stronger ones
after cheaper algorithms. 


# Instructions

This is just a guide with instructions on how to install and play around with GIT using VsCode for the PV CVS presentation.
Aditionally I left some instructions on how to run a simple python script that creates a few endpoints so you can try out Postman as well.
Feel free to message me on teams with any questions.


### GIT Demo
#### Step 1 - installing GIT
Installing GIT is generally pretty straight forward, just use the official site (https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) and go to the section relevant to your Operative System (OS).
For windows you can use a regular installer that you can find in the downloads page, or, if you are feeling brave today, you can open powershell and run this command ```winget install --id Git.Git -e --source winget```.


#### Step 2 - Installing VsCode
VsCode is an Integrated Development Enviroment (IDE) made by Microsoft that's super versatile and easy to use. Especially for PVs if they need to do simple things like opening a JSON file, scripts, etc. 
In this demo we are going to use it to clone this repository, make a new branch, make some small change and commit it. 
You can find it here https://code.visualstudio.com/download , just pick the right one for your OS. 

Installation should be straight forward, just open it when you are done.


#### Step 3 - clonning a repo
By default VsCode should already detect that you have GIT installed. Git is the 3rd button counting from the top in the left sidebar.
Afterwards what you need to do is to create a GitHub account, and configure your login. You can configure your login by setting your username and email in Git like this:

1st - open your terminal/command line (in windows you can do ctrl + ç)
2nd - type this command, ```git config --global user.name "yourusername"``` and replace ```"yourusername"``` with your username
3rd - type this command, ```git config --global user.email "email@youremail.com"``` and replace ```"email@youremail.com"``` with your email
4th - when you make an action with Git in VSCode it should open a prompt where you fill in your PW and authenthicate. So let's try to clone something.

In this repository https://github.com/luis-cmrodrigues/CSV-demo you can just click the green button that says "Code" and copy the URL in the HTTPS section.
You will then go to the Source Control section in VSCode and initialize/clone the repository to your computer.
Since by default the master branch is the branch that's selected, you will get the code in master in your local repository.


#### Step 4 - making a new branch
Next you can try to create a new branch.
You can start by going to the same "Source Control" button and expanding the options under the ... on the right of that sidebar.
Then, just select 





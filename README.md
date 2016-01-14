# Assignment 1

You are going to be installing some things, taking some screenshots, etc.  If you don't know how to take screenshots, here are some helpful websites:

* Taking a screenshot [Windows](http://windows.microsoft.com/en-us/windows/take-screen-capture-print-screen#take-screen-capture-print-screen=windows-7) (also see [the snipping tool](http://www.makeuseof.com/tag/awesome-screenshots-windows-7/))
* Taking a screenshot [OSX](https://support.apple.com/en-us/HT201361)

## Github

We are going to use Github as a central repository for all of our code.  Although we will discuss git and version control during class, you are also encouraged to learn more about both git and github on your own.

* What is Github?
  * [article](http://readwrite.com/2013/09/30/understanding-github-a-journey-for-beginners-part-1)
  * [wikipedia](https://en.wikipedia.org/wiki/GitHub)
* The [Pro Git](https://progit.org/) book (free)
* The [git manual](https://git-scm.com/documentation) (also free)

### Tasks

1. Create a [github][] account
2. Take a [screenshot][] of your [github][] account (e.g. https://github.com/brantfaircloth), showing that you have an account and that you are logged in.  Make sure that the name of the screenshot reflects it is from [github][].
3. Download and install [Github Desktop](https://desktop.github.com/).  This is an application (or "app") that lets you more easily work with git and github

## Slack

[Slack][] is a real-time collaboration tool (basically like SMS or iMessage) that allows our class to keep in contact.  It's nice because it allows you to ask everyone in class a question without sending an email.  It's also allows different groups in class to create and use different chatrooms, and it allows us to pin/highlight particular answers that are useful.

### Tasks

4. Accept your invitation to the [Slack][] channel
5. Take a [screenshot][] showing that your are logged into your [Slack][] account.  You can either use the online client or the ["native" client for Windows or OSX](https://slack.com/downloads).  Make sure that the name of the screenshot reflects this is from [Slack][].
6. Add your name, github username, and [Slack][] username to the Google Doc that I put on the [Slack][] `#general` channel

## Text Editor

A good [text editor](https://en.wikipedia.org/wiki/Text_editor) is worth it's weight in gold.  It can help you write, manage, and maintain your code.  A good text editor basically makes your life easier, once you know how to use it (which can sometimes be _very_ hard).

There are a plethora of text-editors out there: [textmate](https://github.com/textmate/textmate), [sublime text](http://www.sublimetext.com/), [vim](http://www.vim.org/), [emacs](https://www.gnu.org/software/emacs/), [text wrangler](http://www.barebones.com/products/textwrangler/), etc., etc.  Each have their own costs and benefits, and almost everyone that uses a text editor frequently has [pretty strong feelings](https://en.wikipedia.org/wiki/Editor_war) about "their" text editor.

You can use whichever text editor you like during this class.  That said, I suggest we all use the same editor.  A new, interesting, and relatively strong text editor is named "[Atom][]" and was originally built by the [github][] folks so that there would be a decent, open-source text editor available to everyone.  [Atom][] is that editor.  It offers many common benefits (code colorization, autocompletion, good find and replace, multiplatform, etc.), as well as offering an extensible package system for installing new capabilities - like a [code linter](https://en.wikipedia.org/wiki/Lint_(software), which can help point out errors in your code before you run it.

Like all complex tools, [Atom][] has a manual.  It would be a good idea, like all complex tools, to read that:

* [Atom manual](https://atom.io/docs/v1.3.3/)

### Tasks

1. Download and install
1. Take a screenshot of [Atom][] on your computer
1. Twiddle with the Preferences if you want to change the color-scheme, etc.
1. Go to Preferences > Settings.
    * Turn on "Scroll past end"
    * Set "Tab length" to 4
1. Figure how to install (and install) the following [Atom][] packages:
    * linter
    * linter-flake8
1. Take a screenshot showing that [linter-flake8][] is installed

## Anaconda

As explained in the [syllabus][], the programming language that we are using for this class will be [Python](https://www.python.org/) 3.5.1, and we will be using the [Anaconda Python Distribution](http://docs.continuum.io/anaconda/index).  

### Tasks

1. Install Anaconda Python for your [operating system](https://en.wikipedia.org/wiki/Operating_system)
    * [OSX Installer](https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.4.1-MacOSX-x86_64.pkg)
    * [Windows Installer](https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.4.1-Windows-x86_64.exe)
    * [Linux Installer](https://3230d63b5fc54e62148e-c95ac804525aac4b6dba79b00b39d1d3.ssl.cf1.rackcdn.com/Anaconda3-2.4.1-Linux-x86_64.sh)
1. Once that's installed, crank up Python.  Take a screenshot of the Python [REPL][].  Exit Python.
1. Figure out how to start the [iPython notebook][ipython] (now, more correctly known as "[jupyter notebook][jupyter]")
1. Create a new [ipython][] notebook

## Your first set of programs

We haven't covered anything at all about programming.  It's cool - it's not that hard (ha!).  Without any real knowledge of what you're doing, I want you to create a (very small) tutorial using Python and the iPython notebook.  This notebook should explain the step(s) you are running, provide the correct input, and produce the correct output for the following tasks.  You are welcome to [use the Internet](http://lmgtfy.com/?q=famous+first+programming+exercise) to help you find the answers (as you are for all assignments - just be sure to give credit where it is due).

* More about [ipython/jupyter notebooks](https://youtu.be/H6dLGQw9yFQ)

### Tasks

1. Who in the hell is Guido Van Rossum?  Have Python print the answer, using [jupyter][]
1. Explain (what it is) and execute the most famous first programming exercise.  Where does this come from?  Feel free to just add your answer to the iPython notebook as [markdown-formatted](https://en.wikipedia.org/wiki/Markdown) text.
1. Produce the sum of the year of your birthday and the year of this class
1. Divide 3 by 2 and return the expected result.  Is this what you expected?  Why or why not?
1. Print the numbers 0 to 50 by 5
1. Draw and print 10 discrete numbers from a uniform distribution spanning the interval [0,1000000]
1. Python is what is known as a zero-indexed programming language.  Illustrate what this means.
1. ```import this```

## Using Git/Github

Now, it's time to turn in your assignment.  You should generally follow the [instructions for turning in assignments](https://github.com/biolprogramming/syllabus#submitting-assignments)

1. Fork and clone the [Assignment 1 repository](https://github.com/biolprogramming/test-assignment-1) to your computer
1. Open that repository in [Github Desktop](https://desktop.github.com/)
1. Create a directory, nested in the **answers** directory **in the cloned, forked assignment repository** that is your **username on github**
1. Navigate to this directory on your computer
1. Add the following:
    * Screenshot of [github][] account
    * Screenshot of [Slack][] session
    * Screenshot of [Atom][] installed on your computer
    * Screenshot showing that you installed [linter-flake8][]
    * Screenshot of the Anaconda [REPL][] on your computer
    * You mini-tutorial from [Your first set of programs](#your-first-set-of-programs), above, in ipynb format
    * A screenshot of everything above, in the repository, displayed by [Github Desktop](https://desktop.github.com/)
1. Commit all of the changes to your repository
1. Push/Sync that to Github
1. Make a pull request to the main [biolprogramming](https://github.com/biolprogramming) repository

[screenshot]: https://en.wikipedia.org/wiki/Screenshot
[git]: https://git-scm.com/
[github]: https://github.com
[Slack]: https://biolprogramming.slack.com
[Atom]: https://atom.io/
[linter-flake8]: https://atom.io/packages/linter-flake8
[syllabus]: https://github.com/biolprogramming/syllabus
[ipython]: http://ipython.org/notebook.html
[jupyter]: http://jupyter.org/
[REPL]: https://en.wikipedia.org/wiki/Read%E2%80%93eval%E2%80%93print_loop

# Breact: A python library for single page web apps

This project was started by dewball345. 

Breact is similar to react, with components and state. The main difference, however, 
is that Breact doesn't have a virtual dom; 
instead, each stateful element (element that uses setState) is assigned a unique id and is retrieved
and changed when necessary. There isn't much that I have added - just the bare minimum, for now. The source
code is around 40 lines of code and the simple hash router, which is a python implementation of the simple
router in Dev.to's tutorial, caps at around 50. 
You can find the tutorial at: https://dev.to/pixari/build-a-very-basic-spa-javascript-router-2k4p

Breact is powered by Brython.
- [Website](https://brython.info/)
- [Git repo](https://github.com/brython-dev/brython)

Contributions are welcome as the project is largely unfinished; for example, sanitizing data to prevent XSS
attacts, lifecycle methods, and many more need to be implemented.

Installation
-------

- Option 1: with ```git-svn```

If you have git-svn installed, you can clone the ```breact``` folder in this repository, as that contains the main source code. 
```
git svn clone https://github.com/dewball345/Breact/trunk/breact
```

- Option 2: Click [this](https://downgit.github.io/#/home?url=https://github.com/dewball345/Breact/tree/master/breact) downloadable link, generated by [DownGit](https://downgit.github.io)

Unfortunately, you cannot do ```pip install breact``` at the moment because of some issues with importing with brython.

Features
--------
1. The most obvious: Use python instead of javascript to create complex web apps
2. Work with a component-based system with state-management when developing SPA's
3. Use preexisting libraries like bootstrap, tailwind, and more!

Usage
------------

You can find a tutorial at [this link](TUTORIAL.md)

(VERY IMPORTANT) Hosting
------
Breact cannot work with github hosting for some reason(probably because it is for static sites)

You can use firebase hosting instead.

Solution

Put your main code in a directory. You can name it anything.
```
.
└── fbhosting/
    └── your main code
```
Then, follow the normal directions for firebase hosting. Select the directory that you put your main code in when it asks for a ```/public``` folder.

Examples
------ 
An example breact project can be found at:
https://github.com/dewball345/breact-example

Want to see a [Live Demo](https://breact-playground.web.app/#/)?

Contribute
----------

- Issue Tracker: github.com/dewball345/Breact/issues
- Source Code: github.com/dewball345/Breact

For now don't contribute anything yet, but once i finish this up, I will set up a contributing.md

Support
-------

Please write issues in the issue tracker

License
-------

dewball345/Breact is licensed under the BSD 3-Clause "New" or "Revised" License

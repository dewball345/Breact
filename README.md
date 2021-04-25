# Breact: A python library for single page web apps

Breact is similar to react, with components and state. The main difference, however, 
is that Breact doesn't have a virtual dom; 
instead, each stateful element (element that uses setState) is assigned a unique id and is retrieved
and changed when necessary. There isn't much that I have added - just the bare minimum, for now. The source
code is around 40 lines of code and the simple hash router, which is a python implementation of the simple
router in Dev.to's tutorial, caps at around 50. 
You can find the tutorial at: https://dev.to/pixari/build-a-very-basic-spa-javascript-router-2k4p

Contributions are welcome as the project is largely unfinished; for example, sanitizing data to prevent XSS
attacts, lifecycle methods, and many more need to be implemented.

not finished

    import project
    # Get your stuff done
    project.do_stuff()

Features
--------

- Be awesome
- Make things faster

Installation
------------

Install $project by running:

    install project

Contribute
----------

- Issue Tracker: github.com/$project/$project/issues
- Source Code: github.com/$project/$project

Support
-------

If you are having issues, please let us know.
We have a mailing list located at: project@google-groups.com

License
-------

The project is licensed under the BSD license.

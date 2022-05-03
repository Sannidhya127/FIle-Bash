File Bash Documentation
=======================

**File Bash** is a simple command line interface application developed and maintained in *The Python Programming Language*. Inspired by the *Linux Terminal* and the *Windows Powershell*, File Bash tries to frame the basic commands of a command prompt coded completely in python. The project is not intended to be deployed for public use but for a better practise of python and project management.

*Is there any practical use of this project?*

Yes, there are suffice reasons to justify the practical use of this project. This project might not be worth market value as there tons of free softwares like this. But this project can certainly be used for educational purposes. Every functionality of this cmd has been codes completely in python without plagiarism or modules that make things in just one line (except of core-python modules like os, time, win32, etc). Programmers can certainly study the code and also make contributions to the code and its logic.



Indices and Search
==================

* :ref:`genindex`
* :ref:`search`



Source Code
-----------

- Source Code: https://github.com/Sannidhya127/FIle-Bash


Installation
------------

For installing File Bash in your pc, you will need to have the following requirments satisfied:

- The latest version of Python installed
- The latest version of Git installed (reccommended)
- Windows 10 or higher prefered

To install File Bash, follow the steps accordingly (For users installing with git):

- Copy the github link of File Bash (given above)
- Open your Git Terminal and type *git clone https://github.com/Sannidhya127/FIle-Bash*
- The File Bash repository is now cloned to your local pc
- Open the File Bash directory which includes all the files
- Launch the *main.py* file
- DONE :)

*You can also use pyinstaller to convert the .py file to .exe*

To install File Bash, follow the steps accordingly (For users installing with github .zip download):

- Open https://github.com/Sannidhya127/FIle-Bash in your web browser
- Click on the the dropdown menu on the ``code`` button
- Select download as zip
- Extract the downloaded zip file
- Open the File Bash directory which includes all the files
- Launch the *main.py* file
- DONE :)


.. toctree::
   :maxdepth: 2
   :caption: Contents:


Contents
--------

.. toctree::
   quickstart
   commands
   functions
   root
   api
   conduct
   about
   contribute
   liscense
   updates
   author


Documentation Acknowledgements
------------------------------

This documentation is powered by the Python module *sphinx*. The documentation code is written in pure RestructeredText and is converted to html with reference to the configuration written in python by sphinx. The theme used in this documentation is the *tibas.tt* theme by Pradyun Gedam. A part of the :doc:`about` page has been borrowed from the Python Documentation with nessescary changes applied. Important reference links are provided below:

- Sphinx Module Documentation - https://www.sphinx-doc.org/
- tibas-tt documentation - https://sphinx-themes.org/sample-sites/tibas-tt/


Expected Upcoming Changes
-------------------------

This section documents changes that have been planned and drafted for implementation in the software. The current EUCs include (the ETAs may change):

- Standard API for all functions (with exceptions) [ETA - 12/08/2022]
- Complete the development of Rooter [ETA - 15/07/2022]
- Configuration system for users, like login and password [ETA - 30/05/2022]
- Complete the Documentation :) [ETA - ¯\\_(ツ)_/¯]


Troubleshoot
------------

For any kind of bugs that you come across while using File Bash, you are encouraged to attempt to fix it by making pull request in its github repository. If not possible for you to fix, you can open an issue in the repository or mail me at sannidhya127@gmail.com.

Support Me
----------

If you found File Bash an interesting project, it would be worth a million blessings for me if you oblige to follow me on GitHub at github.com/Sannidhya127 and if possible, propose an idea in the form of pull request in the repository. Refer to :doc:`contribute` for details on pull requests.

*This documentation is written and maintained by Sannidhya127*


FAQs
----

**What Language is File Bash written in?**

File Bash is coded completely in python

**Why not use modules that make functions executions so easy instead of the detailed code written?**

File Bash was made with the intentions of learning and exploring the core basics of python. If I just used a single module that would do all the stuffs for the entire function, it would be of no credit for me


**What would happen if I enter extra whitespaces in a command?**

Nothing, the compiler is written such that it ignores the extra whitespaces.

**Why isn't all the File Bash not well commented?**

I had tried to provide comments for as much of the functions possible, I have probably missed some. But that should not be a problem as a detailed description is provided in this documentation

**What is Rooter?**

Rooter is File Bash software testing utility. It is still under development and intends to serve as an in-depth issue traced for File Bash.

**What Language is Rooter written in?**

Rooter is also written in Python

**How does the File Bash API work?**

The File Bash API simply functions by retrieving a list of requested data in JSON format. It has no web connection and only treats GET requests.


**How was the documentation developed**

The Documentation is developed and maintained using Sphinx. The code is written in RestructeredText.

**What kind of a documentation is this?**

The File Bash documentation is not of a particular type. It is mixed product of system-user documentation
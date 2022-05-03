Quickstart Manual to the use of a Bash
======================================

For none cli users File Bash can be quite of a hectic to be used. The basic concept of any command prompt is to provide the end-user with a command line interface that intakes commands. The commands are pre defined and entering an undefined command would result in the bash showing an error. If the correct commmand is entered with required parameters and arguments (not nessescary that all commands will have parameters and arguments) the command will be executed and the desired result can be collected.
The following tutorial will help you understand how a terminal system or a bash works and how to use it. 

The Interface
-------------

On launching the File Bash Terminal you will observe an interface similar to this:

.. image:: https://i.imgur.com/sog6b7Q.png


In the above image we see a path given with a colon at the end. This is a basic command prompt interface, interface may slightly vary depending on the application being used. Towards the other side of the colon is the point where the user enters his/her desired command to the terminal and recieves the desired result unless a wrong command is passed. The path that we see is the current working directory, i.e, the folder in which the terminal is currently open.



Basic Commands (Visit :doc:`commands` page for details)
-------------------------------------------------------

Some of the most basic commands of the bash are :ref:`ls <ls>` (lists all directory items), :ref:`rm <rm>` (deletes given item), :ref:`mv <mv>` (renames given item with a new name from user), etc.

>>> C:\Users\Desktop\MyTestDir: ls

Result

>>> SomeTextFile.txt
    APythonFile.py
    /NiceFolder
    main.c
    image.png

The ``ls`` command lists the items of a dire

 
>>> C:\Users\Desktop\MyTestDir: rm SomeUnluckyFile.txt

The ``rm`` command deletes a File

>>> C:\Users\Desktop\MyTestDir: mv OriginalFile.txt NewFileName.txt

The ``mv`` command renames a file

Visit :doc:`commands` for further details.



We believe you have gained a standard command prompt knowledge from the following introductory tutorial. For more details, refer to the documentation.



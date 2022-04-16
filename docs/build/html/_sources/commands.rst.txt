Commands
========

A detailed list of commands and their functionalities for the ease of users.


.. _ls:

1. ls [List Directory items]
----------------------------

...

To print a list of all items in the current directory, use the ``ls`` command:

.. py:function:: ls(arg=None)

   Return a list of all items in current directory

   :param --docs: lists all items in directory with extensions .docs, .txt, .doc, .docxs, .rtf

   :param --dir/dirs: lists all directories

   :param --imgs: lists all items in directory with extensions .jpg, .png, .jpeg
   
   :param --aud: lists all items in directory with extensions .wav, .flv, .mp3, .aiff, .mkv
   
   :param --med: lists all items in directory with extensions .mp4, .webm, .gif, .wmv, .wav
   
   :param --progs: lists all items in directory with extensions .py, .c, .c++, .cpp, .exe, .rb, .r, .php, .js, .html, .java, .css


The ``ls`` command parameters can only track files with specifiend extensions. Other extensions will be *ignored* even if they fall in the requested category

.. _rm:


2. rm [Remove Item]
-------------------

...

To delete a file/folder, use the ``rm`` command:

    >>> C:\Users\Desktop\MyTestDir: rm HelloWorld.txt
    Deletes a file
    
    >>> C:\Users\Desktop\MyTestDir: rm MyLovelyFolder
    Deletes a folder

.. py:exception:: Del.ItemNotFoundError()

    Raised if given item does not exist


.. _mv:

3. mv [Rename Item]
-------------------

...

The ``mv`` command is used for renaming a file or directory. The syntax of the command is

>>> C:\Users\Desktop\MyTestDir: mv OrginalFile.py NewlyNamedFile.py

With the help of the above command, the system renames the initial file name (``OriginalFile.py``) with the new name proposed by the user (``NewlyNamedFile.py``).

If seperated with whitespaces, the index[1] argument is the current name and the index[2] argument is the new name to be given

.. py:exception:: ListIndexOutOfRangeError


    *Raises the error when names of items contain whitespaces. Developers are working to fix this*

.. py:exception:: FileNotFoundError


    *Raises the error when file bash failes to track file with specified name in index[1]*

.. _crf:

4. crf [Create File]
--------------------

...

The ``crf`` command is used for a creating a new *file* (note not a folder). The syntax of the command is

>>> C:\Users\Desktop\MyTestDir: crf MyNewFile.c

Here the file name with extension supplied after the command is created in the current working directory. 

.. py:exception:: FileExistionError

    Displays fatal error when a pre-existent file name is given with this hidden exception.

*Whitespaces* in name are supported

.. _crd:

5. crd [Create Directory]
-------------------------

...

The ``crd`` command is used to create a new directory. The syntax usage is

>>> C:\Users\Desktop\MyTestDir: crd MyNewFolder

A new folder called ``MyNewFolder`` is created with the help of this command.
To create a folder in another directory, specify full path

>>> C:\Users\Desktop\MyTestDir: crf C:\Users\Desktop\Code\NewFolder

This creates a new folder named *NewFolder* in the path ``C: -> Users -> Desktop -> Code``


.. py:exception:: DirectoryExistionError

    Displays fatal error when a pre-existent directory name is given with this hidden exception.

.. _cd:

6. cd [Current Directory/Change Directory]
------------------------------------------

...

The ``cd`` command has multiple purposes depending on its usage.

If user only inputs the command ``cd`` with no extra parameters, the command returns the Current Directory.

>>> C:\Users\Desktop\MyTestDir: cd
    >>> C:\Users\Desktop\MyTestDir


If user enters command ``cd`` and then a valid path on the local disk, the bash's *current working directory* is changed to the given path. Here ``cd`` stands for *Change Directory*

>>> C:\Users\Desktop\MyTestDir: cd \
    C:\: 

.. py:exception:: InvalidPathError

    Raises fatal error on passing invalid *arg[1][path]*

.. _sysinfo:

7. sys --info [System Information Printer]
------------------------------------------

...

The command ``sys --info`` is used for printing a very precise and detailed output of your system. 
By definition, the ``sys --info`` command prints a set of information in presentable format about System, Disk, Network and GPU

The syntax is such:

>>> C:\Users\Desktop\MyTestDir: sys --info

From the following command, we recieve an output of such, varying from system to system:

The first part

.. image:: https://i.imgur.com/NUCeVmO.png

The second part

.. image:: https://i.imgur.com/eXcNk3X.png

The third part

.. image:: https://i.imgur.com/R8opY7P.png

The output couldn't be fit in a single screenshot
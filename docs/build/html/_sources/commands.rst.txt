
.. .. code-block:: console

..    (.venv) $ pip install lumache

Commands
========

.. _ls:

1. ls
-----

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


2. rm
-----

...

To delete a file/folder, use the ``rm`` command:

    >>> C:\Users\Desktop\MyTestDir: rm HelloWorld.txt
    Deletes a file
    
    >>> C:\Users\Desktop\MyTestDir: rm MyLovelyFolder
    Deletes a folder

.. py:exception:: Del.ItemNotFoundError()

    Raised if given item does not exist


.. _mv:

3. mv
-----

...

The ``mv`` command is used for renaming a file or directory. The syntax of the command is

>>> C:\Users\Desktop\MyTestDir: mv OrginalFile.py NewlyNamedFile.py

With the help of the above command, the system renames the initial file name (``OriginalFile.py``) with the new name proposed by the user (``NewlyNamedFile.py``).

If seperated with whitespaces, the index[1] argument is the current name and the index[2] argument is the new name to be given


.. _crf:

4. crf
------

...

The ``crf`` command is used for a creating a new *file* (note not a folder). The syntax of the command is

>>> C:\Users\Desktop\MyTestDir: crf MyNewFile.c

Here the file name with extension supplied after the command is created in the current working directory. 

.. py:exception:: FileExistionError

    Displays fatal error when a pre-existent file name is given with this hidden exception.

*Whitespaces* in name are supported
Usage
=====

Installation
------------

To use File Bash, use the File Bash Installer Wizard

.. .. code-block:: console

..    (.venv) $ pip install lumache



Commands
----------------

I. To print a list of all items in the current directory, use the ``ls`` command:

.. py:function:: ls(arg=None)

   Return a list of all items in current directory

   :param --docs: lists all items in directory with extensions .docs, .txt, .doc, .docxs, .rtf

   :param --dir/dirs: lists all directories

   :param --imgs: lists all items in directory with extensions .jpg, .png, .jpeg
   
   :param --aud: lists all items in directory with extensions .wav, .flv, .mp3, .aiff, .mkv
   
   :param --med: lists all items in directory with extensions .mp4, .webm, .gif, .wmv, .wav
   
   :param --progs: lists all items in directory with extensions .py, .c, .c++, .cpp, .exe, .rb, .r, .php, .js, .html, .java, .css


The ``ls`` command parameters can only track files with specifiend extensions. Other extensions will be *ignored* even if they fall in the requested category

2. To delete a file/folder, use the ``rm`` command:

    ``Delete a file``

    ``C:\Users\Desktop\MyTestDir: rm HelloWorld.txt``

    ``Delete a folder``

    ``C:\Users\Desktop\MyTestDir: rm MyLovelyFolder``

.. py:exception:: Del.ItemNotFoundError()

    Raised if given item does not exist

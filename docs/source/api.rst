File Bash API Reference
-----------------------


.. http:get:: rm item -a -h

Retrieves set of data interpreted by the ``rm`` command during runtime

**Request Command**

>>> C:\Users\USER\Desktop\Altogether\Code: rm HelloWorld.txt -a -h --rm

The above request retrieves the following data in format ``json``

.. code-block::

    {
        "item" : "name",
        "type" : "Directory/File",
        "version" : version,
        "time" : current_time,
        "Existence" : True/False
    }
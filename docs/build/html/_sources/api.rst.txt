File Bash API Reference
-----------------------


.. http:get:: rm item -GET
--------------------------


Retrieves set of data interpreted by the ``rm`` command during runtime

**Request Command**

>>> C:\Users\USER\Desktop\Altogether\Code: rm HelloWorld.txt -GET

The above request retrieves the following data in format ``json``

.. code-block::

    {
        "item" : "name",
        "type" : "Directory/File",
        "version" : version,
        "time" : current_time,
        "Existence" : True/False,
        "Creation Time" : Time Of Creation,
        "Last Modified" : Last time of modification
    }



.. http:get:: crf item -GET
---------------------------

Retrieves set of interpreted data by the ``crf`` command during runtime

**Request Command**

>>> C:\Users\USER\Desktop\Altogether\Code: crf HelloWorld.txt -GET


The above request retrieves the following data in format ``json``

.. code-block:: json

    {
        "item" : "name",
        "version" : version,
        "Existence" : True/False,
        "Creation Time" : Time Of Creation,
    }

More values are expected to be added in future updates
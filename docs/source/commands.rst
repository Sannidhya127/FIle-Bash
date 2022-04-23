Commands
========

A detailed list of commands and their functionalities for the ease of users.


.. _ls:

1. ls (List Directory items)
----------------------------



To print a list of all items in the current directory, use the ``ls`` command:

.. py:function:: ls(arg=None)

   Return a list of all items in current directory

   :param --docs: lists all items in directory with extensions .docs, .txt, .doc, .docxs, .rtf

   :param --dir/dirs: lists all directories

   :param --imgs: lists all items in directory with extensions .jpg, .png, .jpeg
   
   :param --aud: lists all items in directory with extensions .wav, .flv, .mp3, .aiff, .mkv
   
   :param --med: lists all items in directory with extensions .mp4, .webm, .gif, .wmv, .wav
   
   :param --progs: lists all items in directory with extensions .py, .c, .c++, .cpp, .exe, .rb, .r, .php, .js, .html, .java, .css


The ``ls`` command attributes can only track files with specifiend extensions. Other extensions will be *ignored* even if they fall in the requested category

.. _rm:


2. rm (Remove Item)
-------------------



.. py:function:: delete(arg=item)


To delete a file/folder, use the ``rm`` command:

    >>> C:\Users\Desktop\MyTestDir: rm HelloWorld.txt
    Deletes a file
    
    >>> C:\Users\Desktop\MyTestDir: rm MyLovelyFolder
    Deletes a folder

.. py:exception:: Del.ItemNotFoundError()

    Raised if given item does not exist


.. _mv:

3. mv (Rename Item)
-------------------

.. py:function:: FileRename(arg=item)

The ``mv`` command is used for renaming a file or directory. The syntax of the command is

>>> C:\Users\Desktop\MyTestDir: mv OrginalFile.py NewlyNamedFile.py

With the help of the above command, the system renames the initial file name (``OriginalFile.py``) with the new name proposed by the user (``NewlyNamedFile.py``).

If seperated with whitespaces, the index[1] argument is the current name and the index[2] argument is the new name to be given

.. py:exception:: ListIndexOutOfRangeError


    *Raises the error when names of items contain whitespaces. Developers are working to fix this*

.. py:exception:: FileNotFoundError


    *Raises the error when file bash failes to track file with specified name in index[1]*

.. _crf:

4. crf (Create File)
--------------------

.. py:function:: CreateFile(arg=file)

The ``crf`` command is used for a creating a new *file* (note not a folder). The syntax of the command is

>>> C:\Users\Desktop\MyTestDir: crf MyNewFile.c

Here the file name with extension supplied after the command is created in the current working directory. 

.. py:exception:: FileExistionError

    Displays fatal error when a pre-existent file name is given with this hidden exception.

*Whitespaces* in name are supported

.. _crd:

5. crd (Create Directory)
-------------------------

.. py:function:: CreateDir(arg=directory)

The ``crd`` command is used to create a new directory. The syntax usage is

>>> C:\Users\Desktop\MyTestDir: crd MyNewFolder

A new folder called ``MyNewFolder`` is created with the help of this command.
To create a folder in another directory, specify full path

>>> C:\Users\Desktop\MyTestDir: crf C:\Users\Desktop\Code\NewFolder

This creates a new folder named *NewFolder* in the path ``C: -> Users -> Desktop -> Code``


.. py:exception:: DirectoryExistionError

    Displays fatal error when a pre-existent directory name is given with this hidden exception.

.. _cd:

6. cd (Current Directory/Change Directory)
------------------------------------------

.. py:function:: cwdPrint(arg=None)
.. py:function:: cwdChange(arg=path)

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

7. sys --info (System Information Printer)
------------------------------------------

.. py:function:: sys_info(arg=None)

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

.. tip::
    Note that in the above pics, the GPU details are missing. This is because of an unrecognisable intel hd integrated graphics card in the system. To fix this try the following steps:

    - Open Settings

    - Navigate to System > Display > Graphics

    - Click on the browse button and select the file bash application

    - Once added, click on options and select your GPU as the default File Bash GPU

    This process is not guaranteed to fix the issue, but might fix it. Development is in progress

.. _sr:

8. sr (Search Directory)
------------------------

.. py:function:: searchDir(arg=path)

The ``sr`` command has its usage in searching for a required item in the current working directory.
The syntax is

>>> C:\Users\Desktop\MyTestDir: sr HelloWorld.rb

Here the argument passed to the command is ``HelloWorld``, the sr command used the function ``searchDir(query)`` function where the query parameter holds reponsibilty of the item name. 

For a directory having items with names:
- main.py
- mainFile.c
- index.html
- main.css
- MainFolder
- AnotherFolder

If the user passes ``main`` as the ``query`` parameter, the output would include
``main.py, mainFile.c, main.css, MainFolder``

These names include the *query* ``main`` in them and are thus displayed

When *query* recieves an operand with no existence in the currrent working directory, it raises a *No Result Found* error.

.. _delf:

9. delf (Deletes only files)
----------------------------

.. py:function:: DelFile(command)

.. warning::
    This command is an early File Bash command and is depreceted from use. For better performance, use the :ref:`rm <rm>`
    command for better performance and efficiency.

The ``delf`` command was initially developed as a command for deleting only files in File Bash. The command, unlike ``rm`` command has no file/folder tracing system. On entering a folder name it raise a fatal Folder error.

.. py:exception:: FolderError

    Raised when operand is a folder

The command recieves the file name as argument with syntax 

>>> C:\Users\Desktop\MyTestDir: delf HelloWorld.java

This command deletes the file ``HelloWorld.java``.

For a non-existen file,

>>> C:\Users\Desktop\MyTestDir: delf SomeNonExistentFile.c++
    'SomeNonExistentFile.c++' does not exist

.. _deld:


10. deld (Delete Directory)
---------------------------

.. py:function:: DelDir(arg=directory)

.. warning::
    This command is an early File Bash command and is depreceted from use. For better performance, use the :ref:`rm <rm>`
    command for better performance and efficiency.

The ``deld`` command is used to delete only directories. It lacks the ability to track files and delete them. The command used *Python shutil* module to delete folders. The recently added ``rm`` command has outdone both ``delf`` and ``deld`` commands.

The syntax for ``deld`` is:

>>> C:\Users\Desktop\MyTestDir: deld MyDocs

Here the operand ``MyDocs`` is the target directory to be deleted. 

.. py:exception:: OperandNotFolderError

    Raised when entered operand is not a folder but a file.


.. _bash0:

11. bash --sys 0 (shutdown system)
----------------------------------

.. py:function:: shutdown(arg=None)

The ``bash --sys 0`` command shuts down the system.

.. _uid:

12. process --uid (lists running process)
-----------------------------------------

.. py:function:: processes(arg=None)

``process - - uid`` lists all running functions in a paginated format inclusive of their priority, 
processId, ThreadCount, WorkingSetSize, HandleCount.

The output is something like this:

>>> C:\Users\Desktop\MyTestDir: process --uid
b'HandleCount  Name                         Priority  ProcessId  ThreadCount  WorkingSetSize  
0            System Idle Process          0         0          8            8192
3981         System                       8         4          209          139264
0            Registry                     8         120        4            50270208
57           smss.exe                     11        448        2            999424
732          csrss.exe                    13        716        14           6045696
156          wininit.exe                  13        796        1            6537216
729          services.exe                 9         936        6            9687040
1386         lsass.exe                    9         980        8            19595264
1855         svchost.exe                  8         572        11           35430400
33           fontdrvhost.exe              8         992        5            2519040
334          WUDFHost.exe                 13        1088       11           13987840
1309         svchost.exe                  8         1144       12           15835136
321          svchost.exe                  8         1184       6            8749056
246          svchost.exe                  8         1360       3            8454144
233          svchost.exe                  8         1368       2            12566528
264          svchost.exe                  8         1376       6            11755520
259          svchost.exe                  8         1452       4            10170368
208          svchost.exe                  8         1540       5            10358784
415          svchost.exe                  8         1548       1            7983104
429          svchost.exe                  8         1564       7            15986688
139          IntelCpHDCPSvc.exe           8         1580       3            6852608
361          svchost.exe                  8         1604       10           8974336
146          svchost.exe                  8         1760       3            8810496
273          svchost.exe                  8         1848       6            11550720
844          svchost.exe                  8         1864       11           15884288
138          IntelCpHeciSvc.exe           8         1924       3            6909952
233          svchost.exe                  8         1156       5            12779520
171          svchost.exe                  8         2088       2            5853184
205          svchost.exe                  8         2260       2            7581696
329          SynTPEnhService.exe          8         2268       7            9375744
195          dasHost.exe                  8         2444       2            10842112
286          svchost.exe                  8         2472       11           8298496
205          svchost.exe                  8         2480       1            8986624
466          svchost.exe                  8         2556       7            16777216
184          svchost.exe                  8         2612       6            7393280
226          svchost.exe                  8         2624       3            14372864
213          svchost.exe                  8         2640       4            5562368
0            Memory Compression           8         2744       46           127373312
187          svchost.exe                  8         2760       3            8433664
115          svchost.exe                  8         2824       1            6246400
176          igfxCUIService.exe           8         2868       2            8781824
151          svchost.exe                  8         2904       7            7557120
240          svchost.exe                  8         2912       4            8851456
224          svchost.exe                  8         3068       6            7184384
502          svchost.exe                  8         2136       13           15527936
419          svchost.exe                  8         1268       6            9314304
265          svchost.exe                  8         2964       8            7606272
148          svchost.exe                  8         2532       3            6266880
351          svchost.exe                  8         3232       4            15683584        
180          svchost.exe                  8         3272       3            7065600
533          svchost.exe                  8         3384       12           18837504
240          svchost.exe                  8         3408       4            14442496
437          spoolsv.exe                  8         3436       7            12025856
428          svchost.exe                  8         3496       13           16584704
169          svchost.exe                  8         3552       3            7290880
193          wlanext.exe                  8         3736       9            7966720
82           conhost.exe                  8         3764       2            4718592
608          svchost.exe                  8         3912       11           29700096
390          svchost.exe                  8         3920       9            14319616
386          svchost.exe                  8         3928       16           23179264
267          svchost.exe                  8         3956       5            7868416
687          DSAService.exe               8         3972       12           21864448
779          OneApp.IGCC.WinService.exe   8         3988       7            25911296
785          OfficeClickToRun.exe         8         4008       21           39268352
364          svchost.exe                  8         4020       5            10805248
163          svchost.exe                  8         4044       3            7069696
106          esif_uf.exe                  13        4084       3            5554176
145          svchost.exe                  8         3524       1            6361088
218          LMS.exe                      8         4120       3            8421376
205          svchost.exe                  8         4136       5            8978432
191          svchost.exe                  8         4160       4            9445376
168          setup.exe                    8         4168       2            6565888
350          RtkAudUService64.exe         8         4180       14           11735040
130          RstMwService.exe             8         4188       3            5844992
178          SynAudSrv.exe                8         4196       5            7868416
145          SECOMN64.exe                 8         4204       4            8577024
157          RtkBtManServ.exe             8         4220       2            7565312
316          CxAudioSvc.exe               8         4240       8            23183360
777          SurSvc.exe                   4         4284       9            70680576
1630         MsMpEng.exe                  8         4348       40           245993472
457          svchost.exe                  8         4360       13           18546688
413          svchost.exe                  8         4400       8            22011904
141          svchost.exe                  8         4416       3            5369856
492          XtuService.exe               8         4504       14           29057024
133          jhi_service.exe              8         4604       2            5873664
438          svchost.exe                  8         4952       12           12165120
256          svchost.exe                  8         5324       8            8536064
90           AggregatorHost.exe           8         5700       3            5431296
313          WmiPrvSE.exe                 8         6604       6            16785408
431          DSAUpdateService.exe         8         6688       7            27566080
202          dllhost.exe                  8         6292       4            10850304
225          NisSrv.exe                   8         6932       12           11251712
255          svchost.exe                  8         7036       3            21028864
240          PresentationFontCache.exe    8         6972       4            13692928
166          svchost.exe                  8         6312       3            8343552
465          svchost.exe                  8         7240       10           21708800
204          svchost.exe                  8         7588       4            11997184
1438         SearchIndexer.exe            8         8688       15           38604800
180          GoogleCrashHandler.exe       4         1476       3            1667072
162          GoogleCrashHandler64.exe     4         3208       3            380928
298          svchost.exe                  8         9452       11           11231232
433          svchost.exe                  8         4320       11           17502208
271          svchost.exe                  8         4748       1            14934016
107          SgrmBroker.exe               8         10968      9            8515584
301          svchost.exe                  8         1096       9            14266368
221          svchost.exe                  8         10844      8            9875456
313          SecurityHealthService.exe    8         6708       4            13230080
301          svchost.exe                  8         10448      6            14422016
379          svchost.exe                  8         1796       3            18661376
310          svchost.exe                  8         5336       4            14237696
115          conhost.exe                  8         1680       3            6094848
887          esrv.exe                     13        9752       62           26288128
4345         esrv_svc.exe                 13        7076       84           66383872
542          csrss.exe                    13        9620       13           6684672
273          winlogon.exe                 13        2736       5            10358784
33           fontdrvhost.exe              8         4556       5            5054464
1282         dwm.exe                      13        11320      19           113324032
397          svchost.exe                  8         8048       6            17281024
349          audiodg.exe                  8         2664       6            23326720
681          sihost.exe                   8         11692      12           31219712
141          svchost.exe                  8         9520       1            8892416
514          svchost.exe                  8         10496      14           34574336
676          svchost.exe                  8         1260       7            35971072
335          igfxEM.exe                   8         5284       3            13582336
268          taskhostw.exe                8         6920       8            15159296
4424         explorer.exe                 8         6724       90           204386304
271          svchost.exe                  8         12000      9            19947520
505          SynTPEnh.exe                 10        6172       10           21618688
107          crashpad_handler.exe         8         11836      6            5701632
841          StartMenuExperienceHost.exe  8         4624       10           79355904
1481         SearchHost.exe               8         11984      63           85770240
605          RuntimeBroker.exe            8         240        12           39628800
280          RuntimeBroker.exe            8         2352       2            26439680
133          svchost.exe                  8         7668       1            8335360
245          dllhost.exe                  8         6104       7            14032896
450          ctfmon.exe                   13        12084      12           20979712
1430         TextInputHost.exe            13        5432       33           100003840
357          RtkAudUService64.exe         8         7204       12           12718080
455          MiniSearchHost.exe           8         12644      11           48721920
1610         chrome.exe                   8         10644      25           214237184
209          chrome.exe                   8         392        7            7270400
839          chrome.exe                   10        8320       16           170676224
340          chrome.exe                   8         12008      12           44531712
213          chrome.exe                   8         2672       8            17076224
236          chrome.exe                   8         2460       15           34983936
247          chrome.exe                   8         7768       15           112562176
238          chrome.exe                   8         1744       15           35041280
238          chrome.exe                   8         9568       15           37675008
247          chrome.exe                   8         11528      11           19161088
936          Code.exe                     8         3100       29           87969792
222          Code.exe                     8         10424      7            25473024
647          Code.exe                     10        11464      17           221683712
291          Code.exe                     8         13440      13           39960576        
588          Code.exe                     8         9412       20           216788992
239          chrome.exe                   8         11376      15           37822464
264          svchost.exe                  8         15152      4            13819904
384          Code.exe                     8         14752      23           81457152
233          Code.exe                     8         13332      16           56696832
244          svchost.exe                  8         11368      1            12328960
942          ShellExperienceHost.exe      8         15044      32           72110080
441          RuntimeBroker.exe            8         15296      11           26173440
185          Code.exe                     8         5260       14           69312512
298          Code.exe                     8         3200       17           145039360
107          conhost.exe                  8         6528       5            6479872
722          pwsh.exe                     8         3516       12           71077888
621          YourPhone.exe                8         9092       14           68878336
539          LockApp.exe                  8         9372       13           63373312
481          RuntimeBroker.exe            8         14072      10           36683776
196          svchost.exe                  8         14472      6            14159872
100          git.exe                      8         7304       11           6307840
181          RuntimeBroker.exe            8         2500       4            10215424
677          Widgets.exe                  8         11704      9            33959936
1069         msedgewebview2.exe           8         3356       28           43253760
145          msedgewebview2.exe           8         1884       7            6811648
643          msedgewebview2.exe           10        7856       15           9605120
276          msedgewebview2.exe           8         4276       10           31956992
198          msedgewebview2.exe           8         14488      7            18493440
410          msedgewebview2.exe           4         6396       14           34652160
590          SystemSettingsBroker.exe     8         9756       22           34607104
300          ApplicationFrameHost.exe     8         3180       1            27561984
136          svchost.exe                  8         2820       2            11051008
232          hpqwmiex.exe                 8         7524       5            11608064
322          chrome.exe                   4         5480       15           70184960
306          chrome.exe                   4         2452       17           98590720
221          chrome.exe                   4         12464      15           31698944
118          svchost.exe                  8         3164       2            7761920
159          svchost.exe                  8         9924       3            7409664
113          svchost.exe                  8         9296       3            6037504
212          Code.exe                     8         11972      13           183382016
109          conhost.exe                  8         11468      7            6721536
658          pwsh.exe                     8         12540      23           73854976
369          python.exe                   8         9884       8            44732416
189          WMIC.exe                     8         13696      8            12918784
163          WmiPrvSE.exe                 8         8136       9            9805824


.. _hide:

13. hide (hides any item)
-------------------------

.. py:function:: hide(arg=item)

``hide`` command hides any item on providing path.
NOTE:- It hides the item from File Explorer, some third party explorers might still track it.

Syntax:

>>> C:\Users\Desktop\MyTestDir: hide superSecretLol.c
Successfully hidden item superSecretLol.c with exit status 0

For a non-existent operand in *arg[1]*, it returns a non-existent error

>>> C:\Users\Desktop\MyTestDir: hide DoIExistsLol.bf
DoIExistsLol.bf does not exist


.. _uhd:

14 uhd (unhide)
---------------

.. py:function:: unide(arg=HiddenItem)

``uhd`` command unhides the target file or directory (is hidden).

Syntax:

>>> C:\Users\Desktop\MyTestDir: uhd superSecretLol.c

The above command unhides the file ``superSecretLol.c``

- For missing operand, no output is supplied
- For an operand with valid path but not hidden, no output is supplied
- For an invalid operand path, it returns a ``File not found - FileName`` error



.. _read:

15. read (prints file content)
------------------------------

.. py:function:: read(arg=File)

The ``read`` command is used to print the contents of a given file in the console. argument[1] is the target file to be read

For example, there is a file called HelloWorld.txt whose content is

Hello World

For reading the content of this file, we will have to use the ``read`` command with the following syntax applied

>>> C:\Users\Desktop\MyTestDir: read HelloWorld.txt
    Hello World!

If a file has a larger content size, like

Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt voluptatum tenetur libero nulla esse veritatis 
accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam

The output will be: 

>>> C:\Users\Desktop\MyTestDir: read LoremIpsum.txt
    Lorem ipsum dolor sit amet consectetur adipisicing elit. Accusamus, sunt voluptatum tenetur libero nulla esse veritatis 
    accusantium earum commodi hic voluptatem officia culpa optio atque. Quaerat sed quibusdam ratione nam

.. py:exception:: UNICODE.characters.execeptionError()

    Raised when a file with binary characters/unicode characters is passed

.. py:exception:: isFolderError()

    Raised when target item is folder


.. _write:


16. write (write to a file)
---------------------------

The ``write`` command is used for editing a file. The default text editor is Notepad.

To use the ``write`` command, follow the given syntax

>>> C:\Users\Desktop\MyTestDir: write LoremIpsum.txt

On running this command File Bash launches the target file ``LoremIpsum.txt`` in Notepad. The few instances during and after running this command look like this:

.. image:: https://i.imgur.com/t9W27DC.png

.. image:: https://i.imgur.com/whDjZJE.png

.. image:: https://i.imgur.com/VDiqihG.png

.. image:: https://i.imgur.com/6cRB9qJ.png

One of the primary advantages of the ``write`` command is that it displays the additions and deletions made to a file.

.. py:exception:: IsDirectoryError()

    Raised when target is a Directory and not a file. The bash responds by saying ``It's a dir good sir :)``

If a non-existent file is targeted, File Bash prompts the user if he/she wants to create a file with that name, if not created, it returns a ``Failed to read file`` error and a ``Could not load file changes (file unexistent)`` error

.. _rmrf:

17. rm -rf (Delete a git repository)
------------------------------------

**This is a Git Software Command, but due to certain unspecifiable reasons, it is mentioned individually here**

The ``rm -rf`` command simply deletes the git repository, if the cwd is one

For details of this command, visit the Git Documentation at https://git-scm.com/doc

18. help (Use your brain)
-------------------------

Prints the help text. (what else do you expect it to do??)

19. Git and python commands (selective)
---------------------------------------

Supports 99% of the Git commands and 74% of the Python commands.


20. exit (Exits bash)
---------------------

Exits File Bash, my friend
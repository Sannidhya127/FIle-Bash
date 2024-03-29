Changelog
=========

Timestamps according to 24-hour clock system

v0.0.1-beta [15/04/2022 15:08]
------------------------------

- First setup of this Documentation. 
- The versioning will follow the semantic versioning of https://semver.org/.

v0.0.2-beta [15/04/2022 13:09]
------------------------------

- First developmental release inclusive of documentation. 
- The documentation is being developed with sphinx and is yet to be completed. 
- Contents added to documentation:
    - Switched to theme Furo  
    - The ls command and its parameters 
    - rm command and related references  

v0.0.3-beta [15/04/2022 18:10]
------------------------------

- Added new commands to commands page and a quickstart guide page for beginners.

v0.1.0 [16/04/2022 12:12 ]
--------------------------

- Transfered the complete documentation setup to a seperate folder with git repository initialisation for hosting the page on GitHub Pages.

v0.1.1 [16/04/2022 12:15]
-------------------------

- Brought back the docs as github pages failed to host the site for it not being fully static.
- Documentation will be accessed as a local file and not a website hosted on a server.

v0.1.2 [16/04/2022 17:17]
-------------------------

- Changed changelog.rst to update.rst and removed Changelog sub heading. It is now displayed as a link just like commands and quickstart pages.

- Added ``sys --info`` command to commands page. Details regarding GPU information missing and screenshots provided.

v0.1.3 [16/04/2022 18:18]
-------------------------

- Added several pages according to a pre-designed blueprint to the documentation. The pages are:
    - Some important functions used to code commands
    - API Reference
    - About 
    - Contribute
    - LISCENSE

- The pages only have their headings for now and the :doc:`functions` page has a small note item regarding its content. 

v0.1.4 [16/04/2022 18:47]
-------------------------

- Added a command named ``documentation`` which when entered opens the documentation in the default web browser

v0.2.0 [16/04/2022 20:15]
-------------------------

- Added LICENSE.md file containing the MIT License in repository

- Same text as in LICENSE is copied to :doc:`liscense` in documentation.

v.0.3.0 [17/04/2022 1:03]
-------------------------

- Added Code Of Conduct File in repo and also in documentation.
- Added details of File Bash in :doc:`about` section
- Added Code Of Conduct and mini guide for contribution in :doc:`contribute` section

v.0.4.0 [17/04/2022 12:13]
--------------------------

- Added ``license`` command that prints license document
- Added ``code of conduct`` command that prints the Code Of Conduct document
- fixed the closest match tracked for wrong command by adding all updated commands to its list
- Removed some unused functions

v0.5.1 [17/04/2022 20:21]
-------------------------

- Added ``sr`` command to :doc:`commands`
- Added ``delf`` command to :doc:`commands`
- Added ``deld`` command to :doc:`commands`
- Added the function used for all commands
- Removed API Reference page
- Added a page for the upcoming File Bash Project Testing system, Rooter

v0.5.2 [18/04/2022 22:21]
-------------------------

- Added ``deld`` command's remaining details

v0.5.3 [18/04/2022 19:24]
-------------------------

- Added ``bash --sys 0`` command
- Added ``process --uid`` command
- Added ``hide`` command
- Changed theme to **sphinx_rtd_theme**

v0.5.4 [20/04/2022 13:12]
-------------------------
- Adomnition to the Rooter page regarding its launch time.
- ``uhd`` (unhide) command added

v0.5.5 [21/04/2022 19:55]
-------------------------

- Added ``read`` command
- Added ``write`` command
- Fixed issue about the crashing of File Bash when directory name is given to ``write`` command
- Made a new API page cause some new plans are being cooked

v0.6.0 [22/04/2022 20:35]
-------------------------

- Added the first ever **API** of File Bash
- The api is framed over the ``rm`` command
- On running the api command, the rm command returns the ``item``, ``type``, ``version``, ``time`` and ``existence`` details of given item.

v0.6.1 [22/04/2022 21:32]
-------------------------

- Added ``rm api`` to API references page
- Changed api call attribute from ``-a -h --rm`` to ``-a -h`` for ``rm api``

v0.6.2 [23/04/2022 12:06]
-------------------------

- Added ``rm -rf`` command to docs
- Added ``help`` command to docs
- Added git and python commands reference
- Added ``exit`` command to docs

v0.6.3 [23/04/2022 20:29]
-------------------------

- Added ``creation time`` and ``modification time`` tracker to ``rm api``
- Framed rooter's first functionality
- Changed theme to ``python-docs``
- Changed documentation intro

v0.7.0 [25/04/2022 22:59]
-------------------------

- Started making the ``FullScan()`` function, for now it scans ``ls`` command
- Added logging to rooter for saving reports

v0.7.1 [27/04/2022 20:52]
-------------------------

- Added full scan fucntion in rooter with command ``rooter -sc 0``. The function is still under development
- Made ``crf api``
- Changed api call function to ``-GET``
- Updates API Documentation

v0.7.2 [02/05/2022 18:48]
-------------------------

- Added ``blockPrint()`` and ``enablePrint()`` functions to rooter to show or hide the function outputs during test run.
- Added  ``printImg()``, ``printMed()``, ``printAud()`` and ``Delete()`` functions to rooter. The ``Delete()`` function includes api check.
- Added ``cls`` command
- Implemented python's ``strip()`` function to get rid of the input commands unessessary whitespaces


v0.7.3 [07/05/2022 16:57]
-------------------------

- Added an **Acknowledgements** section in index
- Added an **Expected Upcoming Changes** section in index
- Added installation intructions in index for git clone and .zip file download
- Changed **About** page content
- Added an **About Author** page
- Added links for my projects in **About Author** page
- Added a new ``cp`` command for copy pasting items
- Added a **FAQs** section to answer some commonly asked questions
- Removed number bullet from **commands** page
- Added ``curt user`` command to **commands** page
- Added ``install --check`` command to **commands** page
- Added ``reload --colored`` command to **commands** page
- Added ``license`` command to **commands** page
- Added ``code of conduct`` command to **commands** page


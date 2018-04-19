IT105 Directions for Runestone Server
=======================================

.. image:: https://badge.waffle.io/RunestoneInteractive/RunestoneServer.png?label=ready&title=Ready
   :target: https://waffle.io/RunestoneInteractive/RunestoneServer
   :alt: 'Stories in Ready'

.. image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/bnmnetp/runestone
   :target: https://gitter.im/bnmnetp/runestone?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge


.. image:: http://bnmnetp.me:8088/buildStatus/icon?job=RunestoneServer
   :alt: Build Status

Installation
------------

#. Install python.

   First, make sure you have Python 2.7 installed.  Web2py has not yet been ported to Python3.  Even if you don't care about the web2py part of the install, the version of paverutils on pypi is still a Python 2.x package, although the development version is now at 3.x.

#. Install and make a Python virtualenv

   Note, development works well with a Python ``virtualenv``  If  you don't have root privileges on your computer I strongly recommend you install ``virtualenv`` and install all of the dependencies there.

   * Documentation here:  https://virtualenv.pypa.io/en/stable/
   * Video here:  https://www.youtube.com/watch?v=IX-v6yvGYFg
   * For the impatient:

     ::

        /home/USMAEDU/first.last: virtualenv it105Env
        /home/USMAEDU/first.last: cd it105Env
        /home/USMAEDU/first.last: source bin/activate

#. Install web2py. Make sure that you are in /home/USMAEDU/first.last/it105Env:

   :: 
   
      /home/USMAEDU/first.last/it105Env: git clone https://github.com/usma-eecs/web2py.git
      /home/USMAEDU/first.last/it105Env: cd web2py
      ###need to add in the other dependencies

#. Clone this repository **into the web2py/applications directory**. When you make the clone you should clone it into ``runestone`` rather than the default ``RunestoneServer``.  All the web2py stuff is configured assuming that the application will be called **runestone**.

   ::

       /home/USMAEDU/first.last/it105Env/web2py: cd applications
       /applications: git clone https://github.com/RunestoneInteractive/RunestoneServer  runestone
       /home/USMAEDU/first.last/it105Env/web2py/applications: cd runestone
       /home/USMAEDU/first.last/it105Env/web2py/applications/runestone: pip install -r requirements.txt

#. Set up your environmental variables to connect to the database. Make the changes in ``~/.bashrc``

   * The ``username`` and ``password`` are in a seperate secure file. Please see the IT105 Course Director for more information.

   ::

       export WEB2PY_CONFIG=production
       export WEB2PY_MIGRATE=Yes
       export DBURL=postgresql://username:pw@host/runestone
       export TEST_DBURL=postgresql://username:pw@host/runestone
       export DEV_DBURL=postgresql://username:pw@host/runestone

#. Use ``rsmanage`` for all additional requirements. You must be in an active virtualenv.

   * Build the book. In this example the book is for AY184. Each semester will be a difference github repo. The ``--skipclone`` writes over an older version of that book. 

   ::
   
      : rsmanage build --course AY184_IT105 --repo https://github.com/usma-eecs/AY184_IT105.git --skipclone

   * Restart the server. 
   
   ::
   
      /home/USMAEDU/first.last/it105Env/web2py/applications/runestone: rsmanage shutdown
      killing process 18415
      /home/USMAEDU/first.last/it105Env/web2py/applications/runestone: rsmanage run
      /home/USMAEDU/first.last/it105Env/web2py/applications/runestone: web2py Web Framework
      Created by Massimo Di Pierro, Copyright 2007-2018
      Version 2.16.1-stable+timestamp.2018.03.08.10.23.01
      Database drivers available: sqlite3, psycopg2, pymysql, imaplib

      please visit:
            http://127.0.0.1:8080/
      use "kill -SIGTERM 24477" to shutdown the web2py server


      starting scheduler for "runestone"...
      Currently running 1 scheduler processes
      Processes started


      
      


Documentation
-------------

See the Read Me in https://github.com/RunestoneInteractive/RunestoneServer. 

Browser Notes
-------------

Note, because this interactive edition makes use of lots of HTML 5 and Javascript
I highly recommend either Chrome, or Safari.  Firefox 6+ works too, but has
proven to be less reliable than the first two.  I have no idea whether this works
at all under later versions of Internet Explorer.

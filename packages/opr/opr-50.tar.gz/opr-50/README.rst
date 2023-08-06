README
######


**NAME**


``OPR`` - object programming runtime.


**SYNOPSIS**

::

 python3 -m opr [<cmd>|-c|-d] [key=value] [key==value]


**DESCRIPTION**


``opr`` is a python3 runtime, intended to be programmable, with a client
program (opr), it provides object persistence, an event handler and some
basic code to load modules that can provide additional functionality.

``opr`` uses object programming, object oriented programming without the
oriented. Object programming is programming where the methods are seperated
out into functions that use the object as the first argument of that funcion.
This gives base class definitions a clean namespace to inherit from and to load
json data into the object's __dict__. A clean namespace prevents a json loaded
attribute to overwrite any methods.

``opr`` stores it's data on disk where objects are time versioned and the
last version saved on disk is served to the user layer. Files are JSON dumps
and paths carry the type in the path name what makes reconstruction from
filename easier then reading type from the object.


**INSTALL**

to make typing more simpler use an alias::

 $ alias opr="python3 -m opr"

::

 $ sudo pip3 install opr --upgrade --force-reinstall

 (*) use remove and reinstall if ``opr`` doesn't work properly


**USAGE**

create a mod dir::

 $ mkdir mod

open the file mod/hello.py and add the following::

 def hello(event):
     event.reply("hello world!")

then run the following on the prompt::

 $ python3 -m opr hello
 hello world!


use the -c option if you want a console to run commands::

 $ python3 -m opr -c
 > hello
 hello world!

running ``opr`` in the background is done by using the ``-d`` option::

 $ python3 -m opr -d
 $


**PROGRAMMING**


The ``opr`` package provides an Object class, that mimics a dict while using
attribute access and provides a save/load to/from json files on disk.
Objects can be searched with database functions and uses read-only files
to improve persistence and a type in filename for reconstruction. Methods are
factored out into functions to have a clean namespace to read JSON data into.

basic usage is this::

 >>> from opr.objects import Object
 >>> o = Object()
 >>> o.key = "value"
 >>> o.key
 >>> 'value'

Objects try to mimic a dictionary while trying to be an object with normal
attribute access as well. hidden methods are provided, the methods are
factored out into functions like get, items, keys, register, set, update
and values.

great for giving objects peristence by having their state stored in files::

 >>> from opr.persist import Object, write
 >>> o = Object()
 >>> write(o)
 opr.objects.Object/89efa5fd7ad9497b96fdcb5f01477320/2022-11-21/17:20:12.221192


**AUTHOR**


B.H.J. Thate <thatebhj@gmail.com>


**COPYRIGHT**


``opr`` is placed in the Public Domain.

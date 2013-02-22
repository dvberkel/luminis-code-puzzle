Python Solution for Binary Look and Say
=======================================

This project aims to solve the [binary look-and-say puzzle][puzzle].
It uses [python][]

In order to run various programs make sure to include the current
directory in your `PYTHONPATH`. E.g

    export PYTHONPATH=.

Running Tests
-------------

To run all the test created for this project execute the following
command

    python conway/test/test_all.py 

Running Programs
----------------

Currently, the following programs are provided.

* *look-and-say* will perform one step of the look and say
   procedure. E.g `bin/look-and-say 112` will echo `2112`. Run
   `bin/look-and-say` to see how to use it.
* *look-and-say-term* will a particular term of the look and say
   sequence. E.g. `bin/look-and-say-term 3` will echo `21`. Run
   `bin/look-and-say-term` to see how to use it.

[puzzle]: https://github.com/dvberkel/luminis-code-puzzle/wiki/Binary-Look-and-Say
[python]: http://www.python.org/ "Official Website".
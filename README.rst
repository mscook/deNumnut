deNumnut
========

Suppose some numnuts provides incorrect specification when uploading reads to
the SRA. You download SRA toolkit and run fastq-extract and you still get
broken files... Never fear deNumnut is here!

*numnuts:* Numnuts or num-nuts is a slang term that is used to depict someone 
who is a constant source of trouble. Usually an individual who screws up, or 
constant makes mistakes. Someone who botches a job, event, or situation.


Overview
--------

Suppose you have 76 base read pairs and their stored in the SRA as a 101
and 51 bp read respectively. deNumnut will rescue the two 76 bp read pairs. 


Usage
-----

Something like this::

    $ cd DIRECTORY_WITH_SRA_FILES
    $ python denumnut.py 76


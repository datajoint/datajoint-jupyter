
=================
datajoint-jupyter
=================

Overview
========

This package provides `djwidgets`, a module providing utilities for
interacting with datajoint from jupyter notebook.

Currently, there is a simple text-based entry widget available as
the class DJRecord or via the utility function 'create' which will
add a single record to a DataJoint table using text enrty widgets.
The DJRecord class does not look up related foreign keys; these
must be entered correctly in order to prevent integrity errors
resulting from missing or incorrect foreign key data. Eventually,
it is hoped that a more full featured widget will also be provided
to assist in filling out these values automatically.

Installation
============

Installation is via the usual pip and setup.py methods::

    $ pip install -r requirements.txt
    $ python ./setup.py install

If you have not already configured jupyter notebook to use jupyter widgets
extension package, you'll also need to run the following:

    $ jupyter nbextension enable --py widgetsnbextension 

see also: https://ipywidgets.readthedocs.io/en/stable/user_install.html

Usage
=====

To use the package, simply pass a DataJoint table class to the 
provided 'create' function. For example::

    import datajoint as dj
    from djwidgets import create

    schema = dj.schema('demo', locals())

    @schema
    class Demo(dj.Manual):
        definition = '''
        demo_id: int  # demo id
        ---
        demo_desc: varchar(1024)  # demo description
        '''

    create(Demo)

defines the DataJoint table class 'Demo' and uses the djwidgets 'create'
function to interactively add a new Demo record.

A more illustrative example jupyter notebook session is provided
in the file 'djwidgets.ipynb' within the 'example' subdirectory of
the code repository.


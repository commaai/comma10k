# Pencil Tool

## Description

This tool makes editing the Comma10k corpus much easier. No fiddling with non-pixelic editors
for pixel "art" and an optimized GUI!

### Setup of the Tool

## *ALL*

The following isn't strictly required but is helpful for interacting with GitHub.

* `git` 
    * This allows you to use the commit functionality of the GUI.
* `hub` 
    * is less likely to be present and it isn't required 

Even if those tools are out of commission or aren't available, the image editing
functionality is fully available. 

## Linux and/or macOS

TODO: elaborate

In a Python environment, 

* `pip install -r requirements.txt`
* `python server.py`

## Windows

The above can be done in Windows as well if you have a Python environment.

### No Python Installation?

... but we understand not everyone is a Python programmer or knows how to setup an
environment for Python stuff.

For users without a pre-installed Python installation, there is a pre-compiled
server distribution that bundles dependencies such as Python and Flask.

Obtain a pre-compiled ZIP from the Artifacts of a recent "Pencil Tool Windows
Compile" run on GitHub Actions.

Extract the ZIP out to a folder called `dist`. Place it at
`comma10k\pencil\dist` where `comma10k` is the repository root on your local
machine. There should be a `server.exe` at
`comma10k\pencil\dist\server\server.exe`. Run the server by clicking on the
`launch_compiled_server.bat` in `comma10k\pencil\`.

You can then visit http://localhost:5000 .


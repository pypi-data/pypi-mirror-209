######
charex
######

`charex` is a Unicode and character set explorer for understanding
issues with character set translation and Unicode normalization.


Why Did I Make This?
====================
I find the ambiguity of text data interesting. In memory its all ones
and zeros. There is nothing inherent to the data that makes `0x20` mean
a space character, but we've mostly agreed that it does. That "mostly"
part is what's interesting to me, and where a lot of fun problems lie.


How Do I Use This?
==================
Right now, the best way to use it is to clone the repository. Then in
the root of the repository, run `charex` as a module.::

    python -m charex

That will bring you to the `charex` shell::

    Welcome to the charex shell.
    Press ? for a list of comands.
    
    charex>

From here you can type `?` to see the list of available commands::

    Welcome to the charex shell.
    Press ? for a list of comands.
    
    charex> ?
    The following commands are available:

    * cd: Decode the given address in all codecs.
    * ce: Encode the given character in all codecs.
    * cl: List registered character sets.
    * ct: Count denormalization results.
    * dm: Build a denormalization map.
    * dn: Perform denormalizations.
    * dt: Display details for a code point.
    * el: List the registered escape schemes.
    * es: Escape a string using the given scheme.
    * fl: List registered normalization forms.
    * help: Display command list.
    * nl: Perform normalizations.
    * sh: Run in an interactive shell.

    For help on individual commands, use "help {command}".

    charex>

And then type `help` then a name of one of the commands to learn what
it does::

    charex> help dn
    usage: charex dn [-h] [-m MAXDEPTH] [-n NUMBER] [-r] [-s SEED]
                     {nfc,nfd,nfkc,nfkd} base

    Denormalize a string.

    positional arguments:
      {nfc,nfd,nfkc,nfkd}   The Unicode normalization form for the
                            denormalization.
      base                  The base normalized string.

    options:
      -h, --help            show this help message and exit
      -m MAXDEPTH, --maxdepth MAXDEPTH
                            Maximum number of reverse normalizations to use for
                            each character.
      -n NUMBER, --number NUMBER
                            Maximum number of results to return.
      -r, --random          Randomize the denormalization.
      -s SEED, --seed SEED  Seed the randomized denormalization.

    charex>

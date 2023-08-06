# copyright-claim

This very simple python package allows to add or remove copyright/license claims at
the beginning of your  source files (single file use or whole folder use, the
files being filtered based on their extensions).

 Yes it has only two functions !


Yet, it also defines a terminal command that allows to call the add and remove functions.



## Installation
This package can be installed with pip as follows.

```
$ pip install copyright-claim
```

Most likely, you need not install this package in a virtual environment,
since its only dependencies are packages which are provided
in the standard library at least since version 3.7 of Python. 



## Documentation

A detailed documentation of this package is available on 
[GitHub Pages](https://completementgaga.github.io/copyright-claim/) --- as a website.

It is also available in pdf format
[here](https://github.com/completementgaga/copyright-claim/blob/master/sphinx/build/latex/copyright-claim.pdf).

For the command line version, if you used pip to install the package,

you can run 
```
$ copyright-claim -h
```
in your terminal and observe
```
usage: copyright_claim [-h] [--project_path PROJECT_PATH]
                       [--claim_path CLAIM_PATH] [-r] [--ext EXT]
                       [--comment_symbol COMMENT_SYMBOL]
                       [--start_string START_STRING] [--end_string END_STRING]
                       {add,remove,dummy}

Adds and removes copyright claims at the beginning of text files.

positional arguments:
  {add,remove,dummy}    Choose "add" if you want to add the claim, "remove" if
                        you want to remove it. The "dummy" option simply
                        outputs our dummy example of a copyright claim.

options:
  -h, --help            show this help message and exit
  --project_path PROJECT_PATH, -p PROJECT_PATH
                        The path to the file or directory to be treated. It is
                        a compulsory argument, unless the 'dummy' option is
                        being used
  --claim_path CLAIM_PATH, -c CLAIM_PATH
                        The path to the text of your copyright claim. In case
                        the add option is used, this argument is necessary.
                        Useless otherwise. For testing purposes you can use
                        the special value 'dummy' which allows to use our
                        dummy copyright claim.
  -r                    This flag must be used when treating a directory is
                        desired. In this case all the file within the
                        directory and its subdirectories will be affected,
                        provided they have the chosen extension.
  --ext EXT             The extension that characterizes the file(s) to be
                        treated. Defaults to ".py". When processing a single
                        file, this argument is ignored.
  --comment_symbol COMMENT_SYMBOL
                        The string to be used to comment out the lines of the
                        claim block. Defaults to '# '.
  --start_string START_STRING, -s START_STRING
                        The string that marks the beginning of the copyright
                        claim block. Defaults to "COPYRIGHT CLAIM".
  --end_string END_STRING, -e END_STRING
                        The string that marks the beginning of the copyright
                        claim block. Defaults to "END OF COPYRIGHT CLAIM".

```



## Further developments of the project

Feel free to open the discussion through issues and pull requests on the [GitHub repository](https://github.com/completementgaga/copyright-claim).

Feedback is also welcome by e-mail or by giving the project a star.
















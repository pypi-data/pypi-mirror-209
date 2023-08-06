# Copyright-claim - Add and remove copyright claims to your source code.
#
# (C) 2023 Gaël Cousin.
# You may use and distribute this program under the terms of the
# BSD-2-Clause License.
#
# Gaël Cousin can be contacted at gcousin333@gmail.com.

"""
--------------------------
The copyright_claim module
--------------------------

It has two functions add_claim and remove_claim that are wrapped together
by the third and last function main. This last one is called
when the file copyright_claim.py is executed by python and allows terminal
interaction with the module. Use the --help flag to get details on this 
terminal aspect.

The same script is made available through the terminal command::


    copyright-claim


upon installation of the package copyright-claim with pip.

"""

import argparse
import os
import pkgutil
import warnings

# The following will allow to reach the data within the package directory
# hopefully, whatever the installation scheme.
package_dir = os.path.dirname(pkgutil.resolve_name(__name__).__file__)
dummy_claim_path = os.path.join(package_dir, "dummy_copyright_claim.txt")


def add_claim(
    file_path: str,
    claim_path: str,
    comment_symbol: str = "# ",
    start_string: str = "COPYRIGHT CLAIM",
    end_string: str = "END OF COPYRIGHT CLAIM",
) -> None:
    """Add a copyright claim to a file.

    Args:
        file_path (str): The path to the file to be treated.
        claim_path (str): The path to a file containing the claim text
            string.
        start_string (str, optional): A string to mark the beginning of
            the copyright claim block. Defaults to "COPYRIGHT CLAIM".
        end_string (str, optional): A string to mark the beginning of
            the copyright claim block. Defaults to "END OF COPYRIGHT
            CLAIM".
        comment_symbol (str, optional): The symbol that marks comment
            lines in the treated files. Defaults to "# ".
    """

    with open(claim_path, "r") as claim_file:
        claim = claim_file.read()
    claim = "\n" + start_string + "\n\n" + claim + "\n\n" + end_string
    claim = claim.replace("\n", "\n" + comment_symbol)
    claim += "\n\n"

    with open(file_path, "r") as original:
        data = original.read()
    with open(file_path, "w") as modified:
        modified.write(claim + data)


def remove_claim(
    file_path: str,
    comment_symbol: str = "# ",
    start_string: str = "COPYRIGHT CLAIM",
    end_string: str = "END OF COPYRIGHT CLAIM",
):
    """Remove a copyright claim previously added by add_claim.

    Args:
        file_path (str): The path to the file to be treated.

        start_string (str, optional): The start_string used by add_claim
            when inserting the claim. Defaults to "COPYRIGHT CLAIM".
        end_string (str, optional):The end_string used by add_claim
            when inserting the claim. Defaults to "END OF COPYRIGHT CLAIM".
        comment_symbol (str, optional): The comment_symbol used by
            add_claim when inserting the claim. Defaults to "# ".

    """

    no_claim_block = (
        "The passed text file "
        + file_path
        + " does not contain a copyright claim "
        + "block as it would be built with passed start_string, "
        + "end_string and comment_symbol."
    )
    with open(file_path, "r") as original:
        lines = original.readlines()
    try:
        u = lines.index(comment_symbol + start_string + "\n")
        v = lines.index(comment_symbol + end_string + "\n")
    except:
        warnings.warn(no_claim_block)
        return None

    # Check the lines between indices u and v are all commented out.
    for i in range(u + 1, v):
        if lines[i][: len(comment_symbol)] != comment_symbol:
            warnings.warn(no_claim_block)
            return None

    # We also wish to remove the skiplines that were added before and after
    # the claim block, so that remove_claim cancels totally add_claim.
    # We take some precautions, in case the file would have been edited
    # after claim addition, by addition of white spaces or removal of skiplines
    # before and after the claim block.
    if u > 0 and lines[u - 1].replace(" ", "") == "\n":
        u -= 1
    if lines[v + 1].replace(" ", "") == "\n":
        v += 1
    lines = lines[:u] + lines[v + 1 :]

    with open(file_path, "w") as modified:
        modified.write("".join(lines))


def dummy():
    print(pkgutil.get_data(__name__, "dummy_copyright_claim.txt").decode())


def main():
    "Wraps everything to form a terminal command."
    # Argument parsing.
    parser = argparse.ArgumentParser(
        prog="copyright_claim",
        description="Adds and removes copyright claims at the beginning of text files.",
    )
    parser.add_argument(
        "mode",
        choices=["add", "remove", "dummy"],
        help='Choose "add" if you want to add the claim, "remove" if you '
        + 'want to remove it. The "dummy" option simply outputs our dummy '
        + "example of a copyright claim.",
    )
    parser.add_argument(
        "--project_path",
        "-p",
        help="The path to the file or directory to be "
        + "treated. It is a compulsory argument, unless the 'dummy' option "
        + "is being used",
    )
    parser.add_argument(
        "--claim_path",
        "-c",
        help="The path to the text of your copyright claim. In case the add"
        + " option is used, this argument is necessary. "
        + "Useless otherwise. For testing purposes you can use the special "
        + "value 'dummy' which allows to use our dummy copyright claim.",
    )

    parser.add_argument(
        "-r",
        action="store_true",
        help="This flag must be used when treating a directory is desired.\n"
        + "In this case all the file within the directory and its "
        + "subdirectories will be affected, provided they have the "
        + "chosen extension.",
    )
    parser.add_argument(
        "--ext",
        default=".py",
        help="The extension that characterizes the file(s) to be treated. "
        + 'Defaults to ".py".'
        + " When processing a single file, this argument is ignored.",
    )
    parser.add_argument(
        "--comment_symbol",
        help="The string to be used to comment out the lines of the claim block."
        + " Defaults to '# '.",
        default="# ",
    )
    parser.add_argument(
        "--start_string",
        "-s",
        help="The string that marks the beginning of "
        + ' the copyright claim block. Defaults to "COPYRIGHT CLAIM".',
    )
    parser.add_argument(
        "--end_string",
        "-e",
        help="The string that marks the beginning of the copyright claim block. "
        + 'Defaults to "END OF COPYRIGHT CLAIM".',
    )
    args = parser.parse_args()
    if args.mode == "dummy":
        dummy()
        return None
    if args.claim_path == "dummy":
        args.claim_path = dummy_claim_path
    my_last_args = [args.claim_path, args.comment_symbol]
    if args.mode == "remove":
        my_last_args.pop(0)
        chosen_function = remove_claim
    else:
        chosen_function = add_claim
        if args.claim_path is None:
            parser.error(
                "add requires --claim_path. " + "claim_path was not specified."
            )

    if not os.path.exists(args.project_path):
        parser.error("The specified project_path does not exist.")
    # End of argument parsing

    # ACTION!
    if os.path.isfile(args.project_path):
        chosen_function(args.project_path, *my_last_args)

    if os.path.isdir(args.project_path):
        if not args.r:
            parser.error(
                "The project path leads to a directory, "
                + "but the -r flag was not used."
            )
        else:
            for root, dir, files in os.walk(args.project_path):
                for name in files:
                    if os.path.splitext(name)[-1] == args.ext:
                        file_path = os.path.join(root, name)
                        chosen_function(file_path, *my_last_args)


if __name__ == "__main__":
    main()

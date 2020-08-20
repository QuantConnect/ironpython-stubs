import sys
import os
import json

from ironstubs.utils.docopt import docopt
from stubsGenerator import generator

__version__ = '1.0.0'
__doc__ = """
    IronPython-Stubs | {version}

    IronPython Stubs Generator

    Usage:
      stubsGenerator [options]

    Examples:
      python -m  ironstubs RhinoCommon --overwrite

    Options:
        --path=<dir>            full stub path to process [default: ]
        --keep-partial          [default: False].
        --partition             split big file [default: False]
        --size-limit            split big file [default: 1048576]
        -h, --help              Show this screen.

    """.format(out_dir='stubs', version=__version__)

arguments = docopt(__doc__, version=__version__)

# OPTIONS
option_path_dir = arguments['--path']
option_keep_partial = not arguments['--keep-partial']
option_partition = arguments['--partition']
option_size_limit = int(arguments['--size-limit'])

generator.generate(rootdir=option_path_dir, keep_partial=option_keep_partial, partition=option_partition, size_limit=option_size_limit)

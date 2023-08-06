"""A library that provides a widgets for selecting things from the filesystem."""

######################################################################
# Main app information.
__author__     = "Dave Pearson"
__copyright__  = "Copyright 2023, Dave Pearson"
__credits__    = [ "Dave Pearson" ]
__maintainer__ = "Dave Pearson"
__email__      = "davep@davep.org"
__version__    = "0.0.3"
__licence__    = "MIT"

##############################################################################
# Local imports.
from .file_open    import FileOpen
from .path_filters import Filters

##############################################################################
# Export the imports.
__all__ = [ "FileOpen", "Filters" ]

### __init__.py ends here

#!/usr/bin/python3
"""
Script to copy the generated libraries to the libs/ directory

"""

import os
import sys
import shutil
import subprocess

#------------------------------------------------------------------------------
# Make sure the environment is properly set
NQBP_BIN = os.environ.get('NQBP_BIN')
if ( NQBP_BIN == None ):
    sys.exit( "ERROR: The environment variable NQBP_BIN is not set!" )
sys.path.append( NQBP_BIN )

# Find the Package & Workspace root
from nqbplib import utils
from nqbplib import my_globals
utils.set_pkg_and_wrkspace_roots(__file__)


#------------------------------------------------------------------------------
# MAIN ENTRY POINT....
#
utils.set_verbose_mode( True )
prjdir          = os.path.dirname(os.path.abspath(__file__))
srcpath         = os.path.join( prjdir, 'src', 'Catch', 'precompiled' )
dstpath_release = os.path.join( my_globals.NQBP_PKG_ROOT(), 'libs', 'x86', 'windows', 'vc14', 'cpp11', '32bit', "release" )
dstpath_debug   = os.path.join( my_globals.NQBP_PKG_ROOT(), 'libs', 'x86', 'windows', 'vc14', 'cpp11', '32bit', "debug" )

                 
#
# Build non-debug version
#
err, msg = utils.run_shell2( "nqbp.py -t", True )
if ( err != 0 ):
    sys.exit( "ERROR: Release build failed.")
print( "Copying: {} TO\n         {}".format( srcpath, dstpath_release ) )
shutil.rmtree( dstpath_release, True );
shutil.copytree(srcpath,dstpath_release)


# 
# Build debug version
#
err, msg = utils.run_shell2( "nqbp.py -gt", True )
if ( err != 0 ):
    sys.exit( "ERROR: Release build failed.")
print( "Copying: {} TO\n         {}".format( srcpath, dstpath_debug ) )
shutil.rmtree( dstpath_debug, True );
shutil.copytree(srcpath,dstpath_debug)

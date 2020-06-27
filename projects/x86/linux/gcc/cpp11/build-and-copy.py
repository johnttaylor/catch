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

#
# 32 Bit versions
#
dstpath_release = os.path.join( my_globals.NQBP_PKG_ROOT(), 'src', 'Catch', 'libs', 'x86', 'linux', 'gcc', 'cpp11', '32bit', "release" )
dstpath_debug   = os.path.join( my_globals.NQBP_PKG_ROOT(), 'src', 'Catch', 'libs', 'x86', 'linux', 'gcc', 'cpp11', '32bit', "debug" )

                 
#
# Build non-debug version
#
err, msg = utils.run_shell2( "nqbp.py -tb posix", True )
if ( err != 0 ):
    sys.exit( "ERROR: Release build failed.")
print( "Copying: {} TO\n         {}".format( srcpath, dstpath_release ) )
shutil.rmtree( dstpath_release, True )
# HACK: For some reason copytree fails with permission error -->but the copy actually occurred!!!! Probably a WSL/Python thingy
try:
    shutil.copytree(srcpath,dstpath_release)
except:
    pass


# 
# Build debug version
#
err, msg = utils.run_shell2( "nqbp.py -gtb posix", True )
if ( err != 0 ):
    sys.exit( "ERROR: Release build failed.")
print( "Copying: {} TO\n         {}".format( srcpath, dstpath_debug ) )
shutil.rmtree( dstpath_debug, True );
# HACK: For some reason copytree fails with permission error -->but the copy actually occurred!!!! Probably a WSL/Python thingy
try:
    shutil.copytree(srcpath,dstpath_debug)
except:
    pass


#
# 64 Bit versions
#
dstpath_release = os.path.join( my_globals.NQBP_PKG_ROOT(), 'src', 'Catch', 'libs', 'x86', 'linux', 'gcc', 'cpp11', '64bit', "release" )
dstpath_debug   = os.path.join( my_globals.NQBP_PKG_ROOT(), 'src', 'Catch', 'libs', 'x86', 'linux', 'gcc', 'cpp11', '64bit', "debug" )
                 
#
# Build non-debug version
#
err, msg = utils.run_shell2( "nqbp.py -tb posix64", True )
if ( err != 0 ):
    sys.exit( "ERROR: Release build failed.")
print( "Copying: {} TO\n         {}".format( srcpath, dstpath_release ) )
shutil.rmtree( dstpath_release, True )
# HACK: For some reason copytree fails with permission error -->but the copy actually occurred!!!! Probably a WSL/Python thingy
try:
    shutil.copytree(srcpath,dstpath_release)
except:
    pass


# 
# Build debug version
#
err, msg = utils.run_shell2( "nqbp.py -gtb posix64", True )
if ( err != 0 ):
    sys.exit( "ERROR: Release build failed.")
print( "Copying: {} TO\n         {}".format( srcpath, dstpath_debug ) )
shutil.rmtree( dstpath_debug, True )
# HACK: For some reason copytree fails with permission error -->but the copy actually occurred!!!! Probably a WSL/Python thingy
try:
    shutil.copytree(srcpath,dstpath_debug)
except:
    pass


# <nl > Below, I have fleshed it out with a more useable Flock class.  The

# code below works like this: You create an instance of the class,

# providing a filename. It will create/access the file in a default way

# and provide an hfile filehandle.  If you don't want the

# default(shared/blocking), you can then specify in a dictionary what

# type of locking you want.  Call the lock method on the file. Do

# whatever you want with the hfile filehandle, then call the unlock

# method which will remove the locks and close the filehandle.


# Looking at the code below, for desiredAccess and shareMode, I have

# both read and write on for most flexibility. The OPEN_ALWAYS means

# that it will either use the current file or create a new one if none

# is to be found. I use default security for the security attributes

# option. The lock method basically determines what lock flags should be

# used, depending on the type of locking you want and then calls

# LockFileEx. An interesting option to LockFileEx is self.highbits.  You

# can use that to specify portions of a file to lock instead of the

# entire thing. When you're done with whatever you need to do, using the

# hfile, filehandle, if necessary, then call the unlock method, to

# remove the lock and close the filehandle.


# <nl > Now for some code|

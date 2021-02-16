import win32file

import win32con

import win32security

import win32api

import pywintypes


highbits = 0xffff0000  # high-order 32 bits of byte range to lock

file = "History.txt"

secur_att = win32security.SECURITY_ATTRIBUTES()

secur_att.Initialize()


hfile = win32file.CreateFile(file,

                             win32con.GENERIC_READ | win32con.GENERIC_WRITE,

                             win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,

                             secur_att,

                             win32con.OPEN_ALWAYS,

                             win32con.FILE_ATTRIBUTE_NORMAL, 0)


ov = pywintypes.OVERLAPPED()  # used to indicate starting region to lock

win32file.LockFileEx(hfile, win32con.LOCKFILE_EXCLUSIVE_LOCK, 0, highbits, ov)

win32api.Sleep(4000)  # do something here

win32file.UnlockFileEx(hfile, 0, highbits, ov)

hfile.Close()


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


class Flock:

    def __init__(self, file):

        self.file = file

        self.type = {'LOCK_EX': 0, 'LOCK_NB': 0}

        secur_att = win32security.SECURITY_ATTRIBUTES()

        secur_att.Initialize()

        self.highbits = 0xffff0000  # high-order 32 bits of byte range to lock

        # make a handel with read/write and open or create if doesn't exist

        self.hfile = win32file.CreateFile(self.file,

                                          win32con.GENERIC_READ | win32con.GENERIC_WRITE,

                                          win32con.FILE_SHARE_READ | win32con.FILE_SHARE_WRITE,

                                          secur_att,

                                          win32con.OPEN_ALWAYS,

                                          win32con.FILE_ATTRIBUTE_NORMAL, 0)

    def lock(self):

        if self.type['LOCK_EX']:  # exclusive locking

            if self.type['LOCK_NB']:  # don't wait, non-blocking

                lock_flags = win32con.LOCKFILE_EXCLUSIVE_LOCK | win32con.LOCKFILE_FAIL_IMMEDIATELY

            else:  # wait for lock to free

                lock_flags = win32con.LOCKFILE_EXCLUSIVE_LOCK

        else:  # shared locking

            if self.type['LOCK_NB']:  # don't wait, non-blocking

                lock_flags = win32con.LOCKFILE_FAIL_IMMEDIATELY

            else:  # shared lock wait for lock to free

                lock_flags = 0

        self.ov = pywintypes.OVERLAPPED()  # used to indicate starting region to lock

        win32file.LockFileEx(self.hfile, lock_flags, 0, self.highbits, self.ov)

    def unlock(self):

        win32file.UnlockFileEx(
            self.hfile, 0, self.highbits, self.ov)  # remove locks

        self.hfile.Close()


l = Flock("History.txt")

l.type['LOCK_EX'] = 0

l.type['LOCK_NB'] = 0


print('calling lock')

l.lock()

print('now locked ')


win32api.Sleep(1000)

l.unlock()

print('now unlocked')

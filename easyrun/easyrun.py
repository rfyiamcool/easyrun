#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import subprocess
import time
import os
import signal
import tempfile

class Result(object):
    def __init__(self, command=None, retcode=None, output=None):
        self.command = command or ''
        self.retcode = retcode
        import tempfile
        self.output = output
        self.success = False
        if retcode == 0:
            self.success = True

class AsyncResult(object):
    def __init__(self, fd=None, output=None):
        fd.stdout.readline() 

class TimeoutError(Exception):
    pass

def run(command):
    process = subprocess.Popen(command, shell=True)
    process.communicate()
    return Result(command=command, retcode=process.returncode)

def run_async(command):
    PIPE = subprocess.PIPE
    pipe = subprocess.Popen(cmd , shell=True, stdin=PIPE, stdout=PIPE,stderr=subprocess.STDOUT, close_fds=True) 
    return Result(fd=pipe)

def run_stream(command):
    name = tempfile.NamedTemporaryFile(mode='w+b')
    name = tempfile.TemporaryFile()
    process = subprocess.Popen(command, stdout=name, stderr=proc.STDOUT, close_fds=True,shell=True)
    time.sleep(0.1)
    name.seek(0)
    while True:
        time.sleep(0.1)
        ret = process.poll()
        name.seek(0)
        yield name.read()
        if (ret is not None):
            print 'exit'
            break
    

def run_timeout(command,timeout=10):
    process = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, shell=True)
    t_beginning = time.time()
    seconds_passed = 0
    while True:
        if process.poll() is not None:
            break
        seconds_passed = time.time() - t_beginning
        if timeout and seconds_passed > timeout:
            process.terminate()
        time.sleep(0.1)
    output, _ = process.communicate()
    return Result(command=command, retcode=process.returncode,output=output)

def run_capture(command):
    outpipe = subprocess.PIPE
    errpipe = subprocess.STDOUT
    process = subprocess.Popen(command, shell=True, stdout=outpipe,
                                                    stderr=errpipe)
    output, _ = process.communicate()
    return Result(command=command, retcode=process.returncode, output=output)


def run_capture_limited(command, maxlines=20000):

    import collections
    import threading

    lines = collections.deque(maxlen=maxlines)
    def reader_thread(stream, lock):
        for line in stream:
            lines.append(line)

    outpipe = subprocess.PIPE
    errpipe = subprocess.STDOUT
    process = subprocess.Popen(command, shell=True, stdout=outpipe,
                                                    stderr=errpipe)
    lock = threading.Lock()
    thread = threading.Thread(target=reader_thread, args=(process.stdout, lock))
    thread.start()


    process.wait()
    thread.join()

    return Result(command=command, retcode=process.returncode, output=''.join(lines))

def run_killpid(pid):
    os.kill(pid, signal.SIGTERM)

if __name__ == '__main__':
    print('---[ .success ]---')
    print(run('ls').success)
    print(run('dir').success)

    print('---[ .retcode ]---')
    print(run('ls').retcode)
    print(run('dir').retcode)

    print('---[ capture ]---')
    print(len(run_capture('ls').output))
    print(len(run_capture('dir').output))

    print('---[ limited capture ]---')
    print(run_capture_limited('ls', maxlines=2).output)
    print(run_capture_limited('dir', maxlines=2).output)

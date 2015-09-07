#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import subprocess

class Result(object):
    def __init__(self, command=None, retcode=None, output=None):
        self.command = command or ''
        self.retcode = retcode
        self.output = output
        self.success = False
        if retcode == 0:
            self.success = True


def run(command):
    process = subprocess.Popen(command, shell=True)
    process.communicate()
    return Result(command=command, retcode=process.returncode)

# To Do list
def run_async(command):
    pass

def run_stream(command):
    pass
#end

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

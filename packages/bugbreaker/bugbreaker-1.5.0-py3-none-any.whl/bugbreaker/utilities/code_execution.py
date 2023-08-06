import os
from queue import Queue
from subprocess import PIPE, Popen
from threading import Thread
from bugbreaker.utilities.parsers import get_commands, get_error


def read(pipe, funcs):
    for line in iter(pipe.readline, b''):
        for func in funcs:
            func(line.decode('utf-8'))

    pipe.close()


def write(get):
    print()
    for line in iter(get, None):
        line = line.replace('\n', '')
        print(f'\033[37m{line}\033[0m')


def execute_code(args, language):
    command = get_commands(args, language)
    process = Popen(
        command,
        cwd=None,
        shell=False,
        close_fds=True,
        stdout=PIPE,
        stderr=PIPE,
        bufsize=-1
    )

    output, errors = [], []
    pipe_queue = Queue()

    stdout_thread = Thread(target=read, args=(
        process.stdout, [pipe_queue.put, output.append]))
    stderr_thread = Thread(target=read, args=(
        process.stderr, [pipe_queue.put, errors.append]))

    writer_thread = Thread(target=write, args=(pipe_queue.get,))

    for thread in (stdout_thread, stderr_thread, writer_thread):
        thread.daemon = True
        thread.start()

    process.wait()

    for thread in (stdout_thread, stderr_thread):
        thread.join()

    pipe_queue.put(None)

    errors = ''.join(errors)
    # print(errors)

    if 'java' != command[0] and not os.path.isfile(command[1]):
        return None

    return get_error(errors, language)

import re


def get_language(args):
    file_path = args[1].lower()
    if file_path.endswith('.py'):
        return 'python3'
    elif file_path.endswith('.js'):
        return 'node'
    elif file_path.endswith(".go"):
        return "go run"
    elif file_path.endswith(".rb"):
        return "ruby"
    elif file_path.endswith('.java'):
        return 'javac'
    elif file_path.endswith('.class'):
        return 'java'
    else:
        return ''  # language not recognized


def get_commands(args, language):
    fp_and_args = args[1:]
    if language == 'java':
        fp_and_args = [arg.replace('.class', '') for arg in fp_and_args]
    return [language] + fp_and_args


def get_error(error, language):
    if error == '' or not error:
        return None
    elif language == 'python3':
        if any(e in error for e in ['SystemExit', 'KeyboardInterrupt', 'GeneratorExit']):
            return None
        else:
            return error.split('\n')[-2].strip()
    elif language == 'node':
        return error.split('\n')[4][1:]
    elif language == 'go run':
        return error.split('\n')[1].split(": ", 1)[1][1:]
    elif language == "ruby":
        error_message = error.split('\n')[0]
        return error_message[error_message.rfind(": ") + 2:]
    elif language == 'javac':
        m = re.search(r'.*error:(.*)', error.split('\n')[0])
        return m.group(1) if m else None
    elif language == 'java':
        for line in error.split('\n'):
            m = re.search(r'.*(Exception|Error):(.*)', line)
            if m and m.group(2):
                return m.group(2)
            m = re.search(r'Exception in thread ".*" (.*)', line)
            if m and m.group(1):
                return m.group(1)
        return None

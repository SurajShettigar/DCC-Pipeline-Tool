import glob

import six

if six.PY2:
    from pathlib2 import Path


def getFiles(base_path, extensions):
    # clean base path
    if str(base_path).endswith('/') or str(base_path).endswith('\\'):
        base_path = str(base_path)[:-1]
    # clean extensions
    for i in range(len(extensions)):
        if extensions[i].startswith('.'):
            extensions[i] = extensions[i][1:]

    # find files of given extension
    found_files = []

    for e in extensions:
        if six.PY2:
            for path in Path(base_path).rglob('*.{}'.format(e)):
                found_files.append(str(path.absolute()))
        else:
            pattern = base_path + '/**/*.' + e
            found_files.extend(glob.glob(pattern, recursive=True))

    return found_files


if __name__ == '__main__':
    print(getFiles('D:/Personal_Work/PIPELINE/MOVIE/ASSETS/', ['.ma', '.mb']))

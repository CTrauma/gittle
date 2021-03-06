import os
from functools import partial

from gittle import Gittle

BASE_DIR = '/Users/aaron/git/'
absbase = partial(os.path.join, BASE_DIR)

TRIES = 1
PATHS = map(absbase, [
    'gittle/',
    'loadfire/',
])


def paths_exists(repo):
    tracked_files = repo.tracked_files

    return all([
        os.path.exists(path)
        for path in [
            repo.abspath(repopath)
            for repopath in tracked_files
        ]
    ])


def changed_entires(repo):
    return repo._changed_entries()

TESTS = (
    paths_exists,
    changed_entires,
)


def test_repo(repo_path):
    repo = Gittle(repo_path)
    return all([
        test(repo)
        for test in TESTS
    ])


def main():
    paths = PATHS * TRIES
    for path in paths:
        print('Testing : %s' % path)
        test_repo(path)


if __name__ == '__main__':
    main()

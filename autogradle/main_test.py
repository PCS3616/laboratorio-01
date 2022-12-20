from pathlib import Path

from sign import verify

submission_path = Path("./submission")

def test_2_1():
    file = submission_path / '2_1.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        assert(content.startswith("/home/ubuntu"))

def test_2_2():
    file = submission_path / '2_2.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        assert(content == "/home/ubuntu")

def test_2_3():
    file = submission_path / '2_3.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        assert(content == "mkdir: cannot create directory ‘/tmp’: File exists")

def test_2_4():
    file = submission_path / '2_4.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        files = content.split('\n')

        assert('Desktop' in files)

def test_2_5():
    file = submission_path / '2_5.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        files = content.split('\n')

        assert('bin' in files)
        assert('tmp' in files)
        assert('dev' in files)


def test_2_6():
    file = submission_path / '2_6.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        files = content.split('\n')

        assert('.bashrc' in files)
        assert('.bash_history' in files)

def test_2_7():
    file = submission_path / '2_7.out'
    assert(file.exists())

    with open(file) as fp:
        content = fp.read().strip()
        assert(content == "/root")

def test_desafio():
    file = submission_path / 'clmystery.sh'

    with open(file) as fp:
        lines = fp.readlines()

    assert(len(lines) > 5)

    assasino = lines[-1].strip()

    assert(
        verify(assasino, 'segunda') \
        or verify(assasino, 'segunda')
   )

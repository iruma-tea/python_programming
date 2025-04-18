import tarfile

with tarfile.open('test.tar.gz', 'w:gz') as tr:
    tr.add('test_dir')

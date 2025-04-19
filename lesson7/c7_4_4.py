import tempfile

with tempfile.TemporaryDirectory() as td:
    print(td)

temp_dir = tempfile.mkdtemp()
print(temp_dir)

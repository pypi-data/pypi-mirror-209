import importlib.resources as pkg_resources
import qnpy

# https://stackoverflow.com/questions/6028000/how-to-read-a-static-file-from-inside-a-python-package
inp_file = (pkg_resources.files(qnpy) / 'data.json')
with inp_file.open("rt") as f:
    file_contents = f.read()
    print(file_contents)


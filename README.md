# PArgs

Testing argsparse

## Develop

```
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -e .
```

## Build

### pip

```
python3 -m build
py -m pip install .
```

### Debian Package

```
python3 -m build
mv dist/pargs-<version>.tar.gz debian/pargs_<version>.orig.tar.gz
cd debian
tar -xvf pargs_<version>.orig.tar.gz
cd pargs-<version>.tar.gz
debmake
debuild -us -uc
```

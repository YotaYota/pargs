# PArgs

Testing argsparse

## Develop

```
python3 -m venv ../.venv-pargs
. .venv/bin/activate
python3 -m pip install -e .
```

## Build with pip

```
python3 -m build
py -m pip install .
```

## Build Debian Package

Using pbuilder, first need to create a _base.tar.gz_ file, if not already exist

```
sudo pbuilder create --distribution sid --mirror http://ftp.us.debian.org/debian/ --debootstrapopts "--keyring=/usr/share/keyrings/debian-archive-keyring.gpg"
```

update with

```
pbuilder update
```

build packet with

```
python3 -m build
cd dist
mv pargs-<version>.tar.gz pargs_<version>.orig.tar.gz
tar -xvf pargs_<version>.orig.tar.gz
pdebuild
```

Note: `debmake` is good for creating sensible template files.

## Build with git-buildpackage

```
sudo apt install git-buildpackage
```

```
git switch debian
gbp buildpackage
```

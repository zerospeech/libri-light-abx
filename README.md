# LibriLight ABX

This is a wrapper module around the abx implementation found in [libri-light/eval](https://github.com/facebookresearch/libri-light/tree/main/eval).
This module only adds a wrapper function to directly call abx evaluation and a dataclass object annotating all arguments as well as a setup.py to allow installation
as a module.


# Building Package

For security & compatibility reasons build is required to happen in a docker using manylinux1 as build target.

To do this

```shell
> docker pull quay.io/pypa/manylinux2014_x86_64
>  docker run --rm -v `pwd`:/io quay.io/pypa/manylinux2014_x86_64 bash /io/build_wheel.sh
```

This allows to populate with compiled versions of libriabx for python3.7, python3.8, python3.9, python3.10
The package can then be uploaded to pypi as normally

[ManyLinux Implementation](https://github.com/pypa/manylinux)
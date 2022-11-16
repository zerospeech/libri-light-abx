# Compile wheels
declare -a PyVersions=( 'cp38-cp38' 'cp39-cp39' 'cp310-cp310' 'cp311-cp311')
rm -rf /io/dist/*

for PYVER in "${PyVersions[@]}"; do
  PYBIN="/opt/python/${PYVER}/bin"
  rm -rf /io/build/
  "${PYBIN}/pip" install -U setuptools build numpy "setuptools_scm[toml]" cython
  "${PYBIN}/python" -m build /io/
done

# Bundle external shared libraries into the wheels
for whl in /io/dist/*.whl; do
    auditwheel repair "$whl" -w /io/dist/
done

# Install packages and test
#for PYVER in ${PyVersions[@]}; do
#  PYBIN="/opt/python/${PYVER}/bin"
#  "${PYBIN}/pip" install zerospeech-libriabx -f /io/dist/
#done

# remove all linux_x86_64 flagged binary wheels
find /io/dist/ -name "*linux_x86_64.whl" -type f -delete
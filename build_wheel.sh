# Compile wheels
declare -a PyVersions=( 'cp39-cp39' )

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

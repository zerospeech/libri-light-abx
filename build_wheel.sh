# Compile wheels
for PYBIN in /opt/python/cp{37,38,39,310}*/bin; do
    rm -rf /io/build/
    "${PYBIN}/pip" install -U setuptools build numpy "setuptools_scm[toml]" cython numpy
    "${PYBIN}/python" -m build
done

# Bundle external shared libraries into the wheels
for whl in /io/dist/*{cp37,cp38,cp39,cp310}*.whl; do
    auditwheel repair "$whl" -w /io/dist/
done

# Install packages and test
for PYBIN in /opt/python/cp{37,38,39,310}*/bin; do
    "${PYBIN}/pip" install zerospeech-libriabx -f /io/dist/
done

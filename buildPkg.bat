if exist "%~dp0dist\" (
    cd dist
    del /f resf-*
    cd ..
)
py setup.py sdist bdist_wheel

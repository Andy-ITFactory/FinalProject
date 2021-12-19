pip install -U selenium
pip install behave
pip install behave-html-formatter

run test
behave -f html -o behave-report.html --tags=smoke
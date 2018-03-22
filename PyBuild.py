from subprocess import run
print(run("pip install pytest"))
print(run("pip install pytest-cov"))
print(run("pip install doctest2"))
print(run("pip install -r requirements.txt"))
print(run("python -m pytest --junitxml=pytestresults.xml --cov-report=xml --cov-report=html"))
print(run("python -m pytest  --junitxml=doctestresultsmod.xml --doctest-modules --doctest-report udiff"))
print(run("python -m pytest  --junitxml=doctestresultstxt.xml --doctest-modules --doctest-report udiff"))



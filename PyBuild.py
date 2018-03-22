!pip install pytest
!pip install pytest-cov
!pip install doctest2
!pip install -r requirements.txt
!python -m pytest --junitxml=pytestresults.xml --cov-report=xml --cov-report=html
!python -m pytest  --junitxml=doctestresultsmod.xml --doctest-modules --doctest-report udiff
!python -m pytest  --junitxml=doctestresultstxt.xml --doctest-modules --doctest-report udiff
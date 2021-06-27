# ***topography*** package distribution

:warning: ***Make sure to increment `V = f"{release}.{feature}.{update}"` in __setup.py__*** :warning:

1. Building the distribution

```shell
python setup.py sdist bdist_wheel
```

2. Uploading to ***testpypi***

```shell
twine upload -r testpypi dist/* -u <$username> -p <$password>
```

3. Uploading to ***pypi***
```shell
twine upload -r pypi dist/* -u <$username> -p <$password>
```

# Setup

- open the colab file here [sample notebook](https://colab.research.google.com/drive/1HQ_0KRGTe37YGH7wT7va_d_ds3etVSln#scrollTo=TZ7bAT_JX7Ad)

- click on `changes will not be saved on the right side of tabs`

- click on save a copy in drive, then you will get a fork of the notebook


# usage of converter cli

- install dependencies
```
pipenv install --skip-lock
```

- run virtualenv
```
pipenv shell

```

- show cli info
```
pipenv run python converter.py --help

```

- run cli, by default convert the input file to csv
```
pipenv run python converter.py --textgrid_file TG_00301.TextGrid --sample_rate 10
```

- also can convert to pickle or json, the file extension will be added automaticlly
```
pipenv run python converter.py --textgrid_file TG_00301.TextGrid --sample_rate 10 --output_type json --export_path output
```




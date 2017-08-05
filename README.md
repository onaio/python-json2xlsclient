[![python-json2xlsclient travis](https://secure.travis-ci.org/onaio/python-json2xlsclient.png?branch=master)](http://travis-ci.org/onaio/python-json2xlsclient)

Python bindings to the [json-to-xls][1] API
===========================================

This repo contains the sources for the json-to-xls API. The json-to-xls
service generates XLS files from XLS templates given valid JSON datasets.
You can read more about that [here][1]

#### Installation

`pip install git+https://github.com/onaio/python-json2xlsclient.git`
OR as a [pip editable](http://pip.readthedocs.org/en/latest/reference/pip_install.html#editable-installs) if you'd like to develop this in parallel with your project:-
`pip install -e git://github.com/onaio/python-json2xlsclient.git#egg=j2xclient`


#### Sample Usage

***Initialization***

```python
from json2xlsclient.client import Client
client = Client('http://json-2-xls.endpoint/')
```

***Working with templates***

```python
# Create template
template_token = client.template.create('/path/to/template.xls')

# Get existing template
template = client.template.get(template_token)

# Update template
template_token = client.template.update(template, '/path/to/template.xls')
```

***Working with excel sheets***

```python
# Generate spreadsheet
url_path_only_to_spreadsheet = client.xls.create(template_token, json_data)

# Download existing spreadsheet
spreadsheet_data = client.xls.get(xls_token)
```

#### Contributing

- [Fork and] create a branch named according to the feature you want to work on
- Clone your new repo & cCreate a virtualenv for that
- Install deps: `pip install -r dev-requiremets`
- Setup the pre-commit Hook: `ln -s ../../pre-commit.sh .git/hooks/pre-commit`
- Contribute/Develop/Hack
- Send a pull request against the [master][2] branch


[1]: https://github.com/onaio/json-to-xls
[2]: https://github.com/onaio/python-json2xlsclient/tree/master

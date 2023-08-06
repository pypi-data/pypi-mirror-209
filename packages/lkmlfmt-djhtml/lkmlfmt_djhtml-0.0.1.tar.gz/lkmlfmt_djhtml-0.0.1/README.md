# lkmlfmt-djhtml
A plugin for [lkmlfmt](https://github.com/kitta65/lkmlfmt).

## Installation

```sh
pip install lkmlfmt lkmlfmt-djhtml
```

## CLI

```sh
lkmlfmt --plugin lkmlfmt_djhtml
```

## API

```python
from lkmlfmt import fmt

lkml = fmt("""\
view: view_name {
  dimension: column_name {
    html:
{% if value == "foo" %}
<img src="https://example.com/foo"/>
{% else %}
<img src="https://example.com/bar"/>
{% endif %} ;;
  }
}
""", plugins=["lkmlfmt_djhtml"])

assert lkml == """\
view: view_name {
  dimension: column_name {
    html:
      {% if value == "foo" %}
        <img src="https://example.com/foo"/>
      {% else %}
        <img src="https://example.com/bar"/>
      {% endif %}
    ;;
  }
}
"""
```

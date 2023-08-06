import re
from typing import Any

from djhtml.lines import Line  # type: ignore
from djhtml.modes import DjHTML  # type: ignore

LIQUID_MARKER = "{{% set LKMLFMT_MARKER = {} %}}"
TEMPLATE = re.compile(
    r"""(?P<tag>\{%-?\s*(?P<type>#|([a-z]*))([^"'}]*|'[^']*?'|"[^"]*?")*?-?%\})"""
    + r"""|(?P<obj>\{\{([^"'}]*|'[^']*?'|"[^"]*?")*?\}\})"""
    + r"""|(?P<looker>(\$|@)\{[^}]*?\})""",
)


def to_jinja(liquid: str) -> tuple[str, list[str], list[str]]:
    jinja = ""
    templates = []
    dummies = []
    id_ = 0
    skip_to: str | None = None

    while True:
        match = TEMPLATE.search(liquid)
        if match is None:
            jinja += liquid
            break

        type_ = match.group("type")
        if skip_to is not None and skip_to != type_:
            jinja += liquid[: match.end()]
            templates.append(match.group(0))
            liquid = liquid[match.end() :]
            continue

        skip_to = None
        match type_:
            # control flow https://shopify.github.io/liquid/tags/control-flow/
            case "if":
                dummy = "{% if True %}"
            case "elsif":
                dummy = "{% elif True %}"
            case "unless":
                dummy = "{% if True %}"
            case "endunless":
                dummy = "{% endif %}"
            case "case":
                dummy = "{% if True %}"
            case "when":
                dummy = "{% elif True %}"
            case "endcase":
                dummy = "{% endif %}"
            # iteration https://shopify.github.io/liquid/tags/iteration/
            case "for":
                dummy = "{% for i in [] %}"
            case "cycle":
                dummy = "{{ var }}"
            case "tablerow":
                dummy = "{% for i in [] %}"
            case "endtablerow":
                dummy = "{% endfor %}"
            # template https://shopify.github.io/liquid/tags/template/
            case "comment":
                dummy = "{% raw %}"
                skip_to = "endcomment"
            case "endcomment":
                dummy = "{% endraw %}"
            case "#":
                dummy = "{% set x = 'x' %}"
            case "liquid":
                dummy = "{% set x = 'x' %}"
            case "echo":
                dummy = "{{ var }}"
            case "raw":
                dummy = "{% raw %}"
                skip_to = "endraw"
            case "endraw":
                dummy = "{% endraw %}"
            case "render" | "include":
                dummy = "{% set x = 'x' %}"
            # variable https://shopify.github.io/liquid/tags/variable/
            case "assign":
                dummy = "{% set x = 'x' %}"
            case "capture":
                dummy = "{% set var %}"
            case "endcapture":
                dummy = "{% endset %}"
            case "increment" | "decrement":
                dummy = "{{ var }}"
            # looker
            # https://cloud.google.com/looker/docs/liquid-variable-reference#liquid_variable_definitions
            case "date_start" | "date_end":
                dummy = "{{ var }}"
            case "condition":
                dummy = "{% filter upper %}"
            case "endcondition":
                dummy = "{% endfilter %}"
            case "parameter":
                dummy = "{{ var }}"
            # {{...}} or ${...}
            case None:
                dummy = "{{ var }}"
            # default
            case _:
                dummy = f"{{% {type_} %}}"

        # append results
        marker = LIQUID_MARKER.format(id_)
        jinja += f"{liquid[: match.start()]}{dummy}{marker}"

        templates.append(match.group(0))
        dummies.append(dummy)

        # prepare for next iteration
        liquid = liquid[match.end() :]
        id_ += 1

    return jinja, templates, dummies


def to_liquid(jinja: str, templates: list[str], dummies: list[str]) -> str:
    liquid = ""
    trailing = jinja

    for i in range(len(templates)):
        leading, trailing, *_ = jinja.split(f"{dummies[i]}{LIQUID_MARKER.format(i)}")
        liquid += leading + templates[i]
        jinja = trailing

    liquid += trailing
    return liquid


def fmt_html(html: str, indent: int) -> str:
    jinja, templates, dummies = to_jinja(html)

    f: Any = (
        lambda s, w: " " * (w * (s.level + indent) + s.offset) + t
        if (t := s.text.strip())
        else t
    )
    Line.indent = f
    jinja = DjHTML(jinja).indent(2)
    liquid = to_liquid(jinja, templates, dummies)
    return liquid

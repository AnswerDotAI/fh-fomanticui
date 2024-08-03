from fasthtml.common import *
from fh_fomanticui.button import FButton
from fh_fomanticui.card import Card
from html import escape
import nbformat
import uvicorn

# Since this is just a CSS POC, for now we don't include jQuery or the js for each CSS framework
stylesheets = {
    'pico': 'https://cdn.jsdelivr.net/npm/@picocss/pico@2/css/pico.min.css',
    'fomantic': 'https://cdn.jsdelivr.net/npm/fomantic-ui@2.9.3/dist/semantic.min.css',
}

hdrs = [
    HighlightJS(
        langs=[
            "python",
        ]
    ),
    Meta(name="description", content="fh-ui: FastHTML UI"),
    Link(href=stylesheets["fomantic"], rel="stylesheet", id="dynamic-stylesheet"),
    Script(src="https://unpkg.com/htmx.org@2.0.1/dist/htmx.js"),
]

app, rt = fast_app(hdrs=hdrs, live=True, default_hdrs=False)

@rt('/change_stylesheet')
def post(style: str):
    return Link(href=stylesheets[style], rel='stylesheet', id='dynamic-stylesheet')




with open("nbs/elements/00_button.ipynb") as f:
    nb = nbformat.read(f, as_version=4)

cell = nb.cells[5]
FButtonSource = "\n".join(cell.source.split("\n")[1:])

@rt("/")
def get():
    return (
        Title("fh-fomanticui: Fomantic UI components for FastHTML"),
        Div(
            H1("fh-fomanticui", cls="ui header"),
            P("Fomantic UI FastTags to use in FastHTML projects."),
            A(
                "GitHub fh-fomanticui",
                href="https://github.com/AnswerDotAI/fh-fomanticui",
                cls="ui button",
            ),
            Button(
                "PyPI fh-fomanticui", href="pypi.org/project/fh-fomanticui", cls="ui disabled button"
            ),
            H2("Background", cls="ui header"),
            P(
                "FastHTML comes with a set of Pico CSS components. This project showcases:"
            ),
            Ul(
                Li("How to follow the FastHTML pattern from fasthtml/nbs/02_xtend.ipynb to create new components"),
                Li("How to use the Fomantic UI CSS framework in FastHTML"),
                Li("What all the FastTags in fh-fomanticui do"),
            ),

            H2("Buttons", cls="ui header"),

            FButton("Click me"),

            Div(Pre(Code(FButtonSource))),

            cls="ui container",
        ),
    )

if __name__ == '__main__':
    serve()

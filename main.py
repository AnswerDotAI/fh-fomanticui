from fasthtml.common import *
from fh_fomanticui.button import FButton, FAnimatedButton
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

fts_to_document = []

for cell in nb.cells:
    cell_lines = cell.source.split("\n")
    if cell.cell_type == "code" and cell_lines[0] == "# | export":
        print(cell.source)
        print(nb.cells.index(cell))
        
        # HACK: Find all FastTags in the notebook
        if cell_lines[2].endswith("-> FT:") or cell_lines[2].endswith("->FT"):
            print("FastTag definition")
            
            # Append this cell to the list of FastTags to document, but without the export line
            fts_to_document.append("\n".join(cell_lines[1:]))
        print("\n")

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

            H2("Buttons", cls="ui header"),

            

            Div(
                FButton("Click me"),   
                Pre(Code(fts_to_document[0], cls="python"), cls="code"), cls="ui segment"),
            
            Div(
                FAnimatedButton("Next", I(cls="right arrow icon")),
                Pre(Code(fts_to_document[1], cls="python"), cls="code"), cls="ui segment"),

            # [Div(Pre(Code(fui_ft, cls="python"), cls="code"), cls="ui segment") for fui_ft in fts_to_document],

            cls="ui container",
        ),
    )

if __name__ == '__main__':
    serve()

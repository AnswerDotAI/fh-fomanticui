from fasthtml.common import *
import uvicorn

hdrs = [
    Meta(name='description', content='FastHTML Semantic/Fomantic UI'),
    # For Fomantic UI, since this is just a CSS POC, for now we don't include jQuery or the js
    Link(href='https://cdn.jsdelivr.net/npm/fomantic-ui@2.9.3/dist/semantic.min.css', rel='stylesheet'),
]

app, rt = fast_app(hdrs=hdrs, live=True, default_hdrs=False)

@rt("/")
def get():
    return (
        Title("fh-ui: FastHTML UI"), 
        Div(
            H1("fh-ui: FastHTML UI", cls='ui header'),
            P("A set of FastHTML components that build upon UI components"),
            Ul(
                Li('Franken UI'),
                Li('Fomantic UI / Semantic UI')
            ),
            A('GitHub fh-ui', href='https://github.com/AnswerDotAI/fh-ui', cls='ui button'),
            Button('PyPI fh-ui', href='pypi.org/project/fh-ui', cls='ui disabled button'),
            cls='ui container'
        )
    )

if __name__ == '__main__':
    # TODO: replace with something like run_uv(fname='__main__') 
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=5001)))

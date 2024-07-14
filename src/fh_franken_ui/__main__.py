from fasthtml.common import *
import uvicorn

hdrs = [
    Meta(name='description', content='FastHTML Franken UI'),
    # Slate is 1 of 12 Franken UI CSS options.
    # TODO: allow easy swapping
    Link(href='https://unpkg.com/franken-wc@0.0.2/dist/css/slate.min.css', rel='stylesheet'),
]

app, rt = fast_app(hdrs=hdrs, live=True, default_hdrs=False)

@rt("/")
def get():
  return (
    Title("fh-franken-ui: FastHTML Franken UI"), 
    H1("fh-franken-ui: FastHTML Franken UI"),
    P("A set of FastHTML components that build upon Franken UI components")
  )
  
if __name__ == '__main__':
    # TODO: replace with something like run_uv(fname='__main__') 
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=5001)))

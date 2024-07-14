from fasthtml.common import *
import uvicorn

app = FastHTML()
rt = app.route

@rt("/")
def get():
  return (
    Title("fh-franken-ui: FastHTML Franken UI"), 
    H1("fh-franken-ui: FastHTML Franken UI"),
    P("A set of FastHTML components that build upon Franken UI components")
  )
  
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=int(os.getenv("PORT", default=8000)))

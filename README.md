# fh-ui

FastHTML UI components that can be rendered with the structure of your preferred CSS UI framework

As a POC, we have a FastHTML `Card` that can be rendered with any of:

* [Bootstrap](https://getbootstrap.com/docs/5.3/components/card/)
* [Pico CSS](https://picocss.com/docs/card)
* [Semantic UI / Fomantic UI](https://fomantic-ui.com/views/card.html)
* [Franken UI](https://franken-ui.dev/docs/card)

## Quickstart

Run main.py from any of the UI framework directories. So far just this one works:

```bash
python fh_ui/semantic_ui/main.py
```

Open it in the browser. You'll see 2 cards:

* A card rendered from XT components to match https://fomantic-ui.com/views/card.html
* A card rendered from a generic Card dataclass using `render_semanticui()`

I'm still building out this POC and it's still unstable, but so far you can:

* Compare the code for both cards in main.py and card.py
* Notice how there is a renderer registry with the ability to register new renderers
* Look at how new renderers would work
* Imagine people creating third-party packages with new renderers

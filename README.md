### Convert marimo notebook to quarto document

This is repo try to describe the workflow where you create a marimo notebook for a datascience project and then wants to share it in your blog as a markdown document.

### Required

1. quarto is installed globaly
   `uv tool install quarto-cli`

2. Define root folder as default python path in your `pyproject.toml`
   ```toml
   [tool.marimo.runtime]
   pythonpath = ["."]
   ```

### Steps to reproduce

1. Create a marimo notebook or clone this repo
   `git clone https://github.com/laguill/marimo-quarto-render-plots.git`

2. `uv sync -U`

3. `uv run marimo edit notobooks/plots.py`

4. Once finish editing convert to quarto document

   ```bash
   uv run marimo export md notebooks/plots.py -o notebooks/plots.qmd
   ```

5. Install marimo-quarto extension
   `quarto add marimo-team/quarto-marimo`

6. Preview document
   `quarto preview notebooks/plots.qmd`

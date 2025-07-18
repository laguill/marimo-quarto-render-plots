import marimo

__generated_with = "0.13.15"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import matplotlib.pyplot as plt

    return (plt,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""Output a plot object, such as an axis or figure, to see the plot.""")
    return


@app.cell
def _(plt):
    import numpy as np

    x = np.linspace(0, 10)
    plt.plot(x, x**2)
    plt.gca()
    return (x,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        """
    Calling `show()` methods displays the plot in the console area, which can be
    helpful for debugging because console outputs do not show up in the "app" preview.
    """
    )
    return


@app.cell
def _(plt, x):
    plt.plot(x, x**3)
    plt.show()
    return


if __name__ == "__main__":
    app.run()

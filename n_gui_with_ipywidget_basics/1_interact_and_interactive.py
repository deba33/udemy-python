# %%
from ipywidgets import interact, interactive, fixed
import ipywidgets as widgets
from IPython.display import display


def func(x):
    return x


interact(func, x=10)

# %%
interact(func, x=True)

# %%
interact(func, x=fixed("Hello"))

# %%
interact(func, x=widgets.IntSlider(min=-100, max=100, step=1, value=0))

# %%
interact(func, x=(-20, 20, 2))

# %%
interact(func, x=(-20.0, 20.0, 0.2))

# %%
@interact(x=True, y=fixed(1.0))
def g(x, y):
    return(x, y)

# %%
@interact(x=(0.0, 20.0, 0.5))
def h(x=5.0):
    return x


# %%
interact(func, x=["hello", "world", "other"])

# %%
interact(func, x={"one": 10, "two": 20})

# %%


def f(a, b):
    display(a + b)
    return a + b


w = interactive(f, a=10, b=10)
display(w)

# %%

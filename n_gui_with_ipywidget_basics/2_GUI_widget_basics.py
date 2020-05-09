# %%
import ipywidgets as widgets
from IPython.display import display

w = widgets.IntSlider()
display(w)

# %%
# w.close()
w.value

# %%
# to view all satateful propreties
w.keys

# %%
w.max = 200

# %%
w.disabled = True

# %%
w.disabled = False

# %%
a = widgets.FloatText()
b = widgets.FloatSlider()

display(a, b)

mylink = widgets.jslink((a, "value"), (b, "value"))
# to unlink
# mylink.unlink()

# %%

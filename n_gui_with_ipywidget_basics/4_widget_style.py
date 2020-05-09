# %%
import ipywidgets as widgets
from IPython.display import display

w = widgets.IntSlider()
display(w)

w.layout.margin = "auto"
w.layout.height = "75px"
# %%
x = widgets.IntSlider(value=15, description="New Slider")
display(x)
x.layout = w.layout
# %%
widgets.Button(description="Ordinary Button", button_style="danger")
# %%
b1 = widgets.Button(description="Custom color")
b1.style.button_color = "lightgreen"
display(b1)
# %%
b2 = widgets.Button()
b2.style = b1.style
display(b2)
# %%

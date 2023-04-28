# Key Variables:
* `self.length`: the length of the pole
* `self.masspole`: the mass of the pole

# Render
Once you change `self.length`, the screen will show it autometically.    
The rendered texts are defined at the head of `render()`. Currently the screen shows `self.masspole` and `self.length`. If you want to show more parameters, you can modify those texts.

# Code Usage
Replace the original `cartpole.py` in the `gym` module with this modified one.    
Whenever you make some changes to the module source, go to the directory containing `setup.py` of this module and execute the following,
```
  /bin/python3 -m pip install .
```
Then execute
```
  /bin/python3 get_started.py
```
to see the gif

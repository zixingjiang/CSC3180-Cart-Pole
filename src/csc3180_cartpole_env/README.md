# how to install csc3180_cartpole_env
## Part1: creat a virtual env
I recommand you to install the packet in the virtual env
```
pip install virtualenv virtualenvwrapper
```
Then, you first need to add some lines to your ~/.bashrc profile. Open the file using nano , vim , or emacs and append these lines to the end:
```
export WORKON_HOME=$HOME/.local/bin/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=$HOME/.local/bin/virtualenv
source $HOME/.local/bin/virtualenvwrapper.sh
```
Save the file. Then “source it” in your terminal:
```
source ~/.bashrc
```

create a Python 3 virtual environment for csc3180

```
mkvirtualenv csc3180 -p python3
workon csc3180
```
## Part2: installation by setup.py
To use setup.py to install our env packet 
```
cd ./CSC3180-Cart-Pole/src/csc3180_cartpole_env

python3 -m pip install .
```

## Part3: how to use this env
```
env = gym.make('csc3180/CartPole_v1', render_mode='human')
```
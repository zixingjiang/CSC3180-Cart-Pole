# CSC3180-Cart-Pole
 CSC3180 Course Project

- [Openai Cart Pole](https://www.gymlibrary.dev/environments/classic_control/cart_pole/)

## Modified "cart-pole" Environment
In this project, we customized the OpenAI Gym environment for the cart-pole problem to create a more challenging scenario for our RL agent. We adjusted the cart’s mass, pole length, and gravitational constant to create a more volatile environment that our agent could learn to balance the pole in. The customized environment is
"csc3180_cartpole_env". You can find the source code at "CSC3180-Cart-Pole/src/csc3180_cartpole_env".

Our aim was to train an agent using an RL algorithm that could maintain balance for as long as possible in this customized environment. As part of our project, we customized the environment and designed specific APIs for the RL simulation program, such as "change_poleLength", "change_poleMass" and "set_i_episode". These APIs allowed the RL simulation program could effectively train the agent in the customized environment and improve performance in the specific task we designed.

### How to install csc3180_cartpole_env
#### Part1: creat a virtual env
We highly recommend you create a virtual environment to test our project. The Virtual environment will isolate project dependencies and package installations, allowing for effective version control of packages and avoiding conflicts with other Python projects or the system environment. However, the virtual environment is not mandatory and you can skip it.

We recommend you to install the packet in the virtual env
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

#### Part2: installation by setup.py
You can install our customized packet into your virtual environment by executing setup.py

```
cd ./CSC3180-Cart-Pole/src/csc3180_cartpole_env

python3 -m pip install .
```
Once the installation process is complete, ensure that the customized environment has been installed successfully by using the "pip list" command. This will provide a comprehensive list of all installed Python packages, including "csc3180_cartpole_env".


#### Part3: how to use this env
```
import csc3180_cartpole_env
import gymnasium as gym

env = gym.make('csc3180/CartPole_v1', render_mode='human')
```

Moreover, we have successfully developed an RL algorithm that is tailored to our specific gym environment. To run the algorithm, please execute the following code, which will enable our algorithm to interact with the customized environment and begin the training process.

```
cd ./CSC3180−Cart−Pole/src

python qlearning.py
```

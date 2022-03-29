# Hybrid Reward Architecture for MsPacman

This fork of the OpenAi baselines repository implements a version of Hybrid Reward Architecture (HRA) based on the papers
[Hybrid Reward Architecture for Reinforcement Learning](https://papers.nips.cc/paper/2017/hash/1264a061d82a2edae1574b07249800d6-Abstract.html)
 and [Explainable Reinforcement Learning via Reward Decomposition](https://web.engr.oregonstate.edu/~erwig/papers/ExplainableRL_XAI19.pdf).


The main idea is to split the reward and train a separate head of fully connected layers for each type of reward.
The convolutional layers are shared.

The current version only works for the *deepq* algorithm on Ms. Pac-Man.
It uses 4 different heads for *normal pills*, *power pills*, *eating blue ghosts*, and *dying*.
The reward is split by checking in which range the reward lies.
Each object has a specific reward (e.g. 10 points for a *normal pill* and 50 for a *power pill*). 
Using ranges accounts for cases where the agent obtains multiple rewards at once (e.g. eating two *normal pills*).
The specific ranges can be defined in `baselines/head_settings`.

To replicate our training use the following command line arguments:
```
--alg=deepq
--env=MsPacmanNoFrameskip-v4
--num_timesteps=10000000
--save_path=./models/{model_name}
--log_path=./logs/{model_name}
--dueling=False
--prioritized_replay=False
```
Run the trained model with:
```
--alg=deepq
--env=MsPacmanNoFrameskip-v4
--num_timesteps=0
--load_path=./models/{model_name}
--dueling=False
--play
```

The project originated as a student project of Simone Pompe and Julian Stockmann.


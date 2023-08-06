# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['cleanrl',
 'cleanrl.ppo_continuous_action_isaacgym',
 'cleanrl_utils',
 'cleanrl_utils.evals']

package_data = \
{'': ['*'], 'cleanrl.ppo_continuous_action_isaacgym': ['isaacgym/*']}

install_requires = \
['gym==0.23.1',
 'gymnasium>=0.28.1',
 'huggingface-hub>=0.11.1,<0.12.0',
 'moviepy>=1.0.3,<2.0.0',
 'pygame==2.1.0',
 'stable-baselines3==1.2.0',
 'tensorboard>=2.10.0,<3.0.0',
 'torch>=1.12.1',
 'wandb>=0.13.11,<0.14.0']

extras_require = \
{'atari': ['ale-py==0.7.4',
           'AutoROM[accept-rom-license]>=0.4.2,<0.5.0',
           'opencv-python>=4.6.0.66,<5.0.0.0'],
 'c51-atari': ['ale-py==0.7.4',
               'AutoROM[accept-rom-license]>=0.4.2,<0.5.0',
               'opencv-python>=4.6.0.66,<5.0.0.0'],
 'c51-atari-jax': ['ale-py==0.7.4',
                   'AutoROM[accept-rom-license]>=0.4.2,<0.5.0',
                   'opencv-python>=4.6.0.66,<5.0.0.0',
                   'jax>=0.3.17,<0.4.0',
                   'jaxlib>=0.3.15,<0.4.0',
                   'flax>=0.6.0,<0.7.0'],
 'c51-jax': ['jax>=0.3.17,<0.4.0',
             'jaxlib>=0.3.15,<0.4.0',
             'flax>=0.6.0,<0.7.0'],
 'cloud': ['boto3>=1.24.70,<2.0.0', 'awscli>=1.25.71,<2.0.0'],
 'dm-control': ['mujoco<=2.3.3', 'shimmy[dm-control]>=1.0.0'],
 'docs': ['mkdocs-material>=8.4.3,<9.0.0',
          'markdown-include>=0.7.0,<0.8.0',
          'openrlbenchmark>=0.1.1b4,<0.2.0'],
 'dqn-atari': ['ale-py==0.7.4',
               'AutoROM[accept-rom-license]>=0.4.2,<0.5.0',
               'opencv-python>=4.6.0.66,<5.0.0.0'],
 'dqn-atari-jax': ['ale-py==0.7.4',
                   'AutoROM[accept-rom-license]>=0.4.2,<0.5.0',
                   'opencv-python>=4.6.0.66,<5.0.0.0',
                   'jax>=0.3.17,<0.4.0',
                   'jaxlib>=0.3.15,<0.4.0',
                   'flax>=0.6.0,<0.7.0'],
 'dqn-jax': ['jax>=0.3.17,<0.4.0',
             'jaxlib>=0.3.15,<0.4.0',
             'flax>=0.6.0,<0.7.0'],
 'envpool': ['envpool>=0.6.4,<0.7.0'],
 'jax': ['jax>=0.3.17,<0.4.0', 'jaxlib>=0.3.15,<0.4.0', 'flax>=0.6.0,<0.7.0'],
 'mujoco': ['mujoco<=2.3.3', 'imageio>=2.14.1,<3.0.0'],
 'mujoco-py': ['free-mujoco-py>=2.1.6,<3.0.0'],
 'optuna': ['optuna>=3.0.1,<4.0.0',
            'optuna-dashboard>=0.7.2,<0.8.0',
            'rich<12.0'],
 'pettingzoo': ['PettingZoo==1.18.1',
                'SuperSuit==3.4.0',
                'multi-agent-ale-py==0.1.11'],
 'ppo-atari-envpool-xla-jax-scan': ['ale-py==0.7.4',
                                    'AutoROM[accept-rom-license]>=0.4.2,<0.5.0',
                                    'opencv-python>=4.6.0.66,<5.0.0.0',
                                    'jax>=0.3.17,<0.4.0',
                                    'jaxlib>=0.3.15,<0.4.0',
                                    'flax>=0.6.0,<0.7.0',
                                    'envpool>=0.6.4,<0.7.0'],
 'procgen': ['procgen>=0.10.7,<0.11.0'],
 'pytest': ['pytest>=7.1.3,<8.0.0']}

setup_kwargs = {
    'name': 'cleanrl',
    'version': '1.2.0',
    'description': 'High-quality single file implementation of Deep Reinforcement Learning algorithms with research-friendly features',
    'long_description': '# CleanRL (Clean Implementation of RL Algorithms)\n\n\n[<img src="https://img.shields.io/badge/license-MIT-blue">](https://github.com/vwxyzjn/cleanrl)\n[![tests](https://github.com/vwxyzjn/cleanrl/actions/workflows/tests.yaml/badge.svg)](https://github.com/vwxyzjn/cleanrl/actions/workflows/tests.yaml)\n[![docs](https://img.shields.io/github/deployments/vwxyzjn/cleanrl/Production?label=docs&logo=vercel)](https://docs.cleanrl.dev/)\n[<img src="https://img.shields.io/discord/767863440248143916?label=discord">](https://discord.gg/D6RCjA6sVT)\n[<img src="https://img.shields.io/youtube/channel/views/UCDdC6BIFRI0jvcwuhi3aI6w?style=social">](https://www.youtube.com/channel/UCDdC6BIFRI0jvcwuhi3aI6w/videos)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)\n[<img src="https://img.shields.io/badge/%F0%9F%A4%97%20Models-Huggingface-F8D521">](https://huggingface.co/cleanrl)\n[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vwxyzjn/cleanrl/blob/master/docs/get-started/CleanRL_Huggingface_Integration_Demo.ipynb)\n\n\nCleanRL is a Deep Reinforcement Learning library that provides high-quality single-file implementation with research-friendly features. The implementation is clean and simple, yet we can scale it to run thousands of experiments using AWS Batch. The highlight features of CleanRL are:\n\n\n\n* 📜 Single-file implementation\n   * *Every detail about an algorithm variant is put into a single standalone file.* \n   * For example, our `ppo_atari.py` only has 340 lines of code but contains all implementation details on how PPO works with Atari games, **so it is a great reference implementation to read for folks who do not wish to read an entire modular library**.\n* 📊 Benchmarked Implementation (7+ algorithms and 34+ games at https://benchmark.cleanrl.dev)\n* 📈 Tensorboard Logging\n* 🪛 Local Reproducibility via Seeding\n* 🎮 Videos of Gameplay Capturing\n* 🧫 Experiment Management with [Weights and Biases](https://wandb.ai/site)\n* 💸 Cloud Integration with docker and AWS \n\nYou can read more about CleanRL in our [JMLR paper](https://www.jmlr.org/papers/volume23/21-1342/21-1342.pdf) and [documentation](https://docs.cleanrl.dev/).\n\nCleanRL only contains implementations of **online** deep reinforcement learning algorithms. If you are looking for **offline** algorithms, please check out [tinkoff-ai/CORL](https://github.com/tinkoff-ai/CORL), which shares a similar design philosophy as CleanRL.\n\n> ℹ️ **Support for Gymnasium**: [Farama-Foundation/Gymnasium](https://github.com/Farama-Foundation/Gymnasium) is the next generation of [`openai/gym`](https://github.com/openai/gym) that will continue to be maintained and introduce new features. Please see their [announcement](https://farama.org/Announcing-The-Farama-Foundation) for further detail. We are migrating to `gymnasium` and the progress can be tracked in [vwxyzjn/cleanrl#277](https://github.com/vwxyzjn/cleanrl/pull/277). \n\n\n> ⚠️ **NOTE**: CleanRL is *not* a modular library and therefore it is not meant to be imported. At the cost of duplicate code, we make all implementation details of a DRL algorithm variant easy to understand, so CleanRL comes with its own pros and cons. You should consider using CleanRL if you want to 1) understand all implementation details of an algorithm\'s varaint or 2) prototype advanced features that other modular DRL libraries do not support (CleanRL has minimal lines of code so it gives you great debugging experience and you don\'t have do a lot of subclassing like sometimes in modular DRL libraries).\n\n## Get started\n\nPrerequisites:\n* Python >=3.7.1,<3.11\n* [Poetry 1.2.1+](https://python-poetry.org)\n\nTo run experiments locally, give the following a try:\n\n```bash\ngit clone https://github.com/vwxyzjn/cleanrl.git && cd cleanrl\npoetry install\n\n# alternatively, you could use `poetry shell` and do\n# `python run cleanrl/ppo.py`\npoetry run python cleanrl/ppo.py \\\n    --seed 1 \\\n    --env-id CartPole-v0 \\\n    --total-timesteps 50000\n\n# open another temrminal and enter `cd cleanrl/cleanrl`\ntensorboard --logdir runs\n```\n\nTo use experiment tracking with wandb, run\n```bash\nwandb login # only required for the first time\npoetry run python cleanrl/ppo.py \\\n    --seed 1 \\\n    --env-id CartPole-v0 \\\n    --total-timesteps 50000 \\\n    --track \\\n    --wandb-project-name cleanrltest\n```\n\nIf you are not using `poetry`, you can install CleanRL with `requirements.txt`:\n\n```bash\n# core dependencies\npip install -r requirements/requirements.txt\n\n# optional dependencies\npip install -r requirements/requirements-atari.txt\npip install -r requirements/requirements-mujoco.txt\npip install -r requirements/requirements-mujoco_py.txt\npip install -r requirements/requirements-procgen.txt\npip install -r requirements/requirements-envpool.txt\npip install -r requirements/requirements-pettingzoo.txt\npip install -r requirements/requirements-jax.txt\npip install -r requirements/requirements-docs.txt\npip install -r requirements/requirements-cloud.txt\n```\n\nTo run training scripts in other games:\n```\npoetry shell\n\n# classic control\npython cleanrl/dqn.py --env-id CartPole-v1\npython cleanrl/ppo.py --env-id CartPole-v1\npython cleanrl/c51.py --env-id CartPole-v1\n\n# atari\npoetry install -E atari\npython cleanrl/dqn_atari.py --env-id BreakoutNoFrameskip-v4\npython cleanrl/c51_atari.py --env-id BreakoutNoFrameskip-v4\npython cleanrl/ppo_atari.py --env-id BreakoutNoFrameskip-v4\npython cleanrl/sac_atari.py --env-id BreakoutNoFrameskip-v4\n\n# NEW: 3-4x side-effects free speed up with envpool\'s atari (only available to linux)\npoetry install -E envpool\npython cleanrl/ppo_atari_envpool.py --env-id BreakoutNoFrameskip-v4\n# Learn Pong-v5 in ~5-10 mins\n# Side effects such as lower sample efficiency might occur\npoetry run python ppo_atari_envpool.py --clip-coef=0.2 --num-envs=16 --num-minibatches=8 --num-steps=128 --update-epochs=3\n\n# procgen\npoetry install -E procgen\npython cleanrl/ppo_procgen.py --env-id starpilot\npython cleanrl/ppg_procgen.py --env-id starpilot\n\n# ppo + lstm\npoetry install -E atari\npython cleanrl/ppo_atari_lstm.py --env-id BreakoutNoFrameskip-v4\n```\n\nYou may also use a prebuilt development environment hosted in Gitpod:\n\n[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/vwxyzjn/cleanrl)\n\n## Algorithms Implemented\n\n\n| Algorithm      | Variants Implemented |\n| ----------- | ----------- |\n| ✅ [Proximal Policy Gradient (PPO)](https://arxiv.org/pdf/1707.06347.pdf)  |  [`ppo.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo.py),   [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppopy) |\n| |  [`ppo_atari.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari.py),   [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_ataripy)\n| |  [`ppo_continuous_action.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_continuous_action.py),   [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_continuous_actionpy)\n| |  [`ppo_atari_lstm.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari_lstm.py),   [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_atari_lstmpy)\n| |  [`ppo_atari_envpool.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari_envpool.py),   [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_atari_envpoolpy)\n| | [`ppo_atari_envpool_xla_jax.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari_envpool_xla_jax.py), [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_atari_envpool_xla_jaxpy)\n| | [`ppo_atari_envpool_xla_jax_scan.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari_envpool_xla_jax_scan.py), [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_atari_envpool_xla_jax_scanpy))\n| |  [`ppo_procgen.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_procgen.py),   [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_procgenpy)\n| |  [`ppo_atari_multigpu.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_atari_multigpu.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_atari_multigpupy)\n| | [`ppo_pettingzoo_ma_atari.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_pettingzoo_ma_atari.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_pettingzoo_ma_ataripy)\n| | [`ppo_continuous_action_isaacgym.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_continuous_action_isaacgym/ppo_continuous_action_isaacgym.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/ppo/#ppo_continuous_action_isaacgympy)\n| ✅ [Deep Q-Learning (DQN)](https://web.stanford.edu/class/psych209/Readings/MnihEtAlHassibis15NatureControlDeepRL.pdf) |  [`dqn.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/dqn.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/dqn/#dqnpy) |\n| | [`dqn_atari.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/dqn_atari.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/dqn/#dqn_ataripy) |\n| | [`dqn_jax.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/dqn_jax.py), [docs](https://docs.cleanrl.dev/rl-algorithms/dqn/#dqn_jaxpy) |\n| | [`dqn_atari_jax.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/dqn_atari_jax.py), [docs](https://docs.cleanrl.dev/rl-algorithms/dqn/#dqn_atari_jaxpy) |\n| ✅ [Categorical DQN (C51)](https://arxiv.org/pdf/1707.06887.pdf) |  [`c51.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/c51.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/c51/#c51py) |\n| |  [`c51_atari.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/c51_atari.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/c51/#c51_ataripy) |\n| | [`c51_jax.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/c51_jax.py), [docs](https://docs.cleanrl.dev/rl-algorithms/c51/#c51_jaxpy) |\n| | [`c51_atari_jax.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/c51_atari_jax.py), [docs](https://docs.cleanrl.dev/rl-algorithms/c51/#c51_atari_jaxpy) |\n| ✅ [Soft Actor-Critic (SAC)](https://arxiv.org/pdf/1812.05905.pdf) |  [`sac_continuous_action.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/sac_continuous_action.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/sac/#sac_continuous_actionpy) |\n| |  [`sac_atari.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/sac_atari.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/sac/#sac_atarinpy) |\n| ✅ [Deep Deterministic Policy Gradient (DDPG)](https://arxiv.org/pdf/1509.02971.pdf) |  [`ddpg_continuous_action.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ddpg_continuous_action.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/ddpg/#ddpg_continuous_actionpy) |\n| | [`ddpg_continuous_action_jax.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ddpg_continuous_action_jax.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/ddpg/#ddpg_continuous_action_jaxpy)\n| ✅ [Twin Delayed Deep Deterministic Policy Gradient (TD3)](https://arxiv.org/pdf/1802.09477.pdf) |  [`td3_continuous_action.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/td3_continuous_action.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/td3/#td3_continuous_actionpy) |\n|  | [`td3_continuous_action_jax.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/td3_continuous_action_jax.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/td3/#td3_continuous_action_jaxpy) |\n| ✅ [Phasic Policy Gradient (PPG)](https://arxiv.org/abs/2009.04416) |  [`ppg_procgen.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppg_procgen.py),  [docs](https://docs.cleanrl.dev/rl-algorithms/ppg/#ppg_procgenpy) |\n| ✅ [Random Network Distillation (RND)](https://arxiv.org/abs/1810.12894) |  [`ppo_rnd_envpool.py`](https://github.com/vwxyzjn/cleanrl/blob/master/cleanrl/ppo_rnd_envpool.py),  [docs](/rl-algorithms/ppo-rnd/#ppo_rnd_envpoolpy) |\n\n\n## Open RL Benchmark\n\nTo make our experimental data transparent, CleanRL participates in a related project called [Open RL Benchmark](https://github.com/openrlbenchmark/openrlbenchmark), which contains tracked experiments from popular DRL libraries such as ours, [Stable-baselines3](https://github.com/DLR-RM/stable-baselines3), [openai/baselines](https://github.com/openai/baselines), [jaxrl](https://github.com/ikostrikov/jaxrl), and others. \n\nCheck out https://benchmark.cleanrl.dev/ for a collection of Weights and Biases reports showcasing tracked DRL experiments. The reports are interactive, and researchers can easily query information such as GPU utilization and videos of an agent\'s gameplay that are normally hard to acquire in other RL benchmarks. In the future, Open RL Benchmark will likely provide an dataset API for researchers to easily access the data (see [repo](https://github.com/openrlbenchmark/openrlbenchmark)).\n\n![](docs/static/o1.png)\n![](docs/static/o2.png)\n![](docs/static/o3.png)\n\n\n## Support and get involved\n\nWe have a [Discord Community](https://discord.gg/D6RCjA6sVT) for support. Feel free to ask questions. Posting in [Github Issues](https://github.com/vwxyzjn/cleanrl/issues) and PRs are also welcome. Also our past video recordings are available at [YouTube](https://www.youtube.com/watch?v=dm4HdGujpPs&list=PLQpKd36nzSuMynZLU2soIpNSMeXMplnKP&index=2)\n\n## Citing CleanRL\n\nIf you use CleanRL in your work, please cite our technical [paper](https://www.jmlr.org/papers/v23/21-1342.html):\n\n```bibtex\n@article{huang2022cleanrl,\n  author  = {Shengyi Huang and Rousslan Fernand Julien Dossa and Chang Ye and Jeff Braga and Dipam Chakraborty and Kinal Mehta and João G.M. Araújo},\n  title   = {CleanRL: High-quality Single-file Implementations of Deep Reinforcement Learning Algorithms},\n  journal = {Journal of Machine Learning Research},\n  year    = {2022},\n  volume  = {23},\n  number  = {274},\n  pages   = {1--18},\n  url     = {http://jmlr.org/papers/v23/21-1342.html}\n}\n```\n',
    'author': 'Costa Huang',
    'author_email': 'costa.huang@outlook.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7.1,<3.11',
}


setup(**setup_kwargs)

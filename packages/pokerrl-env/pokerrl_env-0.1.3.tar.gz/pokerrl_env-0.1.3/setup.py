# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pokerrl_env']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.5,<2.0.0',
 'pytest>=6.2.4,<7.0.0',
 'setuptools-rust>=1.5.2,<2.0.0']

setup_kwargs = {
    'name': 'pokerrl-env',
    'version': '0.1.3',
    'description': 'A poker environment for reinforcement learning',
    'long_description': "# Poker environment for reinforcement learning\n\nTo instantiate the environment, pass in the config.\n\nthe config consists of the following parameters:\n\n- number of players (2-6), default 2\n- bet limit (fixed limit, no limit, pot limit), default pot limit\n- bet sizes allowed (array of floats), default (1, 0.9, 0.75, 0.67, 0.5, 0.33, 0.25, 0.1)\n- Game type [Holdem, OmahaHI], default OmahaHI\n\n## Example usage\n\nThis is the recommended way to use the environment.\n\n```\nfrom pokerrl import Config, Game\n\nconfig = Config(\n    num_players=2,\n    bet_limit=BetLimits.POT_LIMIT,\n    bet_sizes=[1, 0.5],\n    game_type=GameTypes.OMAHA_HI,\n)\ngame = Game(config)\nplayer_state,done,winnings,action_mask = game.reset()\nwhile not done:\n  action = model(player_state)\n  player_state,done,winnings,action_mask = game.step(action)\n```\n\n## Play a game (both sides)\n\n```\nfrom pokerrl import play_game\nplay_game()\n```\n\n## Example usage (low level)\n\n```\nfrom pokerrl import Config, init_state, step_state, GameTypes, BetLimits, player_view, Positions, get_current_player\n\nconfig = Config(\n    num_players=2,\n    bet_limit=BetLimits.POT_LIMIT,\n    bet_sizes=[1, 0.5],\n    game_type=GameTypes.OMAHA_HI,\n)\nglobal_state,done,winnings,action_mask = init_state(config)\nwhile not done:\n  player_idx = get_current_player(global_state)\n  player_state = player_view(global_state, player_idx)\n  action = model(player_state)\n  global_state,done,winnings,action_mask = step_state(global_state, action, config)\n```\n\n## Player view (low level)\n\n```\nfrom pokerrl import Config, init_state, step_state, GameTypes, BetLimits, player_view, Positions, get_current_player\n\nconfig = Config()\nglobal_state,done,winnings,action_mask = init_state(config)\nwhile not done:\n  player_idx = get_current_player(global_state)\n  human_readable_view(global_state,player_idx, config)\n  action = get_action(action_mask,global_state,config)\n  global_state,done,winnings,action_mask = step_state(global_state, action, config)\n```\n\n## State\n\nThe state is an array. To get a player's view of the state, pass the state into the view with the appropriate player index.\n\n## Design decisions\n\n- Record the total amount raised.\n  If you record the actual amount raised this means its more difficult to tell what the raise size is when facing multiple raises. But easier to tell what the raise size is when facing a single raise. Also complicates the process of determining how much a player has to call, as the raise size is in relation to the previous bet, which in multiplayer games, is not necessarily us.\n- Global state player numbers are identical to their position.\n- SB and BB posts are the first two states.\n\n- A raise is the total amount. Subtract player street total\n- A call vs a raise is the difference = villain bet - player street total\n- A call vs a bet is the full amount = villain bet - player street total\n- A bet is the full amount\n- A fold is 0\n",
    'author': 'Morgan Griffiths',
    'author_email': 'rareducks101@yahoo.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

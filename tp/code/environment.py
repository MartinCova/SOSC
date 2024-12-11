from pathlib import Path
from typing import Optional

import gymnasium as gym
import numpy as np
import pandas as pd

from utils import (
    read_wrdata_file,
    run_exe,
    NGSpiceEnvironment,
)


class CmosInverterEnvironment(NGSpiceEnvironment):
    r"""
    Custom gym environment for optimizing a CMos inverter.

    Private attributes starts with _, those attributes must be kept
    as is after their definition in the constructor __init__.

    Attributes
    ----------
    _netlist_src : Path
        Path to original netlist, use at beginning to load the netlist.
    _tmpdir : Path
        Tempory dictionary that contains modified netlists to run.
    _netlist_content : str
        Unformatted string representing the content of the simulation
        netlist.
    _netlist : Path
        Path to the ouput file for the formatted netlist.
    """


    def __init__(
            self,
            widths: bool = True,
            lengths: bool = False,
            borders: Optional[dict[str, tuple[float, float]]] = None,
    ):
        # TODO : Path to netlist
        self._netlist = "../models/inverter_45nm.txt"


        # TODO : Setup all useful class attributes you need in your functions


        # TODO : Filter parameters
        #        By default, all .param in the netlists are considered
        #        as parameters, however all parameters must be defined
        #        in the actions, which is not necessarily relevant
        #        (for example a vdd parameter with the voltage power
        #        value).
        #        ⠀
        #        These .param can be removed from the netlist, or kept
        #        (because for example you use it in the code to get
        #        some meta values that must not be optimized).
        #        ⠀
        #        If you keep it, you must separate the parameters in
        #        two dictionaries : self._parameters and
        #        self._hidden_parameters. The second one must exist in
        #        all cases, if you don't have hidden parameters set it
        #        to empty : self._hidden_parameters = {}
        self._parameters = {"Wn": 90e-9, "Wp": 90e-9}
        self._hidden_parameters = {"Vdd": 1.8, "Vin": 1.8, "L": 45e-9, "Cload": 1e-12}

        # TODO : Define the action space : self._action_space
        #        Use gym spaces for that, remember that the
        #        actions are dictionaries associating
        #        parameters to their new values (don't forget
        #        the limits)
        self._action_space = gym.spaces.Dict({"Wn": gym.spaces.Box(low=45e-9, high=1e-6, dtype=np.float64),
                                              "Wp": gym.spaces.Box(low=45e-9, high=1e-6, dtype=np.float64)})

        # TODO : define the observation space : self.observation_space
        #        As for action space, use gym spaces to define it, the
        #        observations are a dictionary associating each metric
        #        to its value
        raise NotImplementedError("Observation space is not defined")

    def _get_obs(self) -> dict:
        r"""
        Run the simulation and extract the data.

        Returns
        -------
        None
        """
        # Generate netlist
        with open(self._netlist, "w") as fd:
            fd.write(self._netlist_content.format(**self._parameters, **self._hidden_parameters))

        # Run simulation and extract data
        # TODO : Write a code to call the simulator and to extract
        #        data from output files.
        #        Some class attributes can be helpful :
        #          - self._netlist : contains path to the netlist to
        #            simulate, netlist has been parsed with the
        #            parameters value given by action dictionary
        #          - self._generated_files : list of files generated
        #            by the simulation (wrdata instructions) (only
        #            the name of the file, not their path)
        #        Also you can use the following class method from
        #        parent :
        #          - get_output_path
        #        You have the following utils functions to help you :
        #          - utils.run_exe
        #          - utils.read_wrdata_file
        #        ⠀
        #        Observations must be a dictionary {
        #           "metric_1": 0.1,
        #           "metric_2": 0.2,
        #        }, I recommend you to write other methods _compute_*
        #        and call it to construct this dictionary : {
        #           "metric_1": compute_metric_1(data),
        #           "metric_2": compute_metric_2(data),
        #           ...
        #        }
        raise NotImplementedError("NGSpiceEnvironment._get_ops method not implemented")


    def _get_info(self):
        return {}

    def reset(self, seed: Optional[int] = None, options: Optional[dict] = None):
        r"""
        Reset the environment.

        Parameters
        ----------
        seed : seed, optional
            Seed to use for reproducibility.
        options : dict, optional
            Options for the environment, unused.

        Returns
        -------
        observation : dict
            Dictionary of observations, for example : {
                "metric_1": 0.5,
                "metric_2": 1.2,
            }
        info : dict
            Dictionary with useful information, empty in this
            environment.
        """
        super().reset(seed=seed)

        params = self.action_space.sample()

        self._parameters.update(params)

        obs = self._get_obs()
        info = self._get_info()

        return obs, info

    def _compute_reward(self, *_) -> float:
        r"""
        Compute the reward.

        Returns
        -------
        Float
            The reward, as a float, or anything you want (but be careful).
        """
        # TODO : Write this method and return the reward, you are
        #        free to replace *args by any number of arguments you
        #        need
        raise NotImplementedError("Method _compute_reward is not implemented")

    def step(self, action: dict) -> tuple[dict, float, bool, bool, dict]:
        r"""
        Do one step in the environment.

        Parameters
        ----------
        action : dict
            Dictionary of the new values for the parameters, for
            example : {
                "param_1": 0.1,
                "param_2": 0.2,
            }
            Parameters in the dictionary must match the .param
            parameters in the netlist.

        Returns
        -------
        observation : dict
            Dictionary of observations, for example : {
                "metric_1": 0.5,
                "metric_2": 1.2,
            }
        reward : float
            Floating value representing the reward.
        terminated : bool
            If the environment as reach the end, always False because
            non-episodic environment.
        truncated : bool
            If the environment ended unexpectedly, always False
            because the environment cannot stop.
        info : dict
            Dictionary with useful information, empty in this
            environment.
        """
        self._parameters.update(action)

        obs = self._get_obs()

        # TODO : Pass the arguments needed to compute the reward
        reward = self._compute_reward(...)
        raise NotImplementedError("Call to reward has not been implemented")

        info = self._get_info()

        terminated = False
        truncated = False

        return obs, reward, terminated, truncated, info


class CmosInverterEnvironmentDiscrete(gym.Env):

    def __init__(self):
        super().__init__()

        # Back-end environment
        self._env = CmosInverterEnvironment()

        # TODO : Continuous environment are not the best to use in
        #        reinforcement learning for this task, we go to a
        #        discrete actions environment.
        #        The discrete actions are a step added or subtracted
        #        in the parameter values :
        #            param_1_action == 1 => param_1_value += step
        #        ⠀
        #        Stable baselines 3 does not want dictionary actions,
        #        the workaround is to define a front-end environment
        #        for SB3 that uses the previous environment in
        #        back-end.
        #        ⠀
        #        And the actions are now arrays :
        #            [param_1_action, param_2_action, ...]
        #        ⠀
        #        Write the new action space.
        raise NotImplementedError("Discrete action space is not defined")

        # TODO : The issue with SB3 and Dict spaces is the same for
        #        observation space. Adapt it in the same way as action
        #        space.
        raise NotImplementedError("Discrete observation space is not defined")

    @property
    def _parameters(self):
        return self._env._parameters

    def reset(self, seed: Optional[int] = None, options: Optional[dict] = None):
        obs, info = self._env.reset()

        return (
            np.array([obs[key] for key in self._observations_order]),
            {"obs": obs, **info},
        )

    def step(self, action):
        # TODO : Write a code that converts the actions from discrete
        #        to direct values, call the step method of the
        #        back-end environment self._env, then convert the
        #        observation to the SB3 valid format before return.
        #        ⠀
        #        Don't forget anything :)
        raise NotImplementedError("Discrete step method not implemented")

    def close(self):
        super().close()
        self._env.close()

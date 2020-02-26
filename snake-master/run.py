#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C0103,C0111

import argparse

from snake.game import Game, GameConf, GameMode

dict_solver = {
    "hamilton": "HamiltonSolver",

}

dict_mode = {
    "normal": GameMode.NORMAL,
    "bcmk": GameMode.BENCHMARK,

}

parser = argparse.ArgumentParser(description="Run snake game agent.")
parser.add_argument("-s", default="hamilton", choices=dict_solver.keys(),
                    help="name of the solver to direct the snake (default: hamilton)")
parser.add_argument("-m", default="bcmk", choices=dict_mode.keys(),
                    help="game mode (default: bcmk)")
args = parser.parse_args()

conf = GameConf()
conf.solver_name = dict_solver[args.s]
conf.mode = dict_mode[args.m]
print("Solver: %s    Mode: %s" % (conf.solver_name, conf.mode))

Game(conf).run()

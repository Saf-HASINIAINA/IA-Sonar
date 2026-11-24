#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Point d'entrée : python main.py [--exp 1|2|all]"""
import argparse
from src import experience1, experience2_training


def main():
    p = argparse.ArgumentParser(description="Projet Sonar - Mines vs Roches")
    p.add_argument("--exp", choices=["1", "2", "all"], default="all")
    a = p.parse_args()
    if a.exp in ("1", "all"):
        experience1.run()
    if a.exp in ("2", "all"):
        experience2_training.run()


if __name__ == "__main__":
    main()

import matplotlib.pyplot as plt
import numpy as np


class GridWorld:
    def __init__(self) -> None:
        self.board=np.zeros((3,4))
        self.board[1,2]=2
        self.board[0,3]=1
        self.board[1,3]=-1
        
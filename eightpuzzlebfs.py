# -*- coding: utf-8 -*-

import timeit
import resource

import timeit


class board_param():

    def __init__(self, board: str, path: list, depth: int):
        self.state = board
        self.path = path
        self.depth = depth


def move_up(board, zeroindex):
    elementchanged = board.state[zeroindex - 3]
    newpath = board.path[:]
    newstate = board.state[0:zeroindex - 3] + "0" + board.state[
                                                    zeroindex - 2: zeroindex] + elementchanged + board.state[
                                                                                                 zeroindex + 1:]
    newboard = board_param(newstate, newpath + ["Up"], board.depth + 1)
    return (newboard)


def move_down(board, zeroindex):
    elementchanged = board.state[zeroindex + 3]
    newpath = board.path[:]
    newstate = board.state[0:zeroindex] + elementchanged + board.state[zeroindex + 1:zeroindex + 3] + "0" + board.state[
                                                                                                            zeroindex + 4:]
    newboard = board_param(newstate, newpath + ["Down"], board.depth + 1)
    return (newboard)


def move_left(board, zeroindex):
    elementchanged = board.state[zeroindex - 1]
    newpath = board.path[:]
    newstate = board.state[0:zeroindex - 1] + "0" + elementchanged + board.state[zeroindex + 1:]
    newboard = board_param(newstate, newpath + ["Left"], board.depth + 1)
    return (newboard)


def move_right(board, zeroindex):
    elementchanged = board.state[zeroindex + 1]
    newpath = board.path[:]
    newstate = board.state[0:zeroindex] + elementchanged + "0" + board.state[zeroindex + 2:]
    newboard = board_param(newstate, newpath + ["Right"], board.depth + 1)
    return (newboard)


legaldict = {0: ["Down", "Right"],
             1: ["Down", "Left", "Right"],
             2: ["Down", "Left"],
             3: ["Up", "Down", "Right"],
             4: ["Up", "Down", "Left", "Right"],
             5: ["Up", "Down", "Left"],
             6: ["Up", "Right"],
             7: ["Up", "Left", "Right"],
             8: ["Up", "Left"]}


def legalmoves(board, zeroindex):
    return (legaldict[zeroindex])


def success(board, expanded, mytime, myram):
    f = open('output.txt', "w")
    f.write("path_to_goal: " + str(board.path) + "\n")
    f.write("cost_of_path: " + str(len(board.path)) + "\n")
    f.write("nodes_expanded: " + str(expanded) + "\n")
    f.write("search_depth: " + str(board.depth) + "\n")
    f.write("max_search_depth: " + str(board.depth) + "1" + "\n")
    f.write("running_time: " + str(mytime) + "\n")
    f.write("max_ram_usage: " + str(myram) + "\n")
    f.close()
        
def bfs(state):
    state = ''.join(state.split(','))
    time_start = timeit.default_timer()
    board = board_param(state, [], 0)
    queue = [board]
    frontier = {board.state : 0}
    explored = {}
    expanded = 0

    while len(queue) > 0:
        ## deque
        queue.pop(0)
        ## add explored
        explored[board.state] = 0
        ## checksuccess
        if board.state == '012345678':
            time_stop = timeit.default_timer()
            success(board, expanded, time_stop - time_start, resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
            break

        ## possible moves
        myindex = board.state.index("0")
        possiblemoves = legalmoves(board, myindex)

        ## generate new boards
        if "Up" in possiblemoves:
            newboard = move_up(board, myindex)
            if newboard.state not in frontier:
                if newboard.state not in explored:
                    queue.append(newboard)
                    frontier[newboard.state] = 0
                    expanded += 1

        if "Down" in possiblemoves:
            newboard = move_down(board, myindex)
            if newboard.state not in frontier:
                if newboard.state not in explored:
                    queue.append(newboard)
                    frontier[newboard.state] = 0
                    expanded += 1

        if "Left" in possiblemoves:
            newboard = move_left(board, myindex)
            if newboard.state not in frontier:
                if newboard.state not in explored:
                    queue.append(newboard)
                    frontier[newboard.state] = 0
                    expanded += 1

        if "Right" in possiblemoves:
            newboard = move_right(board, myindex)
            if newboard.state not in frontier:
                if newboard.state not in explored:
                    queue.append(newboard)
                    frontier[newboard.state] = 0
                    expanded += 1

        board = queue[0]
        
    return("Failure")
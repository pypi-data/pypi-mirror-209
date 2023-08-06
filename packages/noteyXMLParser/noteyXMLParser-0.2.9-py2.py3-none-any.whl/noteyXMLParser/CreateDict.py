from .played_sounds import *
import json


def createfingerDict():
    fingerDict = {}
    finger = 0
    for i in range(len(FretBoard)):
        for j in range(len(FretBoard[i])):
            # print(FretBoard[i][j])
            if j == 0:
                finger = j % 4
                print(finger)
            elif j % 4 == 0 or j >= 5:
                finger = 4
            else:
                finger = j % 4

            if FretBoard[i][j] in fingerDict:
                fingerDict[FretBoard[i][j]].append([i + 1, j, finger])
            else:
                fingerDict[FretBoard[i][j]] = [[i + 1, j, finger]]
            finger = 0
    return fingerDict


def createChromaToChord():
    chroma_to_chord = {}
    for i in CHORD_TYPES.keys():
        for k in CHORD_TYPES[i].keys():
            name = k + ":" + i
            chroma_to_chord[str(CHORD_TYPES[i][k])] = name
    return chroma_to_chord

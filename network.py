#!/usr/bin/env python
# -*- coding: utf-8 -*-

class network(object):

    learn_rate = 0.1
    qtdInputs = 0
    qtdOutputs = 0
    hiddenLayers = []
    matrix = 0
    matrixInputs = []


    def __init__(self, arg):
        super(network, self).__init__()
        self.arg = arg

    def setLearnRate(learn_rate):
        self.learn_rate = learn_rate

    def setQtdInputs(qtdInputs):
        self.qtdInputs = qtdInputs

    def setQtdOutputs(qtdOutputs):
        self.qtdOutputs = qtdOutputs

    def setInput(matrixInputs):
        self.matrixInputs = matrixInputs

    def clearHiddenLayer():
        self.hiddenLayers = []

    def addHiddenLayer(hiddenLayer):
        self.hiddenLayers.append(hiddenLayer)

    def removeHiddenLayer(hiddenLayerIndex):
        try:
            self.hiddenLayers.pop(hiddenLayerIndex)
        except IndexError:
            print "Trying to remove a unexistent hidden layer. Check it out the hidden layer index."
        except:
            print "Unexpected error: ", sys.exec_info()[0]
            raise

    def feedFoward():
        pass

    def backPorpagate():
        pass





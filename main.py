
import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from bfs import Graph_bfs
from dfs import Graph_dfs
from Uniform_Cost_Search import Graph_uniform
from Iterative_Deepening_Search import Graph_iterative
from astar import Graph_astar
from bestfirst_search import Graph_bestfirst
from Simulated_Annealing import SimulatedAnnealing
from Alpha_Beta_Pruning import AlphaBetaPruning

DG = nx.DiGraph()
G = nx.Graph()
Node1_arr = ['A'] * 30
Node2_arr = ['A'] * 30
Goal_list = []

class Ui_AISearchingTechniquesMainWindow(object):
    counter = 0
    counterG = 0
    EdgeWeight_arr = [1] * 30
    HeuristicDict = dict()
    H = {}
    graphastar = Graph_astar(directed=False)
    graphastarD = Graph_astar(directed=True)
    graphbestfirst = Graph_bestfirst()
    simulatedannealing = SimulatedAnnealing()
    alphabeta = AlphaBetaPruning()

    def GeneratePathClicked(self):
        original_stdout = sys.stdout

        with open('test.txt', 'w') as f:
            sys.stdout = f
            searchType = str(self.SearchTypecomboBox.currentText())
            graphType = str(self.GraphTypecomboBox.currentText())
            if graphType == "Undirectd Graph":
                if searchType == "BFS":
                    graphbfs = Graph_bfs(directed=False)
                    for i in range(0, self.counter):
                        graphbfs.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path1, goal = graphbfs.breadth_first_search(start, goals)
                    if traced_path1:
                        print('Path:', end=' ')
                        Graph_bfs.print_path(traced_path1, goal)
                        print()

                elif searchType == "DFS":
                    graphdfs = Graph_dfs(directed=False)
                    for i in range(0, self.counter):
                        graphdfs.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2, goal = graphdfs.depth_first_search(start, goals)
                    if traced_path2:
                        print('Path:', end=' ')
                        Graph_dfs.print_path(traced_path2, goal)
                        print()

                elif searchType == "Uniform Cost":
                    graphuniform = Graph_uniform(directed=False)
                    for i in range(0, self.counter):
                        graphuniform.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path3, cost1, goal = graphuniform.uniform_cost_search(int(start), goals)
                    if traced_path3:
                        print('Path:', end=' ')
                        Graph_uniform.print_path(traced_path3, goal)
                        print('\nCost:', cost1)

                elif searchType == "Iterative Deepening":
                    graphiterative = Graph_iterative(directed=False)
                    for i in range(0, self.counter):
                        graphiterative.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path4 = graphiterative.IDS(start, goals)
                    if traced_path4:
                        print(traced_path4)
                        print()

                elif searchType == "A*":
                    for i in range(0, self.counter):
                        self.graphastar.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    self.graphastar.set_huristics(self.HeuristicDict)
                    traced_path5, cost3, goal = self.graphastar.a_star_search(start, goals)
                    if traced_path5:
                        print('Path:', end=' ')
                        Graph_astar.print_path(traced_path5, goal)
                        print('\nCost:', cost3)

                elif searchType == "Best First":
                    for i in range(0, self.counter):
                        self.graphbestfirst.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    self.graphbestfirst.set_heuristics(self.HeuristicDict)
                    traced_path6, goal = self.graphbestfirst.best_first_search(start, goals)
                    if traced_path6:
                        print('Path:', end=' ')
                        Graph_bestfirst.print_path(traced_path6, goal)

                elif searchType == "Simulated Annealing":
                    for i in range(0, self.counter):
                        self.simulatedannealing.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goal = Goal_list[0]
                    traced_path7 = self.simulatedannealing.simulated_annealing(start, goal, 1, 0.5)
                    if traced_path7:
                        print('Path:', end=' ')
                        print(traced_path7)

            else:
                if searchType == "BFS":
                    graphbfs = Graph_bfs(directed=True)
                    for i in range(0, self.counter):
                        graphbfs.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path1, goal = graphbfs.breadth_first_search(start, goals)
                    if traced_path1:
                        print('Path:', end=' ')
                        Graph_bfs.print_path(traced_path1, goal)
                        print()

                elif searchType == "DFS":
                    graphdfs = Graph_dfs(directed=True)
                    for i in range(0, self.counter):
                        graphdfs.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path2, goal = graphdfs.depth_first_search(start, goals)
                    if traced_path2:
                        print('Path:', end=' ')
                        Graph_dfs.print_path(traced_path2, goal)
                        print()

                elif searchType == "Uniform Cost":
                    graphuniform = Graph_uniform(directed=True)
                    for i in range(0, self.counter):
                        graphuniform.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path3, cost1, goal = graphuniform.uniform_cost_search(start, goals)
                    if traced_path3:
                        print('Path:', end=' ')
                        Graph_uniform.print_path(traced_path3, goal)
                        print('\nCost:', cost1)

                elif searchType == "Iterative Deepening":
                    graphiterative = Graph_iterative(directed=True)
                    for i in range(0, self.counter):
                        graphiterative.add_edge(Node1_arr[i], Node2_arr[i])
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    traced_path4 = graphiterative.IDS(start, goals[0],6)
                    if traced_path4:
                        print(traced_path4)
                        print()

                elif searchType == "A*":
                    for i in range(0, self.counter):
                        self.graphastar.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    self.graphastar.set_huristics(self.HeuristicDict)
                    traced_path5, cost3, goal = self.graphastar.a_star_search(start, goals)
                    if traced_path5:
                        print('Path:', end=' ')
                        Graph_astar.print_path(traced_path5, goal)
                        print('\nCost:', cost3)

                elif searchType == "Best First":
                    for i in range(0, self.counter):
                        self.graphbestfirst.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goals = Goal_list
                    self.graphbestfirst.set_heuristics(self.HeuristicDict)
                    traced_path6, goal = self.graphbestfirst.best_first_search(start, goals)
                    if traced_path6:
                        print('Path:', end=' ')
                        Graph_bestfirst.print_path(traced_path6, goal)


                elif searchType == "Simulated Annealing":
                    graph = nx.DiGraph()
                    for i in range(0, self.counter):
                        self.simulatedannealing.add_edge(Node1_arr[i], Node2_arr[i], int(self.EdgeWeight_arr[i]))
                    start = self.StartNode_input.text()
                    goal = Goal_list[0]
                    traced_path7 = self.simulatedannealing.simulated_annealing(start, goal,1,0.5)
                    if traced_path7:
                        print('Path:', end=' ')
                        print(traced_path7)

        sys.stdout = original_stdout

        with open("test.txt") as f:
            contents = f.read()

        self.TheResult_Label.setText(contents)

    def GenerateGraphClicked(self):
        if self.GraphTypecomboBox.currentText() == "Undirected Graph":
            pos = nx.spring_layout(G)
            nx.draw(G, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(G, pos, font_size=26, edge_labels=nx.get_edge_attributes(G, 'weight'))
            plt.show()
        elif self.GraphTypecomboBox.currentText() == "Directed Graph":
            pos = nx.spring_layout(DG)
            nx.draw(DG, pos, with_labels=True, node_size=1500)
            nx.draw_networkx_edge_labels(DG, pos, font_size=26, edge_labels=nx.get_edge_attributes(DG, 'weight'))
            plt.show()

    def AddNodeClicked(self):
        N1 = self.Node1_input.text()
        N2 = self.Node2_input.text()
        W = self.EdgeWieght_input.text()
        G.add_edge(N1, N2, weight=W)
        DG.add_edge(N1, N2, weight=W)
        Node1_arr[self.counter] = N1
        Node2_arr[self.counter] = N2
        self.EdgeWeight_arr[self.counter] = int(W)
        self.counter = self.counter + 1
        self.Node1_input.clear()
        self.Node2_input.clear()
        self.EdgeWieght_input.clear()

    def HeuristicPushed(self):
        InputHeuristic = int(self.NodeHeuristic_input.text())
        InputNodeH = self.Node_Input.text()
        self.H[self.Node_Input.text()] = self.NodeHeuristic_input.text()
        self.HeuristicDict.update({InputNodeH: int(InputHeuristic)})
        self.graphastar.set_huristics(self.HeuristicDict)
        self.graphastarD.set_huristics(self.HeuristicDict)
        self.Node_Input.clear()
        self.NodeHeuristic_input.clear()

    def SubmitClicked(self):
        G = self.GoalNode_input.text()
        Goal_list.append(G)
        self.GoalNode_input.clear()

    def AlphaBetaClicked(self):
        # Perform Alpha-Beta Pruning here
        pass

    def SimulatedAnnealingClicked(self):
        # Perform Simulated Annealing here
        pass

    def setupUi(self, AISearchingTechniquesMainWindow):
        AISearchingTechniquesMainWindow.setObjectName("AISearchingTechniquesMainWindow")
        AISearchingTechniquesMainWindow.resize(779, 790)
        self.centralwidget = QtWidgets.QWidget(AISearchingTechniquesMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.SearchTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.SearchTypecomboBox.setGeometry(QtCore.QRect(630, 50, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.SearchTypecomboBox.setFont(font)
        self.SearchTypecomboBox.setObjectName("SearchTypecomboBox")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")
        self.SearchTypecomboBox.addItem("")  # Uniform Cost
        self.SearchTypecomboBox.addItem("")  # Iterative Deepening
        self.SearchTypecomboBox.addItem("")  # A*
        self.SearchTypecomboBox.addItem("")  # Best First
        self.SearchTypecomboBox.addItem("")  # Simulated Annealing
        self.SearchTypecomboBox.addItem("")  # Alpha-Beta Pruning

        self.GenerateGraphButton = QtWidgets.QPushButton(self.centralwidget)
        self.GenerateGraphButton.setGeometry(QtCore.QRect(630, 240, 131, 31))
        self.GenerateGraphButton.setObjectName("GenerateGraphButton")
        self.GenerateGraphButton.clicked.connect(self.GenerateGraphClicked)

        self.Node1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node1_input.setGeometry(QtCore.QRect(26, 48, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1_input.setFont(font)
        self.Node1_input.setText("")
        self.Node1_input.setObjectName("Node1_input")

        self.Node2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node2_input.setGeometry(QtCore.QRect(26, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2_input.setFont(font)
        self.Node2_input.setObjectName("Node2_input")

        self.Node1Label = QtWidgets.QLabel(self.centralwidget)
        self.Node1Label.setGeometry(QtCore.QRect(26, 25, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node1Label.setFont(font)
        self.Node1Label.setObjectName("Node1Label")

        self.Node2Label = QtWidgets.QLabel(self.centralwidget)
        self.Node2Label.setGeometry(QtCore.QRect(26, 78, 40, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node2Label.setFont(font)
        self.Node2Label.setObjectName("Node2Label")

        self.EdgeWieghtLabel = QtWidgets.QLabel(self.centralwidget)
        self.EdgeWieghtLabel.setGeometry(QtCore.QRect(26, 131, 72, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieghtLabel.setFont(font)
        self.EdgeWieghtLabel.setObjectName("EdgeWieghtLabel")

        self.EdgeWieght_input = QtWidgets.QLineEdit(self.centralwidget)
        self.EdgeWieght_input.setGeometry(QtCore.QRect(26, 157, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.EdgeWieght_input.setFont(font)
        self.EdgeWieght_input.setObjectName("EdgeWieght_input")

        self.AddNodesButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodesButton.setGeometry(QtCore.QRect(26, 189, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodesButton.setFont(font)
        self.AddNodesButton.setObjectName("AddNodesButton")
        self.AddNodesButton.clicked.connect(self.AddNodeClicked)

        self.TheResult_Label = QtWidgets.QLabel(self.centralwidget)
        self.TheResult_Label.setGeometry(QtCore.QRect(10, 280, 751, 481))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.TheResult_Label.setFont(font)
        self.TheResult_Label.setFrameShape(QtWidgets.QFrame.Box)
        self.TheResult_Label.setLineWidth(2)
        self.TheResult_Label.setText("")
        self.TheResult_Label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.TheResult_Label.setObjectName("TheResult_Label")

        self.GeneratePathButton = QtWidgets.QPushButton(self.centralwidget)
        self.GeneratePathButton.setGeometry(QtCore.QRect(460, 240, 131, 31))
        self.GeneratePathButton.setObjectName("GeneratePathButton")
        self.GeneratePathButton.clicked.connect(self.GeneratePathClicked)

        self.TheResultLabel = QtWidgets.QLabel(self.centralwidget)
        self.TheResultLabel.setGeometry(QtCore.QRect(10, 230, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.TheResultLabel.setFont(font)
        self.TheResultLabel.setObjectName("TheResultLabel")

        self.Node_Input = QtWidgets.QLineEdit(self.centralwidget)
        self.Node_Input.setGeometry(QtCore.QRect(227, 49, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.Node_Input.setFont(font)
        self.Node_Input.setText("")
        self.Node_Input.setObjectName("Node_Input")

        self.NodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeLabel.setGeometry(QtCore.QRect(227, 26, 33, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeLabel.setFont(font)
        self.NodeLabel.setObjectName("NodeLabel")

        self.NodeHeuristicLabel = QtWidgets.QLabel(self.centralwidget)
        self.NodeHeuristicLabel.setGeometry(QtCore.QRect(227, 78, 82, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristicLabel.setFont(font)
        self.NodeHeuristicLabel.setObjectName("NodeHeuristicLabel")

        self.NodeHeuristic_input = QtWidgets.QLineEdit(self.centralwidget)
        self.NodeHeuristic_input.setGeometry(QtCore.QRect(227, 101, 137, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.NodeHeuristic_input.setFont(font)
        self.NodeHeuristic_input.setObjectName("NodeHeuristic_input")

        self.AddNodeHeuristicButton = QtWidgets.QPushButton(self.centralwidget)
        self.AddNodeHeuristicButton.setGeometry(QtCore.QRect(227, 130, 117, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.AddNodeHeuristicButton.setFont(font)
        self.AddNodeHeuristicButton.setObjectName("AddNodeHeuristicButton")
        self.AddNodeHeuristicButton.clicked.connect(self.HeuristicPushed)

        self.StartNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.StartNode_input.setGeometry(QtCore.QRect(460, 50, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNode_input.setFont(font)
        self.StartNode_input.setObjectName("StartNode_input")

        self.GoalNode_input = QtWidgets.QLineEdit(self.centralwidget)
        self.GoalNode_input.setGeometry(QtCore.QRect(460, 100, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNode_input.setFont(font)
        self.GoalNode_input.setObjectName("GoalNode_input")

        self.StartNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.StartNodeLabel.setGeometry(QtCore.QRect(460, 26, 75, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.StartNodeLabel.setFont(font)
        self.StartNodeLabel.setObjectName("StartNodeLabel")

        self.GoalNodeLabel = QtWidgets.QLabel(self.centralwidget)
        self.GoalNodeLabel.setGeometry(QtCore.QRect(460, 78, 59, 16))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalNodeLabel.setFont(font)
        self.GoalNodeLabel.setObjectName("GoalNodeLabel")

        self.GoalAddButton = QtWidgets.QPushButton(self.centralwidget)
        self.GoalAddButton.setGeometry(QtCore.QRect(460, 130, 93, 28))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GoalAddButton.setFont(font)
        self.GoalAddButton.setObjectName("GoalAddButton")
        self.GoalAddButton.clicked.connect(self.SubmitClicked)

        self.GraphTypecomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.GraphTypecomboBox.setGeometry(QtCore.QRect(630, 150, 121, 22))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.GraphTypecomboBox.setFont(font)
        self.GraphTypecomboBox.setObjectName("GraphTypecomboBox")
        self.GraphTypecomboBox.addItem("")
        self.GraphTypecomboBox.addItem("")

        
        
        
        

        
        
        
        

        AISearchingTechniquesMainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AISearchingTechniquesMainWindow)
        self.statusbar.setObjectName("statusbar")
        AISearchingTechniquesMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AISearchingTechniquesMainWindow)
        QtCore.QMetaObject.connectSlotsByName(AISearchingTechniquesMainWindow)

    def retranslateUi(self, AISearchingTechniquesMainWindow):
        _translate = QtCore.QCoreApplication.translate
        AISearchingTechniquesMainWindow.setWindowTitle(_translate("AISearchingTechniquesMainWindow", "AI Searching Techniques"))
        self.SearchTypecomboBox.setItemText(0, _translate("AISearchingTechniquesMainWindow", "Select"))
        self.SearchTypecomboBox.setItemText(1, _translate("AISearchingTechniquesMainWindow", "BFS"))
        self.SearchTypecomboBox.setItemText(2, _translate("AISearchingTechniquesMainWindow", "DFS"))
        self.SearchTypecomboBox.setItemText(3, _translate("AISearchingTechniquesMainWindow", "Uniform Cost"))
        self.SearchTypecomboBox.setItemText(4, _translate("AISearchingTechniquesMainWindow", "Iterative Deepening"))
        self.SearchTypecomboBox.setItemText(5, _translate("AISearchingTechniquesMainWindow", "A*"))
        self.SearchTypecomboBox.setItemText(6, _translate("AISearchingTechniquesMainWindow", "Best First"))
        self.SearchTypecomboBox.setItemText(7, _translate("AISearchingTechniquesMainWindow", "Simulated Annealing"))
        self.SearchTypecomboBox.setItemText(8, _translate("AISearchingTechniquesMainWindow", "Alpha-Beta Pruning"))
        self.GenerateGraphButton.setText(_translate("AISearchingTechniquesMainWindow", "Generate Graph"))
        self.Node1Label.setText(_translate("AISearchingTechniquesMainWindow", "Node 1"))
        self.Node2Label.setText(_translate("AISearchingTechniquesMainWindow", "Node 2"))
        self.EdgeWieghtLabel.setText(_translate("AISearchingTechniquesMainWindow", "Edge Weight"))
        self.AddNodesButton.setText(_translate("AISearchingTechniquesMainWindow", "Add Nodes"))
        self.GeneratePathButton.setText(_translate("AISearchingTechniquesMainWindow", "Generate Path"))
        self.TheResultLabel.setText(_translate("AISearchingTechniquesMainWindow", "The Result"))
        self.NodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Node"))
        self.NodeHeuristicLabel.setText(_translate("AISearchingTechniquesMainWindow", "Node Heuristic"))
        self.AddNodeHeuristicButton.setText(_translate("AISearchingTechniquesMainWindow", "Add Node Heuristic"))
        self.StartNodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Start Node"))
        self.GoalNodeLabel.setText(_translate("AISearchingTechniquesMainWindow", "Goal Node"))
        self.GoalAddButton.setText(_translate("AISearchingTechniquesMainWindow", "Add"))
        self.GraphTypecomboBox.setItemText(0, _translate("AISearchingTechniquesMainWindow", "Undirected Graph"))
        self.GraphTypecomboBox.setItemText(1, _translate("AISearchingTechniquesMainWindow", "Directed Graph"))
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AISearchingTechniquesMainWindow = QtWidgets.QMainWindow()
    ui = Ui_AISearchingTechniquesMainWindow()
    ui.setupUi(AISearchingTechniquesMainWindow)
    AISearchingTechniquesMainWindow.show()
    sys.exit(app.exec_())


import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

import kmeans
import spectralClustering
import meanShift
import dbscan
import optics
import affinityPropagation
import elbowKmeans
from algorithms.patternmining.createDB import createDB
from algorithms.patternmining.euclidDistance import EuclidDistance
import periodicFrequentPattern


class GUImain:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("miniRasterminer: Discovering Knowledge Hidden in Raster Images")
        self.root.minsize(600,400)

    def uploadInputDir(self, event=None):
        # filename = filedialog.askopenfilename()
        inputDir = filedialog.askdirectory()
        print('Selected:', inputDir)
        inputRasterFolder = inputDir
        return inputRasterFolder

    def uploadOutputDir(self, event=None):
        # filename = filedialog.askopenfilename()
        outDir = filedialog.askdirectory()
        print('Selected:', outDir)
        outputFolder = outDir
        return outputFolder

    def uploadInputFile(self):
        inputFile = filedialog.askopenfilename()
        print('selected:', inputFile)
        return inputFile

    def uploadOutputFile(self):
        outputFile = filedialog.askopenfilename()
        print('selected:', outputFile)
        return outputFile

    def judgeClusteringAlg(self, target):
        self.root.destroy()
        if target == 'k-Means/k-Means++':
            kmeans.kmeansGUI().Main()
        elif target == 'DBScan':
            dbscan.DBScanGUI().Main()
        elif target == 'MeanShift':
            meanShift.meanShiftGUI().Main()
        elif target == 'SpectralClustering':
            spectralClustering.spectralGUI().Main()
        elif target == 'OPTICS':
            optics.opticsGUI().Main()
        elif target == 'AffinityPropagation':
            affinityPropagation.affinityPropagationGUI().Main()
        elif target == 'Elbow-kmeans':
            elbowKmeans.elbowKmeansGUI().Main()
        # elif target == 'Elbow-kmeans++':
        #     elbowKmeansPl.elbowKmeansPlGUI().Main()

    def judgePatternMiningAlg(self, target):
        self.root.destroy()
        if target == 'Frequent-spatial Pattern':
            periodicFrequentPattern.periodicFrequentPattern().Main()
    #def judgeClassificationAlg(self):
        # if oneNNEDFlag == True:

    def rootGUI(self):


        clusteringAlgorithms = {'Parameter tuning': ["Elbow-kmeans", "Elbow-kmeans++"],
                          'individual algorithm': ["k-Means/k-Means++", "DBScan", "SpectralClustering", "MeanShift",
                                                   "OPTICS","BIRCH","AffinityPropagation"]}
        pamiAlgorithms = ['Periodic-frequent Pattern', 'Partial-periodic Pattern', 'Frequent-spatial Pattern', 'Periodic-frequent spatial Pattern']
        classificationOptions = ['1folderValue','prediction']
        mineOptions = ['Temporal File', 'Neighborhood File', 'Mining']
        condition = ['<=', '>=','<','>']


        tabControl = ttk.Notebook(self.root)
        tab2 = ttk.Frame(tabControl)
        tab3 = ttk.Frame(tabControl)
        tab4 = ttk.Frame(tabControl)
        tab5 = ttk.Frame(tabControl)

        subTab2 = ttk.Notebook(tab2,height=450,width=850)
        subTab2.pack(expand=True,side='top',fill='both')
        subTab3 = ttk.Notebook(tab3,height=450,width=850)
        subTab3.pack(expand=True,side='top',fill='both')
        subTab4 = ttk.Notebook(tab4,height=450,width=850)
        subTab4.pack(expand=True,side='top',fill='both')

        tabControl.add(tab2, text='Pattern Mining')
        tabControl.add(tab3, text='Clustering')
        tabControl.add(tab4, text='Classification')
        tabControl.add(tab5, text='Prediction')
        tabControl.pack(expand=1, fill="both")

        v2 = tk.StringVar()

        inputTempFileName = tk.StringVar()
        conditionVar = tk.StringVar()
        thresholdVar = tk.StringVar()
        inputNeighborFileVar = tk.StringVar()
        outputNeighborFolderVar = tk.StringVar()
        pamiAlgVar = tk.StringVar()
        oTempFolderVar = tk.StringVar()
        oneNNEDFlag = tk.BooleanVar()
        oneNNEDTWFlag = tk.BooleanVar()
        oneNNHausdorffFlag = tk.BooleanVar()
        oneNNmaxinormFlag = tk.BooleanVar()



        for mineOption in mineOptions:
            subFrame2 = ttk.Frame(subTab2)
            subTab2.add(subFrame2, text=mineOption)
            if mineOption == 'Temporal File':
                iTempFile_label = ttk.Label(subFrame2, text='input file')
                iTempFile_label.grid(column=0, row=0, padx=60, pady=30, sticky='W')
                iTempFile_TB = ttk.Entry(subFrame2, textvariable=inputTempFileName, width=40)
                iTempFile_TB.grid(column=1, row=0, padx=60, pady=30)
                iTempFile_B = tk.Button(subFrame2, text='Browse',
                                    command=lambda :inputTempFileName.set(str(self.uploadInputFile())))
                iTempFile_B.grid(row=0, column=2, padx=60, pady=30)

                oTempFolder_label = ttk.Label(subFrame2, text='output folder')
                oTempFolder_label.grid(column=0, row=1, padx=60, pady=30, sticky='W')
                oTempFolder_TB = ttk.Entry(subFrame2, textvariable=oTempFolderVar, width=40)
                oTempFolder_TB.grid(column=1, row=1, padx=60, pady=30)
                oTempFolder_B = tk.Button(subFrame2, text='Browse',
                                    command=lambda :oTempFolderVar.set(str(self.uploadOutputDir())))
                oTempFolder_B.grid(row=1, column=2, padx=60, pady=30)

                condition_label = ttk.Label(subFrame2, text='condition')
                condition_label.grid(column=0,row=2, padx=60, pady=30, sticky='W')
                condition_CB = ttk.Combobox(subFrame2, textvariable=conditionVar, values=condition, state='readonly')
                condition_CB.grid(column=1, row=2, padx=60, pady=30)

                threshold_label = ttk.Label(subFrame2, text='threshold')
                threshold_label.grid(column=0, row=3, padx=60, pady=30)
                threshold_TB = ttk.Entry(subFrame2, textvariable=thresholdVar)
                threshold_TB.grid(column=1, row=3, padx=60, pady=30)

                submit = tk.Button(subFrame2, text='submit', command=lambda :createDB(inputTempFileName.get(), oTempFolderVar.get()
                                                                                      ,conditionVar.get(), int(thresholdVar.get())).run())
                submit.grid(row=4, column=0, pady=30)

            elif mineOption == 'Mining':
                patternMiningAlg_label = ttk.Label(subFrame2, text='select the algorithm')
                patternMiningAlg_label.grid(column=0, row=0, padx=60, pady=30, sticky='W')

                patternMiningAlg_CB = ttk.Combobox(subFrame2, textvariable=pamiAlgVar, values=pamiAlgorithms, state='readonly',width=50)
                patternMiningAlg_CB.grid(column=1, row=0, padx=60, pady=30)

                submit = tk.Button(subFrame2, text='submit', command=lambda : self.judgePatternMiningAlg(pamiAlgVar.get()))
                submit.grid(row=1, column=0, pady=30)

            elif mineOption == 'Neighborhood File':
                iNeighborFile_label = ttk.Label(subFrame2, text='Select the file:')
                iNeighborFile_label.grid(row=0, column=0, padx=60, pady=30, sticky='W')
                iNeighborFile_TB = tk.Entry(subFrame2, textvariable=inputNeighborFileVar, width=40)
                iNeighborFile_TB.grid(row=0, column=1)

                iNeighborFile_B = tk.Button(subFrame2, text='Browse',
                                    command=lambda: inputNeighborFileVar.set(str(self.uploadInputFile())))
                iNeighborFile_B.grid(row=0, column=2, padx=60)

                outputNeighborFolder_label = ttk.Label(subFrame2, text='Select output folder:')
                outputNeighborFolder_label.grid(column=0, row=1, padx=60, pady=30, sticky='W')
                outputNeighborFolder_TB = tk.Entry(subFrame2, textvariable=outputNeighborFolderVar, width=40)
                outputNeighborFolder_TB.grid(row=1, column=1)

                outputNeighborFolder_B = tk.Button(subFrame2, text='Browse',
                                    command=lambda: outputNeighborFolderVar.set(str(self.uploadOutputDir())))
                outputNeighborFolder_B.grid(row=1, column=2, padx=60)

                threshold_label = ttk.Label(subFrame2, text='threshold')
                threshold_label.grid(column=0, row=2, padx=60, pady=30)
                threshold_TB = ttk.Entry(subFrame2, textvariable=thresholdVar)
                threshold_TB.grid(column=1, row=2, padx=60, pady=30)

                submit = tk.Button(subFrame2, text='submit', command=lambda :EuclidDistance(inputNeighborFileVar.get(), outputNeighborFolderVar.get(),
                                                                                            int(thresholdVar.get())).run())
                submit.grid(row=3, column=0, pady=30)

        for algorithm in clusteringAlgorithms.keys():
            subFrame3 = ttk.Frame(subTab3)
            subTab3.add(subFrame3,text=algorithm)
            cb2 = ttk.Combobox(subFrame3, textvariable=v2, state='readonly')
            cb2.place(relx=0.25, rely=0.5, relwidth=0.5)
            if algorithm == 'Parameter tuning':
                cb2.config(values=clusteringAlgorithms['Parameter tuning'])
            elif algorithm == 'individual algorithm':
                cb2.config(values=clusteringAlgorithms['individual algorithm'])
            submit = ttk.Button(subFrame3, text='submit', command=lambda :self.judgeClusteringAlg(v2.get()))
            submit.place(relx=0.378, rely=0.7, relwidth=0.25, relheight=0.125)

        for classificationOption in classificationOptions:
            subFrame4 = ttk.Frame(subTab4)
            subTab4.add(subFrame4,text=classificationOption)
            oneNNED_CHB = ttk.Checkbutton(subFrame4,text='1NNED',variable=oneNNEDFlag)
            oneNNED_CHB.grid(row=0, column=0, padx=30, pady=30)
            oneNNEDTW_CHB = ttk.Checkbutton(subFrame4,text='1NNEDTW',variable=oneNNEDTWFlag)
            oneNNEDTW_CHB.grid(row=0, column=1, padx=30, pady=30)
            oneNNHausdorff_CHB = ttk.Checkbutton(subFrame4,text='1NNHausdorff',variable=oneNNHausdorffFlag)
            oneNNHausdorff_CHB.grid(row=1, column=0, padx=30, pady=30)
            oneNNmaxinorm_CHB = ttk.Checkbutton(subFrame4,text='1NNmaxinorm',variable=oneNNmaxinormFlag)
            oneNNmaxinorm_CHB.grid(row=1, column=1, padx=30, pady=30)
            if classificationOption == '1folderValue':
                iTrainingFile_label = ttk.Label(subFrame4, text='input training file')
                iTrainingFile_label.grid(column=0, row=2, padx=60, pady=30, sticky='W')
                iTrainingFile_TB = ttk.Entry(subFrame4, textvariable=inputTempFileName, width=40)
                iTrainingFile_TB.grid(column=1, row=2, padx=60, pady=30)
                iTrainingFile_B = tk.Button(subFrame4, text='Browse',
                                    command=lambda :inputTempFileName.set(str(self.uploadInputFile())))
                iTrainingFile_B.grid(row=2, column=2, padx=60, pady=30)

                iTestingFile_label = ttk.Label(subFrame4, text='input test file')
                iTestingFile_label.grid(column=0, row=3, padx=60, pady=30, sticky='W')
                iTestingFile_TB = ttk.Entry(subFrame4, textvariable=inputTempFileName, width=40)
                iTestingFile_TB.grid(column=1, row=3, padx=60, pady=30)
                iTestingFile_B = tk.Button(subFrame4, text='Browse',
                                    command=lambda :inputTempFileName.set(str(self.uploadInputFile())))
                iTestingFile_B.grid(row=3, column=2, padx=60, pady=30)
            if classificationOption == 'prediction':
                iPredictionFile_label = ttk.Label(subFrame4, text='input file for prediction')
                iPredictionFile_label.grid(column=0, row=2, padx=60, pady=30, sticky='W')
                iPredictionFile_TB = ttk.Entry(subFrame4, textvariable=inputTempFileName, width=40)
                iPredictionFile_TB.grid(column=1, row=2, padx=60, pady=30)
                iPredictionFile_B = tk.Button(subFrame4, text='Browse',
                                    command=lambda :inputTempFileName.set(str(self.uploadInputFile())))
                iPredictionFile_B.grid(row=2, column=2, padx=60, pady=30)


        self.root.mainloop()

if __name__ == '__main__':
    GUImain().rootGUI()

# def elbowAlgSelected():
#     selectBtn1.state(['pressed'])
#     selectBtn2.state(['!pressed'])
# def simpleAlgSelected():
#     selectBtn1.state(['!pressed'])
#     selectBtn2.state(['pressed'])

# ttk.Label(subFrame3, text='Select algorithm',font=("Arial", 20)).place(relx=0,rely=0,relwidth=1,relheight=0.125)

# make textbox

# button3 = tk.Button(tab3, text='submit', command=)

# v2 = tk.StringVar()

# selectBtn1 = ttk.Button(tab3,text='Parameter tuning',padding=(10),command=elbowAlgSelected)
# selectBtn1.bind('<1>', lambda e: cb2.config(values=Algorithms['elbowAlg']))
# selectBtn2 = ttk.Button(tab3,text='Individual algorithms',padding=(10),command=simpleAlgSelected)
# selectBtn2.bind('<1>', lambda e: ))
# selectBtn1.place(relx=0,rely=0.2,relwidth=0.5,relheight=0.125)
# selectBtn2.place(relx=0.5,rely=0.2,relwidth=0.5,relheight=0.125)
# selectBtn1.grid(row=1,column=1,sticky='W')
# selectBtn2.grid(row=1,column=2,sticky='W')
# print(str(v2.get))



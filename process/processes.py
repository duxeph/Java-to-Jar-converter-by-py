from control.controllers import Controllers
from os import system


class Processes:
    def __init__(self, main_path, path, files, ind, ui):
        self.main_path = main_path
        self.path = path
        self.files = files
        self.ind = ind
        self.ui = ui

    def convertionStartProcess(self):
        print("[INFO] Convertion is started.")
        self.cppOne()

    def cppOne(self):  # convertion process part one
        c1 = "javac -d . " + self.path[1:]  # series of c$ means command $ such as c1 = command 1
        try:
            system(c1)  # javac -d . com/company/Main.java

            print("[INFO] Part 1 is completed. .class file(s) was created.")
            self.ui.barProgress.setValue(1)

            self.cppTwo()
        except Exception as e:
            print("[EXCEPTION] Part 1: " + str(e))
            self.ui.labelShortInfo.setText("[EXCEPTION]")
            self.ui.labelInfo.setText("Part 1 is failed.")

    def cppTwo(self):
        self.manifestPath = '/'.join(self.path.split("/")[1:-1]) + "/MANIFEST.MF"
        c2 = "echo \"Main-class: " + '.'.join(self.path.split("/"))[1:-5] + "\" >> " + self.manifestPath
        try:
            system(c2)  # echo "Main-class: com.company.Main" >> com/company/MANIFEST.MF

            print("[INFO] Part 2 is completed. MANIFEST.MF is written.")
            self.ui.barProgress.setValue(2)

            self.cppThree()
        except Exception as e:
            print("[EXCEPTION] Part 2: " + str(e))
            self.ui.labelShortInfo.setText("[EXCEPTION]")
            self.ui.labelInfo.setText("Part 2 is failed.")

    def cppThree(self):
        self.jarPath = self.path[1:-5] + ".jar"
        files = Controllers().getPathInfo()
        classes = " "
        for i in range(len(files)):
            for j in range(len(files[i][1])):
                file = files[i][0] + "/" + files[i][1][j]
                classes += ('/'.join(file.split('/')[self.ind:]) + " ") if file.endswith(".class") else ""
        c3 = "jar -cvmf " + self.manifestPath + " " + self.jarPath + classes
        try:
            system(c3)  # jar -cvmf com/company/MANIFEST.MF com/company/Main.jar *

            print("[INFO] Part 3 is completed. .jar file was created.")
            self.ui.barProgress.setValue(3)

            self.cppFour()
        except Exception as e:
            print("[EXCEPTION] Part 3: " + str(e))
            self.ui.labelShortInfo.setText("[EXCEPTION]")
            self.ui.labelInfo.setText("Part 3 is failed.")

    def cppFour(self):
        c4 = "chmod +x " + self.jarPath
        try:
            system(c4)  # chmod + x com/company/Main.jar

            print("[INFO] Part 4 is completed. .jar files was converted into an executable file.")
            self.ui.barProgress.setValue(4)

            self.convertionEndProcess()
        except Exception as e:
            print("[EXCEPTION] Part 4: " + str(e))
            self.ui.labelShortInfo.setText("[EXCEPTION]")
            self.ui.labelInfo.setText("Part 4 is failed.")

    def convertionEndProcess(self):
        print("Deletion process starts ---")
        Controllers().destroyNewPathInfos(self.files, self.ui, self.main_path[:-5] + ".jar")
        print("Deletion process end. ---")

        print("[SUCCEED] Convertion process has been completed.")
        self.ui.labelShortInfo.setText("[SUCCEED]")
        self.ui.labelInfo.setText("Process is done.")
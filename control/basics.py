class Basics:
    def checkVersions(self, ui):
        from control.controllers import Controllers
        if not Controllers().checkVersions(): # "update-alternatives --config java(or javac)" is a good way to solve that in ubuntu
            print("[EXCEPTION] App could not configured: chosen Java and Javac versions are not same.\n[LOG] Java version: " + Controllers().checkJava() + " :: Javac version: " + Controllers().checkJavac())
            ui.labelShortInfo.setText("[EXCEPTION]")
            ui.labelInfo.setText("Java and Javac versions are not same.")
            ui.buttonPath.setEnabled(False)
            ui.buttonExit.setDefault(True)
        else:
            print("[INFO] Java and Javac versions are same. (Runnable)")

    def mainFilePathSelection(self, main_path, ui):
        ui.lineEditPath.setText(main_path)

        ui.lineEditPath.setEnabled(True)

        print("[INFO] Path updated: " + main_path)
        ui.labelShortInfo.setText("[INFO]")
        ui.labelInfo.setText("Path updated.")

    def pathControlDirector(self, main_path, ui):
        from control.controllers import Controllers
        path,_ = Controllers().checkPathes(main_path, ui.lineEditPath.text())

        if path == -1: pass_case = False
        else: pass_case = True

        ui.buttonStart.setEnabled([True if pass_case == True else False][0])
        print("[INFO] Path controlled. Pass case: " + ["Yes" if pass_case == True else "No"][0])
        ui.labelShortInfo.setText("[INFO]")
        ui.labelInfo.setText(["Runnable" if pass_case == True else "Not Runnable"][0])

    def takeConvertionAsk(self, main_path, ui):
        print("[INFO] Start pressed.")
        ui.labelShortInfo.setText("[INFO]")
        ui.labelInfo.setText("Start pressed.")

        from os import chdir
        from control.controllers import Controllers
        from process.processes import Processes
        path,ind = Controllers().checkPathes(main_path, ui.lineEditPath.text())
        print("[INFO] Path is chosen as: " + path)
        new_path = '/'.join(main_path.split('/')[:ind])
        chdir(new_path)
        print("[INFO] Path changed into: " + new_path)

        files = Controllers().getPathInfo()
        Processes(main_path, path, files, ind, ui).convertionStartProcess()
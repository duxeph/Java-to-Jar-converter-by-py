class Controllers:
    def checkPathes(self, main_path, path):
        i1 = main_path.split('/')[1:]
        i2 = path.split('/')[1:]
        ind = -1
        for i in range(len(i1)):
            if i1[i:] == i2:
                ind = i
                break

        if ind != -1 and main_path != path and path[0] == "/":
            return path, ind + 1
        else:
            return -1, -1


    def checkJava(self):
        from subprocess import getstatusoutput
        version = getstatusoutput('java -version')[1].split('"')[1]
        return version

    def checkJavac(self):
        from subprocess import getstatusoutput
        version = getstatusoutput('javac -version')[1][6:] # (javac = 5 chars) + (<space> = 1 char) = 6 char => start from sixth index since starts from 0
        return version

    def checkVersions(self):
        pass_case = False
        if self.checkJava() == self.checkJavac():
            pass_case = True
        return pass_case


    def getPathInfo(self):
        from os import getcwd, walk
        files = [(x[0], x[2]) for x in walk(getcwd())]
        return files

    def destroyNewPathInfos(self, old, ui, jarPath):
        from os import remove
        new = self.getPathInfo()
        try:
            for i in range(len(new)):
                for j in range(len(new[i][1])):
                    if old[i][1].count(new[i][1][j]) == 0:
                        gonna_deleted = new[i][0] + '/' + new[i][1][j]
                        if gonna_deleted != jarPath:
                            remove(gonna_deleted)
                            print("[INFO] " + new[i][1][j] + " is removed.")
                            ui.labelShortInfo.setText("[INFO]")
                            ui.labelInfo.setText(new[i][1][j] + " is removed.")
                        else:
                            print("[INFO] " + new[i][1][j] + " is passed.")
                            ui.labelShortInfo.setText("[INFO]")
                            ui.labelInfo.setText(new[i][1][j] + " is passed.")
        except Exception as e:
            print("[EXCEPTION] " + str(e))
            ui.labelShortInfo.setText("[EXCEPTION]")
            ui.labelInfo.setText("Destroying new files failed.")
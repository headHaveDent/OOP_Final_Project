import datetime as dt
import json # Kinda Overkill
from pathlib import Path

class NoJsonFile(Exception): pass

class ProblemDataLog:

    def __init__(self):
        self._file = None
        self._log_path = Path("json") / "problemlog.jsonl"
        self._name_path = Path("json") / "username.json"
        self._lost_file = False

        self._user_name = self.getNameString()

    #Checks if either username.json or problemlog.jsonl exist, creates it otherwise
    def _check_file_log(self, _log_path):
        try:
            if not _log_path.exists():
                self._lost_file = True
                raise NoJsonFile

        except NoJsonFile:
            lost_file = _log_path.stem + _log_path.suffix
            if not _log_path.parent.exists():
                lost_file = str(_log_path.parent) + " directory"

            _log_path.parent.mkdir(parents=True, exist_ok=True)
            _log_path.touch(exist_ok=True)

            if _log_path == self._name_path:
                with open(self._name_path, "w", encoding="utf-8") as json_file:
                    json.dump({"userName": "User"}, json_file, ensure_ascii=False, indent=4)


            #Write an error message with some details
            with self._log_path.open(mode="a", encoding="utf-8") as jsonl_file:
                newProblemDataLog = {"name": "SYSTEM",
                                    "date": dt.datetime.now().strftime("%Y-%m-%d"),
                                    "time": dt.datetime.now().strftime("%H:%M:%S"),
                                    "problem": str(lost_file) + " NOT FOUND"
                                    }
                jsonl_file.write(json.dumps(newProblemDataLog) + "\n")

    def is_lost_file(self):
        return self._lost_file

    #return the value username in string
    def getNameString(self):
        self._check_file_log(self._name_path)
        with open(self._name_path, "r", encoding="utf-8") as jsonl_file:  # parse one JSON object
            return json.load(jsonl_file)["userName"]

    #renames the username
    def rename(self, newName):
        self._user_name = newName
        newName = {"userName": newName}
        self._check_file_log(self._name_path)
        with open(self._name_path, "w", encoding="utf-8") as jsonl_file:
            json.dump(newName, jsonl_file, ensure_ascii=False, indent=4)

    #add a log into the problemlog.jsonl
    def addProblemDataLog(self, ProblemName):
        self._check_file_log(self._log_path)
        newProblemDataLog = {"name": self._user_name,
                            "date": dt.datetime.now().strftime("%Y-%m-%d"),
                            "time": dt.datetime.now().strftime("%H:%M:%S"),
                            "problem": ProblemName
                            }
        with open(self._log_path, "a", encoding="utf-8") as json_file:
            json_file.write(json.dumps(newProblemDataLog) + "\n")

    #returns formatted log for texts
    def getLogString(self):
        self._check_file_log(self._log_path)
        with open(self._log_path, "r", encoding="utf-8"):

            lines = []
            text = Path(self._log_path).read_text(encoding="utf-8")

            for line in text.splitlines():
                line = line.strip()
                if not line:  # skip blank lines
                    continue

                record = json.loads(line)  # parse one JSON object
                text = ", ".join(f"{key}: {value}" for key, value in record.items())
                lines.append(text)

            return "\n".join(lines)

    #clears the log (duh)
    def clearLog(self):
        with open(self._log_path, "w", encoding="utf-8"):
            pass

problem_log = ProblemDataLog()





"""
### TESTING AREA BEGINS ###
### WILL DESTROY DATA IN JSONL IF RUN AS PART OF TEST ###
''' Below are test code for this python code
Runs if directly Executed
Does not run if used as module '''

def main():
    admin = ProblemDataLog()
    admin.addProblemDataLog("Problem")
    admin.addProblemDataLog("Problem2")

    admin.rename("Test")
    admin.addProblemDataLog("Problem3")

    dataa = admin.getLog()
    for data in dataa:
        print(f"{data}")

    #admin.clearLog() #TESTING THE clearLog()
    print("Log Cleared")
    dataa = admin.getLogString()
    print(dataa)

if __name__ == '__main__':
    main()

### TESTING AREA END ###
"""



"""# Unused methods for ProblemDataLog. It is here for possible future use
#returns raw name
def getName(self):

    self._check_file_log(self._name_path)
    with open(self._name_path, "r", encoding="utf-8") as jsonl_file:
        return json.load(jsonl_file)

#returns raw log in dict
def getLog(self):
    data = []
    with open(self._log_path, "r", encoding="utf-8") as f:
        for line in f:
            data.append(json.loads(line))
    return data
"""
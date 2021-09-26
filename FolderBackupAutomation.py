import dropbox
import os
import time
from dropbox.files import WriteMode

startTime = time.time()

class TransferData:
    def __init__(self,accessToken):
        self.accessToken = accessToken

    def uploadFolder(self, origin, destination):
        dbx = dropbox.Dropbox(self.accessToken)

        for root, dirs, files in os.walk(origin):
            for fileName in files:
                localPath = os.path.join(root, fileName)
                relativePath = os.path.relpath(localPath, origin)
                dropboxPath = os.path.join(destination, relativePath).replace('\\', '/')

                print(relativePath)
                print(dropboxPath)

                with open(localPath, 'rb') as f:
                    dbx.files_upload(f.read(), dropboxPath, mode = WriteMode('overwrite'))

        startTime = time.time

def main():
    while True:
        accessToken = '3MrzxP9a90oAAAAAAAAAAR8WRNqeC_foH2_6XA8UIH5eyD94Bt2-3kHLMweU73nk'
        transferData = TransferData(accessToken)

        origin = "BackupPython"
        destination = "/BackupAutomation/"

        if (time.time() - startTime) >= 3600:
            transferData.uploadFolder(origin, destination)
            print("Files have been moved")

main()
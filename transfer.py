import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to,)

def main():
    access_token = '1SqVpfBX6uYAAAAAAAAAAVr3am6BUP7GLrWA1-sMgvJXMWC28mXz-nMyaAFk6wES'
    #generate the token once again on dropbox it will work
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer : -")
    # commands.txt
    
    # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.
    file_to = input("enter the full path to upload to dropbox:- ") 
    # /san1--2/commands.txt or /first/commands.txt

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")

if __name__ == '__main__':
    main()
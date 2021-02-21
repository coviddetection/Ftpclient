
from ftplib import FTP




def download():
    file_download=input("file for download")  
    file_write=input("file for write:")
    with open(file_write,'wb') as f:
        ftp.retrbinary('RETR'+file_download,f.write,1024)
        except:
            print("cannot download file")
        ftp.quit()
    except:
        print("cannot open target file")



def upload():
    file_upload=input("file for upload:")
    with open(file_upload,'rb') as f:
        ftp.storbinary('STOR'+file_upload,f)
        except:
            print("cannot upload file")
        ftp.quit()
    except:
        print("cannot open target file")
    
    
    



ip=input("server_ip:")
user=input("username:")
password=input("password:")




with FTP(ip) as ftp:
    ftp.login(user=user,passwd=password)
    except:
        print("cannot connect to server")

    
    print(ftp.getwelcome())
    islem=input("islem:")
    if islem=="upload":
        upload()
    if islem=="download":
        download()
    if islem=="select dir":
        directory=input("directory:")
        ftp.cwd(directory)


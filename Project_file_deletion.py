#This script helps you to delete the file (x number of days old) with specific extentsion from a directory

#!/usr/bin/python3

import os, time, shutil, sys


def deletefile():

    from datetime import datetime
    date = datetime.now().strftime("%Y_%m_%d_%p")
    log_file_name= f'/log{date}.txt'
   
   
    timein_seconds = time.time() - (1 * 3)
    extension = ".docx"
    path = "C:/Users/ABC/XYZ"
    log_path=(f'{path}{log_file_name}')
 
    
    sys.stdout = open(f'{log_path}', "w")

       
    
    if os.path.exists(path):
            for root_folder, folders, files in os.walk(path):
                for i in os.listdir(path):
                    segment_file = os.path.join(path, i)
                    # print(segment_file)
                    file_extension = os.path.splitext(segment_file)[1]
                    # if not os.path.isfile(segment_file):
                    #  continue
                    if os.path.isfile(segment_file) and os.stat(segment_file).st_mtime <= timein_seconds and extension == file_extension: 
                        
                        try:
                            os.remove(segment_file)
                            print(f"{segment_file} deleted successfully")
                            
                        except:
                            print("Check the error with file extension",i)
                    
            else:
                print("Could not remove file as there are no files older than 7 days or file with csv extension does not exist")                 

sys.stdout.close()
deletefile()
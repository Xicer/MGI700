import pandas as pd
import os
import fnmatch
import watchdog.events
import watchdog.observers
import time
import shutil
import turtle
from turtle import textinput


os.chdir('c:/users/mohamed.hagog/documents/mgi7000')


## Watchdog for checking if a file is updated or created in a set folder. 
class Handler(watchdog.events.PatternMatchingEventHandler):
    def __init__(self):
        # Set the patterns for PatternMatchingEventHandler
        watchdog.events.PatternMatchingEventHandler.__init__(self, patterns=['*.csv'],
                                                             ignore_directories=True, case_sensitive=False)
  
    def on_created(self, event):
 
        

        for file in fnmatch.filter(os.listdir("."), '*.csv'):
            # remove input files
            time.sleep(2)
            if fnmatch.fnmatch(file, '?????????????? Input.csv'):
                try :
                    os.replace(file, '../inputfiles/' + file)
                except OSError as e:
                    print(f"{type(e)}: {e}")

            if fnmatch.fnmatch(file, '?????????????? Output Position? 0.csv') or fnmatch.fnmatch(file, '?????????????? Output Position?? 0 .csv'): 
                

                try :
                    os.replace(file, '../outputnoworklist/' + file)
                except OSError as e:
                    print(f"{type(e)}: {e}")

            if fnmatch.fnmatch(file, '?????????????? Output Position?.csv') :

                df = pd.read_csv(file)

                if df[df.columns[0]].count() < 2 : 

                    time.sleep(2)

                    ### move the file to output no worklist folder
                    try :
                        os.replace(file, '../outputnoworklist/' + file)
                    except OSError as e:
                        print(f"{type(e)}: {e}")
                
                else :
                    for file in fnmatch.filter(os.listdir("."), '?????????????? Output Position?.csv') :
                        fileName = os.path.basename(file)
                        fileName = fileName.split('Position')
                        fileName = fileName[1].split('.')
                        worklistID = turtle.textinput("Worklist ID", "Please enter Worklist ID from Position " + fileName[0] + " :")
                        if len(worklistID) == 9 or worklistID == '0' :
                            newFileName = file.split('.')
                            newFileName = str(newFileName[0] + ' ' + worklistID + '.csv')
                            
                            ### change the filename to the new filename
                            try :
                                    os.replace(file, newFileName)
                            except OSError as e:
                                    print(f"{type(e)}: {e}")
                            
                            if worklistID == '0' : 
                                
                                ### move the file to worklist no number folder
                                try :
                                    os.replace(newFileName, '../outputnoworklist/' + newFileName)
                                except OSError as e:
                                    print(f"{type(e)}: {e}")
                            
                            elif df[df.columns[9]].count() == df[df.columns[8]].count() :
                                
                                ### move the file to elab and backup folder
                                try :
                                    shutil.copy(newFileName, '../BackupWorklist/' + newFileName)
                                    shutil.move(newFileName, 'X:/' + newFileName)
                                except OSError as e:
                                    print(f"{type(e)}: {e}")

            time.sleep(2)
            if fnmatch.fnmatch(file, '?????????????? Output Position??.csv'): 
               
                df = pd.read_csv(file)

                if df[df.columns[0]].count() < 2 : 

                    time.sleep(2)

                    ### move the file to output no worklist folder
                    try :
                        os.replace(file, '../outputnoworklist/' + file)
                    except OSError as e:
                        print(f"{type(e)}: {e}")
                        
                for file in fnmatch.filter(os.listdir("."), '?????????????? Output Position??.csv') :
                        fileName = os.path.basename(file)
                        fileName = fileName.split('Position')
                        fileName = fileName[1].split('.')
                        worklistID = turtle.textinput("Worklist ID", "Please enter Worklist ID from Position " + fileName[0] + " :")
                        if len(worklistID) == 9 or worklistID == '0' :
                            newFileName = file.split('.')
                            newFileName = str(newFileName[0]  + worklistID + '.csv')
                            
                            ### change the filename to the new filename
                            try :
                                    os.replace(file , newFileName)
                            except OSError as e:
                                    print(f"{type(e)}: {e}")
                            
                            if worklistID == '0' : 
                                
                                ### move the file to worklist no number folder
                                try :
                                    os.replace(newFileName, '../outputnoworklist/' + newFileName)
                                except OSError as e:
                                    print(f"{type(e)}: {e}")
                            
                            elif df[df.columns[9]].count() == df[df.columns[8]].count() :
                                
                                ### move the file to elab and backup folder
                                try :
                                    shutil.copy(newFileName, '../BackupWorklist/' + newFileName)
                                    shutil.move(newFileName, 'X:/' + newFileName)
                                except OSError as e:
                                    print(f"{type(e)}: {e}")

            time.sleep(2)
            if fnmatch.fnmatch(file, '?????????????? Output Position? ?????????.csv') :
                
                df = pd.read_csv(file)

                # print('this is before adding')
                # print(df)
                if df[df.columns[9]].count() == df[df.columns[8]].count() :
                    
                    ### move the file to elab and backup
                    try :
                        shutil.copy(file, '../BackupWorklist/' + file)
                        shutil.move(file, 'X:/' + file)
                    except OSError as e:
                        print(f"{type(e)}: {e} ")
                else :
                    for file in fnmatch.filter(os.listdir("."), 
                             '?????????????? Output Position? ?????????.csv') :
                        emptyCellsNum = df[df.columns[4]].count() - df[df.columns[9]].count()
                        plateID = file.split(' ')
                        plateID = plateID[3].split('.')
                        for i in range(emptyCellsNum) :
                            emptyBar =  df.iloc[:,9].isna()
                            blank_row_index =  [i for i, x in enumerate(emptyBar) if x][0]
                            barcode = textinput("Barcode", 
                                                    "Please enter the barcode of " + df.iloc[blank_row_index, 4] +
                                                        " from plate " + plateID[0] + " :")
                            df.iloc[blank_row_index, 9] = barcode
                            df.to_csv(file, index=False)

                            if df[df.columns[9]].count() == df[df.columns[8]].count():
                                
                                # print('this after adding')
                                # print(df)
                                ### move the file to elab and backup
                                try :
                                    shutil.copy(file, '../BackupWorklist/' + file)
                                    shutil.move(file, 'X:/' + file)
                                except OSError as e:
                                    print(f"{type(e)}: {e} ")
                






if __name__ == "__main__":
    src_path = "."
    event_handler = Handler()
    observer = watchdog.observers.Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(30)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

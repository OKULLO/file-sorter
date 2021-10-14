import os
from os.path import join, isfile
import shutil
from exceptions import ResponseException


class AutomatePc:

  def __init__(self):


  def sortFiles(self,f_path):


    files = [ f for f in listdir(f_path) if isfile(join(f_path,f))]
    file_type_list = []
    file_type_folder = {}

    for file in files:
      if file.strip():
        fs = file.strip("\n ' '")
        f_type = fs.split('.')[-1]
        if f_type not in file_type_list:
          file_type_list.append(f_type)

          new_folder_name = f_path+'/'+ f_type + '_folder'
          file_type_folder[str(f_type)]=str(new_folder_name)


          if os.path.isdir(new_folder_name)==True:  #folder exists
              continue
          else:
              os.mkdir(new_folder_name)

    for file in files:
        src_path= f_path+'/'+file
        filetype=file.split('.')[-1]
        if filetype in file_type_folder.keys():
            dest_path=file_type_folder[str(filetype)]
            shutil.move(src_path,dest_path)
    print(src_path + '>>>' + dest_path)


  def deleteFiles(self,fl_path):
    pass
    
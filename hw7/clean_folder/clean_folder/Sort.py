import sys
import re
import os
import shutil

categories_and_format = {'image': ('.jpeg', '.png', '.jpg', '.svg'),
                    'documents':('.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx'),
                    'audio':('.mp3', '.ogg', '.wav', '.amr'),
                    'video':('.avi', '.mp4', '.mov', '.mkv'),
                    'arhives':('.zip', '.gz', '.tar')}


def folders_for_type_files(path): #create folders
    dict_typefolders = {}
    for name_folder in categories_and_format:
        dict_typefolders[name_folder] = path + '\\' + name_folder
        
        try:
            os.mkdir(path + '\\' + name_folder)
        except FileExistsError:
                pass
    return dict_typefolders


def normalize(name):
    slovar = {'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo',
      'ж':'zh','з':'z','и':'i','й':'i','к':'k','л':'l','м':'m','н':'n',
      'о':'o','п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'h',
      'ц':'c','ч':'ch','ш':'sh','щ':'sch','ъ':'','ы':'y','ь':'','э':'e',
      'ю':'u','я':'ya', 'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'YO',
      'Ж':'ZH','З':'Z','И':'I','Й':'I','К':'K','Л':'L','М':'M','Н':'N',
      'О':'O','П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'H',
      'Ц':'C','Ч':'CH','Ш':'SH','Щ':'SCH','Ъ':'','Ы':'y','Ь':'','Э':'E',
      'Ю':'U','Я':'YA',',':'','?':'',' ':'_','~':'','!':'','@':'','#':'',
      '$':'','%':'','^':'','&':'','*':'','(':'',')':'','-':'','=':'','+':'',
      ':':'',';':'','<':'','>':'','\'':'','"':'','\\':'','/':'','№':'',
      '[':'',']':'','{':'','}':'','ґ':'','ї':'', 'є':'','Ґ':'g','Ї':'i',
      'Є':'e', '—':''}
        
   
    for key in slovar:
      name = name.replace(key, slovar[key])
    return name

def get_category(ext):
    for category, extensions in categories_and_format.items():
        if ext in extensions:
            return category
    return None


def arhive(root, base_dir,file):
    
        src_path = os.path.join(root)
        file_name = os.path.splitext(os.path.basename(src_path))[0]
        dest_path= os.path.join(base_dir, 'arhives', normalize(file_name))
        shutil.unpack_archive(src_path, dest_path)
        print(f'Распаковал архив {file}')
        os.unlink(src_path)
        print(f'Удалил файл{file}')
        
    
    
    

def move_files(base_dir, root, files):
    for file in files:
        print(file)
        src_path = os.path.join(root, file)
        
        file_name = normalize(os.path.splitext(file)[0])
        extension = os.path.splitext(file)[1]
        dest_path = os.path.join(base_dir, file_name+extension)
        category = get_category(extension)
        
        if category:
            if extension in categories_and_format['arhives']:
                arhive(src_path, base_dir, file)
                continue
            else:
                dest_path = os.path.join(base_dir, category, file_name+extension)
        os.replace(src_path, dest_path)
        print(f'Перенёс файл {file} в {category} из {root}')
        

def sort(path = None):
    if path == None:
        path = sys.argv[1]
    
    dict_typefolders = folders_for_type_files(path)
    path_list = {root: files for root, dirs, files in os.walk(path, topdown = False)}
    try:
        for root, files in path_list.items(): 
            print('    '+root+'   ')
            if root not in [i for i in dict_typefolders.values()]:
                
                if files:
                    move_files(path, root, files)
                os.rmdir(root)
    except OSError:
        pass


if __name__ == '__main__':
    main_path = sys.argv[1]
    #main_path = r'C:\Users\vadim\OneDrive\Рабочий стол\Goit\Sort\Хлам'
    sort(main_path)
    

  
    

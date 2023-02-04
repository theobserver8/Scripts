from pathlib import Path

def ls(ruta = Path.cwd()):
    return [arch.name for arch in Path(ruta).iterdir() if not arch.is_file()]

folder_list = ls()

for folder in folder_list:
    ruta = Path(str(Path.cwd()) + '\\' + folder) #Creo la ruta de cada carpeta

    file_name = ([arch.name for arch in Path(ruta).iterdir() if arch.is_file()]) #Accedo a los archivos de cada carpeta

    for file in file_name:
        file_path = Path(str(ruta) + '\\' + file) #Ruta de cada archivo en las carpetas
        file_path.rename(Path(str(Path.cwd()) + '\\' + folder + '.srt')) #Renombro con el nombre de la carpeta y a un nivel inferior

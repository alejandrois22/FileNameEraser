import os

def rename_files_and_folders(root_path, text_to_remove):
    # Recorrer todos los archivos y carpetas en el directorio actual
    for item in os.listdir(root_path):
        old_path = os.path.join(root_path, item)

        # Separar el nombre del archivo de su extensión
        file_name, file_extension = os.path.splitext(item)

        # Eliminar el texto deseado y espacios adicionales
        file_name = file_name.replace(text_to_remove, '').rstrip()

        # Reconstruir el nombre completo con la extensión
        new_name = f"{file_name}{file_extension}" if file_extension else file_name
        new_path = os.path.join(root_path, new_name)

        # Renombrar si es necesario
        if new_path != old_path:
            print(f'Renaming {old_path} to {new_path}')
            os.rename(old_path, new_path)

        # Recursivamente renombrar en subdirectorios
        if os.path.isdir(old_path):
            rename_files_and_folders(old_path, text_to_remove)

# Ruta de la carpeta y texto a eliminar
folder_path = 'G:\\Users\\Isaac\\Desktop\\JUEGOS\\mundotecnico'
text_to_remove = '(2017_02_09 01_15_02 UTC)'

# Llamar a la función
rename_files_and_folders(folder_path, text_to_remove)
print("Proceso de actualización de nombres completado.")

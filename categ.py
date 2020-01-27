import os
import sys

path = sys.argv[1].strip()
os.chdir(path)

def move(source, dir):
    os.system(f'move "{source}" "{dir}/{source}"')

# stream = os.popen('cd')
# print(stream.read())
for file in os.listdir():
    if file.endswith('.exe') or file.endswith('.jar'):
        # Put in Binaries folder
        if not os.path.exists('Binaries'):
            os.system('mkdir Binaries')
        move(file, 'Binaries')
    elif file.endswith('.zip'):
        # Put in archives folder
        if not os.path.exists('Archives'):
            os.system('mkdir Archives')
        move(file, 'Archives')
    elif file.endswith('.pdf') or file.endswith('.docx'):
        # Put in Documents folder
        if not os.path.exists('Documents'):
            os.system('mkdir Documents')
        move(file, 'Documents')
    elif file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg') or file.endswith('.gif') or file.endswith('.tiff') or file.endswith('.svg'):
        # Put in images folder
        if not os.path.exists('Images'):
            os.system('mkdir Images')
        move(file, 'Images')
    elif file.endswith('.mp4') or file.endswith('.flv') or file.endswith('.avi') or file.endswith('.wmv') or file.endswith('.mov'):
        # Put in video folder
        if not os.path.exists('Videos'):
            os.system('mkdir Videos')
        move(file, 'Videos')
    elif file.endswith('.cpp') or file.endswith('.py') or file.endswith('.c')or file.endswith('.java') or file.endswith('.js') or file.endswith('.html') or file.endswith('.css') or file.endswith('.txt') or file.endswith('.dat'):
        # Put in Code folder
        if not os.path.exists('Code'):
            os.system('mkdir Code')
        move(file, 'Code')
    elif os.path.isdir(file):
        pass
    else:
        # Put in misc folder.
        if not os.path.exists('Misc'):
            os.system('mkdir Misc')
        move(file, 'Misc')
    
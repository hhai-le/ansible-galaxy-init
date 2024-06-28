import os
import sys
from jinja2 import Environment, FileSystemLoader

if len(sys.argv) != 2: 
    print("Role name?") 
    exit() 

pwd_path = os.getcwd()
path = os.path.join(sys.argv[1])
environment = Environment(loader=FileSystemLoader(os.path.join(os.path.dirname(__file__),"templates/")))


# Check whether the specified path exists or not
isExist = os.path.exists(path)
if not isExist:
   # Create a new directory because it does not exist
    os.makedirs(path)
    folders = ["defaults","files","handlers","meta","tasks","templates","tests","vars"]
    #defaults,files,handlers,meta,tasks,templates,tests,vars
    for folder in folders:
        os.mkdir(os.path.join(path,folder))
        
    main_folders = ["defaults","handlers","tasks","vars"]
    template = environment.get_template("main.j2")
    for folder in main_folders:
        filename = os.path.join(path,folder,"main.yml")
        content = template.render(
            file_name = folder,
            role_name = sys.argv[1]
        )
        with open(filename, mode="w", encoding="utf-8") as fp:
            fp.write(content)
            
    template = environment.get_template("meta.j2")
    filename = os.path.join(path,"meta/main.yml")
    content = template.render(
        author_name = "Hai Le",
        role_desc = sys.argv[1]
    )
    with open(filename, mode="w", encoding="utf-8") as fp:
        fp.write(content)
    template = environment.get_template("test_yml.j2")
    filename = os.path.join(path,"tests/main.yml")
    content = template.render(
        role_name = sys.argv[1]
    )
    with open(filename, mode="w", encoding="utf-8") as fp:
        fp.write(content)
        
    template = environment.get_template("test_inventory.j2")
    filename = os.path.join(path,"tests/inventory")
    content = template.render()
    with open(filename, mode="w", encoding="utf-8") as fp:
        fp.write(content)
else:
    print("Folder is already exists")

os.system("pause")

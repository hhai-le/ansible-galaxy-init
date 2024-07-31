![image](https://github.com/hhai-le/ansible-galaxy-init/assets/69373181/78d06983-645d-4760-bc1f-5f260e876dfb)

```powershell
python -m venv ansible-galaxy-init
ansible-galaxy-init\Scripts\Activate
.\Scripts\python.exe -m pip install --upgrade pyinstaller jinja2
```

![image1](image/image1.png)

```powershell
pyinstaller --add-data ".\src\templates:templates" --onefile .\src\script.py
```

![](image/image2.png)


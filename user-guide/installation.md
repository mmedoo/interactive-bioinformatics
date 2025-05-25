---
icon: inboxes
layout:
  title:
    visible: true
  description:
    visible: true
  tableOfContents:
    visible: true
  outline:
    visible: true
  pagination:
    visible: true
---

# Installation

## Setup Instructions

**1. Clone the Repository**

```bash
git clone https://github.com/mmedoo/manim
cd manim
```

**2. Create and Activate a Virtual Environment**

```bash
python -m venv venv
```

**3. Install Dependencies**

**On Linux/macOS:**

```bash
source venv/bin/activate
pip install -r reqs.txt
```

**On Windows:**

```bash
venv\Scripts\activate
pip install -r reqs.txt
```

You may encounter this error:

```powershell
venv/Scripts/activate : File path\to\folder\venv\Scripts\Activate.ps1
cannot be loaded because running scripts is disabled on this system. For more information, see
about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170.
At line:1 char:1
+ venv/Scripts/activate
+ ~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : SecurityError: (:) [], PSSecurityException
    + FullyQualifiedErrorId : UnauthorizedAccess
```

Run the following in an administrator PowerShell to allow virtual environment activation:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

then run these commands again:

```powershell
venv\Scripts\activate
pip install -r reqs.txt
```

***

## Run the Visualizer

**On Linux/macOS:**

```bash
venv/bin/manim -p -qh --fullscreen --renderer=opengl main.py Run
```

**On Windows:**

```bash
venv\Scripts\activate
manim -p -qh --fullscreen --renderer=opengl main.py Run
```

You can change render quality to your preference by setting the `-qh` parameter:

| Parameter | Resolution  | Frames per second |
| --------- | ----------- | ----------------- |
| `-ql`     | 854 x 480   | `15`              |
| `-qm`     | 1280 x 720  | `30`              |
| `-qh`     | 1920 x 1080 | `60`              |
| `-qp`     | 2560 x 1440 | `60`              |
| `-qk`     | 3840 x 2160 | `60`              |

Increase fps for smoother animation.

Try reducing quality if having performance issues.

After running this command, visualization window will open. In the next chapter, we will discuss how to start interacting with the app.

***

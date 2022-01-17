# Loading and displaying an FBX File

[Adobe Mixamo](https://www.mixamo.com/) has thousands of 3-D models performing typical animation sequences (e.g., falling, jumping, etc.).

This experiment follows the [Introduction to the Python FBX SDK](https://www.youtube.com/watch?v=OgT1B69BqWg&ab_channel=AutodeskScriptingandSDKLearningChannel) tutorial to use an example the [FaillingDown.fbx](FaillingDown.fbx) file.

It requires installing the [FBX SDK](https://www.autodesk.com/products/fbx/overview). I installed both the SDK and Python SDK, might only require the Python version (TBD). See the [Autodesk FBX Help for SDK](https://download.autodesk.com/us/fbx/20112/fbx_sdk_help/index.html?url=WS1a9193826455f5ff-150b16da11960d83164-6bff.htm,topicNumber=d0e1422) for more information.

**Note**: The `fbx` module will only load with Python 3.7.x 64-bit edition. It will fail with DLL load errors using any other version (e.g., 3.10.x)!

## How do I initialize the application

```sh

# Create the virtual environment
virtualenv -p "c:\tools\python3.7\python.exe" .env

# Activate it
.env/Scripts/activate.ps1

# Install the dependencies
pip3 install -r requirements.txt

# Copy the python modules
#copy -R "C:\Program Files\Autodesk\FBX\FBX Python SDK\2020.2.1\lib\Python37_x64" ".env\Lib\site-packages"
copy -R "C:\Program Files\Autodesk\FBX\FBX Python SDK\2020.2.1\lib\Python37_x64" "C:\tools\python3.7\Lib\site-packages"
```

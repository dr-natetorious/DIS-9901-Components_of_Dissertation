import sys
print(sys.version)

def load_with_fbx():
  import libs.fbx as fbx

  manager = fbx.FbxManager.Create()
  importer = fbx.FbxImporter.Create(manager, 'Importer')
  scene = fbx.FbxScene.Create(manager, 'Scene')
  importer.Import(scene)
  importer.Initialize('FailingDown.fbx')
  importer.Destroy()


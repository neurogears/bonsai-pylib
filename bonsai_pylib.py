def load_bonsai_config(path = r"bonsai\Bonsai.config", root_path = None):
    import sys, os
    import xml.etree.ElementTree as ET

    if root_path is None:
        root_path = os.path.dirname(os.path.abspath(path))


    tree = ET.parse(path)
    root = tree.getroot()

    ## Load assemblies
    assembly_locations = root.findall("AssemblyLocations/AssemblyLocation")
    for i in assembly_locations:
        sys.path.insert(0,
                        os.path.join(
            root_path,
            os.path.dirname(i.attrib['location'])
            )
            )

    library_locations = root.findall("LibraryFolders/LibraryFolders")
    for i in library_locations:
        sys.path.insert(0,
                        os.path.join(
            root_path,
            os.path.dirname(i.attrib['path'])
            )
            )

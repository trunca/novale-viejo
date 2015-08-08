#Modulo falso para compatibilidad con Oe-Alliance

def getMachineBuild():
    return "vusolo"

def getMachineProcModel():
    return "vusolo"

def getMachineBrand():
    return "Vu+"

def getMachineName():
    return "solo"

def getMachineMtdKernel():
    return "mtd2"

def getMachineKernelFile():
    return "kernel.bin"

def getMachineMtdRoot():
    return "mtd0"

def getMachineRootFile():
    return "rootfs.bin"

def getMachineMKUBIFS():
    return "-m 2048 -e 126976 -c 4096"

def getMachineUBINIZE():
    return "-m 2048 -p 128KiB"

def getBoxType():
    return "vusolo"

def getBrandOEM():
    return "vu"

def getOEVersion():
    return "OE-SFteam 2.0"

def getDriverDate():
    return "20150610"

def getImageVersion():
    return "4"

def getImageBuild():
    return "1"

def getImageDistro():
    return "sfteam"

def getImageFolder():
    return "vuplus/solo"

def getImageFileSystem():
    return "ubi"
from pymem import Pymem
from re import search
from pymem.process import module_from_name
from pymem.exception import ProcessNotFound

try:
    processName='csgo.exe'
    pm = Pymem(processName)
    client = module_from_name(pm.process_handle,'client.dll')

    clientLpBaseOfDll=client.lpBaseOfDll
    clientModule = pm.read_bytes(clientLpBaseOfDll, client.SizeOfImage)
    address = clientLpBaseOfDll + search(rb'\x83\xF8.\x8B\x45\x08\x0F',
                                          clientModule).start() + 2

    pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
    pm.close_process()

    print("hack completed")
    
except ProcessNotFound:
    print("error: couldn't find process",processName)

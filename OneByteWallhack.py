from pymem import Pymem,process,exception
from re import search

try:
    processName='csgo.exe'
    pm = Pymem(processName)
    client = process.module_from_name(pm.process_handle,'client.dll')

    clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + search(rb'\x83\xF8.\x8B\x45\x08\x0F',
                                          clientModule).start() + 2

    pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
    pm.close_process()

    print("hack completed")
    
except exception.ProcessNotFound:
    print("error: couldn't find process",processName)

from pymem import Pymem,process
from re import search

pm = Pymem('csgo.exe')
client = process.module_from_name(pm.process_handle,'client_panorama.dll')

clientModule = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
address = client.lpBaseOfDll + search(rb'\x83\xF8.\x8B\x45\x08\x0F',
                                         clientModule).start() + 2

pm.write_uchar(address, 2 if pm.read_uchar(address) == 1 else 1)
pm.close_process()

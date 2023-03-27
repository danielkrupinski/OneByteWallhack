import pymem
import re

# Define constants
CSGO_EXE = 'csgo.exe'
CLIENT_DLL = 'client.dll'
BYTE_PATTERN = rb'\x33\xC0\x83\xFA.\xB9\x20'

try:
    # Open process handle and module
    pm = pymem.Pymem(CSGO_EXE)
    client = pymem.process.module_from_name(pm.process_handle, CLIENT_DLL)

    # Read module into memory and search for byte pattern
    client_module = pm.read_bytes(client.lpBaseOfDll, client.SizeOfImage)
    address = client.lpBaseOfDll + re.search(BYTE_PATTERN, client_module).start() + 4

    # Modify function byte and close process handle
    new_value = 2 if pm.read_uchar(address) == 1 else 1
    pm.write_uchar(address, new_value)

except pymem.exception.ProcessNotFound:
    print(f'{CSGO_EXE} process not found')
except pymem.exception.ProcessError:
    print(f'Error accessing process {CSGO_EXE}')
except pymem.exception.ModuleNotFound:
    print(f'{CLIENT_DLL} module not found')
except pymem.exception.MemoryReadError:
    print('Error reading memory')
except pymem.exception.MemoryWriteError:
    print('Error writing memory')
except AttributeError:
    print('Byte pattern not found')
else:
    with pm:
        pass

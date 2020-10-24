# OneByteWallhack
CS:GO wallhack achieved by patching one byte of game process memory. Written in Python 3.9

This does the same as **r_drawothermodels 2** command but without touching the cvar, so it's VAC - safe.

## How it works
This program patches assembly code produced by compiling the [following line of the game code](https://github.com/ValveSoftware/source-sdk-2013/blob/0d8dceea4310fde5706b3ce1c70609d72a38efdf/mp/src/game/client/c_baseanimating.cpp#L3149):
```cpp
int extraFlags = 0;
if ( r_drawothermodels.GetInt() == 2 )
{	
    extraFlags |= STUDIO_WIREFRAME;	
}
```

The **r_drawothermodels** check is modified to make the `if` expression evaluate to **true** when **r_drawothermodels** cvar is set to default value (1).

𝗜𝗺𝗽𝗼𝗿𝘁𝗮𝗻𝘁! :
Download python 3.9 or newer if you hadn't: https://www.python.org/downloads/
You may need to head to "C:\Users\ username \AppData\Local\Programs\Python\Python38-32\Scripts" press Win+R write "cmd" and "pip install pymem" and or "pip install pywin32" and restart your pc.

Usage: 
Run CSGO before this script. You will also need to run this script as administrator

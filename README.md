# OneByteWallhack
CS:GO wallhack achieved by patching one byte of game memory. Written in Python 3.

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
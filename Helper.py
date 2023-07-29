class ACVars:
    healthP = '0x000000F8' #Pointer 
    healthO = '0xF8' # offset
    LocalP = '0x10F4F4'
    LocalWp = '0x290A708'
    Armor = '0xFC'
    Grenades = '0x40'
    PAmmo = '0x150'
    SAmmo = '0x13C'
    modules = ["ac_client.exe"]


class CSVars:
    dwEntityList = 0x4DFFEF4
    dwGlowObjEctManager = 0x535A9C8
    m_iGlowIndex = 0x10488
    m_iTeamNum = 0xF4
    m_bIsLocalPlayer = 0x3628
    dwLocalPlayer = 0xDEA964
    m_bSpotted = '0x93D'
    dwForceAttack = '0x322DCFC'
    m_iCrosshairId = 0x11838
    modules = ["client.dll"]

class TFVars:
    iFood = 0x2D4CB4C
    localP = [0x05BF5260, 0xb8, 0x38, 0x78, 0xC0, 0x0]
    modules = ["GameAssembly.dll"]



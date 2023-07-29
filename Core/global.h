//pragma once tells C++ compiler if you include this file more then once it will only ever be included more then once so you dont get include errors
#pragma once
//this is a C++ trick / hack that tells dialogs to use the better looking dialogs :)
#pragma comment(linker,"/manifestdependency:\"type='win32' name='Microsoft.Windows.Common-Controls' version='6.0.0.0' processorArchitecture='*' publicKeyToken='6595b64144ccf1df' language='*'\"")
#define _CRT_SECURE_NO_WARNINGS
//include any EXTRA files
#include <windows.h>
#include <stdio.h>
#include "leechcore.h"
#include "vmmdll.h"
#include <utility>
#include <TlHelp32.h>
#include <CommCtrl.h>
#include <emmintrin.h>
#include <xmmintrin.h>
#pragma comment(lib,"leechcore.lib")
#pragma comment(lib,"vmm.lib")
#include "resource.h"
#include "Dialog Callbacks.h"
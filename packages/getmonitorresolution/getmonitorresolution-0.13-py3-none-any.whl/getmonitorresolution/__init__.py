import ctypes
from ctypes import wintypes
import typing as T

from flatten_any_dict_iterable_or_whatsoever import fla_tu

windll = ctypes.LibraryLoader(ctypes.WinDLL)
user32 = ctypes.WinDLL("user32")


class DISPLAY_DEVICEW(ctypes.Structure):
    _fields_ = [
        ("cb", wintypes.DWORD),
        ("DeviceName", wintypes.WCHAR * 32),
        ("DeviceString", wintypes.WCHAR * 128),
        ("StateFlags", wintypes.DWORD),
        ("DeviceID", wintypes.WCHAR * 128),
        ("DeviceKey", wintypes.WCHAR * 128),
    ]


MonitorEnumProc = ctypes.WINFUNCTYPE(
    ctypes.c_int,
    ctypes.c_ulong,
    ctypes.c_ulong,
    ctypes.POINTER(ctypes.wintypes.RECT),
    ctypes.c_double,
)

CCHDEVICENAME = 32
HORZSIZE = 4
VERTSIZE = 6


class MONITORINFOEXW(ctypes.Structure):
    _fields_ = [
        ("cbSize", ctypes.wintypes.DWORD),
        ("rcMonitor", ctypes.wintypes.RECT),
        ("rcWork", ctypes.wintypes.RECT),
        ("dwFlags", ctypes.wintypes.DWORD),
        ("szDevice", ctypes.wintypes.WCHAR * CCHDEVICENAME),
    ]


EnumDisplayDevices = windll.user32.EnumDisplayDevicesW
EnumDisplayDevices.restype = ctypes.c_bool


def get_display_information():
    # based on https://stackoverflow.com/a/65624659/15096247
    displays = []
    i = 0
    j = 0
    while True:
        INFO = DISPLAY_DEVICEW()
        INFO.cb = ctypes.sizeof(INFO)
        Monitor_INFO = DISPLAY_DEVICEW()
        Monitor_INFO.cb = ctypes.sizeof(Monitor_INFO)
        if not EnumDisplayDevices(None, i, ctypes.byref(INFO), 0):
            break
        while EnumDisplayDevices(INFO.DeviceName, j, ctypes.byref(Monitor_INFO), 0):
            j += 1

        displays.append(INFO)
        i += 1

    displaydict = {}
    for ini, x in enumerate(displays):
        displaydict[ini] = {
            "DeviceName": x.DeviceName,
            "DeviceString": x.DeviceString,
            "StateFlags": x.StateFlags,
            "DeviceID": x.DeviceID,
            "DeviceKey": x.DeviceKey,
        }
    return displaydict


def enumerate_monitors():
    # based on https://github.com/rr-/screeninfo
    allist = []

    def _enumerate_monitors():
        monitors = []

        def check_primary(rct: T.Any) -> bool:
            return rct.left == 0 and rct.top == 0

        def callback(monitor: T.Any, dc: T.Any, rect: T.Any, data: T.Any) -> int:
            info = MONITORINFOEXW()
            info.cbSize = ctypes.sizeof(MONITORINFOEXW)
            if windll.user32.GetMonitorInfoW(monitor, ctypes.byref(info)):
                name = info.szDevice
            else:
                name = None

            h_size = windll.gdi32.GetDeviceCaps(dc, HORZSIZE)
            v_size = windll.gdi32.GetDeviceCaps(dc, VERTSIZE)

            rct = rect.contents
            ke = len(allist)
            allist.append(
                {
                    ke: {
                        "x": rct.left,
                        "y": rct.top,
                        "width": rct.right - rct.left,
                        "height": rct.bottom - rct.top,
                        "width_mm": h_size,
                        "height_mm": v_size,
                        "DeviceName": name,
                        "is_primary": check_primary(rct),
                    }
                }
            )

            return 1

        while True:
            try:
                dc_full = windll.user32.GetDC(None)
            except Exception:
                dc_full = 0
            windll.user32.EnumDisplayMonitors(
                dc_full, None, MonitorEnumProc(callback), 0
            )
            windll.user32.ReleaseDC(dc_full)
            del dc_full
            list(monitors)
            if allist:
                break

    _enumerate_monitors()
    return allist


def get_monitors_resolution(dpi_awareness:int=2) -> tuple[dict,dict]:
    windll.shcore.SetProcessDpiAwareness(dpi_awareness)
    allist = enumerate_monitors()
    moninfo = get_display_information()
    fladi = list(fla_tu(allist))
    allmoni = {}
    for key, item in moninfo.items():
        try:
            odi = allist[key]
            done = False
            for fl in fladi:
                if done:
                    break
                try:
                    isgo = item["DeviceName"] == fl[0]
                    newkey = int(fl[0][-1]) - 1
                    if isgo:
                        allmoni[newkey] = item | odi[fl[1][0]]
                        done = True
                except Exception as fa:
                    continue

        except Exception as pe:
            continue
    moninfos = {
        "width_all_monitors": sum([q[1]["width"] for q in allmoni.items()]),
        "height_all_monitors": sum([q[1]["height"] for q in allmoni.items()]),
        "max_monitor_width": max([q[1]["width"] for q in allmoni.items()]),
        "min_monitor_width": min([q[1]["width"] for q in allmoni.items()]),
        "max_monitor_height": max([q[1]["height"] for q in allmoni.items()]),
        "min_monitor_height": min([q[1]["height"] for q in allmoni.items()]),
    }
    return allmoni, moninfos


__all__ = ["get_monitors_resolution"]

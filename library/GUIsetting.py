import subprocess
import platform

system = platform.system().lower()
appearance = None

theme = None
try:
    if system == 'darwin':  # macOS
        result = subprocess.run(
            ['defaults', 'read', '-g', 'AppleInterfaceStyle'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if 'Dark' in result.stdout:
            theme = "Dark"
        else:
            theme = "Light"
    elif system == 'windows':  # Windows
        import winreg
        registry = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER)
        key = winreg.OpenKey(registry, r'SOFTWARE\Microsoft\Windows\CurrentVersion\Themes\Personalize')
        value, _ = winreg.QueryValueEx(key, 'AppsUseLightTheme')
        if value == 0:
            theme = "Dark"
        else:
            theme = "Light"
    else:
        theme = "Light"
except Exception:
    theme = "Light"

APPEARANCE_CONFIG = {
    "darwin":{
        "FontSize": 16,
        "WindowWidth": 500,
        "LabelWidth": 9,
        "IntervalX": 104
    },
    "windows":{
        "FontSize": 14,
        "WindowWidth": 520,
        "LabelWidth": 11,
        "IntervalX": 130
    },
}

appearance = APPEARANCE_CONFIG.get(system, APPEARANCE_CONFIG['darwin'])
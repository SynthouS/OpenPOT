import settings

def potfetch():
    art = fr"""
       _
      (\\      [os] {settings.system_info['os']}
       \||     [kernel] {settings.system_info['kernel']}
     __(_";    [shell] {settings.system_info['shell']}
    /    \     [cpu] {settings.system_info['cpu']}
   ()___)\)_   [memory] {settings.system_info['memory']}
    """
    print(art)
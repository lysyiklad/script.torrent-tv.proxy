import defines
import mainform

if __name__ == '__main__':
    defines.ADDON.setSetting('skin', 'estuary')
    print defines.ADDON_PATH
    print defines.SKIN_PATH
    w = mainform.WMainForm("mainform.xml", defines.SKIN_PATH, defines.ADDON.getSetting('skin'))
    w.doModal()
    defines.showMessage('Close plugin', 'Torrent-TV (HTTPAceProxy)', 1000)
    del w

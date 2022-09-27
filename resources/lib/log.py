#	This file is part of  Shell Script Launcher for Kodi.
#
#	Copyright (C) 2022 wastis    https://github.com/wastis/BluetoothManager
#
#	Bluetooth Manager is free software; you can redistribute it and/or modify
#	it under the terms of the GNU Lesser General Public License as published
#	by the Free Software Foundation; either version 3 of the License,
#	or (at your option) any later version.
#
#

import xbmc

def log(text):
	xbmc.log("osmc: " + text, xbmc.LOGDEBUG)

def loginfo(text):
	xbmc.log("osmc: " + text, xbmc.LOGINFO)

def logerror(text):
	xbmc.log("osmc: " + text, xbmc.LOGERROR)

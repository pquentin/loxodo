#
# Loxodo -- Password Safe V3 compatible Password Vault
# Copyright (C) 2008 Christoph Sommer <mail@christoph-sommer.de>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#

import wx

from .wxlocale import _
from .wxlocale import setup_wx_locale
from .loadframe import LoadFrame


class LoxodoApp(wx.App):
    def OnInit(self):
	print('Init')
	return True

    def MacOpenFile(self, filename):
	print('Open', filename)

    def OnActivate(self, event):
        # if this is an activate event, rather than something else, like iconize.
	print('on active')
        if event.GetActive():
	    print('get active')
	    self.GetTopWindow().Raise()
	print('skip')
        event.Skip()

    def MacReopenApp(self):
	"""Called when the doc icon is clicked, and ???"""
	print('Reopen')
	self.GetTopWindow().Raise()


def main():
    app = LoxodoApp(False)
    setup_wx_locale()
    mainframe = LoadFrame(None, -1, "")
    app.SetTopWindow(mainframe)
    mainframe.Show()
    app.MainLoop()


main()


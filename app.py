#!/usr/bin/env python
# -*- coding: iso-8859-15 -*-
# generated by wxGlade 0.6.5 (standalone edition) on Fri Feb 08 16:33:20 2013

from wxPython.wx import *
from MainWindow import MainWindow

if __name__ == "__main__":
    app = wxPySimpleApp(0)
    wxInitAllImageHandlers()
    frame_1 = MainWindow(None, -1, "")
    app.SetTopWindow(frame_1)
    frame_1.Show()
    app.MainLoop()

#
#  Color_PickerAppDelegate.py
#  Color Picker
#
#  Created by Casey Marshall on 1/26/09.
#  Copyright Casey Marshall 2009. All rights reserved.
#

from Foundation import *
from AppKit import *

class Color_PickerAppDelegate(NSObject):
    def applicationDidFinishLaunching_(self, sender):
        NSLog("Application did finish launching.")

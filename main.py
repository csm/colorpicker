#
#  main.py
#  Color Picker
#
#  Created by Casey Marshall on 1/26/09.
#  Copyright Casey Marshall 2009. All rights reserved.
#

#import modules required by application
import objc
import Foundation
import AppKit

from PyObjCTools import AppHelper

# import modules containing classes required to start application and load MainMenu.nib
import Color_PickerAppDelegate
import ColorPickerController

# pass control to AppKit
AppHelper.runEventLoop()

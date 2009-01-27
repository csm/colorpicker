from Foundation import *
from AppKit import *
import objc

class ColorPickerController(NSObject):
    alphaFloatLabel = objc.IBOutlet()

    alphaHexLabel = objc.IBOutlet()

    alphaPercentLabel = objc.IBOutlet()

    blueFloatLabel = objc.IBOutlet()

    blueHexLabel = objc.IBOutlet()

    bluePercentLabel = objc.IBOutlet()

    brightFloatLabel = objc.IBOutlet()

    brightHexLabel = objc.IBOutlet()

    brightPercentLabel = objc.IBOutlet()

    colorNameLabel = objc.IBOutlet()

    colorWell = objc.IBOutlet()

    cyanFloatLabel = objc.IBOutlet()

    cyanHexLabel = objc.IBOutlet()

    cyanPercentLabel = objc.IBOutlet()

    greenFloatLabel = objc.IBOutlet()

    greenHexLabel = objc.IBOutlet()

    greenPercentLabel = objc.IBOutlet()

    hueFloatLabel = objc.IBOutlet()

    hueHexLabel = objc.IBOutlet()

    huePercentLabel = objc.IBOutlet()

    keyFloatLabel = objc.IBOutlet()

    keyHexLabel = objc.IBOutlet()

    keyPercentLabel = objc.IBOutlet()

    magentaFloatLabel = objc.IBOutlet()

    magentaHexLabel = objc.IBOutlet()

    magentaPercentLabel = objc.IBOutlet()

    redFloatLabel = objc.IBOutlet()

    redHexLabel = objc.IBOutlet()

    redPercentLabel = objc.IBOutlet()

    satFloatLabel = objc.IBOutlet()

    satHexLabel = objc.IBOutlet()

    satPercentLabel = objc.IBOutlet()

    yellowFloatLabel = objc.IBOutlet()

    yellowHexLabel = objc.IBOutlet()

    yellowPercentLabel = objc.IBOutlet()

    def awakeFromNib(self):
        NSColorPanel.sharedColorPanel().setShowsAlpha_(True)
        NSColor.setIgnoresAlpha_(False)
        self.colorPicked_(None)

    @objc.IBAction
    def colorPicked_(self, sender):
        color = self.colorWell.color()
        #try:
        #    color2 = color.colorUsingColorSpaceName_(NSNamedColorSpace)
        #    self.colorNameLabel.setStringValue_(color2.colorNameComponent())
        #except:
        #    self.colorNameLabel.setStringValue_("none")
        self.alphaFloatLabel.setStringValue_("%.6f" % color.alphaComponent())
        self.alphaPercentLabel.setStringValue_("%.2f%%" % (color.alphaComponent() * 100))
        self.alphaHexLabel.setStringValue_("0x%x" % int(color.alphaComponent() * 255))

        self.blueFloatLabel.setStringValue_("%.6f" % color.blueComponent())
        self.blueHexLabel.setStringValue_("0x%x" % (color.blueComponent() * 255))
        self.bluePercentLabel.setStringValue_("%.2f%%" % (color.blueComponent() * 100))

        self.greenFloatLabel.setStringValue_("%.6f" % color.greenComponent())
        self.greenHexLabel.setStringValue_("0x%x" % (color.greenComponent() * 255))
        self.greenPercentLabel.setStringValue_("%.2f%%" % (color.greenComponent() * 100))
        
        self.redFloatLabel.setStringValue_("%.6f" % color.redComponent())
        self.redHexLabel.setStringValue_("0x%x" % (color.redComponent() * 255))
        self.redPercentLabel.setStringValue_("%.2f%%" % (color.redComponent() * 100))

        self.brightFloatLabel.setStringValue_("%.6f" % color.brightnessComponent())
        self.brightHexLabel.setStringValue_("0x%x" % (color.brightnessComponent() * 255))
        self.brightPercentLabel.setStringValue_("%.2f%%" % (color.brightnessComponent() * 100))

        self.hueFloatLabel.setStringValue_("%.6f" % color.hueComponent())
        self.hueHexLabel.setStringValue_("0x%x" % (color.hueComponent() * 255))
        self.huePercentLabel.setStringValue_("%.2f%%" % (color.hueComponent() * 100))
        
        self.satFloatLabel.setStringValue_("%.6f" % color.saturationComponent())
        self.satHexLabel.setStringValue_("0x%x" % (color.saturationComponent() * 255))
        self.satPercentLabel.setStringValue_("%.2f%%" % (color.saturationComponent() * 100))

        #color = color.colorUsingColorSpace_(NSColorSpace.deviceCMYKColorSpace())

        #self.keyFloatLabel.setStringValue_("%.6f" % color.blackComponent())
        #self.keyHexLabel.setStringValue_("0x%x" % (color.blackComponent() * 255))
        #self.keyPercentLabel.setStringValue_("%.2f%%" % (color.blackComponent() * 100))
        
        #self.cyanFloatLabel.setStringValue_("%.6f" % color.cyanComponent())
        #self.cyanHexLabel.setStringValue_("0x%x" % (color.cyanComponent() * 255))
        #self.cyanPercentLabel.setStringValue_("%.2f%%" % (color.cyanComponent() * 100))
        
        #self.magentaFloatLabel.setStringValue_("%.6f" % color.magentaComponent())
        #self.magentaHexLabel.setStringValue_("0x%x" % (color.magentaComponent() * 255))
        #self.magentaPercentLabel.setStringValue_("%.2f%%" % (color.magentaComponent() * 100))
        
        #self.yellowFloatLabel.setStringValue_("%.6f" % color.yellowComponent())
        #self.yellowHexLabel.setStringValue_("0x%x" % (color.yellowComponent() * 255))
        #self.yellowPercentLabel.setStringValue_("%.2f%%" % (color.yellowComponent() * 100))

    def ColorPickerController(self):
        pass


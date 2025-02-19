from owrx.source.soapy import SoapyConnectorSource, SoapyConnectorDeviceDescription
# Created by PE3ES / F4VTQ / Erwin in 2025

class FobosSource(SoapyConnectorSource):
    def getDriver(self):
        return "fobos"


class FobosDeviceDescription(SoapyConnectorDeviceDescription):
    def getName(self):
        return "Fobos SDR"

    def supportsPpm(self):
        # not currently supported by the SoapySDR module.
        return False


#    def getSampleRateRanges(self) -> List[Range]:
 #       return [
  #          Range(192000),
   #         Range(256000),
    #        Range(384000),
     #       Range(456000),
      #      Range(768000),
       #     Range(912000),
        #]

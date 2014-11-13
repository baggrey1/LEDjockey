import usb.core
import usb.util
import sys

#input is a 5 byte list
def LWZ_SBA(input):
	#find device
	dev = usb.core.find(idVendor=0xfafa, idProduct=0x00f0)

	if dev is None:
		raise ValueError('LedWiz device not found')

	#claim device
	if dev.is_kernel_driver_active(0) is True:
		dev.detach_kernel_driver(0)
	usb.util.claim_interface(dev,0)

	#activate device
	if not dev.get_active_configuration():
		dev.set_configuration(1)

	msg = [64]+input+[0,0]

	#send message to device
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, msg)

	#bmRequesttype - 0x21 - HID
	#bmrequest - 0x09 - SET_REPORT
	#wValue - Report Type and Rport ID - 0x02 0x00
	#wIndex - Interface -0
	#msg - list of values

	#release device
	usb.util.release_interface(dev,0)

def LWZ_PBA(input):
	#find device
	dev = usb.core.find(idVendor=0xfafa, idProduct=0x00f0)

	if dev is None:
		raise ValueError('LedWiz device not found')

	#claim device
	if dev.is_kernel_driver_active(0) is True:
		dev.detach_kernel_driver(0)
	usb.util.claim_interface(dev,0)

	#activate device
	if not dev.get_active_configuration():
		dev.set_configuration(1)

	msg1 = input[0:8]
	msg2 = input[8:16]
	msg3 = input[16:24]
	msg4 = input[24:32]

	#send message to device
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, msg1)
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, msg2)
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, msg3)
	dev.ctrl_transfer(0x21, 0x09, 0x0200, 0, msg4)


	#bmRequesttype - 0x21 - HID
	#bmrequest - 0x09 - SET_REPORT
	#wValue - Report Type and Rport ID - 0x02 0x00
	#wIndex - Interface -0
	#msg - list of values

	#release device
	usb.util.release_interface(dev,0)

#use like this to turn all lights on

# LWZ_SBA([0,0,0,0,4])
# LWZ_PBA([132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132,132])
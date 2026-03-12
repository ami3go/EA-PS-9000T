# import serial.tools.list_ports
#
# def get_com_port_by_description(target_description):
#     """
#     Returns the COM port number (e.g., 'COM3') for a device
#     matching the given description.
#     Returns None if no matching device is found.
#     """
#     ports = serial.tools.list_ports.comports()
#     for port in ports:
#         print(port.description)
#         if target_description in port.description:
#             return port.device
#     return None
#
# # Example usage:
# # If you have a device connected that shows "USB Serial Device" in its description
# com_port = get_com_port_by_description("PS 9000 T Series")
# # if com_port:
# #     print(f"Found device on: {com_port}")
# # else:
# #     print("Device not found.")


import serial.tools.list_ports
def get_com_port_by_keyword(keyword):
    """
    Returns the COM port number (e.g., 'COM3') for a device
    whose description contains the given keyword.
    Returns None if no matching device is found.
    """
    ports = serial.tools.list_ports.comports()
    for port in ports:
        # print(port)
        # print(port.description.lower())
        # Check if the keyword is present in the port's description
        if keyword.lower() in port.description.lower(): # Using .lower() for case-insensitive search
            return port.device
    return None

com_port = get_com_port_by_keyword("PS 9000 T")
print(com_port)
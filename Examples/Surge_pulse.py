
import time

import EAPS9000T.EAPS9000T_class as ps

cmd = ps.storage()
# print(cmd.configure.current.dc.str())
# print(cmd.measure.current.dc.req())
ps_dev = ps.com_interface()
ps_dev.init("COM8")
ps_dev.send(cmd.system.lock.on())


# Preset
interval = 0.02
pulse_width = 0.01
dc_time = 10
v_dc = 68.8
v_peak = 200
i_lim = 5

ps_dev.send(cmd.source.current.val(i_lim))
time.sleep(0.1)
ps_dev.send("SOUR:VOLT:CONT:SPE SLOW")
time.sleep(0.1)
ps_dev.send(cmd.output.on())
# DC bias
ps_dev.send(cmd.source.voltage.val(v_dc))
time.sleep(dc_time)

# High Voltage pulse
ps_dev.send(cmd.source.voltage.val(v_peak))
time.sleep(pulse_width)
ps_dev.send(cmd.source.voltage.val(v_dc))

time.sleep(dc_time)
ps_dev.send(cmd.output.off())

ps_dev.send(cmd.system.lock.off())
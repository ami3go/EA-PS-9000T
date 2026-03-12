
import time

import EAPS9000T.EAPS9000T_class as ps

cmd = ps.storage()
# print(cmd.configure.current.dc.str())
# print(cmd.measure.current.dc.req())
ps_dev = ps.EaPs9000T()
ps_dev.init("COM8")
ps_dev.send(cmd.system.lock.on())
# print(dev.query("*IDN?"))
# dev.send(cmd.reset.str())

# Preset

i_lim = 2

ps_dev.send(cmd.source.current.val(i_lim))
time.sleep(0.1)

# DC bias

v_high = 60 #  Volts
v_low = 0
Nreps = 1000
high_time = 3
low_time = 0.5
ps_dev.send(cmd.source.voltage.val(v_high))
ps_dev.send(cmd.output.on())
for x in range(0,Nreps ):
    ps_dev.send(cmd.source.voltage.val(v_high))

    time.sleep(high_time)
    v_meas = ps_dev.query(cmd.source.voltage.req())
    i_meas = ps_dev.query(cmd.measure.current.req())
    v_meas = v_meas.split(" ")
    v_meas = v_meas[0]
    i_meas = i_meas.split(" ")
    i_meas = i_meas[0]
    print(f" Cycle {x} / {Nreps} V: {v_meas} V, I: {i_meas} A")
    ps_dev.send(cmd.source.voltage.val(v_low))
    time.sleep(low_time)

time.sleep(2)
ps_dev.send(cmd.output.off())
ps_dev.close()
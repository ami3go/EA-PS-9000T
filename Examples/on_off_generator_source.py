
import time

import EAPS9000T.EAPS9000T_class as ps

cmd = ps.storage()
# print(cmd.configure.current.dc.str())
# print(cmd.measure.current.dc.req())
ps_dev = ps.com_interface()
ps_dev.init("COM8")
ps_dev.send(cmd.system.lock.on())
# print(dev.query("*IDN?"))
# dev.send(cmd.reset.str())

# Preset

i_lim = 2

ps_dev.send(cmd.source.current.val(i_lim))
time.sleep(0.1)

# DC bias

vout = 30 # Volts
Nreps = 30
on_time = 1
off_time = 0.2
ps_dev.send(cmd.source.voltage.val(vout))
ps_dev.send(cmd.output.on())
for x in range(0,Nreps ):
    ps_dev.send(cmd.output.on())

    time.sleep(on_time)
    v_meas = ps_dev.query(cmd.source.voltage.req())
    i_meas = ps_dev.query(cmd.measure.current.req())
    v_meas = v_meas.split(" ")
    v_meas = v_meas[0]
    i_meas = i_meas.split(" ")
    i_meas = i_meas[0]
    print(f" Cycle {x} / {Nreps} V: {v_meas} V, I: {i_meas} A")

    ps_dev.send(cmd.output.off())
    time.sleep(off_time)

time.sleep(2)
ps_dev.send(cmd.output.off())
ps_dev.close()
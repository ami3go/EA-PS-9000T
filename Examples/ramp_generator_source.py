
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



vout = 0.00
voltage_step = 0.05
Vout_high = 30
Vout_low = 0
vout = Vout_low
Nreps = 30
step_delay = 0.01

ps_dev.send(cmd.source.voltage.val(vout))
ps_dev.send(cmd.output.on())
for x in range(0,Nreps ):
    for v in range(round((Vout_high-Vout_low)/voltage_step)):
        ps_dev.send(cmd.source.voltage.val(vout))
        v_meas = ps_dev.query(cmd.source.voltage.req())
        i_meas = ps_dev.query(cmd.measure.current.req())
        v_meas = v_meas.split(" ")
        v_meas = v_meas[0]
        i_meas = i_meas.split(" ")
        i_meas = i_meas[0]
        print(f"V: {v_meas} V, I: {i_meas} A")
        time.sleep(step_delay)
        vout = round((vout + voltage_step),3)# function round should be used beca
    time.sleep(2)
    for v in range(round((Vout_high-Vout_low)/voltage_step)):
        ps_dev.send(cmd.source.voltage.val(vout))
        time.sleep(step_delay)
        vout = round((vout - voltage_step), 3)

time.sleep(2)
ps_dev.send(cmd.output.off())
ps_dev.close()
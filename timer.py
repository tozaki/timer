#!/usr/bin/env python
# -*- coding: utf8 -*-
import tkinter  as tk
import winsound as snd

#### Global Ram ###############################################################
Gmin = u"1"
Gsec  = u"0"
GCouter = u"0"
Gmin_max = u"100"
Gcnt_max = u"99"

Gmin_max = 100 
Gsec_add = 15 

GStatue_Stop = u"STOP"
GStatue_Start = u"Start"
Gstatus = GStatue_Stop   

#### Create Frame class #######################################################
class Frame:
    ### Init ##################################################################
    def __init__(self):
        self.min = Gmin
        self.min_t = Gmin
        self.sec = Gsec
        self.sec_t = Gsec
        self.cont = GCouter
        self.status = Gstatus 
        self.frame = tk.Tk()
        self.frame.geometry('480x200')
        self.frame.title("たいま～")
        self.create_header()
        self.create_statusbar()
        self.create_screen()
        self.set_shortcut()

    def create_header(self):
        self.upper = tk.LabelFrame(self.frame,padx=10,pady=10,text="Header")

        self.b1 = tk.Button(self.upper,text='Start',font=("Meiryo UI",9), command=self.Start)
        self.b1.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)
         
        self.b2 = tk.Button(self.upper,text='Stop',font=("Meiryo UI",9), command=self.Stop)
        self.b2.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)
         
        self.b3 = tk.Button(self.upper,text='Clear',font=("Meiryo UI",9), command=self.Clear)
        self.b3.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)
      
        l1 = tk.Label(self.upper,text='  分:',font=("Meiryo UI",12))
        l1.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)
        self.b4 = tk.Button(self.upper,text='+',width=2,font=("Meiryo UI",9),command=self.minplus)
        self.b4.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)
        self.b5 = tk.Button(self.upper,text='-',width=2,font=("Meiryo UI",9),command=self.minminus)
        self.b5.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)

        l2 = tk.Label(self.upper,text='  秒:',font=("Meiryo UI",12))
        l2.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)
        self.b6 = tk.Button(self.upper,text='+',width=2,font=("Meiryo UI",9),command=self.secplus)
        self.b6.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)
        self.b7 = tk.Button(self.upper,text='-',width=2,font=("Meiryo UI",9),command=self.secminus)
        self.b7.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)

        l3 = tk.Label(self.upper,text='  Counter:',font=("Meiryo UI",12))
        l3.pack(side=tk.LEFT,fill=tk.X,anchor=tk.SW)
        self.b8 = tk.Button(self.upper,text='+',width=2,font=("Meiryo UI",9),command=self.cntplus)
        self.b8.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)
        self.b9 = tk.Button(self.upper,text='-',width=2,font=("Meiryo UI",9),command=self.cntminus)
        self.b9.pack(side=tk.LEFT,fill=tk.X,anchor=tk.NW)
        self.counter = tk.StringVar()
        self.cl = tk.Label(self.upper,textvariable=self.counter,font=("Meiryo UI",12,"bold"))
        self.cl.pack(side=tk.LEFT,fill=tk.X,anchor=tk.SW)
        self.refleshcounter()
        
        self.upper.pack(side=tk.TOP,fill=tk.BOTH)

    def create_screen(self):
        self.lower = tk.LabelFrame(self.frame,padx=10,pady=10,text="Timer")
        self.timer = tk.StringVar()
        self.refleshtime()
        self.text = tk.Label(self.lower,textvariable=self.timer,font=("Meiryo UI",60,"bold"))
        self.text.pack(fill=tk.Y)
        self.lower.pack(side=tk.TOP,fill=tk.BOTH)

    def create_statusbar(self):
        self.st = tk.StringVar()
        self.reflechstatus()
        self.stbar = tk.Label(self.frame, textvariable=self.st, bd=1, relief=tk.SUNKEN, anchor=tk.W,font=("Meiryo UI",12))
        self.stbar.pack(side=tk.BOTTOM, fill=tk.X)

    def set_shortcut(self):
        self.frame.bind_all("<Control-q>", self.quit_s)

    ###Buttun##################################################################
    def Start(self):
        self.refleshtime()
        self.status = GStatue_Start
        self.reflechstatus()
        self.loop()
                
    def Stop(self):
        self.refleshtime()
        self.status = GStatue_Stop
        self.reflechstatus()

    def Clear(self):
        if self.status == GStatue_Stop:
            self.min = Gmin
            self.sec = Gsec
            self.cont = GCouter
            self.refleshtime()
            self.refleshcounter()

    def minplus(self):
        if self.status == GStatue_Stop:
            m = int(self.min)
            m = m + 1 if m + 1 <= int(Gmin_max) else m
            self.min = str(m)
            self.min_t = self.min
            self.refleshtime()

    def minminus(self):
        if self.status == GStatue_Stop:
            m = int(self.min)
            m = m - 1 if m - 1 >= 0 else m
            self.min = str(m)
            self.min_t = self.min
            self.refleshtime()

    def secplus(self):
        if self.status == GStatue_Stop:
            m = int(self.min)
            s = int(self.sec)
            if s + Gsec_add < 60:
                s = s + Gsec_add
            else:
                s = s + Gsec_add - 60
                m = m + 1 if m + 1 <= int(Gmin_max) else m
            self.sec = str(s)
            self.min = str(m)
            self.sec_t = self.sec
            self.min_t = self.min
            self.refleshtime()

    def secminus(self):
        if self.status == GStatue_Stop:
            m = int(self.min)
            s = int(self.sec)
            if s - Gsec_add >= 0:
                s = s - Gsec_add
            else:
                s = s - Gsec_add + 60 if m != 0 else 0
                m = m - 1 if m - 1 >= 0 else m
            self.sec = str(s)
            self.min = str(m)
            self.sec_t = self.sec
            self.min_t = self.min
            self.refleshtime()

    def cntplus(self):
        if self.status == GStatue_Stop:
            c = int(self.cont)
            c = c + 1 if c + 1 <= int(Gcnt_max) else c
            self.cont = str(c)
            self.refleshcounter()

    def cntminus(self):
        if self.status == GStatue_Stop:
            c = int(self.cont)
            c = c - 1 if c - 1 >= 0 else c
            self.cont = str(c)
            self.refleshcounter()

    def quit_s(self,event):
        self.quit()
    def quit(self):
        self.frame.destroy()     

    ###logic###################################################################
    def refleshtime(self):
        tmin = self.min
        tsec = self.sec 
        t = tmin + ":"
        if len(tsec) == 2:
            t = t + tsec
        elif len(tsec) == 1:
            t = t + "0" + tsec
        self.timer.set(t)

    def refleshcounter(self):
        self.counter.set(self.cont)

    def reflechstatus(self):
        self.st.set(self.status)

    ###loop###################################################################
    def loop(self):
        t = int(60*int(self.min) + int(self.sec))
        if t > 0 and self.status == GStatue_Start:
            self.frame.after(1000, self.loop)
            t = t - 1
            self.min = str(int(t / 60))
            self.sec = str(t % 60)
            self.refleshtime()
        
        if t == 0 and self.status == GStatue_Start:
            c = int(self.cont)
            c = c + 1 if c + 1 <= int(Gcnt_max) else c
            self.min = self.min_t
            self.sec = self.sec_t
            self.cont = str(c)
            self.status = GStatue_Stop

            self.reflechstatus()
            self.refleshtime()
            self.refleshcounter()

            snd.Beep(523, 800)

    ###main####################################################################
    def main(self):
        self.frame.resizable(0,0)
        self.frame.mainloop()

if __name__ == '__main__':
    f = Frame()
    f.main()

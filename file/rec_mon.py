import psutil
import pandas as pd
import socket
import platform
import datetime
import threading
import time

def resorceinfo():
    
    while True:
        
        ram=[]
        memory = psutil.virtual_memory()
        m=memory[0]
        m=m/1073741824
        ram.append(round(m))
        m=memory[1]
        m=m/1073741824
        ram.append(round(m))
        m=memory[3]
        m=m/1073741824
        ram.append(round(m))
        m=memory[2]
        ram.append(m)
        
        freq=[]
        fq=psutil.cpu_freq()
        ut=psutil.cpu_percent()
        f=fq[0]/1000
        freq.append(f)
        f=fq[1]/1000
        freq.append(f)
        f=fq[2]/1000
        freq.append(f)
        freq.append(ut)
        
       #ne=['System Name','Username','IP address','Login Time','Boot Time']
       #val=[]
       #hname = socket.gethostname() 
       #val.append(hname)
       #info = psutil.users()
       #k=info[0]
       #user=k[0]
       #val.append(user)
       #hip = socket.gethostbyname(hname)
       #val.append(hip)
       #start=k[3]
       #star=datetime.datetime.fromtimestamp(start).strftime("%d-%m-%Y %H:%M:%S")
       #val.append(star)
       #boot=datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%d-%m-%Y %H:%M:%S")
       #val.append(boot)
        
        
        nm=['system','Operating system',"Operating system Version","Operating system Platform","Sys machine","Processor","Architecture"]
        ver=[]
        k1=platform.system()
        ver.append(k1)
        k2=platform.release()
        ver.append(k2)
        k3=platform.version()
        ver.append(k3)
        k4=platform.platform()
        ver.append(k4)
        k5=platform.machine()
        ver.append(k5)
        k6=platform.processor()
        ver.append(k6)
        k7=platform.architecture()
        ver.append(k7)
        
        #ne = ne + nm
        #v = val + ver
        
        disk=[]
        du = psutil.disk_usage('/')
        d=du[0]
        d=(d/1073741824)
        disk.append(round(d))
        d=du[1]
        d=(d/1073741824)
        disk.append(round(d))
        d=du[2]
        d=(d/1073741824)
        disk.append(round(d))
        d=du[3]
        disk.append(round(d))
        
        names=['IP Address','MegaBytes sent','MegaBytes Receive','Packets sent','Packets Receive','Error while Receive','Error while Sending','Incomming Packets dropped','Outgoing Packets dropped']
        va=[]
    
        host = socket.gethostname()
        ip = socket.gethostbyname(host)
        va.append(ip)   
        net=psutil.net_io_counters()
        t=1024*1024
        a=(net[0]/t)
        va.append(a)
        b=(net[1]/t)
        va.append(b)
        c=net[2]
        va.append(c)
        d=net[3]
        va.append(d)    
        e=net[4]
        va.append(e)
        f=net[5]
        va.append(f)
        g=net[6]
        va.append(g)
        h=net[7]
        va.append(h)
        
        
        #n=len(val)
        #df = pd.DataFrame({'Names':ne,'Values':v})
        #df.index = pd.RangeIndex(start=1, stop=n+1, step=1)
        #pd.set_option('display.max_rows', 500)
        #pd.set_option('display.max_columns', 500)
        #pd.set_option('display.width', 10000)
        
        
        df1 = pd.DataFrame({'Total Memory Capacity (GB)':ram[0],'Available Memory (GB)':ram[1],'Memory Used (GB':ram[2],'RAM Utilization (%)':ram[3]},index=[1])
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 10000)
        #result = df.to_html()
        
        df2 = pd.DataFrame({'CPU Current Frequence':freq[0],'CPU Minimum Frequence':freq[1],'CPU Maximum Frequence':freq[2],'CPU Utilization (%)':freq[3]},index=[1])
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 10000)
        
        df3 = pd.DataFrame({'Total Disk Capacity (GB)':disk[0],'Total Disk Used (GB) ':disk[1],'Total Disk Free (GB)':disk[2],'Disk Utilization (%)':disk[3]},index=[1])
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 10000)
        
        
        n=len(va)
        df4 = pd.DataFrame({'Names':names,'Values':va})
        df4.index = pd.RangeIndex(start=1, stop=n+1, step=1)
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.width', 10000)
        
        
        #html = df.to_html()
          
        # write html to file
        #text_file = open("index.html", "w")
        #text_file.write(html)
        #text_file.close()
        #print(result)
        #HTML(df.to_html(classes='table table-stripped'))
        
        with open("monitor.html", 'w') as _file:
            _file.write('<center>' 
                +'<style> body {background-color: white;} </style>'
                +'<h1 style="color:blue" > SYSTEM RESOURCE STATISTICS </h1><br><hr>'
              #  +'<h2 style="color:blue" style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;" > SYSTEM BASIC INFORMATION </h1>' + df.to_html(index=False,border=3,justify="center") + '<be><hr>'
                +'<h2 style="color:blue" style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;"> SYSTEM MEMORY STATISTICS </h2>' + df1.to_html(index=False,border=2,justify="center") + '<br><hr>'
                +'<h2 style="color:blue" style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;" > SYSTEM CPU STATISTICS </h2>' + df2.to_html(index=False,border=2,justify="center") + '<br><hr>'
                +'<h2 style="color:blue" style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;" > SYSTEM DISK STATISTICS </h2>' + df3.to_html(index=False,border=2,justify="center") + '<br><hr>'
                +'<h2 style="color:blue" style = "font-family:georgia,garamond,serif;font-size:16px;font-style:italic;" > SYSTEM NETWORK STATISTICS </h2>' + df4.to_html(index=False,border=2,justify="center") + '<br><hr>'
                +'</center>')
        
        time.sleep(2)

#resorceinfo()

if __name__ == '__main__':
    # starting thread to generate the number
    x = threading.Thread(target=resorceinfo(), daemon=True)
    x.start()

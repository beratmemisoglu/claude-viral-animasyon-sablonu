import subprocess,sys,numpy as np
f=sys.argv[1]; sr=16000
x=np.frombuffer(subprocess.run(['ffmpeg','-loglevel','error','-i',f,'-ac','1','-ar',str(sr),'-af','highpass=f=70,lowpass=f=1000','-f','s16le','-'],capture_output=True).stdout,np.int16).astype(np.float32)
w=int(.04*sr);h=int(.01*sr);f0=[]
for i in range(0,len(x)-w,h):
    s=x[i:i+w]; s=s-s.mean()
    if np.sqrt((s**2).mean())<800: continue
    c=np.correlate(s,s,'full')[w-1:]; lo,hi=sr//350,sr//70
    k=lo+np.argmax(c[lo:hi])
    if c[k]/c[0]>0.5: f0.append(sr/k)
f0=np.array(f0); print(f, 'voiced frames',len(f0),'median F0 %.0f Hz'%np.median(f0),'p10 %.0f p90 %.0f'%tuple(np.percentile(f0,[10,90])))

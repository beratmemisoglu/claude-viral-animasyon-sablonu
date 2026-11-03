import json,glob,os,sys
import sys; sys.stdout.reconfigure(encoding="utf-8")
root=sys.argv[1]
for ch in ['ricksclips','competitors']:
    rows=[]
    for d in glob.glob(os.path.join(root,'videos',ch,'*')):
        m=json.load(open(os.path.join(d,'meta.json'),encoding='utf-8'))
        j=[f for f in os.listdir(d) if f.endswith('.json3')]
        rows.append((m.get('upload_date'),m['id'],m.get('channel'),m.get('view_count'),m.get('duration'),m.get('width'),m.get('height'),m['title'][:60],j))
    rows.sort(reverse=True)
    for r in rows: print(ch,*r,sep=' | ')

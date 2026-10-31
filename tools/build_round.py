#!/usr/bin/env python3
"""Generic round builder (dry-run). Usage: build_round.py ROUND_ID [--report PATH] [--check-all-urls] [--refreeze]
Never writes manifest.json, never commits/pushes."""
import json,re,sys,hashlib,os,argparse,urllib.request,urllib.error,ssl,concurrent.futures as cf
LL='/workspace/learning-loop'; MAN='/workspace/learning-hub/manifest.json'
def sha(b): return hashlib.sha256(b).hexdigest()
def chash(o): return sha(json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode())
U=lambda v:'' if v.startswith('未记录') else v
def parse(rid,src):
    blocks=re.split(r'\n### ',src.split('## items',1)[1])[1:]; items=[]
    for b in blocks:
        f={}
        for line in b.split('\n'):
            mm=re.match(r'- ([^：]+)：(.*)',line)
            if not mm: continue
            k,v=mm.group(1).strip(),mm.group(2).strip()
            if ' / ' in k:  # newer merged-field line: '- id / title / url：a / b / c'
                ks=[x.strip() for x in k.split(' / ')]
                if ks[-1]=='url' and ' / ' in v:  # url last: rsplit so titles may contain ' / '
                    head,u=v.rsplit(' / ',1); vs=head.split(' / ',len(ks)-2)+[u]
                else: vs=v.split(' / ',len(ks)-1)
                for kk,vv in zip(ks,vs): f.setdefault(kk,vv.strip())
            else: f[k]=v
        if 'id' not in f: continue
        raw=f.get('url','')
        url=raw.split(' ；')[0].split('；')[0].strip()
        notes='; '.join(x for x in [U(f.get('notes','')),'实测：'+f['实测情况'] if U(f.get('实测情况','')) else '链接核实：'+f['链接核实状态'] if 'id / title / url' in b and U(f.get('链接核实状态','')) else '','待用户决定' if f.get('待用户决定','').startswith('是') else ''] if x)
        items.append({"id":f['id'],"title":f.get('title',''),"url":url,"type":U(f.get('type','')),"source":U(f.get('source','')),"category":U(f.get('category','')),"date":f.get('date',''),"summary":U(f.get('summary','')),"quality":None,"relevance":None,"score":None,"round":rid,"reason":U(f.get('reason','')),"read":False,"applied":False,"effect":"","notes":notes,"tags":[]})
    return items
def parse_eval(src):
    """picked table rows; handles '4.5（9.0）' 5-point(+old 10-point) and gate header."""
    rows=[]
    for line in src.split('\n'):
        m=re.match(r'\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*([\d.]+)(?:（([\d.]+)[^）]*）)?\s*\|',line)
        if m: rows.append({"rank":int(m[1]),"tool":m[2],"score5":float(m[3]),"score10_old":float(m[4]) if m[4] else None})
    return {"gate_header":'## 动态门禁' in src,"five_point":'5 分制' in src,"picked":rows}
URLRE=re.compile(r'^https?://[A-Za-z0-9\-._~:/?#\[\]@!$&\'()*+,;=%]+$')
def fmt(u):
    if not u: return 'empty'
    if re.search(r'[\u3000-\u9fff\uff00-\uffef]',u): return 'non-URL text (CJK/fullwidth)'
    if not URLRE.match(u): return 'bad format'
    return 'ok'
CTX=ssl.create_default_context()
def reach(u):
    h={'User-Agent':'Mozilla/5.0 (build_round dry-run)'}
    for meth in ('HEAD','GET'):
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,method=meth,headers=h),timeout=12,context=CTX)
            return meth,r.status,''
        except urllib.error.HTTPError as e:
            if meth=='HEAD': continue
            return meth,e.code,''
        except Exception as e:
            if meth=='HEAD': continue
            return meth,None,type(e).__name__
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('rid'); ap.add_argument('--report'); ap.add_argument('--check-all-urls',action='store_true'); ap.add_argument('--refreeze',action='store_true'); a=ap.parse_args()
    rid=a.rid; out=[f'# Dry-run build_round {rid}','','> 只读试跑：未改 manifest.json、未提交、未推送、未写 Notion。','']
    files={k:f'{LL}/rounds/{k}-{rid}.md' for k in ('search','eval')}
    fz=f'{LL}/tools/freeze/{rid}.json'; old=json.load(open(fz)) if os.path.exists(fz) else {}
    cur={k:sha(open(p,'rb').read()) for k,p in files.items() if os.path.exists(p)}
    out+=['## 1. 交接文件 hash 冻结','','| 文件 | 当前 SHA-256 | 冻结值 | 状态 |','|---|---|---|---|']
    for k,p in files.items():
        c=cur.get(k,'缺失'); o=old.get(k)
        st='新建基线' if o is None else ('一致' if o==c else '**已变更**')
        out.append(f'| {os.path.basename(p)} | `{c}` | `{o or "-"}` | {st} |')
    if not old or a.refreeze: json.dump(cur,open(fz,'w'),indent=1)
    out+=['',f'冻结文件：`{fz}`','']
    items=parse(rid,open(files['search']).read()); ev=parse_eval(open(files['eval']).read()) if 'eval' in cur else {}
    out+=[f'## 2. 解析','',f'- search items：{len(items)}',f'- eval：门禁表头={ev.get("gate_header")}，5 分制={ev.get("five_point")}，picked 行={len(ev.get("picked",[]))}']
    for r in ev.get('picked',[]): out.append(f'  - #{r["rank"]} {r["tool"]}：{r["score5"]}（旧 {r["score10_old"]}）')
    man=json.load(open(MAN)); mi={i['id']:i for i in man['items']}
    # compare only parser-owned fields (score/quality/relevance/tags/read/applied are set downstream)
    keys=['title','url','type','source','category','summary','reason','notes']
    new=[i for i in items if i['id'] not in mi]; diff=[]
    for i in items:
        m=mi.get(i['id'])
        if m:
            d=[k for k in keys if (m.get(k) or '')!=(i[k] or '')]
            if chash({k:i[k] for k in keys})!=chash({k:m.get(k) for k in keys}) and d: diff.append((i['id'],d))
    out+=['','## 3. content_hash 与 manifest 对比','',f'- manifest updatedAt {man.get("updatedAt")}，items {len(man["items"])}，rounds {len(man["rounds"])}',f'- 本轮 manifest 中缺失：{len(new)} {[i["id"] for i in new]}',f'- 字段有差异：{len(diff)}']
    for iid,d in diff: out.append(f'  - {iid}：{d}')
    targets={i['id']:i['url'] for i in items}
    if a.check_all_urls:
        for m in man['items']: targets.setdefault(m['id'],m.get('url',''))
    res={}
    with cf.ThreadPoolExecutor(8) as ex:
        fut={ex.submit(reach,u):k for k,u in targets.items() if fmt(u)=='ok'}
        for f in cf.as_completed(fut): res[fut[f]]=f.result()
    out+=['','## 4. URL 校验（格式 + HEAD→GET，超时 12s）','',f'检查 {len(targets)} 条','','| id | 格式 | 方法 | 状态 | url |','|---|---|---|---|---|']
    bad=[]
    for k,u in targets.items():
        f=fmt(u); meth,st,err=res.get(k,('-',None,''))
        ok=f=='ok' and st and st<400
        if not ok: bad.append(k)
        out.append(f'| {k} | {f} | {meth} | {st or err or "-"} | {u} |')
    out+=['',f'失败/存疑：{len(bad)} → {bad}','']
    txt='\n'.join(out)
    if a.report: open(a.report,'w').write(txt+'\n')
    print(txt)
if __name__=='__main__': main()

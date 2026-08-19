import json,collections,itertools,hashlib
from pathlib import Path
CORE='/mnt/data/STEP6B_CORE_DOMINANCE_V2_CI0.json'
BASE='/mnt/data/AMP_Respec_Rebuild_Step7A_Candidate_Party_Generation_v1'
FILES=['STEP7A_SLOT_0_Dark_Urge.json','STEP7A_SLOT_1_Karlach.json','STEP7A_SLOT_2_Laezel.json','STEP7A_SLOT_3_Shadowheart.json']
OUT='/mnt/data/STEP7B_SURROGATE_FRONTIER.json'
core=json.load(open(CORE));cm={r['ref']:r for r in core['representatives']}
def pop36(s):return int(s,36).bit_count()
def famvals(r):
    st=json.loads(r['structure_key']);out={}
    for k,v,u in zip(st[3],r['vec'],r['upper']):
        fam=k.split('|',1)[0];z=out.get(fam)
        if z is None or u>z[1] or (u==z[1] and v>z[0]):out[fam]=(v,u)
    return out,pop36(st[0]),pop36(st[2]),int(bool(st[1]))
def dom(a,b):return all(x>=y for x,y in zip(a,b)) and any(x>y for x,y in zip(a,b))
slot=[]; slot_summary=[]
for ci,f in enumerate(FILES):
    d=json.load(open(Path(BASE)/f));by=collections.defaultdict(list)
    for c in d['candidates']:
        r=cm[c['ref']];fv,pc,gc,dual=famvals(r)
        for fam,(cv,up) in fv.items():by[fam].append({'ref':c['ref'],'label':c['label'],'family':fam,'upper':up,'core':cv,'prof':pc,'g':gc,'dual':dual})
    fronts={}
    for fam,rows in by.items():
        rows.sort(key=lambda x:(-x['upper'],-x['core'],-x['prof'],-x['g'],-x['dual'],x['ref']));fr=[]
        for x in rows:
            xv=(x['upper'],x['core'],x['prof'],x['g'],x['dual'])
            if any(dom((y['upper'],y['core'],y['prof'],y['g'],y['dual']),xv) for y in fr):continue
            fr=[y for y in fr if not dom(xv,(y['upper'],y['core'],y['prof'],y['g'],y['dual']))];fr.append(x)
        fronts[fam]=fr
    slot.append(fronts);slot_summary.append({'ci':ci,'name':d['character_name'],'input':len(d['candidates']),'family_front_rows':sum(map(len,fronts.values())),'unique_refs':len({x['ref'] for rows in fronts.values() for x in rows}),'families':{k:len(v) for k,v in sorted(fronts.items())}})
fams=sorted(set.intersection(*[set(s) for s in slot]))
weights=[('upper',(1,0,0,0,0)),('core',(0,1,0,0,0)),('prof',(0,0,1,0,0)),('g',(0,0,0,1,0)),('balanced',(1,.5,.2,.02,1)),('core_flex',(.5,1,.3,.02,1)),('flex',(.3,.2,1,.04,2)),('caps',(.3,.2,.2,.08,1))]
best={}
for ci in range(4):
    for fam in fams:
        rows=slot[ci][fam]
        for name,w in weights:
            def sc(x):return w[0]*x['upper']+w[1]*x['core']+w[2]*x['prof']+w[3]*x['g']+w[4]*x['dual']
            best[(ci,fam,name)]=max(rows,key=lambda x:(sc(x),x['upper'],x['core'],x['prof'],x['g'],x['dual'],x['ref']))
parties={};generated=0
for ft in itertools.permutations(fams,4):
    for name,_ in weights:
        rows=[best[(ci,ft[ci],name)] for ci in range(4)];refs=tuple(x['ref'] for x in rows);generated+=1
        m=(round(sum(x['upper'] for x in rows),6),round(sum(x['core'] for x in rows),6),sum(x['prof'] for x in rows),sum(x['g'] for x in rows),sum(x['dual'] for x in rows))
        old=parties.get(refs)
        if old is None or m>tuple(old['metrics']):parties[refs]={'refs':list(refs),'families':list(ft),'metrics':list(m),'source':name}
arr=list(parties.values());arr.sort(key=lambda z:tuple(-x for x in z['metrics'])+(tuple(z['refs']),))
front=[]
for x in arr:
    xv=tuple(x['metrics'])
    if any(dom(tuple(y['metrics']),xv) for y in front):continue
    front=[y for y in front if not dom(xv,tuple(y['metrics']))];front.append(x)
front.sort(key=lambda z:(-z['metrics'][0],-z['metrics'][1],tuple(z['refs'])))
out={'schema':'amp-step7b-surrogate-party-frontier-v1','status':'PASS_WITH_HEURISTIC_SCALARIZATION_SCOPE','families':fams,'objectives':[n for n,_ in weights],'slot_frontiers':slot_summary,'generated_scalarized_parties':generated,'unique_generated_parties':len(parties),'pareto_parties':len(front),'unique_refs_by_slot':[len({x['refs'][i] for x in front}) for i in range(4)],'frontier':front,'scope_note':'Family-aware slot Pareto is deterministic; scalarization seeds are a search heuristic, not a proof over all Step7A Cartesian parties. Exact Forge prefill is the next gate.'}
Path(OUT).write_text(json.dumps(out,indent=2),encoding='utf8');print(json.dumps({k:out[k] for k in ['generated_scalarized_parties','unique_generated_parties','pareto_parties','unique_refs_by_slot']},indent=2))

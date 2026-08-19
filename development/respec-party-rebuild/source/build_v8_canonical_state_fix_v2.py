from pathlib import Path
import hashlib,json
base=Path('/mnt/data/AMP_Lab_v8.0.0_RESPEC_PARTY_REBUILD_STEP9_BETA_v7.exe')
out=Path('/mnt/data/AMP_Lab_v8.0.0_RESPEC_PARTY_REBUILD_STEP9_BETA_v8.exe')
B=base.read_bytes()
COACH_OFF,COACH_SIZE=14761728,26893
APP_OFF,APP_SIZE=14788640,38543
SOL_OFF,SOL_SIZE=14869344,42144
CAP_OFF,CAP_SIZE=17119328,1696510
coach=B[COACH_OFF:COACH_OFF+COACH_SIZE].rstrip(b' \x00').decode()
app=B[APP_OFF:APP_OFF+APP_SIZE].rstrip(b' \x00').decode()
sol_region=B[SOL_OFF:SOL_OFF+SOL_SIZE]
cap_region=B[CAP_OFF:CAP_OFF+CAP_SIZE]
old="function currentCandidate(cap,c){const id=identityOf(c),ident=id.sub||id.cls;if(!cap.identities?.[ident])return null;const cp=componentPath(cap,ident,id.cls,id.level,'primary');return cp?makeCandidate(cap,[cp],id.level):null}"
new="function currentCandidate(cap,c){let i=identityOf(c),a=c?.identity?.classes,p,l;if(a?.length>1){p=a.map((z,j)=>componentPath(cap,z.subclass||z.class,z.class,+z.level,j?'multiclass':'primary')).filter(Boolean);l=p.reduce((n,z)=>n+z.levels,0);if(p.length===a.length&&l===i.level)return makeCandidate(cap,p,l)}let x=i.sub||i.cls;p=componentPath(cap,x,i.cls,i.level,'primary');return p?makeCandidate(cap,[p],i.level):null}"
if old not in coach: raise SystemExit('currentCandidate anchor missing')
coach2=coach.replace(old,new,1)
# Remove only linebreak/leading indentation to reclaim reserved resource bytes; no semantic token rewrite.
coach2=''.join(line.lstrip(' \t') for line in coach2.splitlines())
needle="const data=state.solverData;progress(35,'Evaluating party combinations…');status('Evaluating party combinations…');await new Promise(r=>setTimeout(r,30));const r=await self.AMPV8RespecSearch.f(state.snapshot,data);"
repl="const data=state.solverData,q=new Map;state.snapshot.party.forEach((x,i)=>q.set(i,self.AMPV8Coach.currentCandidate(state.capabilityData,x)));const fs=self.AMPV8Coach.cloneWithChoices(state.snapshot,q);progress(35,'Evaluating party combinations…');status('Evaluating party combinations…');await new Promise(r=>setTimeout(r,30));const r=await self.AMPV8RespecSearch.f(fs,data);"
if needle not in app: raise SystemExit('optimize anchor missing')
app2=app.replace(needle,repl,1)
if 'self.AMPV8Arsenal?.analyze?.(state.snapshot,data,r,self.AMPV8Solver)' not in app2: raise SystemExit('arsenal anchor missing')
app2=app2.replace('self.AMPV8Arsenal?.analyze?.(state.snapshot,data,r,self.AMPV8Solver)','self.AMPV8Arsenal?.analyze?.(fs,data,r,self.AMPV8Solver)',1)
if 'self.AMPV8Shards?.analyze?.(state.snapshot,data,r,state.capabilityData,self.AMPV8Coach,sd,state.arsenalResult,self.AMPV8Solver)' not in app2: raise SystemExit('shards anchor missing')
app2=app2.replace('self.AMPV8Shards?.analyze?.(state.snapshot,data,r,state.capabilityData,self.AMPV8Coach,sd,state.arsenalResult,self.AMPV8Solver)','self.AMPV8Shards?.analyze?.(fs,data,r,state.capabilityData,self.AMPV8Coach,sd,state.arsenalResult,self.AMPV8Solver)',1)
app2=''.join(line.lstrip(' \t') for line in app2.splitlines())
cb=coach2.encode(); ab=app2.encode()
for name,payload,size in [('coach',cb,COACH_SIZE),('app',ab,APP_SIZE)]:
 print(name,len(payload),'/',size,'spare',size-len(payload))
 if len(payload)>size: raise SystemExit(name+' too large')
bb=bytearray(B)
for off,size,payload in [(COACH_OFF,COACH_SIZE,cb),(APP_OFF,APP_SIZE,ab)]: bb[off:off+size]=payload+b' '*(size-len(payload))
out.write_bytes(bb)
Path('/mnt/data/v8_coach_v8.js').write_bytes(cb)
Path('/mnt/data/v8_app_v8.js').write_bytes(ab)
manifest={
 'schema':'amp-beta-v8-canonical-current-state-fix-v2',
 'base':base.name,'base_sha256':hashlib.sha256(B).hexdigest(),
 'output':out.name,'output_sha256':hashlib.sha256(bytes(bb)).hexdigest(),'output_size':len(bb),
 'changes':['Normal Forge current party is passed through the existing canonical Coach overlay before allocation','Arsenal and Shards consume the exact same canonical current snapshot as Forge','currentCandidate now reconstructs existing multiclass paths from SaveInfo identity.classes before falling back to single-class identity'],
 'non_changes':['v8_solver.js byte-for-byte unchanged','capability_graph.json byte-for-byte unchanged','solver_data / scoring weights untouched','Respec and Full Party search algorithms untouched'],
 'solver_region_byte_identical':B[SOL_OFF:SOL_OFF+SOL_SIZE]==bytes(bb)[SOL_OFF:SOL_OFF+SOL_SIZE],
 'capability_graph_region_byte_identical':B[CAP_OFF:CAP_OFF+CAP_SIZE]==bytes(bb)[CAP_OFF:CAP_OFF+CAP_SIZE],
 'patches':[{'name':'v8_coach.js','offset':COACH_OFF,'reserved':COACH_SIZE,'payload_bytes':len(cb),'sha256':hashlib.sha256(cb).hexdigest()},{'name':'v8_app.js','offset':APP_OFF,'reserved':APP_SIZE,'payload_bytes':len(ab),'sha256':hashlib.sha256(ab).hexdigest()}]
}
ranges=sorted([(COACH_OFF,COACH_OFF+COACH_SIZE),(APP_OFF,APP_OFF+APP_SIZE)]);pos=0;ok=True
for a,z in ranges: ok &= B[pos:a]==bytes(bb)[pos:a];pos=z
ok &= B[pos:]==bytes(bb)[pos:]
manifest['outside_patch_ranges_identical']=bool(ok)
Path('/mnt/data/BETA_V8_CANONICAL_STATE_MANIFEST.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps({k:manifest[k] for k in ['output_sha256','solver_region_byte_identical','capability_graph_region_byte_identical','outside_patch_ranges_identical']},indent=2))

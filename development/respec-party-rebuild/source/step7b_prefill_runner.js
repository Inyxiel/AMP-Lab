'use strict';
const fs=require('fs');
const solver=require('/mnt/data/v8_solver_runtime_optimized_internals5.js'),I=solver._internals;
const coach=require('/mnt/data/v8_coach_runtime_export.js');
const ff=require('/mnt/data/step6b_fast_forge.js');
const data=JSON.parse(fs.readFileSync('/mnt/data/solver_data_extracted.json'));
const rawSnap=JSON.parse(fs.readFileSync('/mnt/data/QuickSave_91_direct_snapshot.json'));
const cap=JSON.parse(fs.readFileSync('/mnt/data/work_respec/capability_graph_extracted.json'));
const cat=JSON.parse(fs.readFileSync('/mnt/data/AMP_Respec_Rebuild_Step4_Respec_Profile_Catalog_v1/STEP4_RESPEC_PROFILE_CATALOG.json'));
const normalized=solver.normalize(rawSnap,data),insts=normalized.instances,ctx=ff.buildFastContext(data,insts),pidx=I.producerIndex(insts,data.items);
function candFromRef(ref){if(ref.startsWith('single:')){const id=ref.slice(7),meta=cat.tables.identities.find(x=>x.name===id),cp=coach.componentPath(cap,id,meta.base_class,12,'primary');return coach.makeCandidate(cap,[cp],12)}const pid=Number(ref.slice(4)),r=cat.profiles[pid],a=cat.tables.identities[r[0]],b=cat.tables.identities[r[1]],c1=coach.componentPath(cap,a.name,a.base_class,r[2],'primary'),c2=coach.componentPath(cap,b.name,b.base_class,r[3],'multiclass');return coach.makeCandidate(cap,[c1,c2],12)}
function snapshotForRefs(refs){const choices=new Map;for(let i=0;i<4;i++){const r=refs[i];choices.set(i,r?candFromRef(r):coach.currentCandidate(cap,rawSnap.party[i]));}return coach.cloneWithChoices(rawSnap,choices)}
function prefill(refs){const snap=snapshotForRefs(refs),n=solver.normalize(snap,data),chars=n.characters,lists=chars.map(c=>I.buildCore(c,data,insts,pidx));if(lists.some(x=>!x.length))return {status:'NO_SOLUTION'};const combos=I.topCombos(lists,3);let best=null,bsel=null;for(const [coreSum,sel] of combos){const cb=Object.fromEntries(sel.map(c=>[c.character_id,c])),ordered=chars.map(c=>cb[c.id]),pools=ordered.map((c,i)=>ff.fastPreindexOne(chars[i],c,ctx)),x=ff.fullComboFast(sel,chars,ctx,pools);if(x&&(!best||x[0]>best[0])){best=x;bsel=sel;}}if(!best)return {status:'NO_SOLUTION'};const cb=Object.fromEntries(bsel.map(c=>[c.character_id,c])),ordered=chars.map(c=>cb[c.id]);return {status:'PASS',prefill_score:Math.round(best[0]*1000)/1000,core_score:Math.round(ordered.reduce((s,c)=>s+(Number(c.score)||0),0)*1000)/1000,builds:ordered.map((c,i)=>({character_name:chars[i].name,identity:c.identity,orb_family:c.orb_family,orb_tier:c.orb_tier,core_score:c.score,gear_instance_ids:best[1][i]}))};}
if(require.main===module){const spec=process.argv[2]||'';const refs=[null,null,null,null];for(const part of spec.split(',').filter(Boolean)){const j=part.indexOf('=');refs[Number(part.slice(0,j))]=part.slice(j+1);}console.time('prefill');const r=prefill(refs);console.timeEnd('prefill');console.log(JSON.stringify({refs,result:r},null,2));}
module.exports={prefill,candFromRef,snapshotForRefs};

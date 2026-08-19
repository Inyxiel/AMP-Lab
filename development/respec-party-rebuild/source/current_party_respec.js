(()=>{'use strict';
const round3=x=>Math.round((Number(x)||0)*1000)/1000;
function utility(x){return (x?.char_delta||0)+.45*(x?.party_delta||0)+.02*(x?.step3_support?.score||0)}
function capDelta(a,b){const A=new Set(a||[]),B=new Set(b||[]);return {gain:[...B].filter(x=>!A.has(x)).sort(),loss:[...A].filter(x=>!B.has(x)).sort()}}
function runtimeContext(snapshot,data,orbs,currentKey){
 return {current_key:currentKey,owned_item_profiles:data?.owned_item_profiles||data?.item_profiles||[],owned_orbs:orbs||{},matrix:data?.matrix||data?.orb_matrix||{}};
}
async function evaluateCharacter({snapshot,data,cap,solver,coach,filter,baseline,currentChoices,ci,allCandidates,onProgress}){
 const cur=currentChoices.get(ci), baseBuild=baseline.builds[ci], ctx=runtimeContext(snapshot,data,baseline.owned_orbs||{},cur.key);
 const f=filter.filter(allCandidates,ctx); const evals=[];
 for(let j=0;j<f.candidates.length;j++){
  const cand=f.candidates[j]; onProgress?.({stage:'current-party-respec',characterIndex:ci,candidateIndex:j+1,candidateTotal:f.candidates.length,candidate:cand.label});
  let r;if(cand.key===cur.key)r=baseline;else{const ch=new Map(currentChoices);ch.set(ci,cand);r=solver.allocate(coach.cloneWithChoices(snapshot,ch),data)}
  if(r.status!=='PASS'){evals.push({key:cand.key,label:cand.label,status:r.status,reason:r.reason||'No legal global allocation',step3_support:cand.step3_support});continue}
  const cb=r.builds[ci],d=capDelta(cur.profile.guaranteed_capabilities,cand.profile.guaranteed_capabilities);
  evals.push({...cand,status:'PASS',party_score:r.party_score,party_delta:round3(r.party_score-baseline.party_score),char_score:cb.final_build_score,char_delta:round3(cb.final_build_score-baseBuild.final_build_score),capability_gain:d.gain,capability_loss:d.loss,allocation:r});
 }
 const passing=evals.filter(x=>x.status==='PASS').sort((a,b)=>utility(b)-utility(a)||b.party_score-a.party_score||String(a.key).localeCompare(String(b.key)));
 return {filter:{input:f.input,relevant:f.relevant,efficient:f.efficient,inventory_supported:f.inventory_supported,audit:f.audit},passing,current:passing.find(x=>x.key===cur.key),best:passing[0]||null};
}
async function analyze(opts){
 const {snapshot,data,cap,solver,coach,filter,candidateProvider,onProgress}=opts||{};
 if(!snapshot?.party?.length)throw Error('Current Party Respec requires a parsed party snapshot.');
 if(!solver?.allocate||!coach?.cloneWithChoices||!coach?.currentCandidate)throw Error('Frozen Forge/override hooks unavailable.');
 if(!filter?.filter)throw Error('Step 3 canonical filter unavailable.');
 if(typeof candidateProvider!=='function')throw Error('Canonical candidateProvider unavailable.');
 const currentChoices=new Map;for(let i=0;i<snapshot.party.length;i++){const c=coach.currentCandidate(cap,snapshot.party[i]);if(!c)throw Error('Current identity unresolved at party index '+i);currentChoices.set(i,c)}
 const baseline=solver.allocate(coach.cloneWithChoices(snapshot,currentChoices),data);if(baseline.status!=='PASS')throw Error('Frozen Forge baseline failed: '+(baseline.reason||'unknown'));
 const characters=[];for(let ci=0;ci<snapshot.party.length;ci++){const all=await candidateProvider({ci,character:snapshot.party[ci],current:currentChoices.get(ci),cap,data,snapshot,coach});characters.push(await evaluateCharacter({snapshot,data,cap,solver,coach,filter,baseline,currentChoices,ci,allCandidates:all,onProgress}))}
 return {version:'amp-respec-step6a-current-party-engine-v1',status:'PASS',baseline_party_score:baseline.party_score,characters};
}
const API={version:'amp-respec-step6a-current-party-engine-v1',analyze,evaluateCharacter,runtimeContext,utility};if(typeof module!=='undefined'&&module.exports)module.exports=API;else self.AMPCurrentPartyRespec=API;
})();

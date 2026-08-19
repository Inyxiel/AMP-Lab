(()=>{'use strict';
function m(idx,id,l){const z=idx?.identities?.[id]?.levels?.[String(l)];return z?{total:+z.intrinsic_total||0,gain:+z.gain_from_previous||0}:{total:0,gain:0}}
function featCount(idx,cls,l){return (idx?.feat_asi_levels?.[cls]||[]).filter(x=>+x<=+l).length}
function metrics(c,idx){let total=0,gain=0,feats=0;for(const p of c?.components||[]){const id=p.identity||p.subclass||p.class,cls=p.class,lv=+p.levels||0,z=m(idx,id,lv);total+=z.total;gain+=z.gain;feats+=featCount(idx,cls,lv)}return {intrinsic_total:total,endpoint_gain:gain,feat_asi_slots:feats}}
function sameSplit(a,b){const A=a?.components||[],B=b?.components||[];if(A.length!==B.length)return false;return A.every((x,i)=>x.class===B[i]?.class&&+x.levels===+B[i]?.levels&&String(x.entry_mode||'')===String(B[i]?.entry_mode||''))}
function chooseExactEquivalent(group,idx){if(!Array.isArray(group)||!group.length)return null;const canonical=[...group].sort((a,b)=>String(a.key||a.ref||'').localeCompare(String(b.key||b.ref||'')))[0],eligible=group.filter(x=>sameSplit(x,canonical));eligible.sort((a,b)=>{const A=metrics(a,idx),B=metrics(b,idx);return B.intrinsic_total-A.intrinsic_total||B.feat_asi_slots-A.feat_asi_slots||B.endpoint_gain-A.endpoint_gain||String(a.key||a.ref||'').localeCompare(String(b.key||b.ref||''))});return eligible[0]||canonical}
const API={version:'amp-respec-step8-breakpoint-refinement-v1',metrics,chooseExactEquivalent};if(typeof module!=='undefined'&&module.exports)module.exports=API;else self.AMPRespecBreakpointRefinement=API;
})();

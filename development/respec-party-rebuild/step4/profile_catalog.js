// AMP Lab Step 4 — compact respec profile catalog helper
export function decodeProfile(catalog, id) {
  const r = catalog.profiles[id]; if (!r) return null;
  const ids = catalog.tables.identities, comps = catalog.tables.component_keys;
  return { id, first: ids[r[0]], second: ids[r[1]], firstLevels:r[2], secondLevels:r[3], firstComponent:comps[r[4]], secondComponent:comps[r[5]], totalLevel:r[6] };
}
export function idsForSplit(catalog,total,firstClass,secondClass,firstLevels,secondLevels){
  const range=catalog.indexes.split_ranges[[total,firstClass,secondClass,firstLevels,secondLevels].join('|')];
  if(!range) return []; const out=[]; for(let i=range[0];i<range[1];i++) out.push(i); return out;
}
export function level12Candidates(catalog){ return catalog.indexes.l12.all; }
export function level12ForIdentity(catalog,identity){ return catalog.indexes.l12.identity[identity]||[]; }

# Read-only profiler. Usage: python EVD-C-05-profile.py <path-to-data/synthetic> <manifest.json> > output.json
import csv,json,sys,collections,statistics as st,datetime,os
D=sys.argv[1]; M=json.load(open(sys.argv[2]))
def rd(n): return list(csv.DictReader(open(os.path.join(D,n),newline='',encoding='utf-8')))
def pct_idx(v,p): v=sorted(v); return v[int(p/100*len(v))]
def num(x):
    try: return float(x)
    except: return None
FILES={'shipments.csv':'shipment_id','tracking_events.csv':'event_id','vehicles.csv':'vehicle_id','routes.csv':'route_id','carrier_bookings.csv':'booking_id','ai_invocations.csv':'ai_call_id'}
TS={'shipments.csv':['promised_at'],'tracking_events.csv':['event_time'],'carrier_bookings.csv':['created_at']}
out={'datasets':{}}
data={n:rd(n) for n in FILES}
ship_ids={r['shipment_id'] for r in data['shipments.csv']}
for n,k in FILES.items():
    rows=data[n]; cols=list(rows[0]); keys=collections.Counter(r[k] for r in rows)
    d={'rows':len(rows),'manifest_expected':M['csv_files'][n],'key':k,
       'duplicate_keys':{a:b for a,b in keys.items() if b>1},
       'rows_with_blank':[i+2 for i,r in enumerate(rows) if any(v=='' for v in r.values())],
       'fully_blank_rows':sum(1 for r in rows if all(v=='' for v in r.values())),
       'first_row_key':rows[0][k],'rec_prefixed_keys':[r[k] for r in rows if r[k].startswith('REC-')]}
    d['timestamps']={}
    for c in TS.get(n,[]):
        vals=[r[c] for r in rows if r[c]]
        bad=[v for v in vals if v.startswith('1900') or v.startswith('0001') or v>'2030']
        d['timestamps'][c]={'min':min(vals),'max':max(vals),'out_of_domain':bad}
    d['numeric']={}
    for c in cols:
        vs=[num(r[c]) for r in rows]; vs=[v for v in vs if v is not None]
        if len(vs)>len(rows)*0.9 and c not in (k,): d['numeric'][c]={'min':min(vs),'max':max(vs),'mean':round(st.mean(vs),3),'negative':sum(v<0 for v in vs)}
    d['categorical']={}
    for c in cols:
        vs=[r[c] for r in rows]; u=set(vs)
        if len(u)<=16 and c not in d['numeric']: d['categorical'][c]=dict(collections.Counter(vs))
    out['datasets'][n]=d
# range anomalies
tr=data['tracking_events.csv']; vh=data['vehicles.csv']
out['range_anomalies']={'tracking_confidence_gt1':sum(1 for r in tr if num(r['confidence']) and num(r['confidence'])>1),
 'vehicle_fuel_gt1_or_lt0':sum(1 for r in vh if num(r['fuel_level_pct']) is not None and not 0<=num(r['fuel_level_pct'])<=1),
 'shipments_actual_gt_declared':sum(1 for r in data['shipments.csv'] if num(r['actual_weight_kg']) and num(r['declared_weight_kg']) and num(r['actual_weight_kg'])>num(r['declared_weight_kg']))}
# referential integrity
ri={}
for n in ['tracking_events.csv','carrier_bookings.csv','ai_invocations.csv']:
    orphans=[r[FILES[n]] for r in data[n] if r['shipment_id'] and r['shipment_id'] not in ship_ids]
    ri[n]={'orphan_count':len(orphans),'orphan_keys':orphans[:10]}
cb=collections.Counter(r['shipment_id'] for r in data['carrier_bookings.csv'] if r['shipment_id'])
ri['carrier_bookings.csv']['shipments_with_multiple_bookings']=sum(1 for v in cb.values() if v>1)
out['referential_integrity']=ri
rt=[int(r['retry_count']) for r in data['carrier_bookings.csv'] if r['retry_count'].isdigit()]
out['carrier_retry']={'min':min(rt),'max':max(rt),'mean':round(st.mean(rt),1)}
tk=[int(r['token_count']) for r in data['ai_invocations.csv'] if r['token_count'].isdigit()]
out['ai_tokens']={'rows_parsed':len(tk),'sum':sum(tk)}
ev=[json.loads(l) for l in open(os.path.join(D,'events.jsonl'))]
lat=[e['latency_ms'] for e in ev]; cost=[e['cost_units'] for e in ev]
nul=sum(e['correlation_id'] is None for e in ev)
bye=collections.defaultdict(lambda:{'events':0,'cost':0.0})
for e in ev: bye[e['business_entity']]['events']+=1; bye[e['business_entity']]['cost']+=e['cost_units']
out['events']={'count':len(ev),'manifest_expected':M['jsonl_events'],'null_correlation_id':nul,'correlation_complete_pct':round(100*(len(ev)-nul)/len(ev),1),
 'severity':dict(collections.Counter(e['severity'] for e in ev)),
 'error_plus_critical':sum(e['severity'] in('error','critical') for e in ev),
 'latency_ms':{'p50':pct_idx(lat,50),'p95':pct_idx(lat,95),'p99':pct_idx(lat,99),'max':max(lat)},
 'cost_units':{'total':round(sum(cost),2),'mean':round(st.mean(cost),4)},
 'by_entity':{k:{'events':v['events'],'cost':round(v['cost'],2),'cost_per_event':round(v['cost']/v['events'],3)} for k,v in bye.items()},
 'duplicate_event_ids':len(ev)-len({e['event_id'] for e in ev}),
 'actors_not_in_api_role_list':sorted({e['actor'] for e in ev}-{'admin','operator','clinician','engineer','ai_agent'})}
json.dump(out,sys.stdout,indent=1,default=str)

import csv, sys, os, json
from collections import defaultdict
raw=sys.argv[1]; out=sys.argv[2]
rows=[]
SRC_AI="Indeed Hiring Lab, AI Tracker (github.com/hiring-lab/ai-tracker), CC BY 4.0"
SRC_JP="Indeed Hiring Lab, Job Postings Tracker (github.com/hiring-lab/job_postings_tracker), CC BY 4.0"
# A: AI share of postings, monthly mean of daily 7-day averages
acc=defaultdict(list)
for r in csv.DictReader(open(f"{raw}/ai-tracker/AI_posting.csv")):
    acc[(r['jobcountry'],r['date'][:7])].append(float(r['AI_share_postings']))
for (c,m),v in acc.items():
    rows.append(dict(indicator="ai_share_postings",label="Share of job postings mentioning AI (%)",country=c,group="All postings",month=m,value=round(sum(v)/len(v),3),n_days=len(v),source=SRC_AI))
# B: postings index by occupation group, total postings, monthly mean
base=f"{raw}/job_postings_tracker"
for c in sorted(os.listdir(base)):
    f=f"{base}/{c}/job_postings_by_sector_{c}.csv"
    if not os.path.exists(f): continue
    acc=defaultdict(list)
    for r in csv.DictReader(open(f)):
        if r['variable']!='total postings': continue
        acc[(r['display_name'],r['date'][:7])].append(float(r['indeed_job_postings_index']))
    for (g,m),v in acc.items():
        rows.append(dict(indicator="postings_index_group",label="Job postings index by occupation group (Feb 2020 = 100)",country=c,group=g,month=m,value=round(sum(v)/len(v),2),n_days=len(v),source=SRC_JP))
# C: aggregate postings index (seasonally adjusted where given)
for c in sorted(os.listdir(base)):
    f=f"{base}/{c}/aggregate_job_postings_{c}.csv"
    if not os.path.exists(f): continue
    acc=defaultdict(list)
    for r in csv.DictReader(open(f)):
        if r.get('variable','total postings')!='total postings': continue
        val=r.get('indeed_job_postings_index_SA') or r.get('indeed_job_postings_index')
        if not val: continue
        acc[r['date'][:7]].append(float(val))
    for m,v in acc.items():
        rows.append(dict(indicator="postings_index_total",label="Job postings index, all occupations (Feb 2020 = 100, seasonally adjusted where available)",country=c,group="All postings",month=m,value=round(sum(v)/len(v),2),n_days=len(v),source=SRC_JP))
rows.sort(key=lambda r:(r['indicator'],r['country'],r['group'],r['month']))
with open(f"{out}/cognitive_roi_dataset.csv","w",newline="") as fh:
    w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
from collections import Counter
print(len(rows)); print(Counter(r['indicator'] for r in rows))
print(sorted(set(r['country'] for r in rows)))
for ind in set(r['indicator'] for r in rows):
    ms=[r['month'] for r in rows if r['indicator']==ind]; print(ind,min(ms),max(ms))
summary={"data_points":len(rows),"by_indicator":dict(Counter(r['indicator'] for r in rows)),
 "countries":sorted(set(r['country'] for r in rows)),
 "latest_month":max(r['month'] for r in rows),
 "sources":sorted(set(r['source'] for r in rows))}
json.dump(summary,open(f"{out}/summary.json","w"),indent=2)
print(json.dumps(summary,indent=2))

"""LxthalFC scoring engine (rebuilt 14 Sep 2026). RECENT_MEDIAN recomputed from own catalog."""
import math, json, statistics, datetime
OWN = json.load(open('/root/lx/own.json'))
OWN_MEDIAN = int(statistics.median([r['views'] for r in OWN]))
cut = (datetime.date.today() - datetime.timedelta(days=30)).isoformat()
rec = [r['views'] for r in OWN if r['date'] >= cut]
RECENT_MEDIAN = int(statistics.median(rec)) if len(rec) >= 5 else 180000
LANE_RECENT = {"award-goat-debate":540000,"messi-ronaldo":292751,"every-x-series":469592,"skill-oddity":469540,
 "goalkeeper":558128,"big-brain-iq":747074,"emotion-celebration":140036,"crashout-drama":128402,"world-cup":145636,
 "other":310552,"single-player":85513,"goals-skills-generic":77724,"top3-story":43044}
PLAYBOOK = {"award-goat-debate":1.4,"messi-ronaldo":1.3,"skill-oddity":1.25,"every-x-series":1.2,"goalkeeper":1.2,
 "big-brain-iq":1.2,"emotion-celebration":1.0,"crashout-drama":0.9,"world-cup":0.9,"other":1.0,"single-player":0.4,
 "goals-skills-generic":0.6,"top3-story":0.5}
def precedent_factor(v,c):
    cv=c/v*100 if v else 0
    return min(1.45, 0.75+0.5*min(cv/0.05,1)+0.2*min(c/3000,1))
def outlier_index(v,c,channel_median=None):
    if channel_median: return round(min(10,v/channel_median),1)
    cv=c/v*100 if v else 0
    return round(min(10,math.sqrt(max(v/1e6,.01)*max(cv/0.02,.01))),1)
def score_idea(lane,v,c,outlier_match=1.0,own_parent_views=None,channel_median=None):
    base=LANE_RECENT.get(lane,RECENT_MEDIAN); pm=PLAYBOOK.get(lane,1.0)
    pred = own_parent_views*0.75*outlier_match if own_parent_views else base*pm*precedent_factor(v,c)*outlier_match/1.2
    perf=max(1,min(99,round(20*math.log2(pred/RECENT_MEDIAN)+50)))
    return dict(pred_views=int(round(pred,-3)),pred_range=(int(round(pred*.45,-3)),int(round(pred*2.2,-3))),perf_score=perf,outlier_x=outlier_index(v,c,channel_median))
if __name__=="__main__": print(OWN_MEDIAN,RECENT_MEDIAN,len(rec))

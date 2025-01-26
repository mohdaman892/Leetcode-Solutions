class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        
        mentions = [0 for i in range(n)]
        online = set([str(i) for i in range(n)])

        back_online = []

        event_dict = {}
        for event in events:
            m,t,s = event[0],int(event[1]),event[2]
            if t not in event_dict:
                event_dict[t] = {}
            if m not in event_dict[t]:
                event_dict[t][m] = [] 
            event_dict[t][m].append(s)
                

        # print(event_dict)

        for t in sorted(event_dict.keys()):
            # print(online,mentions,t)
            new_back_online = []
            for x in back_online:
                if t>=int(x[0])+60:
                    online.add(x[1][2:])
                else:
                    new_back_online.append(x)
            back_online = new_back_online
            if "OFFLINE" in event_dict[t]:
                for u_id in event_dict[t]["OFFLINE"]:
                    online.discard(u_id)
                    back_online.append([t,"id"+u_id])   
            if "MESSAGE" in event_dict[t]:
                for s in event_dict[t]["MESSAGE"]:
                    if s == "ALL":
                        for i in range(n):
                            mentions[i]+=1
                    elif s == "HERE":
                        for i in online:
                            mentions[int(i)]+=1
                    else:
                        x = list(map(str, s.split(" ")))
                        # print(x)
                        for u_id in x:
                            u_id = u_id[2:]
                            mentions[int(u_id)]+=1
        
        return mentions
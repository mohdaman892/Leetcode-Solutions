function maximumCandies(candies: number[], k: number): number {

    function check(x: number){
        if(x==0){
            return true
        }
        var s:number = 0
        for(let i in candies){
            s = s + Math.floor(candies[i]/x)
        }
        return s>=k
    }
    
    candies.sort((a,b) => a-b)
    var l:number = 0
    var r:number = candies[candies.length - 1]
    var ans:number = Number.MIN_SAFE_INTEGER
    console.log(l,r)
    while(l<r){
        var mid:number = Math.floor((l+r)/2)
        console.log(mid)
        if(check(mid)){
            ans = Math.max(ans, mid)
            l = mid+1
        }
        else{
            r = mid
        }
    }

    if(check(l)){
        ans = Math.max(ans,l)
    }

    return ans
};
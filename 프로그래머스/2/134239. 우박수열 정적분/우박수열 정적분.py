def make_graph(k, graph):
    while(k != 1):
        graph.append(k)
        if k % 2:
            k = 3*k +1
        else:
            k = k / 2
    graph.append(1)

def solution(k, ranges):
    answer = []
    graph = []
    make_graph(k, graph)
    l = len(graph) 
    
    for ra in ranges:
        a = ra[0]
        b = l + ra[1] -1
        area_sum = 0
        
        if a > b:
            
            area_sum = -1;
            
        else:
            
            for i in range(a, b):
                area_sum += (graph[i] + graph[i + 1]) / 2
            
        """
        if b != 0:
            for i in range(a, l + b - 1):
                area_sum += (graph[i] + graph[i + 1]) / 2
        else:
            for i in range(a, l + b - 1):
                area_sum += (graph[i] + graph[i + 1]) / 2
        """
                
        
            
        answer.append(area_sum)
        
        
    return answer
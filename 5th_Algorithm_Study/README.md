- **********\*\*\*\***********\*\*\*\***********\*\*\*\***********The Concept of the chapter**********\*\*\*\***********\*\*\*\***********\*\*\*\***********
    <aside>
    💡 **수학에서, 좀 더 구체적으로 그래프 이론에서 그래프란 객체의 일부 쌍(pair)들이 ‘연관되어’ 있는 객체 집합 구조를 말한다**
    
    </aside>
    
    ### 1. Eulerinan Trail/Eaulerian Path - 오일러 경로(오일러 정리)
    
    
    ****—**** 정점(vertex), 간선(Edge)으로 구성된 그래프 과정에서 모든 정점이 짝수 개의 차수(Degree)를 갖는다면 모든 간선들을 한 번씩만 건너서 도달하는 것이 성립한다. (한 붓 그리기)
    
    ---
    
    ### 2. Hamilonian Path - 해밀턴 경로
    
    - ********************************************************************************************************************************************************************************************************************************************************************************************************오일러 경로와의 차이 : 오일러 경로는 간선을 기준으로 하고 해밀턴 경로는 정점을 기준으로 하여 진행(NP-완전 문제[NP 문제 중 NP-난해(Hard)인 문제]********************************************************************************************************************************************************************************************************************************************************************************************************
        - **************************************외판원 문제(TSP) : 해밀턴 순환(한 번만 방문하여 출발지로 돌아오는 경로) 중에서 가장 짧은 경로**************************************
        
        
    
    ---
    
    ### 3. Graph Search(그래프 순회/그래프 탐색)
    
    - **************************************************************************************그래프의 각 정점(vertex)를 방문하는 방법**************************************************************************************
        1. **깊이 우선 탐색(Depth-First Search → DFS)**
            - 재귀 구조로 구현(Recursive)
                
                ```python
                def recursive_dfs(v, discovered=[]):
                	discovered.append(v)
                	for w in graph[v]:
                		if not w in discovered:
                			discovered = recursive_dfs(w, discovered)
                	return discovered
                
                # 방문했던 정점, 즉 discovered를 계속 누적된 결과로 만들기 위해 리턴하는 형태만 받아오도록 처리
                # 정점 v의 모든 인접 유향 간선들에 대해 반복
                ```
                
            - 스택을 이용한 반복 구조로 구현
                
                ```python
                def iterative_dfs(start_v):
                	discovered = []
                	stack = [start_v]
                	while stack:
                		v = stack.pop()
                		if v not in discovered:
                			discovered.append(v)
                			for w in graph[v]:
                				stack.append(w)
                	return discovered
                ```
                
            
            
        2. **너비 우선 탐색(Breadth-First Search → BFS)**
            - 큐를 이용한 반복 구조로 구현
                
                ```python
                def iterative_bfs(start_v):
                	discovered = [start_v]
                	queue = [start_v]
                	while queue:
                		v = queue.pop(0)
                		for w in graph[v]:
                			if w not in discovered:
                				discovered.append(w)
                				queue.append(w)
                	return discovered
                ```
                
            
            
    
    ---
    
    ### 4. Backtracking(백트래킹)
    
    - 해결책에 대한 후보를 구축해 나아가다 가능성이 없다고 판단되는 즉시 후보를 포기(백트랙 `Backtrack` )해 정답을 찾아가는 범용적인 알고리즘
    - 제약 충족 문제에 유용 `Constraint Satisfaction Problems`

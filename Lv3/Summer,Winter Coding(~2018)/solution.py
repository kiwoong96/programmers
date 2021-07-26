def solution(skill, skill_trees):
    result = len(skill_trees)
    for now in skill_trees:
        idx = 0
        for now_str in now:
            if now_str in skill:
                find_idx = skill.index(now_str)
                if find_idx > idx:
                    result -=1
                    break
                else: 
                    idx += 1
                    continue
                    
            
    
    return result
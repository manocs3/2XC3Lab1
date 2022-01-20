studentNum = [1,2,3,4,5,6,7]
groups = [[1,3],[2,4,5],[6,7]]

def are_valid_groups(studentNum, groups):
    flattenedGroups = []
    for group in groups:
        for i in group:
            flattenedGroups.append(i)
            
    check =  all(id in flattenedGroups for id in studentNum)
 
    if check is True:
        print("groups contains all studentIDs")    
    else :
        print("No, groups doesn't have all studentIDs.")
    

def goodGroups(groups):
    flattenedGroups = []
    validgroups = 0
    invalidgroups =[]
    
    for group in groups:
        for i in group:
            flattenedGroups.append(i)
    
    for group in groups:
        if ((len(group) == 2) or (len(group) == 3)):
            validgroups = validgroups + 1
        else:
            invalidgroups.append(group)
    
    if (len(flattenedGroups) == len(set(flattenedGroups))) and (validgroups == len(groups)):
        print("Ture! Each student ids appears exactly once in the group list and each group has 2-3 people")
    else:
        print("here is/are group(s) which doesnt/dont have 2-3 people:" ) 
        print(invalidgroups)

        
are_valid_groups(studentNum, groups)
goodGroups(groups)

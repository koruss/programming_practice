
def moveLeft(n,k,r_q, c_q , obstacles):
    count = 0
    for i in range(c_q -1 ,0,-1):
        if ( (r_q,i) ) in obstacles:
            break
        else:
            count += 1
    return count
#-----------------------------------------------------------------
def moveRight(n,k,r_q, c_q , obstacles):
    count = 0
    for i in range(c_q+1,n+1):
        if ( (r_q,i) ) in obstacles:
            break
        else:
            count += 1
    return count
#-----------------------------------------------------------------
def moveUp(n,k,r_q, c_q , obstacles):
    count = 0
    for i in range(r_q+1,n+1):
        if ( (i,c_q) ) in obstacles:
            break
        else:
            count += 1
    return count
#-----------------------------------------------------------------
def moveDown(n,k,r_q, c_q , obstacles):
    count = 0
    for i in range(r_q-1,0, -1 ):
        if ( (i,c_q) ) in obstacles:
            break
        else:
            count += 1
    return count
#-----------------------------------------------------------------
def moveDownLeft(n,k,r_q, c_q , obstacles):
    count = 0
    x = r_q - 1
    y = c_q - 1
    while (x >= 1 and y >= 1):
        if ( (x,y) ) in obstacles:
            break
        else:
            count += 1
        x -=1
        y -=1
    return count
#-----------------------------------------------------------------
def moveDownRight(n,k,r_q, c_q , obstacles):
    count = 0
    x = r_q -1
    y = c_q + 1
    while (x >=1  and y <= n):
        if ( (x,y) ) in obstacles:
            break
        else:
            count += 1
        x -=1
        y +=1
    return count
#-----------------------------------------------------------------
def moveUpLeft(n,k,r_q, c_q , obstacles):
    count = 0
    x = r_q +1 
    y = c_q - 1
    while (x <=n  and y >=1):
        if ( (x,y) ) in obstacles:
            break
        else:
            count += 1
        x +=1
        y -=1
    return count
#-----------------------------------------------------------------
def moveUpRight(n,k,r_q, c_q , obstacles):
    count = 0
    x = r_q + 1
    y = c_q + 1
    while (x <=n  and y<=n):
        if ( (x,y) ) in obstacles:
            break
        else:
            count += 1
        x +=1
        y +=1
    return count
#-----------------------------------------------------------------

# - int n: the number of rows and columns in the board
# - nt k: the number of obstacles on the board
# - int r_q: the row number of the queen's position
# - int c_q: the column number of the queen's position
# - int obstacles[k][2]: each element is an array of  integers, the row and column of an obstacle
def queensAttack(n,k,r_q, c_q , obstacles):
    obs = {}
    for i in obstacles:
        obs[(i[0],i[1])] = True

    return moveDown(n,k,r_q,c_q,obs) + moveUp(n,k,r_q,c_q,obs) + moveLeft(n,k,r_q,c_q,obs) + moveRight(n,k,r_q,c_q,obs) + moveDownLeft(n,k,r_q,c_q,obs) + moveDownRight(n,k,r_q,c_q,obs) + moveUpLeft(n,k,r_q,c_q,obs) + moveUpRight(n,k,r_q,c_q,obs)







print(queensAttack(5,3,4,3,[[5, 5], [4, 2], [2, 3]]))
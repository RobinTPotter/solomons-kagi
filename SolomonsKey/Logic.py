from math import floor
from Joystick import Joystick


# created this for the react to the press down of fire
def event(_keys,key,solomon):
    keys = Joystick()
    if (keys.isFire(_keys)):
            solomon.sol_wand = solomon.sol_wand_limit
            print("ding")
    

def gogogo(level, solomon, _keys):
    
    ## print(solomon,level,_keys)
    keys = Joystick()
    
    if keys.isDown(_keys): solomon.sol_crouch=1
    else: solomon.sol_crouch=0

    left_headwall = solomon.sol_tile_at_left_head(level.grid)
    left_footwall = solomon.sol_tile_at_left_foot(level.grid)
    right_headwall = solomon.sol_tile_at_right_head(level.grid)
    right_footwall = solomon.sol_tile_at_right_foot(level.grid)

    ## print('walls lh {} lf {} rh {} rf {}'.format(left_headwall, left_footwall, right_headwall, right_footwall))
            
    solomon.sol_walking=0

    if keys.isLeft(_keys):
        solomon.sol_dir = -1
        if  (solomon.sol_crouch==0 and left_footwall==0 and left_headwall==0):
            solomon.solx-=solomon.sol_step
            solomon.sol_walking=1
    elif keys.isRight(_keys):
        solomon.sol_dir = 1
        if (solomon.sol_crouch==0 and right_footwall==0 and right_headwall==0):
            solomon.solx+=solomon.sol_step            
            solomon.sol_walking=1
    

    floating=False
    leftfootfloor = solomon.sol_tile_at_left_foot_floor(level.grid)
    rightfootfloor = solomon.sol_tile_at_right_foot_floor(level.grid)
    nofloor=(leftfootfloor==0 and rightfootfloor==0 )
    
    ## print('floor lf {} rf {} nf {}'.format(leftfootfloor, rightfootfloor, nofloor))
    ## print(f"y {solomon.soly} ")
    
    if ((solomon.soly%solomon.tile)!=0 or nofloor ): floating=True  
    #if (nofloor ): floating=True  

    ## print (f"floating {floating}")
    
    if (solomon.sol_crouch==0 and keys.isUp(_keys) and not floating ):
        if (solomon.sol_jump==0): 
            solomon.sol_jump=solomon.sol_jump_limit
            solomon.sol_jump_rest = solomon.sol_jump_rest_limit
        
    
    
    if (solomon.sol_jump>0 and solomon.sol_jump_rest==0):
        solomon.sol_jump -= 1
            
        leftheadceiling = solomon.sol_tile_at_left_head_ceiling(level.grid)
        rightheadceiling = solomon.sol_tile_at_right_head_ceiling(level.grid)
        
        
        if (leftheadceiling==0 and rightheadceiling==0): solomon.soly+=solomon.sol_jump_inc
        else:
            solomon.sol_jump=0
            if  (solomon.sol_dir==-1 and leftheadceiling>0 and leftheadceiling!=3 and solomon.sol_tile_dist_left_head(level.grid)<solomon.sol_size):
                ll = floor((solomon.soly+solomon.sol_size)/solomon.tile)
                cc = (floor(solomon.solx/solomon.tile))
                level.grid[ll][cc] = leftheadceiling-1
                #var b = document.getElementById(`block_cc${cc}ll${ll}`)
                if (level.grid[ll][cc]==0):
                    #document.body.removeChild(b)
                    pass
                elif (level.grid[ll][cc]==1):
                    pass
                    #b.style.backgroundColor = "grey"
            elif (solomon.sol_dir==1 and rightheadceiling>0 and rightheadceiling!=3 and solomon.sol_tile_dist_right_head(level.grid)<(solomon.tile-solomon.sol_size)):
                ll = floor((solomon.soly+solomon.sol_size)/solomon.tile)
                cc = floor((solomon.solx+solomon.sol_size-solomon.sol_step)/solomon.tile)
                level.grid[ll][cc] = rightheadceiling-1
                #var b = document.getElementById(`block_cc${cc}ll${ll}`)
                if (level.grid[ll][cc]==0):
                    #document.body.removeChild(b)
                    pass
                elif (level.grid[ll][cc]==1):
                    pass
                    #b.style.backgroundColor = "grey"
            
        
        
        solomon.sol_crouch = 0 #///decativate crouch
        
    else:
        solomon.sol_jump_rest -= 1
    

    ## print(f"jmp {solomon.sol_jump} fl {floating} wnd {solomon.sol_wand}")

    if (solomon.sol_jump==0 and floating and solomon.sol_wand==0):
        ## print("falling")
        solomon.soly-=solomon.sol_fall_inc
        solomon.sol_crouch = 0 #///decativate crouch
    
    if solomon.sol_wand!=0:
        solomon.sol_wand -= 1
        if (solomon.sol_wand==0):
            #print('wand!', solomon.sol_tile_dist_left_head(level.grid), solomon.sol_tile_dist_right_head(level.grid))
            block = solomon.sol_block(level.grid)
            ## print(block)
            block_x = block[1]+solomon.sol_dir
            block_y = block[0]-solomon.sol_crouch
            if (solomon.sol_dir==1):
                if (solomon.sol_tile_dist_right_head(level.grid)>0):
                    block_x +=1
                 
            elif (solomon.sol_dir==-1):
                if (solomon.sol_tile_dist_left_head(level.grid)>0):
                    pass
                    #//block_x--
            
            level_block = int(level.grid[block_y][block_x])
            print(level_block)
            if (level_block==0):
                level.grid[block_y][block_x] = 2
                print("zing {} {} {} ".format(level_block, level.grid[block_y][block_x], block_y,block_x))
                #var b = document.createElement('div')
                #b.id = `block_cc${block_x}ll${block_y}`
                #b.style=`position:absolute; background-color:black; left:${block_x*tile}px; top:${(level.length-block_y-1)*tile}px; width:${tile}px; height:${tile}px;`
                #document.body.appendChild(b)
            elif (level_block<3):
                level.grid[block_y][block_x] = 0                
                #console.log(block_x, block_y)
                #var b = document.getElementById(`block_cc${block_x}ll${block_y}`)
                ##//b.style=`position:absolute; background-color:black; left:${block_x*tile}px; top:${(level.length-block_y-1)*tile}px; width:${tile}px; height:${tile}px;`
                #document.body.removeChild(b)


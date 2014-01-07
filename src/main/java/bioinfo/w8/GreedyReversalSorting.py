'''
Created on Jan 7, 2014

@author: grmsjac6
'''


def revertOne(p,pos_k):
    pr = list(p)
    pr[pos_k] = -pr[pos_k]
    return pr

def revertString(p,pos_k,pos_l):
    pr = list(p)
    pr_s = pr[pos_k:pos_l+1]
    
    pr_s = [-k for k in reversed(pr_s)]
    
    pr[pos_k:pos_l+1] = pr_s
    return pr

def greedySort(pr):
    p = list(pr)
    pp = []
    k=1
    while k<=len(p):
        pos_k = None
        direct = k in p
        if direct:
            pos_k = p.index(k)
        else:
            pos_k = p.index(-k)
        
        if k != pos_k+1:
            
            
            pp.append(revertString(p,min(pos_k,k-1),max(pos_k,k-1)))
        elif not direct:
            pp.append(revertOne(p,pos_k))
        else:
            k += 1
        
        p = pp[-1]

    return pp


def breakPointCount(pr):
    pp = [0]+pr+[len(pr)+1]
    bkp = 0
    for i in range(1,len(pp)):
        p = pp[i]
        r = pp[i-1]
        if p-r != 1:
            bkp +=1
        
    return bkp
#p=[+138,-160,+340,-101,+368,-187,+234,+31,-6,+224,-361,+419,-65,-354,-12,-239,-217,-267,+175,+193,-387,-253,+320,-406,+307,-278,+46,+249,-204,+18,-222,+244,+174,+268,+420,-186,-272,+334,-190,-345,+87,+66,+39,-167,-414,+233,-118,-356,+197,+21,-386,+145,-379,+391,-92,+383,+154,+303,-120,+413,+389,+41,+300,+109,-238,+336,-170,+335,-108,+182,-80,+410,+399,-1,-104,+81,+416,-94,-58,+37,-318,-355,+270,+15,+237,+245,+140,-381,+395,-183,-242,+19,+366,+269,+322,+257,+165,-377,+415,-263,+288,-305,+207,-70,+274,+315,-43,-373,+151,+86,+275,+123,+423,+401,-17,-324,+9,+211,-325,+32,+20,+219,-215,+132,-260,-333,-282,+251,+218,+232,+85,+408,-311,-178,-209,+316,-370,+192,+208,-16,+250,+147,+298,-203,+284,+426,-38,+54,-188,-57,-177,+277,-27,+159,+388,+121,-297,-385,+371,-96,+369,+36,-229,+348,+166,-328,+191,-338,-220,-241,-352,-256,+216,+143,+180,+176,-364,+146,+61,+295,+111,-372,+102,+195,-265,+185,-150,+30,-5,-421,-262,-319,-365,-103,-376,-291,-99,+181,+49,+342,-294,+312,+35,-287,-206,-84,-194,+404,-129,-105,-164,+424,+11,-124,+135,-127,-2,+55,+418,+310,-261,-73,-359,-10,-130,-302,-95,+60,+122,-367,-378,-384,+380,+214,+82,+374,+173,-226,-125,+382,+343,-69,-327,-358,-331,-254,+155,-313,+304,-68,+393,+126,-134,-33,+44,-255,+357,-74,+200,-71,+184,-169,-106,-112,-292,-339,+280,-50,+290,+425,+264,-405,+422,-409,+363,+398,+77,-142,+326,+116,-271,+152,-139,+223,+407,-286,+417,-63,+283,-114,+235,+90,-52,+210,+78,+243,+248,+314,+309,-397,-34,+149,-221,+266,-25,+91,-171,+323,+375,+79,-279,-349,-225,-133,+360,+329,-168,+83,+347,+128,-240,+24,-172,+23,+64,-76,+390,+230,-115,-412,-344,+330,+228,-141,+276,-28,+107,+59,+72,-7,+53,-22,-337,+137,+199,+246,+47,-100,-202,+332,-341,+13,+14,-351,+40,+205,-299,-236,+403,-259,+148,+353,-29,+321,+296,+158,-306,-42,+144,+346,-98,+119,-402,-301,-213,+4,+110,+156,+227,-48,+247,-400,+196,+258,-273,-189,-45,-67,+308,+212,-289,+62,-131,+75,+201,-113,-392,-362,+26,-3,-8,-411,-163,-396,+231,+88,+317,-89,+285,-394,-252,+350,-136,+293,+281,-162,+51,-56,+93,+153,+198,+97,-161,-179,+157,-117]
#pp = greedySort(p)
#for pt in pp:
#    print("(" + " ".join(["%+d" % i for i in pt]) + ")")


f = open('dataset_88_1.txt')
line = next(f)
print(line[-10:-2])

p = [int(r) for r in line[1:-2].split(" ")]
print(breakPointCount(p))
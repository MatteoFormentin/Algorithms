
#PROBLEM: Given 'data' dataset find wich person to choose that make each skill almost 15with min cost.

SOLUTION = []

def recursive_alg(dataset=[], x=0,  y=0, z=0, sum=0, sol=""):

    ds = dataset.copy() #copy the dataset so that up level isn't modified
    for person in dataset: #dataset should preserved since otherway python wont cycle 
        a = x #x, y, z, sum, sol should also be preserved in the current level
        b = y
        c = z
        d = sum
        sol_temp = sol

        sol_temp += str(person[0]) + " "
        a += person[1]
        b += person[2]
        c += person[3]
        d += person[4]

        print(sol_temp + " " + str(sum))
        ds.remove(person)

        if len(ds) > 0:
            recursive_alg(ds, a, b, c, d, sol_temp)
        if(x >= 15 and y >= 15 and z >= 15):
            SOLUTION.append(sum)


data = [
    #[Name, Skill1, Skill2, Skill3, cost]
    ["amy",	3, 5, 1, 46000],
    ["bill", 1, 2, 5, 43000],
    ["carl"	, 3	, 4, 2, 47000],
    ["dan",	4, 3, 1, 36000],
    ["eva",	4, 2, 2, 43000],
    ["fred", 1, 3, 4, 55000],
    ["greg", 3, 1, 5, 68000],
    ["henry", 5,	4, 2, 64000],
    ["ida",	3, 3, 3, 60000]
]


print("START!!!!!")
recursive_alg(data)

print(min(SOLUTION))

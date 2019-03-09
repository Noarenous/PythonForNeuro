mathgrades= {
    "Noa": ("math",80,90),
    "Raphael": ("math",100,40),
    "Yael": ("math",100,89),
    "Moshe": ("math",82,77)

}

biogrades= {
    "Guy": ("bio",33,56),
    "Noa": ("bio",38,98),
    "Lior": ("bio",94,76),
    "Yael": ("bio",77,99)
}

def highgrade (subj1_all_students,subj2_all_students):
    for student in subj1_all_students: 
        tuple1 = subj1_all_students[student]
        maxgrade1 = max(tuple1[1],tuple1[2])
        
        if student in subj2_all_students.keys():
            tuple2 = subj2_all_students[student]
            maxgrade2= max(tuple2[1],tuple2[2])
            if maxgrade1 > maxgrade2:
                print(student, tuple1[0])
            else: 
                print(student, tuple2[0])
            







highgrade(mathgrades, biogrades)
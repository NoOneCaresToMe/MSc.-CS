import random
  
def HiringProblem(score, n):
      
    sample_size = int(round(n / e))
    print(f"\nRejecting first {sample_size} candidates as sample")

    #finding best candidate in the sample set for benchmark
    best_candidate = 0; 
    for i in range(1, sample_size):
        if (score[i] > score[best_candidate]):
            best_candidate = i
  
    #finding the first best candidate outside the sample set
    for i in range(sample_size, n):
        if (score[i] >= score[best_candidate]):
            best_candidate = i
            break
  
    if (best_candidate >= int(sample_size)):
        print(f"\nThe best Candidate found is {best_candidate+1} with score {score[best_candidate]}")
    else:
        print("Couldn't find a best candidate")
  
# Driver code
if __name__ == "__main__":
    
    e = 2.71828
    n = int(input("Enter number of candidates to simulate\n"))  #total number of candidate 
    score = []
    #populating the list 
    for i in range(n):
        score.append(random.randint(1, n))
    print("Candidate\tScore\n");
      
    for i in range(n):
        print(f"{i+1}\t\t{score[i]}");
       
    HiringProblem(score, n);


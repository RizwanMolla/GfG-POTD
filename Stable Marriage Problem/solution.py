class Solution:
     def stableMarriage(self, men, women):
          # code here
          n = len(men)
          rank = [[-1]*n for _ in range(n)]
          for w in range(n):
               for choice in range(n):
                    m = women[w][choice]
                    rank[w][m] = choice
          
          free_men = [-1] * n
          free_women = [-1] * n
          next_proposal = [0] * n

          while True:
               man = -1
               for i in range(n):
                    if free_men[i] == -1:
                         man = i
                         break
               
               if man == -1:
                    break
               
               woman = men[man][next_proposal[man]]
               next_proposal[man] += 1

               # The choosen woman is unengaged.
               if free_women[woman] == -1:
                    free_women[woman] = man
                    free_men[man] = woman
               
               # The choosen woman is engaged.
               else:
                    rank_current = rank[woman][free_women[woman]]
                    rank_new = rank[woman][man]

                    # Ranking of new partner is lower than the existing partner.
                    if rank_new < rank_current:
                         free_men[free_women[woman]] = -1
                         free_women[woman] = man
                         free_men[man] = woman

          return free_men
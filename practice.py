from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Return all unique combinations of 'candidates' that sum up to 'target'.
        Each candidate may be chosen multiple times.
        
        We'll use a DP array 'dp' of length (target + 1).
        dp[i] will be a list of *all* combinations that sum up to i.
        """
        
        # Step 1: Create the DP array.
        # Initially, dp = [ [], [], [], ..., [] ] (target+1 empty lists).
        dp = [[] for _ in range(target + 1)]
        
        # VISUAL (initial state):
        #
        #    Index:   0     1     2     3     4     5     6     7
        #    dp:    [  ]   [  ]   [  ]   [  ]   [  ]   [  ]   [  ]   [  ]
        #
        # dp[0], dp[1], dp[2], ..., dp[7] are all empty lists right now.

        # Step 2: Process each candidate in the list.
        for c in candidates:
            # We'll try to form sums from 1 up to 'target' using candidate c.
            for i in range(1, target + 1):
                
                # If i is smaller than c, c can't be used to form i,
                # so we skip to the next i.
                if i < c:
                    continue
                
                # If i exactly equals c, that means a single combo [c] forms i.
                if i == c:
                    dp[i].append([c])
                    #
                    # VISUAL: for i == c,
                    #   dp[i] += [ [c] ]
                    # Example: if c=2 and i=2, dp[2] = [ [2] ].
                    #
                    # Over time, you might see dp (for the example c=2, i=2):
                    #   dp[2] = [[2]]
                    
                else:
                    # i > c, so we check dp[i - c].
                    # dp[i - c] holds all combos that sum to i-c.
                    # By appending c to each of those combos,
                    # we get new combos that sum to i.
                    for combo in dp[i - c]:
                        dp[i].append(combo + [c])
                        #
                        # VISUAL:
                        #   dp[i] += [ combo + [c] for each combo in dp[i - c] ]
                        #
                        # Example: if i=5, c=2, then we look at dp[3].
                        # if dp[3] = [[3]], then we form [[3] + [2]] = [[3, 2]] 
                        # and append that to dp[5].
        
        # Step 3: At the end, dp[target] has all unique combos summing to 'target'.
        return dp[target]

candidate_votes = 3345
total_votes = 23123
message_to_candidate =( 
    f"You received {candidate_votes} number of votes."
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes/ total_votes * 100:.2f}% of the total votes") 

print(message_to_candidate)


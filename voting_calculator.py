def voting_calculator(monday_votes: int, tuesday_votes: int, wednesday_votes: int, thursday_votes: int, friday_votes: int) -> str:
    weekdays_votes = [
        {
            "day": 'monday',
            "votes": monday_votes
        },
        {
            "day": 'tuesday',
            "votes": tuesday_votes
        },
        {
            "day": 'wednesday',
            "votes": wednesday_votes
        },
        {
            "day": 'thursday',
            "votes": thursday_votes
        },
        {
            "day": 'friday',
            "votes": friday_votes
        }
    ]

    weekdays_votes.sort(key=lambda x: x['votes'], reverse=True)

    return weekdays_votes[0]['day']

most_voted_weekday = voting_calculator(5, 4, 3, 2, 1)
print('The most voted weekday is {}.'.format(most_voted_weekday))

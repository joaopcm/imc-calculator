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

monday_votes = int(input('Provide Monday votes: '))
tuesday_votes = int(input('Provide Tuesday votes: '))
wednesday_votes = int(input('Provide Wednesday votes: '))
thursday_votes = int(input('Provide Thursday votes: '))
friday_votes = int(input('Provide Friday votes: '))

most_voted_weekday = voting_calculator(monday_votes, tuesday_votes, wednesday_votes, thursday_votes, friday_votes)
print('The most voted weekday is {}.'.format(most_voted_weekday))

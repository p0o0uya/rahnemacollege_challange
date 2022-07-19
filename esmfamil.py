class esmfamil():
    @staticmethod
    def CalcScore(participants, letter):                           # This function will calculate score for each participant
    #   Participants: Dictionary of all participants and their responses
    #   letter: Letter Chosen for the game

        titles = {'city': [], 'food': [], 'color': []}

        for participant in participants:
            for item in titles:
                titles[item].append(participants[participant][item].lower())

        for participant in participants:
            pscore = 0                                             # This integer will accumulate participant's score
            for item in titles:
                presp = participants[participant][item].lower()
                # print(presp[0])
                if presp[0] == letter:
                    if titles[item].count(presp) > 1:
                        pscore += 5
                    else:
                        pscore += 10

            participants[participant]['score'] = pscore
        return participants

if __name__ == "__main__":
    inst = esmfamil()
    participants = {}

    participants['Reza Mousavi']   = {'city': 'Kerman',     'food': 'Khoresht',  'color': 'keremi'}
    participants['Amir Hatami']    = {'city': 'Kermanshah', 'food': 'kabab',     'color': 'sormei'}
    participants['Mahsa pirouzi']  = {'city': 'kerman',     'food': 'kalampolo', 'color': 'keyhani'}
    participants['Fatemeh Salehi'] = {'city': 'Kelardasht', 'food': 'Komaj',     'color': 'koosei'}


    participants = inst.CalcScore(participants, 'k')
    for participant in participants:
        print('{}: {}'.format(participant, participants[participant]))

    
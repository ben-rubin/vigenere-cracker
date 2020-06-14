from vigenere_cracker import find_key_len_candidates, decrypt, find_key


def print_totals(totals_to_print):
    for t_idx, total in totals_to_print.items():
        print('Key length: {}. Index of coincidence: {}'.format(t_idx, round(totals_to_print[t_idx], 3)))


def get_user_key_choice(totals_to_show_user):
    print_totals(totals_to_show_user)
    probable_key_len = [k for k, v in totals_to_show_user.items() if v == max(totals_to_show_user.values())][0]
    print(f'\nIt looks like the key length is {probable_key_len}, or {probable_key_len} is a multiple of the true key length')
    print(f'\nPlease choose one (the higher the better):')

    return int(input())


with open('cypher.txt', 'r') as f:
    cypher = f.read().strip('\n')
    f.close()

totals = find_key_len_candidates(cypher)
choice = get_user_key_choice(totals)
probable_key = find_key(cypher, choice)
plain_text = decrypt(cypher, probable_key)
print(plain_text)

import utils
import score
secret_number = utils.generate_secret_number()
while True:
    if utils.check_user_guess(secret_number):
        break
    else:
        current_score= score.lose_points(current_score)